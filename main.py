import argparse
import json
from src.GetData import GetData
from src.FileUtil import FileUtil

def getArgs():
	parser = argparse.ArgumentParser(description='program to make the setup of a uri question')
	parser.add_argument("-l", "--language", type=str, help="linguagem a ser usada na questao")
	parser.add_argument('-id', "--id_question", type=int, help="id da questao")
	return parser.parse_args()



def main():
	"""
		get external configs (paths and values about the question)
	"""
	args = getArgs()
	id_question = args.id_question
	lang = args.language
	dir_cp = None
	with open('config.json') as json_file:
		config_data = json.load(json_file)
		dir_cp = config_data['dir_cp']

	
	
	# sample_io = GetData(args.id_question).get_uri_io_sample()
	template = FileUtil(id_question, dir_cp['path'], lang)
	template.write_template()
	# print(sample_io)

main()