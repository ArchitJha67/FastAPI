from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(  # model_config tells it to automatically load values from a .env file
        env_file=".env",  # .env files is for storing sensitive data
        env_file_encoding="utf-8",  # tells it to read configuration from a file named .env.
    )  # "utf-8" specifies how to read that file's text.

    secret_key: SecretStr  # used to sign your JWT tokens.
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    max_upload_size_bytes: int = 5 * 1024 * 1024  # 5mb

    posts_per_page: int = 10

    reset_token_expire_minutes: int = 60

    ## Email Configuration Settings
    mail_server: str = "localhost"
    mail_port: int = 587  # standar port number for smtp
    mail_username: str = ""
    mail_password: SecretStr = SecretStr("")
    mail_from: str = "noreply@example.com"   # this is the sender address
    mail_use_tls: bool = True  # tells aiosmtplib whether to use star tls encryption

    frontend_url: str = "http://localhost:8000"


settings = Settings()  # type: ignore[call-arg]   # Loaded from .env file
