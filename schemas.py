from pydantic import BaseModel


class UserBase(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    age: int | None = None
    email: str | None = None

class UserCreate(UserBase):
    password: str
    email: str

class User(UserBase):
    id: int

    class Config:
        from_attributes = True