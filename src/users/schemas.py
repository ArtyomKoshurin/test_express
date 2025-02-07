from pydantic import BaseModel, EmailStr


class UserCreateSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class TokenSchema(BaseModel):
    access_token: str
    token_type: str
