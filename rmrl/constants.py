from pathlib import Path
import pkg_resources

try:
    from xdg import xdg_data_home
except ImportError:
    xdg_data_home = None

try:
    from xdg import BaseDirectory
except ImportError:
    BaseDirectory = None

# From rcu.py, with comment
# Todo: this should be based on the specific RM model
DISPLAY = {
            'screenwidth': 1404,
            'screenheight': 1872,
            'realwidth': 1408,
            'dpi': 226
            }
# Qt docs say 1 pt is always 1/72 inch
# Multiply ptperpx by pixels to convert to PDF coords
PTPERPX = 72 / DISPLAY['dpi']
PDFHEIGHT = DISPLAY['screenheight'] * PTPERPX
PDFWIDTH = DISPLAY['screenwidth'] * PTPERPX

SPOOL_MAX = 10 * 1024 * 1024

# TODO: parameterize
XDG_DATA_HOME = Path().home() / '.local' / 'share'
if xdg_data_home is not None:
    XDG_DATA_HOME = Path(xdg_data_home())
elif BaseDirectory is not None:
    XDG_DATA_HOME = Path(BaseDirectory.xdg_data_home)
TEMPLATE_PATH = XDG_DATA_HOME / 'rmrl' / 'templates'

VERSION = pkg_resources.get_distribution('rmrl').version

HIGHLIGHT_DEFAULT_COLOR = '#FFE949'
HIGHLIGHT_ALPHA = 0.392
