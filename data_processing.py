from dotenv import load_dotenv
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore

# Load documents from directory
txt_loader = DirectoryLoader('data/DATA_ANALYTICS/texts', glob='*.txt')
loaders = [txt_loader]
documents = []
for loader in loaders:
    try:
        documents.extend(loader.load())
    except UnicodeDecodeError as e:
        print(f'Error loading documents: {str(e)}')
    except Exception as e:
        print(f'Error loading documents: {str(e)}')

print(f'You have {len(documents)} document(s) in your data')

# Check the number of characters in the first document
if len(documents) > 0:
    print(f'There are {len(documents[0].page_content)} characters in your document')
else:
    print('No documents found')

# Split documents into chunks
text_splitter = CharacterTextSplitter(chunk_size=1500, chunk_overlap=100)
documents = text_splitter.split_documents(documents)
print(f'Number of document chunks: {len(documents)}')

# Load environment variables
load_dotenv()
openai_api_key = 'OPENAI_API_KEY'
pinecone_api_key = 'PINECONE_API_KEY'

# Create OpenAI embeddings
try:
    embeddings = OpenAIEmbeddings()
except Exception as e:
    print(f'Error creating OpenAI embeddings: {str(e)}')

# Create Pinecone vector store
index_name = "thinkmind-chatbot"
try:
    vectorstore = PineconeVectorStore.from_documents(
        documents, embeddings, index_name=index_name
    )
except Exception as e:
    print(f'Error creating Pinecone vector store: {str(e)}')
