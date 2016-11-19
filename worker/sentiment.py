import json
from watson_developer_cloud import AlchemyLanguageV1

API_KEY='b4e9c20260c444b37c1a34a8265b04f4e17dce4d'

alchemy_language = AlchemyLanguageV1(api_key=API_KEY)
def getdata(tmsg):
	return json.dumps(alchemy_language.sentiment(text=tmsg), indent=2)