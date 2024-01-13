from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_data():
    return "hello"

@app.get("/user")
def user_data():
    return "user is mohsin"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hello:app", reload=True)