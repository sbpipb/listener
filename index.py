import twitter, json
from flask import Flask
app = Flask(__name__)


@app.route('/trends/<path:country_code>')
def get_trending_keywords(country_code):

	CONSUMER_KEY = 'd7tKl4qajMQmpwjIbPw'
	CONSUMER_SECRET ='v5Utf5ewYrKdLe7VIHiNLBiPehSdG5gDoqEbPfHRB8A'
	OAUTH_TOKEN = '126343897-sT0c0Fpt6qzrd91TiBbGlPWS3Uov9Z1yhtG6c2on'
	OAUTH_TOKEN_SECRET = 'uFe1tYjoxX5Tf0o5NjHo0wKxTyzvGEPL3GmoRp0LlCDkD'

	auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

	twitter_api = twitter.Twitter(auth=auth)
	WOE_ID = {'global':1, 
				'PH':23424934,
				'US':23424977
	}

	# us_trends = twitter_api.trends.place(_id=WOE_ID['PH'])
	q = '#pba' 
	count = 30	
	lang = 'us' #tl
	result_type = 'popular'
	until ='2014-03-21'

	search_results = twitter_api.search.tweets(q=q, count=count,  until=until)
	statuses = search_results['statuses']
	# print statuses

	for _ in range(5):
		print "Length of statuses", len(statuses)
		# try:
			# next_results = search_results['search_metadata']['next_results']
		# except KeyError, e: # No more results when next_results doesn't exist
			# break

	return 'done'
	results =  json.dumps(us_trends, indent=1)
	return results

	country_code = country_code.rstrip('/');
	return 'Get trending keywords in  %s' % country_code;



@app.route('/')
def hello_world():
	return 'Welcome to index page!'


if __name__ == '__main__':
		app.run(debug=True)