from ntscraper import Nitter

class Scraper:
    tweet_limit = 50
    def __init__(self):
        self.scraper = Nitter()

    def user(self, username):
        return self.scraper.get_profile_info(username)

    def tweets(self, username):
        try:
            return self.scraper.get_tweets(username, mode='user', number=self.tweet_limit, language='en')
        except Exception as e:
            return str(e)




s = Scraper()
print(s.user('elonmusk'))
