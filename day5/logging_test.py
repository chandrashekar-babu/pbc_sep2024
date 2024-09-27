import logging

logging.basicConfig(filename="test.log", level=logging.DEBUG)
logging.info("this is informational message")
logging.error("this is an error message")
logging.warning("this is a warning message")