import logging

from .config import get_config

_logger = logging.getLogger(__name__)
HAS_PYDEVD_PYCHARM = True

try:
    import pydevd_pycharm
except ImportError:
    HAS_PYDEVD_PYCHARM = False
    _logger.debug("Cannot import 'pydevd_pycharm'. Please make sure it is installed.")

def initialize_debug():
    config = get_config()
    if not (HAS_PYDEVD_PYCHARM and config['enabled']):
        return

    _logger.info("Initializing PyCharm Debug Server")

    pydevd_pycharm.settrace(
        host=config['host'],
        port=config['port'],
        stdoutToServer=config['stdout'],
        stderrToServer=config['stderr'],
    )

def post_load():
    initialize_debug()
