from fastapi import FastAPI

app = FastAPI(
    title="Sample FastAPI Project",
    description="A simple FastAPI application for internship assignment",
    version="1.0.0"
)

# Home API
@app.get("/")
def home():
    return {
        "message": "Welcome to FastAPI",
        "status": "Running successfully"
    }

# Simple GET API
@app.get("/hello/{name}")
def say_hello(name: str):
    return {
        "greeting": f"Hello {name}",
        "note": "This is a GET request"
    }

# Simple POST API
@app.post("/add")
def add_numbers(a: int, b: int):
    return {
        "operation": "Addition",
        "a": a,
        "b": b,
        "result": a + b
    }

