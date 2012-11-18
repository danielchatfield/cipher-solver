from models.models import ApiRequest
import models.helpers as helpers
from models.funcs import *

class LoadSample(ApiRequest):
	def do(self):
		response_object = ApiRequest.do(self)
		sample = self.request.get('sample_name')
		output = get_sample(sample + '.txt')
		response_object['sample'] = sample
		response_object['output'] = output
		return response_object