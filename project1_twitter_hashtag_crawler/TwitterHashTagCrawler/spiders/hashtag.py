# -*- coding: utf-8 -*-
import scrapy
import ipdb
import re
from dateutil import parser
import sys
from scrapy.crawler import CrawlerProcess
from utils import get_links, get_hashtags, get_mentions
import logging

class HashtagSpider(scrapy.Spider):
    name = 'twittercrawler'
    allowed_domains = ["twitter.com"]

    # custom settings for user agent and proxy. Default will get chrome as user agent  and use a proxypool of 50 .
    # Override here
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Safari/537.36',
        'CONCURRENT_REQUESTS': 5, 'DOWNLOAD_DELAY': 0, 'LOG_LEVEL': 'INFO'}

    def __init__(self, filename=''):
        if not filename:
            sys.exit('Please provide the input filename also. Example \n\n$ python3 hashtags.py myinput.csv')
        self.filename = filename

    # the crawler will execute start_requests function at first.
    def start_requests(self):
        with open(self.filename, 'r') as f:
            hashtags = f.read().splitlines()
        if len(hashtags) == 0:
            sys.exit('Emplty File detected.Please provide hashtags separated by newlines')
        else:
            logging.info(f'{len(hashtags)} hashtags found')
        for hashtag in hashtags:
            if hashtag:
                search_url = "https://mobile.twitter.com/hashtag/" + hashtag.lower()

                yield scrapy.Request(search_url, callback=self.find_tweets, dont_filter=True)

    def find_tweets(self, response):
        tweets = response.xpath('//table[@class="tweet  "]/@href').getall()
        logging.info(f'{len(tweets)} tweets found')
        for tweet_id in tweets:
            tweet_id = re.findall("\d+", tweet_id)[-1]
            tweet_url = 'https://twitter.com/anyuser/status/' + \
                        str(tweet_id)
            yield scrapy.Request(tweet_url, callback=self.parse_tweet)

        # finding and visiting next page
        next_page = response.xpath(
            '//*[@class="w-button-more"]/a/@href').get(default='')
        logging.info('Next page found:')
        if next_page != '':
            next_page = 'https://mobile.twitter.com' + next_page
            yield scrapy.Request(next_page, callback=self.find_tweets)

    def parse_tweet(self, response):
        logging.info('Processing --> ' + response.url)
        username = response.xpath(
            '//*[@class="permalink-inner permalink-tweet-container"]//*[@class="username u-dir u-textTruncate"]/b/text()').get(
            default='')
        full_name = response.xpath(
            '//*[@class="permalink-inner permalink-tweet-container"]//*[@class="FullNameGroup"]/strong/text()').get(
            default='')
        
        try:
            tweet_text = response.xpath('//title/text()').get(default='').split(':')[1].strip()
            
        except:
            tweet_text = ' '.join(response.xpath(
                '//*[contains(@class,"permalink-inner permalink-tweet-container")]//*[@class="js-tweet-text-container"]/p//text()').getall()).strip()
        image_list = response.xpath(
            '//*[contains(@class,"permalink-inner permalink-tweet-container")]//*[@class="AdaptiveMediaOuterContainer"]//img/@src').getall()
        date_time = response.xpath(
            '//*[contains(@class,"permalink-inner permalink-tweet-container")]//*[@class="js-tweet-details-fixer tweet-details-fixer"]/div[@class="client-and-actions"]/span[@class="metadata"]/span/text()').get(
            default='')

        date_time = parser.parse(date_time.replace('-', '')).strftime('%Y-%m-%d %H:%M:%S')
        retweets = response.xpath(
            '//*[contains(@class,"permalink-inner permalink-tweet-container")]//*[@class="js-tweet-details-fixer tweet-details-fixer"]/div[@class="js-tweet-stats-container tweet-stats-container"]//*[@class="js-stat-count js-stat-retweets stat-count"]/a/strong/text()').get(
            default='')

        likes = response.xpath(
            '//*[contains(@class,"permalink-inner permalink-tweet-container")]//*[@class="js-tweet-details-fixer tweet-details-fixer"]/div[@class="js-tweet-stats-container tweet-stats-container"]//*[@class="js-stat-count js-stat-favorites stat-count"]/a/strong/text()').get(
            default='')
        replies = response.xpath(
            '//*[contains(@class,"permalink-inner permalink-tweet-container")]//*[contains(@id,"profile-tweet-action-reply-count")]/parent::span/@data-tweet-stat-count').get(
            default='')
        
        mentions = get_mentions(tweet_text)
        hashtags = get_hashtags(tweet_text)
        cta = get_links(tweet_text)

        result = {
            'username': username.lower(),
            'full_name': full_name,
            'twitter_url': response.url,
            'tweet_text': tweet_text,
            'tweet_time': str(date_time),
            'number_of_likes': str(likes),
            'no_of_retweets': str(retweets),
            'no_of_replies': str(replies),
            'mentions': ' | '.join(mentions),
            'no_of_mentions': str(len(mentions)),
            'hashtags': ' | '.join(hashtags),
            'no_of_hashtags': str(len(hashtags)),
            'call_to_action': ' | '.join(cta),
            'image_url': ' | '.join(image_list),

        }
        yield result
        
