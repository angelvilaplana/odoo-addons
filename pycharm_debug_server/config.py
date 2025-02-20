import os

from odoo.tools import str2bool, config

try:
    from odoo.addons.server_environment import serv_config

    if serv_config.has_section("pycharm_debug_server"):
        pycharm_debug_server_config = serv_config["pycharm_debug_server"]
    else:
        pycharm_debug_server_config = {}
except ImportError:
    pycharm_debug_server_config = config.misc.get("pycharm_debug_server", {})

def is_enabled():
    if os.environ.get('PYCHARM_DEBUG_SERVER_ENABLED'):
        return str2bool(os.environ.get('PYCHARM_DEBUG_SERVER_ENABLED'))
    else:
        return pycharm_debug_server_config.get('enabled') or False

def get_host_config():
    return (
        os.environ.get('PYCHARM_DEBUG_SERVER_HOST')
        or pycharm_debug_server_config.get('host')
        or 'localhost'
    )

def get_port_config():
    return int(
        os.environ.get('PYCHARM_DEBUG_SERVER_PORT')
        or pycharm_debug_server_config.get('port')
        or 6899
    )

def get_stdout_config():
    if os.environ.get('PYCHARM_DEBUG_SERVER_STDOUT'):
        return str2bool(os.environ.get('PYCHARM_DEBUG_SERVER_STDOUT'))
    else:
        return pycharm_debug_server_config.get('stdout') or True

def get_stderr_config():
    if os.environ.get('PYCHARM_DEBUG_SERVER_STDERR'):
        return str2bool(os.environ.get('PYCHARM_DEBUG_SERVER_STDERR'))
    else:
        return pycharm_debug_server_config.get('stderr') or True

def get_config():
    return {
        'enabled': is_enabled(),
        'host': get_host_config(),
        'port': get_port_config(),
        'stdout': get_stdout_config(),
        'stderr': get_stderr_config()
    }
