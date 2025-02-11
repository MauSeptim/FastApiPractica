from sqlalchemy.orm import Session
import models
import schemas
from sqlalchemy.exc import IntegrityError

# Crear un nuevo usuario
def crear_usuario(db: Session, usuario: schemas.UsuarioBase):
    db_usuario = models.Usuario(
        nombre=usuario.nombre,
        apellido=usuario.apellido,
        email=usuario.email,
        password=usuario.password
    )

    try:
        db.add(db_usuario)
        db.commit()
        db.refresh(db_usuario)
        return db_usuario
    except IntegrityError:
        db.rollback()
        raise Exception("El email ya esta registrado")

# Obtener un usuario por su id
def obtener_usuario(db: Session, usuario_id: int):
    db_usuario = db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()
    if db_usuario is None:
        raise Exception(f"El usuario con el {usuario_id} no existe")

    return db_usuario

# Obtener un usuario por su email
def obtener_usuario_por_email(db: Session, email: str):
    db_usuario = db.query(models.Usuario).filter(models.Usuario.email == email).first()
    if db_usuario is None:
        return

    return db_usuario


# Obtener todos los usuarios
def obtener_todos_los_usuarios(db:Session):
    return db.query(models.Usuario).all()

# Actualizar un usuario
def actualizar_usuario(db:Session, usuario_id: int, usuario: schemas.UsuarioBase):
    db_usuario = obtener_usuario(db, usuario_id)

    if db_usuario is None:
        raise Exception(f"El usuario con el {usuario_id} no existe")
    
    db_usuario.nombre = usuario.nombre
    db_usuario.apellido = usuario.apellido
    db_usuario.email = usuario.email
    db_usuario.password = usuario.password

    try:
        db.commit()
        db.refresh(db_usuario)
        return db_usuario
    except Exception as e:
        db.rollback()
        raise Exception(f"Error al consultar usuario {str(e)}")

# Eliminar un usuario por su ID
def eliminar_usuario(db:Session, usuario_id: int):
    db_usuario = obtener_usuario(db, usuario_id)

    if db_usuario is None:
        raise Exception(f"El usuario con el {usuario_id} no existe")
    
    try:
        db.delete(db_usuario)
        db.commit()
        return db_usuario
    except Exception as e:
        db.rollback()
        raise Exception(f"Error al eliminar al usuario {str(e)}")
    




