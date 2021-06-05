import logging

logger = logging.getLogger('main')

# This will need to be pulled out and able to be set from the ENV
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s: %(levelname)s - %(message)s")

ch.setFormatter(formatter)

logger.addHandler(ch)
