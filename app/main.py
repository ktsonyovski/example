"""Main source code for FastAPI user management"""
from fastapi import FastAPI

from app.schemas import CreateUser
from app.db import create_user, delete_user, create_table, get_all_users
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifecycle(app:FastAPI):
    create_table()
    yield

app = FastAPI(
    title="User Management API",
    description="User management API for examples",
    summary="User management API for creating and deleting users in a SQLite database",
    lifespan=lifecycle
)

@app.post(f"/api/create_user")
def post_user(user: CreateUser):
    """Create user"""
    create_user(username=user.username, password=user.password)

@app.delete(f"/api/delete_user")
def del_user(username: str):
    """Delete user"""
    delete_user(username=username)

@app.get(f"/api/users")
def show_users():
    """Show all users"""
    return get_all_users()