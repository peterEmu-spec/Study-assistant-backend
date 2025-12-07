# backend/main.py
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from models import get_db, User, Subject, Study_Session, Habit

# create FastAPI instance
app = FastAPI()

# enable CORS for all origins
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

# ----------------- Root -----------------
@app.get("/")
def read_root():
    return {"Hello": "World"}

# ----------------- User Routes -----------------
class UserSchema(BaseModel):
    name: str
    age: int = None
    email: str = None

@app.post("/user")
def create_user(user: UserSchema, session=Depends(get_db)):
    existing = session.query(User).filter(User.name == user.name).first()
    if existing is not None:
        return {"message": "User already exists", "user": {"id": existing.id, "name": existing.name}}
    
    new_user = User(name=user.name, age=user.age, email=user.email)
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return {"message": "User created successfully", "user": {"id": new_user.id, "name": new_user.name}}

@app.get("/user")
def get_users(session=Depends(get_db)):
    users = session.query(User).all()
    return [{"id": u.id, "name": u.name, "age": u.age, "email": u.email} for u in users]

@app.get("/user/{user_id}")
def get_user(user_id: int, session=Depends(get_db)):
    user = session.query(User).filter(User.id == user_id).first()
    if not user:
        return {"error": "User not found"}
    return {"id": user.id, "name": user.name, "age": user.age, "email": user.email}

@app.patch("/user/{user_id}")
def update_user(user_id: int, user_data: UserSchema, session=Depends(get_db)):
    user = session.query(User).filter(User.id == user_id).first()
    if not user:
        return {"error": "User not found"}
    user.name = user_data.name
    user.age = user_data.age
    user.email = user_data.email
    session.commit()
    return {"message": "User updated", "user": {"id": user.id, "name": user.name}}

@app.delete("/user/{user_id}")
def delete_user(user_id: int, session=Depends(get_db)):
    user = session.query(User).filter(User.id == user_id).first()
    if not user:
        return {"error": "User not found"}
    session.delete(user)
    session.commit()
    return {"message": "User deleted"}

# ----------------- Subject Routes -----------------
class SubjectSchema(BaseModel):
    name: str
    difficulty: int = 1
    description: str = ""

@app.post("/subjects")
def create_subject(subject: SubjectSchema, session=Depends(get_db)):
    existing = session.query(Subject).filter(Subject.name == subject.name).first()
    if existing:
        return {"message": "Subject already exists", "subject": {"id": existing.id, "name": existing.name}}
    
    new_subject = Subject(
        name=subject.name,
        difficulty=subject.difficulty,
        description=subject.description
    )
    session.add(new_subject)
    session.commit()
    session.refresh(new_subject)
    return {
        "message": "Subject created successfully",
        "subject": {
            "id": new_subject.id,
            "name": new_subject.name,
            "difficulty": new_subject.difficulty,
            "description": new_subject.description
        }
    }

@app.get("/subjects")
def get_subjects(session=Depends(get_db)):
    subjects = session.query(Subject).all()
    return [
        {
            "id": s.id,
            "name": s.name,
            "difficulty": s.difficulty,
            "description": s.description
        }
        for s in subjects
    ]
# ----------------- Subject Routes (continued) -----------------

@app.get("/subjects/{subject_id}")
def get_subject(subject_id: int, session=Depends(get_db)):
    subject = session.query(Subject).filter(Subject.id == subject_id).first()
    if not subject:
        return {"error": "Subject not found"}
    return {
        "id": subject.id,
        "name": subject.name,
        "difficulty": subject.difficulty,
        "description": subject.description
    }

@app.patch("/subjects/{subject_id}")
def update_subject(subject_id: int, subject_data: SubjectSchema, session=Depends(get_db)):
    subject = session.query(Subject).filter(Subject.id == subject_id).first()
    if not subject:
        return {"error": "Subject not found"}
    
    subject.name = subject_data.name
    subject.difficulty = subject_data.difficulty
    subject.description = subject_data.description
    session.commit()
    session.refresh(subject)
    
    return {
        "message": "Subject updated successfully",
        "subject": {
            "id": subject.id,
            "name": subject.name,
            "difficulty": subject.difficulty,
            "description": subject.description
        }
    }

@app.delete("/subjects/{subject_id}")
def delete_subject(subject_id: int, session=Depends(get_db)):
    subject = session.query(Subject).filter(Subject.id == subject_id).first()
    if not subject:
        return {"error": "Subject not found"}
    
    session.delete(subject)
    session.commit()
    return {"message": "Subject deleted successfully"}

