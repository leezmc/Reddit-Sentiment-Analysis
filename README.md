
# Reddit-Sentiment-Analysis

This project performs sentiment analysis on Reddit posts related to a specific stock. It uses the Python library PRAW (Python Reddit API Wrapper) to access Reddit's API and the TextBlob library for sentiment analysis.


## Requirements
* Install the latest version of [Python 3.X](https://www.python.org/downloads/).
* PRAW library
* TextBlob library


## Installation

* Clone respoitory

* Install Praw and Texblob
```bash
  pip install praw textblob
```
    
## Usage/Examples

* Insert Reddit App API credentials in quotation marks.
```python
reddit = praw.Reddit(
    client_id='',
    client_secret='',
)
```
* Replace subreddits and stocks to search.

```python
subreddit_names = ['wallstreetbets', 'investing', 'stocks'] 
stock_name = 'Facebook' 
```




## License

[MIT](https://choosealicense.com/licenses/mit/)

