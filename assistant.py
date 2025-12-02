#1import api class
from fastapi import FastAPI
# create an instance
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

# start backend

@app.post("/user")
def create_user():
    return{"message":"User created successfully"}

@app.get("/user")
def get_users():
    return[]
