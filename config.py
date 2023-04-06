from pydantic import BaseSettings


class Settings(BaseSettings):
    # MYSQL_USER: str
    # MYSQL_PASSWORD: str
    # MYSQL_HOST: str
    # MYSQL_PORT: str
    # MYSQL_DATABASE: str
    # SECRET_KEY: str
    # ALGORITHM: str
    # ACCESS_TOKEN_EXPIRE_MINUTES: int
    # REFRESH_TOKEN_EXPIRE_MINUTES: int
    HOST_API: str
    PORT_API: str
    EL_NOT_FOUND: str = "cette tâche n'existe pas"
    
    class Config:
        env_file = "./.env"


settings = Settings()