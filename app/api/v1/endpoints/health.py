from app.core.log_config import get_logger
from fastapi import APIRouter
from app.services.health_service import get_health_status

logger = get_logger(__name__)

router = APIRouter()

@router.get("/health", tags=["health"])
def health_check():
    logger.info("GET /health endpoint called")
    return get_health_status()
