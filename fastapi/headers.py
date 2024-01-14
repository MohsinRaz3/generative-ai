from fastapi import FastAPI,Header

app = FastAPI()
@app.post("/headerr")

def post_headers(who:str= Header()):
    return who

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("headers:app",reload=True)