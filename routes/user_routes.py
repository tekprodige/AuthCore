from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import JWTError
from services.user_service import create_user, get_all_user, is_user_admin, find_user
from models.user import User
from services.auth_service import create_token, decode_token

router = APIRouter()
security = HTTPBearer(auto_error=False)

@router.get("/get-all-users")
def get_users():
    return get_all_user()

@router.post("/create-users")
def create_new_user(user: User):
    return create_user(user)

@router.post("/checks/is-admin")
def is_admin_check(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials if credentials else None
    if not token:
        raise HTTPException(status_code=401, detail="Missing token")

    try:
        payload = decode_token(token)
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    if payload.get("role") != "admin":
        raise HTTPException(status_code=403, detail="Access denied, user is not an admin")
    
    return {"message": f"Access granted, welcome {payload['username']}"}

@router.post("/login")
def login(username: str, password: str):
    user = find_user(username, password)

    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_token(user)

    return {"access_token": token, "token_type": "Bearer", "user": user}

