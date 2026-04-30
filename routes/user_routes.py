from fastapi import APIRouter
from services.user_service import create_user, get_all_user
from models.user import User

router = APIRouter()

@router.get("/get-all-users")
def get_users():
    return get_all_user()

@router.post("/create-users")
def create_new_user(user: User):
    return create_user(user)