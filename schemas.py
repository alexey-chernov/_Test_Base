from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class PostCreate(BaseModel):
    text: str

class PostResponse(BaseModel):
    id: int
    text: str

class Token(BaseModel):
    access_token: str
    token_type: str
