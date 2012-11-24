#!/usr/bin/env python
import jinja2
import os
import webapp2
from models.models import Request, ApiRequest
from controllers.get_section import GetSection
from controllers.cryptanalysis import Cryptanalysis
from controllers.load_sample import LoadSample
from controllers.split import Split
from controllers.beaufort import DecryptBeaufort
from google.appengine.api import channel
from google.appengine.api import users



class MainPage(Request):
	"""This page is responsible for rendering the UI and setting up the channel to send/recieve data."""
	def get(self):
		user = users.get_current_user()
		if not user:
			self.redirect(users.create_login_url(self.request.uri))
			return

		template = jinja_environment.get_template('index.html')
		core_sections = [
			'input',
			'cryptanalysis',
			'options_samples',
			'options_samples-cipher_challenge'
		]
		main_sections = [
			'caesar'
		]
		template_values = {
			'token': channel.create_channel(user.user_id() + 'stream'),
			'user': user,
			'signout_url': users.create_logout_url(self.request.uri),
			'core_sections': core_sections,
			'main_sections': main_sections
		}
		self.response.out.write( template.render(template_values) )





jinja_environment = jinja2.Environment(
	loader=jinja2.FileSystemLoader(
		os.path.join(
			os.path.dirname(__file__),
			 'templates'
			)
		)
	)
app = webapp2.WSGIApplication([
	('/', MainPage),
	('/api/get_section/', GetSection),
	('/api/cryptanalysis/', Cryptanalysis),
	('/api/split/', Split),
	('/api/decrypt_beaufort/', DecryptBeaufort),
	('/api/load_sample/', LoadSample)
	],
	debug=True )
