import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("gNW2Brpd93yq64KMViFajYm20", 
    "9QnVAejckcBKzcKz5Hw6uqmZdNwQXnqpCJDgnRlUF6gDwxWpKG")
auth.set_access_token("864553373026136064-HhGQUR71VsiJGE6arUNrtgxu1BmRAqt", 
    "O5nYk5VrXvZHzn72qBYmkfTmeihKPvpgvEIdEAqEqzry1")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

api.update_status("Hello World");