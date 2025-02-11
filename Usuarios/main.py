
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List
import crud
import schemas
from database import get_db



app = FastAPI()


@app.get("/")
def bienvenida():
    return "Bienvenidos a la Api de usuarios"

@app.post("/usuarios", response_model=schemas.UsuarioBase)
def crear_usuario(usuario: schemas.UsuarioBase, db: Session= Depends(get_db)):
    try:
        usuario_creado = crud.crear_usuario(usuario=usuario, db=db)
        return usuario_creado
    except Exception as a:
        raise HTTPException(status_code=500, detail=str(a))

@app.get("/usuarios/email/{email}")
def obtener_usuario_por_email(email: str, db: Session = Depends(get_db)):
    usuario_encontrado = crud.obtener_usuario_por_email(db=db, email=email)
    if not usuario_encontrado:
        return {"mensaje": "No existe usuario con ese email registrado"}
    return usuario_encontrado

@app.post("/usuarios/login")
def login(usuario: schemas.UsuarioVerificarLogin, db: Session = Depends(get_db)):
    usuario_db = crud.obtener_usuario_por_email(db=db, email=usuario.email)

    if not usuario_db:
        return {"mensaje": "No existe usuario con ese email registrado"}
    
    if (usuario.password == usuario_db.password):
        return {"mensaje": "correcto"}
    else:
        return {"mensaje": "password incorrecto"}




@app.get("/usuarios", response_model=List[schemas.UsuarioBase])
async def obtener_todos_los_usuarios(db = Depends(get_db)):
    usuarios = crud.obtener_todos_los_usuarios(db)
    return usuarios

@app.delete("/usuarios/{usuario_id}")
def eliminar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario_eliminado = crud.eliminar_usuario(db=db, usuario_id=usuario_id)
    if usuario_eliminado is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"mensaje": f'usuario {usuario_eliminado.nombre} esta eliminado'}

@app.put("/usuarios")
def crear_usuario():
    return ""


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas las fuentes (puedes especificar dominios en una lista)
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todos los encabezados
)



"""
JSON
XML
"""