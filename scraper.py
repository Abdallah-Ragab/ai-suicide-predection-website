from ntscraper import Nitter

class Scraper:
    tweet_limit = 5
    def __init__(self):
        self.scraper = Nitter(instances=['https://nitter.esmailelbob.xyz'])

    def user(self, username):
        return self.scraper.get_profile_info(username)

    def tweets(self, username):
        try:
            return self.scraper.get_tweets(username, mode='user', number=self.tweet_limit)
        except Exception as e:
            return str(e)


class cli:
    def __init__(self):
        self.scraper = Scraper()
        self.welcome()

    def welcome(self):
        print('Welcome to the Twitter Scraper CLI')
        print('-----------------------------------')
        self.prompt()

    def prompt(self):
        print('Enter a username to scrape (\'q\' to quit):')
        username = input()
        if username == 'q':
            exit()
        print('Scraping tweets...')
        tweets = self.scraper.tweets(username)
        print(tweets)
        self.prompt()


cli()
