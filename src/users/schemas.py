from pydantic import BaseModel, EmailStr


class UserCreateSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserGetSchema(BaseModel):
    username: str
    email: EmailStr


class TokenSchema(BaseModel):
    access_token: str
    token_type: str
