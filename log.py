#!/usr/bin/python

import logging

logger = logging.getLogger('mytool')
logger.setLevel(level=logging.INFO)
handler = logging.FileHandler('/tmp/output.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.info('This is a log info')
logger.debug('Debugging')
logger.warning('Warning exists')
logger.info('Finish')
