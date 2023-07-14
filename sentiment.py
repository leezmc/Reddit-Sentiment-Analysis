import praw
from textblob import TextBlob

# Reddit App API Here
reddit = praw.Reddit(
    client_id='',
    client_secret='',
    # user_agent=''
)

subreddit_names = ['wallstreetbets', 'investing', 'stocks'] # Subreddits to search
stock_name = 'Facebook' # Stock to search

buy_count = 0
sell_count = 0
hold_count = 0

for subreddit_name in subreddit_names:
    subreddit = reddit.subreddit(subreddit_name)
    posts = subreddit.search(stock_name, limit=10)

    for post in posts:
        title_sentiment = TextBlob(post.title).sentiment.polarity
        body_sentiment = TextBlob(post.selftext).sentiment.polarity


        if title_sentiment > 0 or body_sentiment > 0:
            sentiment = 'Positive'
            buy_count += 1
        elif title_sentiment < 0 or body_sentiment < 0:
            sentiment = 'Negative'
            sell_count += 1
        else:
            sentiment = 'Neutral'
            hold_count += 1

        print('Subreddit:', subreddit_name)
        print('Title:', post.title)
        print('Sentiment:', sentiment)
        print('---')

if buy_count > sell_count:
    decision = 'Buy'
elif sell_count > buy_count:
    decision = 'Sell'
else:
    decision = 'Hold'

print('Sentiment Metrics for', stock_name)
print('Buy:', buy_count)
print('Sell:', sell_count)
print('Hold:', hold_count)
print('Decision:', decision)
