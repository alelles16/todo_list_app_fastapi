from fastapi import FastAPI

app = FastAPI(
    debug=True,
    title="Todo API"
)

@app.get("/")
async def read_root():
    return {"message": "Welcome to My API!"}
