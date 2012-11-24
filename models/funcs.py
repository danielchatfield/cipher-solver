import os
import codecs
import re
import models
import logging


def get_upper_alphabet():
	return 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def get_upper_alphabet_list():
	alphabet_list = []
	for char in get_upper_alphabet():
		alphabet_list.append(char)
	return alphabet_list


def get_sample(sample):
	base_dir = get_base_dir()
	sample_path = os.path.join(base_dir, 'data/samples/', sample)
	try:
		sample_data = codecs.open(sample_path, 'r', encoding='utf-8').read()
	except IOError as e:
		sample_data = ''

	return sample_data


def get_base_dir():
	return os.path.dirname(os.path.dirname(__file__))

def get_samples( filter_path = '' ):
	base_dir = get_base_dir()
	samples_dir = os.path.join(base_dir, 'data/samples/')
	filtered_dir = os.path.join(samples_dir, filter_path)
	all_files = list_files( filtered_dir )
	actual_files = []
	for file in all_files:
		file = file.replace(samples_dir, '').replace('\\', '/')
		if file not in actual_files:
			actual_files.append(file)
	return actual_files

def get_selected_samples( path = '' ):
	return get_option('samples', get_samples( path ))



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

def ordered_letter_count(input):
	return letter_count(input, True)

def letter_count(input, ordered = False):
		return_object = {}
		if ordered:
			return_object_tmp = []
			for char in get_upper_alphabet():
				return_object_tmp.append( input.upper().count(char) )
			i = 0
			for count in sorted(return_object_tmp, reverse=True):
				i = i + 1
				return_object[i] = count
		else:
			for char in get_upper_alphabet():
				return_object[char] = input.upper().count(char)
		return return_object


def percentage( numerator, denominator ):
	if denominator == 0:
		return 0
	else:
		return (numerator*10000 / denominator) / float(100)

"""
	Returns a number between -100 and 100 showing the linear proximity to the mean (values out of range are capped)

	+/-50 means the value is at the maximum/minimum and 100 means twice the distance from the mean to the max/min with default range_bound
"""
def linear_offset( value, mean_value, min_value, max_value, range_bound = 50):
	if value < mean_value:
		step = (mean_value - min_value) / range_bound	
	else:
		step = (max_value - mean_value) / range_bound
	linear_offset = (value - mean_value) / step

	if linear_offset < -100:
		return -100
	if linear_offset > 100:
		return 100
	return linear_offset

"""
Converts a linear offset into a color
"""
def linear_offset_color( linear_offset ):
	linear_offset = abs(linear_offset) * 5
	logging.error(linear_offset)
	if linear_offset <= 255:
		return 'rgb(' + str(int(round(linear_offset))) + ',255,0)'
	else:
		return 'rgb(255,' + str(int(round(510-linear_offset))) + ',0)'

def char_to_num(char):
	dictionary = {
		"a" : 0,
		"b" : 1,
		"c" : 2,
		"d" : 3,
		"e" : 4,
		"f" : 5,
		"g" : 6,
		"h" : 7,
		"i" : 8,
		"j" : 9,
		"k" : 10,
		"l" : 11,
		"m" : 12,
		"n" : 13,
		"o" : 14,
		"p" : 15,
		"q" : 16,
		"r" : 17,
		"s" : 18,
		"t" : 19,
		"u" : 20,
		"v" : 21,
		"w" : 22,
		"x" : 23,
		"y" : 24,
		"z" : 25
	}

	return dictionary[char.lower()]

def num_to_char(num):
	dictionary = {
		"0" : "a",
		"1" : "b",
		"2" : "c",
		"3" : "d",
		"4" : "e",
		"5" : "f",
		"6" : "g",
		"7" : "h",
		"8" : "i",
		"9" : "j",
		"10" : "k",
		"11" : "l",
		"12" : "m",
		"13" : "n",
		"14" : "o",
		"15" : "p",
		"16" : "q",
		"17" : "r",
		"18" : "s",
		"19" : "t",
		"20" : "u",
		"21" : "v",
		"22" : "w",
		"23" : "x",
		"24" : "y",
		"25" : "z"
	}

	return dictionary[str(num)].upper()



def sanitize_upper_alpha( input ):
	input = re.sub(r'\W+', '', input ).upper()
	input = re.sub(r'\d+', '', input)
	return input
