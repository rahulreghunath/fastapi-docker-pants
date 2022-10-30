"""_summary_"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import blog, user, authentication

app = FastAPI()

# cross origin resource sharing
origins = [
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)
