import webapp2
import json
import models

options = {}

class Request(webapp2.RequestHandler):
	def get_variables( self ):
		return {}


class ApiRequest( Request ):
	def get(self):
		option_names = self.request.get_all('option_names')
		global options
		options = {}
		for option in option_names:
			options[option] = self.request.get_all(option)
		response_object = self.do()
		response_object['options'] = options
		self.response.headers['Content-type'] = 'application/json'
		self.response.out.write( json.dumps(response_object) )

	def post(self):
		self.get()

	def do(self):
		return {
			'input': self.request.get('input')
		}