from app.core.log_config import setup_logging, get_logger

setup_logging()
logger = get_logger(__name__)

from fastapi import FastAPI
from app.api.v1.endpoints import sample, health

logger.info("Starting FastAPI application")

app = FastAPI()

app.include_router(sample.router, prefix="/api/v1")
app.include_router(health.router, prefix="/api/v1")

# FastAPI entrypoint
