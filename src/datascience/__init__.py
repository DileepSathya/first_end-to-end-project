import os
import sys
import logging


format="[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir="logs"
log_filepath=os.path.join(log_dir,"logging.log")
os.makedirs(log_dir,exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format=format,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)
logger=logging.getLogger("first end-to-end")