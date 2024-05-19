from dotenv import load_dotenv
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore

# Load documents from the specified directory.
txt_loader = DirectoryLoader('data/CYBERLAWS/texts/instance', glob='*.txt')
loaders = [txt_loader]
documents = []
for loader in loaders:
    try:
        documents.extend(loader.load())
    except UnicodeDecodeError as e:
        print(f'Error loading documents: {str(e)}') # specify error for unicode decode error.
    except Exception as e:
        print(f'Error loading documents: {str(e)}') 

print(f'You have {len(documents)} document(s) in your directory.')

# Get the number of characters in the document.
if len(documents) > 0:
    print(f'There are {len(documents[0].page_content)} characters in this document')
else:
    print('No documents found')

# Split documents into chunks of 1500 characters with 100 character overlap.
text_splitter = CharacterTextSplitter(chunk_size=1500, chunk_overlap=100)
documents = text_splitter.split_documents(documents)
print(f'Number of document chunks: {len(documents)}')

# Load environment variables
load_dotenv()
openai_api_key = 'OPENAI_API_KEY'
pinecone_api_key = 'PINECONE_API_KEY'

# check if the environment variables are set.
if not openai_api_key or not pinecone_api_key:
    print('Please set the OPENAI_API_KEY and PINECONE_API_KEY environment variables.')
    exit()

# start the openai embeddings process.
try:
    embeddings = OpenAIEmbeddings()
except Exception as e:
    print(f'Error starting openai embedding: {str(e)}')

# load the embeddings for the documents and store them in the Pinecone vector database.
index_name = "thinkmind-chatbot"
try:
    vectorstore = PineconeVectorStore.from_documents(
        documents, embeddings, index_name=index_name
    )
    print('Embeddings loaded successfully into the vector database with index name: thinkmind-chatbot')
except Exception as e:
    print(f'Error loading the embeddings for the documents to the vector database: {str(e)}')
