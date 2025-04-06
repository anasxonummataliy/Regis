from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentails = ["*"],
    allow_methods = ["*"],
    allow_headers = ["*"]
)

users_data = []

app.post("/user")
async def create_user(
        id : int ,
        name : str,
        email : str, 
        password : str
):
    return { ""}

