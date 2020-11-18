
from fastapi_mail.fastmail import FastMail
from fastapi_mail.config import  ConnectionConfig
from fastapi_mail.schemas import MessageSchema


__author__ = "sabuhi.shukurov@gmail.com"

VERSION = "0.3.0.3"


__all__ = [
    "FastMail", "VERSION", "ConnectionConfig", "MessageSchema", 
]