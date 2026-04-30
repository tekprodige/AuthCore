

user_db = []

ALLOWED_ROLES = ["admin", "user"]

def create_user(user):
    if user.role not in ALLOWED_ROLES:
        raise ValueError("Invalid role")

    user_db.append(user)
    return {"message": "User created successfully", "user": user}

def get_all_user():
    return {"message": "Users fetched successfully", "users": user_db}

def find_user(username, password):
    for user in user_db:
        if user.username == username and user.password == password:
            return user

    return None

def is_user_admin(user):
    return user.role == "admin"