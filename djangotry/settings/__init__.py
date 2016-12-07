
try:
	from .production import *
except Exception, e:
	pass

try:
	from .local import *
except Exception, e:
	pass