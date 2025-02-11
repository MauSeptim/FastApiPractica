from pydantic import BaseModel, EmailStr
from typing import Optional

class UsuarioBase(BaseModel):
    id: Optional[int] = None
    nombre: str
    apellido: str
    email: EmailStr
    password: str

    class Config:
        orm_mode = True

class UsuarioVerificarLogin(BaseModel):
    email: EmailStr
    password: str

    class Config:
        orm_mode = True