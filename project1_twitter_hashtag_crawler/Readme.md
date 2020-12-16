#### Depricated. No longer maintained.

# Twitter Hashtag crawler
> A fast and unofficial twitter crawler to collect tweets using hashtag search.

> Notice: The crawler is meant to be used for collecting data purely for academic and research purpose only. I am not responsible for any legal issue that might arise for any unintended use of this crawler

[![Python 3](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![twitter crawler](https://img.shields.io/badge/twittercrawler-1.0-green)](https://github.com/amitupreti/Hands-on-WebScraping/tree/master/project1_twitter_hashtag_crawler)

This is written using scrapy and python. The logic is straight forward. We are simply sending get requests to the mobile version of the twitter(mobile.twitter.com) to collect the list of tweets and sending get requests to the web version to parse tweet details.
![](header.png)

## Installation

OS X & Linux:

1. Download the project

```sh
git clone https://github.com/amitupreti/Hands-on-WebScraping

cd Hands-on-WebScraping/project1_twitter_hashtag_crawler
```
2. Install the dependencies

```sh
pip install -r requirements.txt --user
```

3. Verify the crawler spider exists

```sh
scrapy list
```
if you see `twittercrawler` than you are all set.


Windows:
1. Install [python3](https://www.python.org/downloads/) if you haven't already
2. Download the project. https://github.com/amitupreti/Hands-on-WebScraping/archive/master.zip
3. Extract the project 
4. Open cmd and navigate inside the project directory
```sh
cd Hands-on-WebScraping/project1_twitter_hashtag_crawler
```
5. Follow step 2 and 3 from Mac/Linux installation



## Usage example

1. Put the hashtags in a csv file seperated by new line. For example, I have included `myhashtags.csv` as a sample.

![Hashtags file](https://i.paste.pics/225079df0d3dc27d66430b1553b2ac39.png)

2. Run the crawler with your hashtag file and the desired [output formats] (https://docs.scrapy.org/en/latest/topics/feed-exports.html)(JSON,JSON lines,CSV,XML)

* For csv
   ```sh
    scrapy crawl twittercrawler -a filename=myhashtags.csv -o mydata.csv

   ```
   
* For JSON
   ```sh
    scrapy crawl twittercrawler -a filename=myhashtags.csv -o mydata.json

   ```
![sample images](https://i.paste.pics/4a5826a6a090522e5326bb11838258df.png)
![sample images](https://i.paste.pics/68a64bab743150e00af4cd9eea9af8dc.png)


### Speeding up the crawls
If you feel like the crawler is a little slow then find the hashtag.py file in the project and edit the custom settings.
```py
custom_settings = {
    'USER_AGENT': 'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Safari/537.36',
    'CONCURRENT_REQUESTS': 2, 'DOWNLOAD_DELAY': 1, 'LOG_LEVEL': 'INFO'}
```
> Here CONCURRENT_REQUESTS is the number of URLs that will be processed parallelly and DOWNLOAD_DELAY is a wait between each  request. So, Increase CONCURRENT_REQUESTS and decrease DOWNLOAD_DELAY (minimum value for download delay is 0).


## Data Columns
* username
* full_name
* twitter_url
* tweet_text
* tweet_time
* number_of_likes
* no_of_retweets
* no_of_replies
* mentions
* no_of_mentions
* hashtags
* no_of_hashtags
* call_to_action
* image_url

## Release History

* 1.0.0
    * first release crawl by hashtags

## Meta

Amit Upreti – [@amitupreti](https://www.linkedin.com/in/amitupreti/) 

Distributed under the MIT license. See ``LICENSE`` for more information.


## Contributing

1. Fork it (<https://github.com/amitupreti/Hands-on-WebScraping/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
