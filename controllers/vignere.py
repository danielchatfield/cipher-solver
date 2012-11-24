from models.models import ApiRequest
from models.ciphertext import Ciphertext
import models.helpers as helpers
import models.funcs as funcs

def get_vignere_table():
	"""
		Constructs a table of form:

		{
			[col index]: {
				[row index]: [element]
				...
			}
			...
		}
	"""
	vignere_table = {}
	for col in funcs.get_upper_alphabet():
		vignere_table[char] = {}
		for row in funcs.get_upper_alphabet():
			offset = funcs.char_to_num(col)
			base = funcs.char_to_num(row)
			vignere_table[col][row] = funcs.num_to_char((offset + base)%26)

	return vignere_table