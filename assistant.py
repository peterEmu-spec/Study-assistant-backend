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
#get a single user
@app.get("/user/{user_id}")
def get_user(user_id):
    #user=db.query(User).filter(id == user_id).first()
    return {"id":user_id}

#update a single user
@app.patch("/user/{user_id}")
def update_user(user_id):
    return{}

#delete a single user
@app.delete("/user/{user_id}")
def delete_user(user_id):
    return{}