

user_db = []

ALLOWED_ROLES = ["admin", "user"]

def create_user(user):
    if user.role not in ALLOWED_ROLES:
        raise ValueError("Invalid role")

    user_db.append(user)
    return {"message": "User created successfully", "user": user}

def get_all_user():
    return {"message": "Users fetched successfully", "users": user_db}

def is_user_admin(user):
    return user.role == "admin"