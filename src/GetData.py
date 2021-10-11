from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class GetData(object):
	"""docstring for GetData"""
	def __init__(self, 	question_id):
		self.question_id = question_id
		self.base_url = 'https://www.urionlinejudge.com.br/repository/UOJ_'
		self.driver = webdriver.Chrome('./chromedriver')

	def make_text(self, element):
		return element.text

	def get_uri_io_sample(self):
		self.driver.get(self.base_url + str(self.question_id) + '.html')
		s = self.driver.find_elements_by_tag_name('td')
		samples = list(map(self.make_text, s))
		inputs = []
		outputs = []
		size = len(samples)
		i = 2
		while(i < size):
			if(i % 2 == 0):
				inputs.append(samples[i])
			else:
				outputs.append(samples[i])
			i += 1
		return {
			'size': len(inputs),
			'inputs': inputs,
			'outputs': outputs
		}