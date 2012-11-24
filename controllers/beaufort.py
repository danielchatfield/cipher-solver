from models.models import ApiRequest
from models.ciphertext import Ciphertext
import models.helpers as helpers
import vignere

def decrypt(input, key):
	beaufort_table = get_beaufort_table()
	sanitized_input = funcs.sanitize_upper_alpha(input)
	key = key.upper()
	key_length = len(key)
	i = 0
	output = ''
	for char in sanitized_input:
		j = i % key_length
		current_key = key[j]
		output = output + beaufort_table[char][current_key]
		i = i + 1
	

def get_beaufort_table():
	"""
		Construct table in form:

		{
			[col index]: {
				[element]: [row index]
				...
			}
			...
		}
	"""
	vignere_table = vignere.get_vignere_table()
	beaufort_table = {}

	for col in vignere_table:
		beaufort_table[col] = {}
		for row in vignere_table[col]:
			element = vignere_table[col][row]
			beaufort_table[col][element] = row

	return beaufort_table

def encrypt(input, key):
	return decrypt(input,key)


class DecryptBeaufort(ApiRequest):
	def do(self):
		response_object = ApiRequest.do(self)
		key = self.request.get( 'key' )
		response_object['key'] = key
		response_object['output'] = decrypt(response_object['input'], key)
		return response_object
