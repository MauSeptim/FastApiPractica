
from sqlalchemy import Column, String, BigInteger
from Usuarios.database import Base


class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(BigInteger, primary_key=True, index=True)
    nombre = Column(String(255), nullable=False)
    apellido = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(14), nullable=False)


class Algo(Base):
    __tablename__ = "algo"

    id = Column(BigInteger, primary_key=True, index=True)
    password = Column(String(14), nullable=False)



