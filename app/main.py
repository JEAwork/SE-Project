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
models.Base.metadata.create_all(bind=engine)

origins = ["*"]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins
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
    return {"message": "Hello World! and all"}


#Pathway
#venv\Scripts\activate.bat 
#uvicorn app.main:app --reload
#https://git.heroku.com/create-eagleeye.git
