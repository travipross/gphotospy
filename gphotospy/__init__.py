import logging


ff = logging.Formatter("%(name)s - %(asctime)s - %(levelname)s - %(message)s")
fh = logging.FileHandler("gphotospy.log", "w")
fh.setFormatter(ff)
fh.setLevel(logging.ERROR)

logger = logging.getLogger("gphotospy")
logger.addHandler(fh)
