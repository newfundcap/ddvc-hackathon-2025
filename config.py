import os
from dataclasses import dataclass


@dataclass
class Config:
    db_host: str
    db_name: str
    db_user: str
    db_password: str
    db_port: int
    api_port: int
    api_host: str


config = Config(
    db_host=os.getenv("DB_HOST", "localhost"),
    db_name=os.getenv("DB_NAME", "ddvc_sourcing"),
    db_user=os.getenv("DB_USER", "ddvc"),
    db_password=os.getenv("DB_PASSWORD", "password"),
    db_port=5432,
    api_port=os.getenv("PORT", 8033),
    api_host=os.getenv("HOST", "localhost"),
)
