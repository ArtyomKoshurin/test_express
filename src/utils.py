import os
import smtplib
from email.message import EmailMessage

from dotenv import load_dotenv


load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", default="random_url")

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", default="random_key")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", default="random_alg")
JWT_ACCESS_COOKIE_NAME = os.getenv("JWT_ACCESS_COOKIE_NAME", default="random_name")
JWT_TOKEN_LOCATION = list(os.getenv("JWT_TOKEN_LOCATION", default="random_loc"))

EMAIL_HOST = os.getenv("EMAIL_HOST", default="random_host")
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER", default="random_user")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD", default="random_pass")
EMAIL_PORT = os.getenv("EMAIL_PORT", default="random_port")


def send_email(username, bookname, email):
    msg = EmailMessage()
    msg["subject"] = "Return of book"
    msg["From"] = EMAIL_HOST_USER
    msg["To"] = email
    msg.set_content(
        f"""\
    Name : {username}
    Dear reader, please return the book {bookname} back in library!
    """)
    with smtplib.SMTP_SSL(EMAIL_HOST, EMAIL_PORT) as smtp:
        smtp.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
        smtp.send_message(msg)
