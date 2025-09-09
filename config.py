"""Configuration management for the Financial Dashboard application."""

import os
from typing import Optional
from pydantic import BaseSettings, Field


class BackendSettings(BaseSettings):
    """Backend-specific configuration."""
    
    host: str = Field(default="localhost", env="BACKEND_HOST")
    port: int = Field(default=8000, env="BACKEND_PORT")
    reload: bool = Field(default=True, env="BACKEND_RELOAD")
    
    # Database
    database_url: str = Field(default="sqlite:///financial_dashboard.db", env="DATABASE_URL")
    
    # Redis
    redis_host: str = Field(default="localhost", env="REDIS_HOST")
    redis_port: int = Field(default=6379, env="REDIS_PORT")
    redis_db: int = Field(default=0, env="REDIS_DB")
    
    # Azure OpenAI
    azure_openai_endpoint: str = Field(..., env="AZURE_OPENAI_ENDPOINT")
    azure_openai_key: str = Field(..., env="AZURE_OPENAI_KEY")
    azure_openai_deployment_name: str = Field(default="gpt-4o-mini", env="AZURE_OPENAI_DEPLOYMENT_NAME")
    azure_openai_api_version: str = Field(default="2023-12-01-preview", env="AZURE_OPENAI_API_VERSION")
    
    # Financial APIs
    alpha_vantage_api_key: Optional[str] = Field(default=None, env="ALPHA_VANTAGE_API_KEY")
    yfinance_cache_dir: str = Field(default="./cache", env="YFINANCE_CACHE_DIR")
    
    # Logging
    log_level: str = Field(default="INFO", env="LOG_LEVEL")
    log_format: str = Field(default="json", env="LOG_FORMAT")
    
    class Config:
        env_file = ".env"
        case_sensitive = False


class FrontendSettings(BaseSettings):
    """Frontend-specific configuration."""
    
    title: str = Field(default="Financial Dashboard", env="FRONTEND_TITLE")
    theme: str = Field(default="dark", env="FRONTEND_THEME")
    
    # Backend connection
    backend_host: str = Field(default="localhost", env="BACKEND_HOST")
    backend_port: int = Field(default=8000, env="BACKEND_PORT")
    
    class Config:
        env_file = ".env"
        case_sensitive = False


# Global instances
backend_config = BackendSettings()
frontend_config = FrontendSettings()
