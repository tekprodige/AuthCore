

user_db = []

def create_user(user):
    user_db.append(user)
    return user

def get_all_user():
    return user_db