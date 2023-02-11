from fastapi import FastAPI
from fastapi import Depends
from fastapi import HTTPException
from database import user_collection
from models import UserLogin
from routes import authenticate_user, verify_token, authenticate_forgot_user

app = FastAPI()

# Login User
@app.post("/login")
def login(user: UserLogin):
    access_token = authenticate_user(user.username, user.password)
    return {"access_token": access_token}


# Protected Route
@app.get("/protected")
def protected(username: str = Depends(verify_token)):
    return {"message": "Welcome to the protected route, {}".format(username)}


@app.post("/register")
async def set_data(user: UserLogin):
    if user_collection.find_one({"username": user.username}):

        raise HTTPException(status_code=409, detail="Item not found")
    else:
        user_collection.insert_one(user.dict())
        raise HTTPException(status_code=201, detail="User Created")

# Reset Password
@app.put("/reset")
def reset_password(user: UserLogin):
    access_token = authenticate_forgot_user(user.username)
    if user_collection.update_one({"username": user.username}, {"$set": {"password": user.password}}):
        return {"access_token": access_token,"message": "Password reset successful"}
    else:
        raise HTTPException(status_code=404, detail="Data Not Found")
