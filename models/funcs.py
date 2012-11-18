import os
import codecs
import models



def get_upper_alphabet():
	return 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def get_upper_alphabet_list():
	alphabet_list = []
	for char in get_upper_alphabet():
		alphabet_list.append(char)
	return alphabet_list


def get_sample(sample):
	base_dir = get_base_dir()
	sample_path = os.path.join(base_dir, 'data/samples/en/', sample)
	try:
		sample_data = codecs.open(sample_path, 'r', encoding='utf-8').read()
	except IOError as e:
		sample_data = ''

	return sample_data


def get_base_dir():
	return os.path.dirname(os.path.dirname(__file__))

def get_samples():
	base_dir = get_base_dir()
	samples_dir = os.path.join(base_dir, 'data/samples/en/')
	all_files = list_files( samples_dir )
	actual_files = []
	for file in all_files:
		file = file.replace(samples_dir, '').replace('\\', '/')
		if file not in actual_files:
			actual_files.append(file)
	return actual_files

def get_selected_samples():
	return get_option('samples', get_samples())



def list_files(directory, files=[]):
	for file in os.listdir(directory):
		file_path = os.path.join(directory, file)
		if os.path.isdir(file_path):
			files = list_files(file_path, files)
		else:
			files.append( file_path )
	return files

def get_option(name, default=''):
	if name in models.models.options:
		return models.models.options[name]
	else:
		return default

def letter_count(input):
		return_object = {}
		for char in get_upper_alphabet():
			return_object[char] = input.upper().count(char)
		return return_object


def percentage( numerator, denominator ):
	if denominator == 0:
		return 0
	else:
		return (numerator*10000 / denominator) / float(100)