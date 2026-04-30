from fastapi import APIRouter, HTTPException
from services.user_service import create_user, get_all_user, is_user_admin, find_user
from models.user import User

router = APIRouter()

@router.get("/get-all-users")
def get_users():
    return get_all_user()

@router.post("/create-users")
def create_new_user(user: User):
    return create_user(user)

@router.post("/checks/is-admin")
def is_admin_check(user:User):
    if not is_user_admin(user):
        raise HTTPException(status_code=403, detail="Access denied, user is not an admin")
    
    return {"message": "Access granted, welcome admin", "user": user}

@router.post("/login")
def login(username: str, password: str):
    user = find_user(username, password)

    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": "Login successful", "role": user.role}