import os
import jinja2
import funcs

jinja_environment = jinja2.Environment(
	loader=jinja2.FileSystemLoader(
		os.path.join(
			os.path.dirname(os.path.dirname(__file__)),
			 'templates/helpers'
			)
		)
	)

def letter_count( letter_count ):
	total = 0
	letter_freq = {}
	letter_height = {}
	min_letter_freq = {}
	max_letter_freq = {}
	maximum = 0
	selected_samples = funcs.get_selected_samples()
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
		sample_letter_count = funcs.letter_count(sample_content)
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
	full_sample_count = funcs.letter_count(full_sample)
	full_sample_total = 0
	for char in full_sample_count:
		full_sample_total = full_sample_total + full_sample_count[char]

	for char in full_sample_count:
		full_sample_letter_freq[char] = funcs.percentage(full_sample_count[char], full_sample_total)

	for char in letter_count:
		total = total + letter_count[char]

	for char in letter_count:
		char_freq = funcs.percentage(letter_count[char], total)
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
		'keys': funcs.get_upper_alphabet_list()
	}
	template = jinja_environment.get_template('freq.html')
	return template.render( template_variables )