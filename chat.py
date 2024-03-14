import streamlit as st
from dotenv import load_dotenv
from langchain.callbacks.base import BaseCallbackHandler
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from langchain_pinecone import PineconeVectorStore
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings

load_dotenv()


@st.cache_resource(ttl='1h')
def get_retriever():
    index_name = "thinkmind-chatbot"
    embeddings = OpenAIEmbeddings()
    vectordb = PineconeVectorStore(index_name=index_name, embedding=embeddings)
    retriever = vectordb.as_retriever(search_type='mmr')
    return retriever


class StreamHandler(BaseCallbackHandler):
    def __init__(self, container: st.delta_generator.DeltaGenerator, initial_text: str = ''):
        self.container = container
        self.text = initial_text

    def on_llm_new_token(self, token: str, **kwargs) -> None:
        self.text += token
        self.container.markdown(self.text)


retriever = get_retriever()

msgs = StreamlitChatMessageHistory()
memory = ConversationBufferMemory(memory_key='chat_history', chat_memory=msgs, return_messages=True, k=5)

llm = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0.3,
                 streaming=True)  # Change the language model and adjust the temperature
qa_chain = ConversationalRetrievalChain.from_llm(llm, retriever=retriever, memory=memory, verbose=False)

if st.sidebar.button('Clear message history') or len(msgs.messages) == 0:
    msgs.clear()
    msgs.add_ai_message(f'Ask me anything about thinkmind!')

avatars = {'human': 'user', 'ai': 'assistant'}
for msg in msgs.messages:
    st.chat_message(avatars[msg.type]).write(msg.content)

user_query = st.chat_input(placeholder='Ask me anything!')
if user_query:
    st.chat_message('user').write(user_query)
    with st.chat_message('assistant'):
        stream_handler = StreamHandler(st.empty())
        response = qa_chain.run(user_query, callbacks=[stream_handler])
