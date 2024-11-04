from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Add your configuration variables here
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "figgi-io-backend"
    OPENAI_API_KEY: str = "ollama"  # Since you're using local Ollama
    class Config:
        env_file = ".env"

settings = Settings()