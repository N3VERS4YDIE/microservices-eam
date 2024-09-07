from fastapi import APIRouter, Body

user_route = APIRouter()

@user_route.post("/")
def create_user(user: User = Body(...)):
    try:
        return user
    except Exception as e:
        print(e)
        return {"error": str(e)}
    
@user_route.get("/")
def read_user():
    return {"message": "Read User"}

@user_route.put("/")
def update_user():
    return {"message": "Update User"}