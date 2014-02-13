# application name: markovtweetsalot

# https://github.com/bear/python-twitter

import twitter
import os

twitter_key = os.environ.get("TWITTER_API_KEY")

api = twitter.Api(consumer_key=twitter_key,
                      consumer_secret='3eJ8bU5H4AXLWDNBakoB9F73dDiuzTP5Hy3UlDNU3E',
                      access_token_key='253795390-BCkmp8CqrVZJG0AINXfO1MfKyHrBYsnmOXnhsx64',
                      access_token_secret='D3LtIMOBvbm54An7YgiUMLJe1HO0tlDnNXXzLuynZqy58')


# print api.VerifyCredentials()

status = api.PostUpdate('I love python-twitter!')

"""
TO-DO Check with other versions? 

my_auth = twitter.OAuth(TOKEN,TOKEN_KEY,CON_SEC,CON_SEC_KEY)
twit = twitter.Twitter(auth=my_auth)
twit.statuses.update(status="I'm tweeting from Python!")
"""