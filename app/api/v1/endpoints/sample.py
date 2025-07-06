from app.core.log_config import get_logger
from fastapi import APIRouter
from app.services.sample_service import get_sample_data

logger = get_logger(__name__)

router = APIRouter()

@router.get("/sample", tags=["sample"])
def read_sample():
    logger.info("GET /sample endpoint called")
    return get_sample_data()
