from fastapi import FastAPI
from pydantic import BaseModel,conint
from motor.motor_asyncio import AsyncIOMotorClient

class User(BaseModel):
    name: str
    email: str
    age: int
    pledge_status: conint(ge=0, le=1)


app = FastAPI()

@app.post("/register/")
async def register_user(user: User):
    # Connect to MongoDB
    client = AsyncIOMotorClient("mongodb+srv://het28082001:dhruvi19121998@cluster0.5csscov.mongodb.net/")
    db = client["pledge_registration"]
    collection = db["Registration"]

    user_data = user.dict()
    await collection.insert_one(user_data)

    # Close the database connection
    client.close()

    return {"message": "User registered successfully"}

if __name__ == "__mongo__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
   