from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def get_data():
    return "hello"

@app.get("/user/{who}")
def user_data(who):
    return f"user is {who}"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hello:app", reload=True)