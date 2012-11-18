import jinja2
import os
from models.models import Request, ApiRequest
from models import funcs

jinja_environment = jinja2.Environment(
	loader=jinja2.FileSystemLoader(
		os.path.join(
			funcs.get_base_dir(),
			 'templates/sections'
			)
		)
	)

class GetSection(ApiRequest):
	def do(self):
		section_id = self.request.get('section')
		column = self.request.get('column')
		section = section_id.split('-')[0]

		core_sections = [
			'input',
			'plaintext',
			'cryptanalysis'
		]
		section_names = {
			'ciphertext': 'Ciphertext'
		}
		if column != 'left' and column != 'right':
			if section in core_sections:
				column = 'left'
			else:
				column = 'right'
		if section in section_names:
			section_name = section_names[section]
		else:
			section_name = section
		template = jinja_environment.get_template(section + '.html')
		template_values = {
			'section_id': section_id,
			'section_name': section_name,
			'funcs': funcs
		}
		return {
			'section': template.render( template_values ),
			'column': column
		}