import streamlit as st
from dotenv import load_dotenv
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from langchain_pinecone import PineconeVectorStore
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

# Load the environment variables
load_dotenv()

@st.cache_resource(ttl='1h') # Cache the retriever for 1 hour
def get_retriever():
    index_name = "thinkmind-chatbot"
    embeddings = OpenAIEmbeddings()
    vectordb = PineconeVectorStore(index_name=index_name, embedding=embeddings)
    retriever = vectordb.as_retriever(search_type='mmr')
    return retriever

# Initialize components for the conversational chain and memory using langchain.
retriever = get_retriever()
msgs = StreamlitChatMessageHistory()
memory = ConversationBufferMemory(memory_key='chat_history', chat_memory=msgs, return_messages=True, k=10)

llm = ChatOpenAI(model_name='gpt-4-turbo', temperature=0.5)
qa_chain = ConversationalRetrievalChain.from_llm(llm, retriever=retriever, memory=memory, verbose=False)

# Sidebar button to clear message history.
if st.sidebar.button('Clear message history') or len(msgs.messages) == 0:
    msgs.clear()
    msgs.add_ai_message('Ask me anything about ThinkMind!')

# Display past messages
avatars = {'human': 'user', 'ai': 'assistant'}
for msg in msgs.messages:
    st.chat_message(avatars[msg.type]).write(msg.content)

# Handle user input and generate response.
user_query = st.chat_input(placeholder='type your question!')
if user_query:
    st.chat_message('user').write(user_query)
    response_container = st.empty() 
    with response_container:
        st.markdown("Generating response...")  
    response = qa_chain.run(user_query)
    response_container.markdown(response)


