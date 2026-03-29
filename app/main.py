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
