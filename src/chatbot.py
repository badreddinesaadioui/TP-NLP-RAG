from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough
import os

class RAGChatbot:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
        self.template = """You are a helpful assistant. Use the following pieces of retrieved context to answer the question.
        If you don't know the answer, just say that you don't know.
        Context: {context}
        Question: {question}
        Answer:"""
        self.prompt = ChatPromptTemplate.from_template(self.template)

    def format_docs(self, docs):
        return "\n\n".join(doc.page_content for doc in docs)

    def get_rag_chain(self, vectorstore):
        retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
        rag_chain = (
            {"context": retriever | self.format_docs, "question": RunnablePassthrough()}
            | self.prompt | self.llm | StrOutputParser()
        )
        return rag_chain
    
    def evaluate_answer(self, query, answer, context_docs):
        eval_prompt = ChatPromptTemplate.from_template(
            """Rate the answer on a scale of 1 to 10 based on the context and query.
            Query: {query}
            Context: {context}
            Answer: {answer}
            Output ONLY the number."""
        )
        chain = eval_prompt | self.llm | StrOutputParser()
        context_text = self.format_docs(context_docs)
        score = chain.invoke({"query": query, "context": context_text, "answer": answer})
        return score