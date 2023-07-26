"""
In this file we are going to write code related to tracking a entire project execution and error. 
"""

import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)      ## This line will create a folder and file where we can track the project.

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)  ## This will create logger file 

logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = "[ %(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s", ## This line indicated the format of logger means the message format of execution.
    level = logging.INFO
)


# if __name__ == "__main__":
#     logging.info("Logging has started testing")
    
