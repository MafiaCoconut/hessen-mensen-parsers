from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class DBSettings(BaseSettings):
    DB_HOST: str = Field(..., env='DB_HOST')
    DB_PORT: int = Field(..., env='DB_PORT')
    DB_USER: str = Field(..., env='DB_USER')
    DB_PASSWORD: str = Field(..., env='DB_PASSWORD')
    DB_NAME: str = Field(..., env='DB_NAME')

    @property
    def DATABASE_URL_asyncpg(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


    @property
    def DATABASE_URL_psycopg(self):
        return f"postgresql+psycopg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    model_config = SettingsConfigDict(env_file="/home/mafiacoconut/PythonProjeckts/hessen-mensen-parsers/.env", extra="ignore")


db_settings = DBSettings()


