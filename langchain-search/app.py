from fastapi import FastAPI
from langchain.tools import DuckDuckGoSearchRun
from langchain.utilities import WikipediaAPIWrapper
from pydantic import BaseModel
import openai
import os
import uvicorn
openai.api_base = "https://api.openai-proxy.com/v1"
os.environ["OPENAI_API_KEY"] = "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"

app = FastAPI()


class SearchQuery(BaseModel):
    command: str


class SearchResponse(BaseModel):
    msg: str


@app.post("/search", response_model=SearchResponse)
async def root(item: SearchQuery):
    tools = DuckDuckGoSearchRun()
    print("收到 info %s" % item.command)
    res = tools.run(item.command)
    print("返回 info %s" % res)
    return {"msg": res}


@app.post("/wikipedia", response_model=SearchResponse)
async def root(item: SearchQuery):
    tools = WikipediaAPIWrapper()
    print("收到 info %s" % item.command)
    res = tools.run(item.command)
    print("返回 info %s" % res)
    return {"msg": res}

if __name__ == '__main__':
    #uvicorn.run
    uvicorn.run(app='app:app', host="127.0.0.1", port=8100, reload=True)