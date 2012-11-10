try:
	from IPython.core import ipapi
except ImportError:
	from IPython import ipapi

def import_all(module):
	ipapi.get().ex('from %s import *' % module)

def import_x(module, submodules):
	if not isinstance(submodules, str):
		submodules = (',').join(submodules)
	ipapi.get().ex('from %s import %s' % (module, submodules))

import_x("bs4", "BeautifulSoup")
import_all("requests")
# ipapi.get().ex('%load_ext autoreload')
# ipapi.get().ex("%autoreload 2")
import_x("db_logic", "DBConnection")
ipapi.get().ex('conn = DBConnection()')
