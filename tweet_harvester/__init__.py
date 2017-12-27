from flask import Flask, json, request
import tweepy

# Init app with proper name
app = Flask(__name__)

# Load config
app.config.from_object('config')

# Setup tweepy auth
# auth = tweepy.OAuthHandler(app.config['TWITTER_CONSUMER_KEY'],
#                            app.config['TWITTER_CONSUMER_SECRET'])
# auth.set_access_token(app.config['TWITTER_ACCESS_TOKEN'],
#                       app.config['TWITTER_ACCESS_TOKEN_SECRET'])
# tweepy_api = tweepy.API(auth)


@app.route('/test')
def hello_world():
    return '<h1>Hello World</h1>'


def get_tweets(username):
    """Gets a list of tweets for a given user.

    Args:
        username (str): -

    Returns:
        list[dict]: list of all valid tweets
    """
    def tweet_map_func(t):
        return {'tweet': t.text,
                'created_at': t.created_at,
                'username': username,
                'headshot_url': t.user.profile_image_url
                }

    out = list(map(tweet_map_func,
                   tweepy_api.user_timeline(screen_name=username)))

    return out
