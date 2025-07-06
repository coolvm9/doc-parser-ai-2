from app.core.log_config import get_logger

logger = get_logger(__name__)

# Health check service
def get_health_status():
    logger.info("Returning health status from service")
    return {"status": "ok"}
