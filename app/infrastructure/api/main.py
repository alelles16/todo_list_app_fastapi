from fastapi import FastAPI
from app.infrastructure.api.routes import todo_list_routes


app = FastAPI(
    title="Todo API",
    description="A simple Todo List API",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.include_router(todo_list_routes.router)

@app.get("/")
def root():
    return {"message": "Todo List API is up"}
