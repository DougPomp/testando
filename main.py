from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Doug_Master(BaseModel):
    canal: str
    msg: str
    dia: int


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.post("/doug/", response_model=Doug_Master)
async def doug():
    return Doug_Master(canal:="Douglas Canal", msg:"Sou o mestre do meu mundo!", dia:111)
    