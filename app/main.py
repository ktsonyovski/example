"""Main source code for FastAPI user management"""
from fastapi import FastAPI

app = FastAPI(
    title="User Management API",
    description="User management API for examples",
    summary="User management API for creating and deleting users in a SQLite database"
)

@app.get("/")
def root():
    """Root function"""
    return "Hello World"

@app.post("/auth/login")
def login(username: str, password: str):
    """Simple login"""

@app.get("/users")
def users_list():
    """Show users list"""

@app.post("/users")
def create_user(username: str, password: str):
    """Create user"""

@app.delete(f"/users{id}")
def delete_user(id: int):
    """Delete user"""
