from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# JSON fayl nomi
JSON_FILE = "users.json"

# JSON fayldan ma'lumotlarni o'qish funksiyasi


def read_users():
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, "r") as file:
            return json.load(file)
    return []  # Agar fayl mavjud bo'lmasa, bo'sh ro'yxat qaytaradi

# JSON faylga ma'lumotlarni yozish funksiyasi


def write_users(users):
    with open(JSON_FILE, "w") as file:
        json.dump(users, file, indent=4)


# Dastur boshlanganda users_data ni JSON fayldan o'qib olamiz
users_data = read_users()


@app.post("/user")
async def create_user(name: str, email: str, password: str):
    new_id = len(users_data) + 1
    new_user = {"id": new_id, "name": name,
                "email": email, "password": password}
    users_data.append(new_user)
    # Yangi foydalanuvchi qo'shilganda JSON faylga yozamiz
    write_users(users_data)
    print("Yangi foydalanuvchi qo'shildi:", new_user)
    print("Joriy users_data:", users_data)
    return new_user


@app.get("/users")
async def get_users():
    print("Foydalanuvchilar ro'yxati so'raldi:", users_data)
    return users_data
