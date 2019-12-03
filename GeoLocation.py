import json
import requests

class Location():
	def __init__(self,APIKEY):
		self.APIKEY	 = APIKEY

	def geoLocation(self,address):
		response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address='+address+'&key='+self.APIKEY)
		
		if response.status_code!=200:
			raise ApiError(response.status_code)
		else:
			response_content = response.json()
			response_result  = response_content['results'][0]['geometry']['location']
			return response_result['lat'],response_result['lng']


locationObject = Location('')
print(locationObject.geoLocation('1600+Amphitheatre+Parkway,+Mountain+View,+CA'))
