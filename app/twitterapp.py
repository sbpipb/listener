from flask import Flask, render_template, request
from app import app
import twitter, json
from app import views, db, models
import datetime
# app = Flask(__name__)  // i don't know what the fuck this means

def twitter_auth():
	#checking import twitter
	#add this to config file
	CONSUMER_KEY = 'd7tKl4qajMQmpwjIbPw'
	CONSUMER_SECRET ='v5Utf5ewYrKdLe7VIHiNLBiPehSdG5gDoqEbPfHRB8A'
	OAUTH_TOKEN = '126343897-sT0c0Fpt6qzrd91TiBbGlPWS3Uov9Z1yhtG6c2on'
	OAUTH_TOKEN_SECRET = 'uFe1tYjoxX5Tf0o5NjHo0wKxTyzvGEPL3GmoRp0LlCDkD'
	#add this to config file

	auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)
	twitter_api = twitter.Twitter(auth=auth)
	return twitter_api

@app.route('/trends/show')
def show_trends():
	trends = models.Trends.query.all()
	for t in trends:
		print t.keyword, t.woe_id, t.woe_code, t.timestamp
	return render_template('results.html', result=trends)

@app.route('/trends/<path:country_code>') 
def get_trending_keywords(country_code):
	
	# if views.checkIfLogin() == True:
	# 	return 'Loginned'
	# else:
	# 	return "F"
	
	login = views.checkIfLogin()
	if login == False:
		return 'False'
	# else:
		# return 'true20'

	country_code = country_code.upper()
	
	#add this to config file, 
	WOE_ID = {		
				'global':1, 
				'PH':23424934,
				'US':23424977
	}

	
	if country_code in WOE_ID:
		country_exists = True
	else:
		country_exists = False

	if country_exists:

		#start twitter authenticate
		twitter_api = twitter_auth()

		trends_results = twitter_api.trends.place(_id=WOE_ID[country_code])
				
		list = []

		if trends_results:

			#file uploading
			# f = request.files['the_file']
			# f.save()

			for child in trends_results:

				if child['locations']:
					for sub in child['locations']:
						country_code = sub['woeid']
						country_name = sub['name']

				if child['trends']:
		    			for subchild in child['trends']:
		        			
		        			if subchild['name']:
		        				list.append(subchild['name'])
		        				# print subchild['name'].encode('utf-8')+subchild['query'].encode('utf-8')+subchild['name'].encode('utf-8')
		        				
						t = models.Trends(keyword=subchild['name'].encode('utf-8'), woe_id=country_code, woe_code=country_name, timestamp = datetime.datetime.utcnow() )
						db.session.add(t)
						db.session.commit()

			result = 'Got trending keywords from Twitter  in  %s' % country_code;		
		
	else:
		message =  'This feature is not available for this country'
		result =  message
		# return result

	return render_template('results.html', result=result)

@app.route('/search/<path:keyword>')
def search_keyword(keyword):
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

	return 'Search for' + keyword