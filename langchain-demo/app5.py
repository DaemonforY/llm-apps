from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo')
chain = ConversationChain(llm=llm, verbose=True)

if __name__ == '__main__':
    output = chain.run(input="give a flask Dockerfile example")
    print(output)