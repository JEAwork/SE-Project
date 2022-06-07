from fastapi import FastAPI
from requests import post
from random import randrange
from .import models
from .database import engine
from .routers import post, user, auth
from .config import settings
from fastapi.middleware.cors import CORSMiddleware

settings.database_password

#sql create models
#models.Base.metadata.create_all(bind=engine)

origins = ["hhtps://EagleEye.com"]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

#get request method url: "/"
@app.get("/")
def root():
    return {"message": "Hello World"}

#Pathway
#venv\Scripts\activate.bat 
#uvicorn app.main:app --reload
