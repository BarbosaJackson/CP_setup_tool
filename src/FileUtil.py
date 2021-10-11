import os

class FileUtil(object):
	"""docstring for FileUtil"""
	def __init__(self, question_id, filepath, lang):
		self.question_id = question_id
		self.filename = str(question_id) + '.' + lang
		self.filepath = filepath
		self.lang = lang

	def write_template(self):
		template_file = open('templates/template.' + self.lang, 'r')
		template_file.read()
		print("Current working directory: {0}".format(os.getcwd()))
		os.chdir(self.filepath)
		os.mkdir(str(self.question_id))
		print("Current working directory: {0}".format(os.getcwd()))