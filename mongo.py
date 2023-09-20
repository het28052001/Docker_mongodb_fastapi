from fastapi import FastAPI
from pydantic import BaseModel,conint
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv 
import os

load_dotenv()

class User(BaseModel):
    name: str
    email: str
    age: int
    pledge_status: conint(ge=0, le=1)


app = FastAPI()

@app.post("/register/")
async def register_user(user: User):
    # Connect to MongoDB
    mongodb_uri = os.getenv("MONGODB_URI")
    client = AsyncIOMotorClient(mongodb_uri)
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
   