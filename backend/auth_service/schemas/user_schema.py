from pydantic import BaseModel,EmailStr

class UserCreate(BaseModel):
    email:EmailStr
    full_name:str
    password: str
    

class UserResponse(BaseModel):
    id:int
    email: str
    full_name:str
    role:str
    is_active:bool

    model_config={
        "from_attributes":True
    }
    