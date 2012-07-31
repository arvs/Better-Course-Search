from pymongo import Connection

class DBConnection(object):
	def __init__(self):
		self.db = Connection('localhost', 27017).bcs

	def classes_for_name(self, name):
		db_class = self.db.classes.find_one({'teacher':name})

		if db_class is not None:
			if db_class.get('no_classes') is True:
				return []
			else:
				classes = [x['link'] for x in list(self.db.classes.find({'teacher':name}))]
				return classes
		else:
			return None

	def insert(self, c, **kw):
		db[c].insert(kw)