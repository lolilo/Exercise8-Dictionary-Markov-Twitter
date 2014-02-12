# https://pypi.python.org/pypi/twitter
# https://dev.twitter.com/docs
# http://wilsonericn.wordpress.com/2011/08/22/tweeting-in-python-the-easy-way/
# application name: markovtweetsalot

from twitter import *

twitter = Twitter(
            auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET,
                       CONSUMER_KEY, CONSUMER_SECRET)
           )
# twitter = Twitter(
# |        auth=OAuth(token, token_key, con_secret, con_secret_key))


# t.statuses.home_timeline()

"""
my_auth = twitter.OAuth(TOKEN,TOKEN_KEY,CON_SEC,CON_SEC_KEY)
twit = twitter.Twitter(auth=my_auth)
twit.statuses.update(status="I'm tweeting from Python!")
"""