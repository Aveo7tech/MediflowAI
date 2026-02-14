import logging
from datetime import datetime

logging.basicConfig(
    filename="mediflow_audit.log",
    level=logging.INFO
)

def log_event(event: str):
    logging.info(f"{datetime.utcnow()} - {event}")
