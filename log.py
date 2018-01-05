import logging as log
# Log to file settings
log.basicConfig(
    filename='gmail.log',
    filemode='w',
    format='[%(asctime)s %(filename)18s] %(levelname)-7s - %(message)7s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=log.DEBUG)

# Log to console setings
# set up log to console
console = log.StreamHandler()
console.setLevel(log.DEBUG)
# set a format which is simpler for console use
formatter = log.Formatter('[%(asctime)s %(filename)18s] %(levelname)-7s - %(message)7s',
                          "%Y-%m-%d %H:%M:%S")
console.setFormatter(formatter)
# add the handler to the root logger
log.getLogger('').addHandler(console)

logger = log.getLogger(__name__)