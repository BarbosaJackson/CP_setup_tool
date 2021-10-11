import sys

sys.setrecursionlimit(0x100000)

def list_print(my_list):
	size = len(my_list)
	for i in range(size):
		print(my_list[i], end=' ')
	print('')

def list_read_ml(size):
	my_list = []
	for i in range(size):
		my_list.append(int(input()))
	return my_list

def list_read_ol():
	my_list = list(map(int, input().split(' ')))
	return my_list

"""
	your code here
"""