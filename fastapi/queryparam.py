from fastapi import FastAPI

app = FastAPI()

@app.get("/hi")
def queryparam(who):
    return f"who is this? , {who}"