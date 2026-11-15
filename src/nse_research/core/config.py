from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "NSE AI Research"
    app_env: str = "development"
    app_timezone: str = "Asia/Kolkata"
    premarket_report_time: str = "09:00"
    database_url: str = "sqlite:///./data/nse_research.db"
    log_level: str = "INFO"
    nse_bhavcopy_mcp_url: str = "https://mcp.nseindia.in/bhavcopy/cm/mcp"
    nse_cm_market_mcp_url: str = "https://mcp.nseindia.in/cmmkt/mcp"
    llm_provider: str = ""
    llm_api_key: str = ""
    llm_model: str = ""

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


@lru_cache
def get_settings() -> Settings:
    return Settings()
