import logging
import os
from datetime import datetime


def setup_logging():
    # Create logs directory if it doesn't exist
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Create log filename with current date
    log_filename = os.path.join(
        log_dir,
        f"marketplace_{datetime.now().strftime('%Y-%m-%d')}.log"
    )

    # Logging format
    log_format = "%(asctime)s [%(levelname)s] %(name)s: %(message)s"

    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format=log_format,
        handlers=[
            logging.FileHandler(log_filename),
            logging.StreamHandler()
        ]
    )

    return logging.getLogger("MarketplaceApp")


# Initialize logger
logger = setup_logging()