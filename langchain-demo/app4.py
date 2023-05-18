#
# from langchain.embeddings.openai import OpenAIEmbeddings
# from langchain.vectorstores import Pinecone
# import pinecone
# import os
# from langchain.document_loaders import DirectoryLoader
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# embeddings = OpenAIEmbeddings()
# my_loader = DirectoryLoader('./data_output_filtered_content', glob='**/*.txt')
# documents = my_loader.load()
# text_splitter = RecursiveCharacterTextSplitter(chunk_size = 700, chunk_overlap = 0)
# docs = text_splitter.split_documents(documents)
#
# pinecone.init(
#  api_key=os.environ['PINECONE_API_KEY'], # find at app.pinecone.io
#  environment=os.environ['PINECONE_ENV'] # next to api key in console
# )
#
# pinecone.create_index(name="langchain-python", metric="cosine", shards=1, dimension=1536)
#
# pinecone_index = pinecone.Index("langchain-python")
#
# docsearch = Pinecone.from_documents(docs, embeddings, index_name=os.environ['PINECONE_INDEX_NAME'])
#
#
#
#
# Pinecone.from_existing_index(os.environ['PINECONE_INDEX_NAME'], embeddings)
# query = "write me langchain code to build my hugging face model"
# docs = docsearch.similarity_search(query)
# from langchain.chains.qa_with_sources import load_qa_with_sources_chain
# from langchain.llms import OpenAI
#
# def load_chain():
#  docsearch = Pinecone.from_existing_index(index_name, embeddings)
#  return docsearch
#
# chain = load_qa_with_sources_chain(llm=OpenAI(), retriever=load_chain(), return_source_documents=True, verbose=True)