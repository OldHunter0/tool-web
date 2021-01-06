from fastapi import FastAPI
from fastapi.requests import Request


app=FastAPI()

@app.get("/")
def get_user_info(request:Request):
    return {"ip":request.client,"method":request.method,
            "path":request.url}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("demo1:app",port=5002,reload=True)