from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def root():
    return{"message": "hello"}

@app.get("/item")
def read_root(name:str):
    return{"message": f"hell0 {name}"}
