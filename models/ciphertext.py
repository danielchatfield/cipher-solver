from md5 import md5
import funcs


class Ciphertext():
	ciphertext = '';
	alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
	upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'

	hash = ''
	def __init__(self, ciphertext):
		self.ciphertext = ciphertext
		self.hash = md5(ciphertext.encode('utf-8')).hexdigest()

	def num_chars(self):
		return len(self.ciphertext)

	def has_punctuation(self):
		punctuation_list = '.,\'\\/":;'

		for punctuation in punctuation_list:
			if self.ciphertext.count(punctuation):
				return True
		return False

	def has_numbers(self):
		numbers = '0123456789'
		for number in numbers:
			if self.ciphertext.count(number):
				return True
		return False

	def has_alpha(self):
		alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
		for char in alphabet:
			if self.ciphertext.count(char):
				return True
		return False

	def has_upper(self):
		for char in self.upper_alphabet:
			if self.ciphertext.count(char):
				return True
		return False

	def has_lower(self):
		for char in self.lower_alphabet:
			if self.ciphertext.count(char):
				return True
		return False

	def is_upper(self):
		return self.ciphertext == self.ciphertext.upper()

	def is_lower(self):
		return self.ciphertext == self.ciphertext.lower()

	def num_alpha_chars(self):
		count = 0
		for char in self.alphabet:
			count = count + self.ciphertext.count(char)
		return count

	def is_cached(self, id):
		return False

	def get_cached(self, id):
		return ''

	def ordered_letter_count(self):
		id = 'ordered_letter_count'
		if self.is_cached(id):
			return self.get_cached(id)
		else:
			return funcs.ordered_letter_count(self.ciphertext)


	def letter_count(self):
		return_object = {}
		for char in self.upper_alphabet:
			return_object[char] = self.ciphertext.upper().count(char)
		return return_object



	def serialize(self):
		return_object = {
			'hash': self.hash,
			'num_chars': self.num_chars(),
			'num_alpha_chars': self.num_alpha_chars(),
			'has_punctuation': self.has_punctuation(),
			'has_numbers': self.has_numbers(),
			'has_alpha': self.has_alpha(),
			'has_upper': self.has_upper(),
			'has_lower': self.has_lower(),
			'is_upper': self.is_upper(),
			'is_lower': self.is_lower(),
			'letter_count': self.letter_count(),
			'ordered_letter_count': self.ordered_letter_count()
		}

		return return_object

	def get_alpha_list(self):
		alpha = []

		for char in self.upper_alphabet:
			alpha.append(char)

		return alpha

	def objects(self):
		return {
			'bool_values' : [
				'has_alpha',
				'has_numbers',
				'has_punctuation',
				'has_upper',
				'has_lower',
				'is_upper',
				'is_lower'
			],
			'num_values' : [
				'num_chars',
				'num_alpha_chars'
			],
			'html_values' : [
			],
			'ignored_values': [
				'hash'
			]
		}

