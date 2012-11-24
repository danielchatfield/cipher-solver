import jinja2
import os
from models.models import ApiRequest
from models.ciphertext import Ciphertext
import models.helpers as helpers
import models.funcs as funcs

jinja_environment = jinja2.Environment(
	loader=jinja2.FileSystemLoader(
		os.path.join(
			funcs.get_base_dir(),
			 'templates/sections'
			)
		)
	)

class Split(ApiRequest):
	def do(self):
		response_object = ApiRequest.do(self)
		input = funcs.sanitize_upper_alpha(response_object['input'])
		split_count = int(self.request.get('split_count'))
		output = {}
		for i in range(len(input)):
			char = input[i]
			j = i % split_count
			if j not in output:
				output[j] = ''
			output[j] = output[j] + char

		template = jinja_environment.get_template( 'split.html' )
		template_variables = {
			'output': output
		}
		response_object['output'] = template.render( template_variables )
		return response_object