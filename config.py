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
    pdl_api_key: str


config = Config(
    db_host=os.getenv("DB_HOST", "localhost"),
    db_name=os.getenv("DB_NAME", "ddvc_sourcing"),
    db_user=os.getenv("DB_USER", "ddvc"),
    db_password=os.getenv("DB_PASSWORD", "password"),
    db_port=os.getenv("DB_PORT", 5432),
    api_port=os.getenv("PORT", 8033),
    api_host=os.getenv("HOST", "localhost"),
    pdl_api_key=os.getenv("PDL_API_KEY", "19def2a487c108856614ed041a9a670daa5e58cf29eafa4898908d401f26f53c"),
)
