
import logging
logging.basicConfig(level=logging.INFO)
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.hello_routes import router as greeting_router
from routes.todos_routes import router as todos_router
from config import settings
app = FastAPI(title= "TODOIST")
tags_metadata = [
    {
        "name": "users",
        "description": "Operations related to users",
    },
]
origins = [
    "http://localhost"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(greeting_router)
app.include_router(todos_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=settings.HOST_API, port=settings.PORT_API)