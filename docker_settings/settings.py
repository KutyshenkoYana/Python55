from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    secret_text: str = "hello"
    password: str | None = None

    min_number: int = 10
    max_number: int = 100

    # читання налаштувань с .env файла
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


# создать обьект этого класса
settings = Settings()

print(settings.password)
