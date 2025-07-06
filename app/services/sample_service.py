from app.core.log_config import get_logger

logger = get_logger(__name__)

# Sample service logic
def get_sample_data():
    logger.info("Returning sample data from service")
    return {"message": "This is sample data from the service."}
