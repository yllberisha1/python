from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def root():
    return{"message": "hello"}

@app.get("/item/")
def read_root():
    return{"items":["item1","item2",'item3']}

@app.get("/item/")
def read_root():
    return {"item_id":}