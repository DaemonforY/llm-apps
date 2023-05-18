import pymysql

import openai
import os

from langchain import OpenAI, SQLDatabase, SQLDatabaseChain

db = SQLDatabase.from_uri("mysql+pymysql://root:corerain123@192.168.0.161:32327/cr")
llm = OpenAI(temperature=0, model_name='gpt-3.5-turbo')

db_chain = SQLDatabaseChain(llm=llm, database=db, verbose=True)

if __name__ == '__main__':
    db_chain.run("查询数据库中有多少张表")
