from models.models import ApiRequest
from models.ciphertext import Ciphertext
import models.helpers as helpers


class Cryptanalysis(ApiRequest):
	def do(self):
		response_object = ApiRequest.do(self)
		ciphertext = Ciphertext(response_object['input'])
		response_object['output'] = self.do_filters(ciphertext.serialize())
		response_object['objects'] = self.do_object_filters(ciphertext.objects())
		return response_object

	def do_filters(self, output):
		output = self.letter_count_graph(output)
		return output

	def do_object_filters(self, objects):
		objects['html_values'].append('letter_count_graph')
		return objects

	def letter_count_graph(self, output):
		letter_count = output['letter_count']
		output['letter_count_graph'] = helpers.letter_count(letter_count)
		return output