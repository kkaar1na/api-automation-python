from pydantic import BaseModel

class UserSchema(BaseModel):
    id: int
    name: str
    username: str
    email: str


class CreateUserResponse(BaseModel):
    id: int
    name: str
    username: str
    email: str