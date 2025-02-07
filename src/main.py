import uvicorn
from fastapi import FastAPI

from database import init_db
from users.routers import router as users_router


app = FastAPI(
    title="Library",
    description="Test project for library"
)

app.include_router(users_router)


if __name__ == "__main__":
    init_db()
    uvicorn.run("main:app", reload=True)
