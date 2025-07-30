from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from crew import crew_compile  


app = FastAPI()

@app.get("/")
def greet():
    return {"message":"Hello, Welcome to our Agent"}

@app.post("/agent")
def crew_execute(query: str):
    result =  crew_compile(query)
    return {"result": result}

if __name__=="__main__":
    uvicorn.run(app, host = "127.0.0.1", port = 8080)