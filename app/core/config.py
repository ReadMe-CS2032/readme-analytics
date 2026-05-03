from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PORT: int = 8005
    JWT_SECRET: str
    ALLOWED_ORIGINS: str = ""
    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_ACCESS_KEY: str
    AWS_SESSION_TOKEN: str = ""
    AWS_REGION: str
    ATHENA_DATABASE: str = "readme_db"
    ATHENA_OUTPUT_BUCKET: str

    model_config = {"env_file": ".env"}


settings = Settings()
