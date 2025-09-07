#!/usr/bin/env python
# coding: utf-8

# In[1]:


from langchain_community.document_loaders import PyPDFLoader
loader = PyPDFLoader("IndianPolitybyMLaxmikanth.pdf")
docs = loader.load()
docs


# In[2]:


from langchain.text_splitter import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
text_splitter.split_documents(docs)[:5]


# In[3]:


documents=text_splitter.split_documents(docs)
documents


# In[4]:



from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
db = FAISS.from_documents(documents, embedding)


# In[5]:


db


# In[6]:


# query="who was the first Governor General of India ?"
# result=db.similarity_search(query)
# print(result[0].page_content)


# In[7]:


from langchain_community.llms import Ollama
## Load Ollama LAMA2 LLM model
llm=Ollama(model="llama2:7b")
llm


# In[8]:


from langchain_core.prompts import ChatPromptTemplate
prompt = ChatPromptTemplate.from_template("""
Answer the following question based only on the provided context. 
Think step by step before providing a detailed answer. 
I will tip you $1000 if the user finds the answer helpful. 
<context>
{context}
</context>
Question: {input}""")


# In[9]:


from langchain.chains.combine_documents import create_stuff_documents_chain

document_chain=create_stuff_documents_chain(llm,prompt)


# In[10]:


"""
Retrievers: A retriever is an interface that returns documents given
 an unstructured query. It is more general than a vector store.
 A retriever does not need to be able to store documents, only to 
 return (or retrieve) them. Vector stores can be used as the backbone
 of a retriever, but there are other types of retrievers as well. 
 https://python.langchain.com/docs/modules/data_connection/retrievers/   
"""

retriever=db.as_retriever()
retriever


# In[11]:


"""
Retrieval chain:This chain takes in a user inquiry, which is then
passed to the retriever to fetch relevant documents. Those documents 
(and original inputs) are then passed to an LLM to generate a response
https://python.langchain.com/docs/modules/chains/
"""
from langchain.chains import create_retrieval_chain
retrieval_chain=create_retrieval_chain(retriever,document_chain)


# In[15]:


response=retrieval_chain.invoke({"input":" Fundamental Rights for women  "})
print(response['answer'])


# In[13]:


print(response['answer'])


# In[ ]:




