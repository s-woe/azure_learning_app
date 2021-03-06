from fastapi import FastAPI
from processing import process

app = FastAPI()


@app.get("/process/{input}")
async def read_item(input : int):
    result=process(input)
    return {"Result": str(result)}


@app.get("/")
async def root():
    return {"message": "Hello Stemmer"}