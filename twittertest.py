# application name: markovtweetsalot

# https://code.google.com/p/python-twitter/
# https://github.com/bear/python-twitter

# https://pypi.python.org/pypi/twitter
# https://dev.twitter.com/docs
# http://wilsonericn.wordpress.com/2011/08/22/tweeting-in-python-the-easy-way/

import twitter
import os

twitter_key = os.environ.get("TWITTER_API_KEY")

api = twitter.Api(consumer_key=twitter_key,
                      consumer_secret='3eJ8bU5H4AXLWDNBakoB9F73dDiuzTP5Hy3UlDNU3E',
                      access_token_key='253795390-BCkmp8CqrVZJG0AINXfO1MfKyHrBYsnmOXnhsx64',
                      access_token_secret='D3LtIMOBvbm54An7YgiUMLJe1HO0tlDnNXXzLuynZqy58')


print api.VerifyCredentials()

"""
my_auth = twitter.OAuth(TOKEN,TOKEN_KEY,CON_SEC,CON_SEC_KEY)
twit = twitter.Twitter(auth=my_auth)
twit.statuses.update(status="I'm tweeting from Python!")
"""