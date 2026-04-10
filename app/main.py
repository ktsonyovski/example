"""Main source code for FastAPI user management"""
from fastapi import FastAPI

from app.schemas import CreateUser
from app.db import create_user, delete_user

app = FastAPI(
    title="User Management API",
    description="User management API for examples",
    summary="User management API for creating and deleting users in a SQLite database"
)

@app.post(f"/api/create_user")
def post_user(user: CreateUser):
    """Create user"""
    create_user(username=user.username, password=user.password)

@app.delete(f"/api/delete_user")
def del_user(username: str):
    """Delete user"""
    delete_user(username=username)