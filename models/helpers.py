import os
import jinja2
import funcs
import logging

jinja_environment = jinja2.Environment(
	loader=jinja2.FileSystemLoader(
		os.path.join(
			os.path.dirname(os.path.dirname(__file__)),
			 'templates/helpers'
			)
		)
	)

def ordered_letter_count( letter_count ):
	return letter_count( letter_count, True )

def letter_count( letter_count, ordered = False ):
	total = 0
	letter_freq = {}
	letter_height = {}
	min_letter_freq = {}
	max_letter_freq = {}
	maximum = 0
	selected_samples = funcs.get_selected_samples( 'en' )
	sample_total = 0
	full_sample = ''

	"""
		Work out letter frequency tables
	"""

	for sample in selected_samples:
		sample_maximum = 0
		sample_total = 0
		sample_content = funcs.get_sample(sample)

		full_sample = full_sample + sample_content
		sample_letter_count = funcs.letter_count(sample_content, ordered)
		sample_letter_freq = {}
		for char in sample_letter_count:
			sample_total = sample_total + sample_letter_count[char]
		for char in sample_letter_count:
			char_freq = funcs.percentage(sample_letter_count[char], sample_total)
			sample_letter_freq[char] = char_freq
			if char not in max_letter_freq or char_freq > max_letter_freq[char]:
				max_letter_freq[char] = char_freq
			if char not in min_letter_freq or char_freq < min_letter_freq[char]:
				min_letter_freq[char] = char_freq
			if char_freq > maximum:
				maximum = char_freq

	full_sample_letter_freq = {}
	full_sample_count = funcs.letter_count(full_sample, ordered)
	full_sample_total = 0
	linear_offset_color = {}
	linear_offset = {}
	total_linear_offset = 0
	for char in full_sample_count:
		full_sample_total = full_sample_total + full_sample_count[char]

	for char in full_sample_count:
		full_sample_letter_freq[char] = funcs.percentage(full_sample_count[char], full_sample_total)

	for char in letter_count:
		total = total + letter_count[char]

	for char in letter_count:
		char_freq = funcs.percentage(letter_count[char], total)
		char_linear_offset = funcs.linear_offset( char_freq, full_sample_letter_freq[char], min_letter_freq[char], max_letter_freq[char])
		linear_offset[char] = char_linear_offset
		total_linear_offset = total_linear_offset + abs(char_linear_offset)
		linear_offset_color[char] = funcs.linear_offset_color( char_linear_offset )
		letter_freq[char] = char_freq
		if char_freq > maximum:
			maximum = char_freq
		letter_height[char] = funcs.percentage(letter_count[char], maximum)


	template_variables = {
		'letter_count': letter_count,
		'letter_freq': letter_freq,
		'maximum': maximum,
		'denominator': maximum * 0.01,
		'sample_max': max_letter_freq,
		'sample_min': min_letter_freq,
		'sample_mean': full_sample_letter_freq,
		'selected_samples': selected_samples,
		'linear_offset_color': linear_offset_color,
		'total_linear_offset': int(round(total_linear_offset)),
		'linear_offset': linear_offset,
		'keys': sorted(letter_count.keys())
	}
	template = jinja_environment.get_template('freq.html')
	return template.render( template_variables )