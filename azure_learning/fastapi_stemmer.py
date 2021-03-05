from fastapi import FastAPI
from processing import process

app = FastAPI()


@app.get("/process/{input}")
async def read_item(input: str):
    result=process(input)
    return {"Result": result}


@app.get("/")
async def root():
    return {"message": "Hello Stemmer"}