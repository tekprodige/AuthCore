from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "supersecretkey"
ALGORITHM = "HS256"

def create_token(user):
    expires_at = datetime.utcnow() + timedelta(hours=1)
    payload = {
        "username": user.username,
        "role": user.role,
        "exp": int(expires_at.timestamp())
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token

def decode_token(token):
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])