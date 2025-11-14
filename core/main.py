from fastapi import FastAPI

test_server = FastAPI()

@test_server.get("/check")
def check():
    return {"test": "running"}