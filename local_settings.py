MY_CONSUMER_KEY = 'XEkEFTRLILyEYTuOZs1b9oFp4'
MY_CONSUMER_SECRET = 'wPpsIfFsZFg92XepcD3kNCSHlmBKoMBzp9jBoK8ag7WJ2JYbLM'
MY_ACCESS_TOKEN_KEY = '897973893440434176-hmqqmnNIcJDWT5hPgDknHMOCxwguGdw'
MY_ACCESS_TOKEN_SECRET = 'DxoXvmlWCaOm6BuRVgDvR6lNjQvql48yte3wHBr3sihuU'

SOURCE_ACCOUNTS = ["cath0lic_guilt"] #A list of comma-separated, quote-enclosed Twitter handles of account that you'll generate tweets based on. It should look like ["account1", "account2"]. If you want just one account, no comma needed.
ODDS = 3 #How often do you want this to run? 1/8 times?
ORDER = 2 #how closely do you want this to hew to sensical? 1 is low and 3 is high.
DEBUG = False #Set this to False to start Tweeting live
STATIC_TEST = False #Set this to True if you want to test Markov generation from a static file instead of the API.
TEST_SOURCE = ".txt" #The name of a text file of a string-ified list for testing. To avoid unnecessarily hitting Twitter API. You can use the included testcorpus.txt, if needed.
TWEET_ACCOUNT = "quintybot" #The name of the account you're tweeting to.
