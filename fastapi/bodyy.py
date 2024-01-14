from fastapi import FastAPI, Body

app = FastAPI()

@app.post("/hi")
def get_body(who:str = Body(embed=True)):
    return f"body is: {who} "



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("bodyy:app", reload=True)