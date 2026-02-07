from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Backend Core FastAPI"
    ENVIRONMENT: str = "development"





setting =  Settings()