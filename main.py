from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello BigLynx. Testing continuous deployment from GitHub."}