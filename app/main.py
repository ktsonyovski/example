"""Main source code for FastAPI user management"""
from fastapi import FastAPI
from app.schemas import CreateUser

app = FastAPI(
    title="User Management API",
    description="User management API for examples",
    summary="User management API for creating and deleting users in a SQLite database"
)

users = {
    1 : {"username" : "root", "password" : "root"}
}

@app.get("/users")
def users_list():
    """Show users list"""
    return users

@app.post(f"/users")
def create_user(user: CreateUser):
    """Create user"""
    add_user = {"username": user.username, "password": user.password}
    users[max(users.keys()) + 1] = add_user
    return add_user
