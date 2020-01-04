
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

2. Run the crawler with your hashtag file and the desired [output formats](https://docs.scrapy.org/en/latest/topics/feed-exports.html)(JSON,JSON lines,CSV,XML)

* For csv
   ```sh
    scrapy crawl twittercrawler -a filename=myhashtags.csv -o mydata.csv

   ```
   
* For JSON
   ```sh
    scrapy crawl twittercrawler -a filename=myhashtags.csv -o mydata.json

   ```


## Development setup

Describe how to install all development dependencies and how to run an automated test-suite of some kind. Potentially do this for multiple platforms.

```sh
make install
npm test
```

## Release History

* 0.2.1
    * CHANGE: Update docs (module code remains unchanged)
* 0.2.0
    * CHANGE: Remove `setDefaultXYZ()`
    * ADD: Add `init()`
* 0.1.1
    * FIX: Crash when calling `baz()` (Thanks @GenerousContributorName!)
* 0.1.0
    * The first proper release
    * CHANGE: Rename `foo()` to `bar()`
* 0.0.1
    * Work in progress

## Meta

Your Name – [@YourTwitter](https://twitter.com/dbader_org) – YourEmail@example.com

Distributed under the XYZ license. See ``LICENSE`` for more information.

[https://github.com/yourname/github-link](https://github.com/dbader/)

## Contributing

1. Fork it (<https://github.com/yourname/yourproject/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

<!-- Markdown link & img dfn's -->
[npm-image]: https://img.shields.io/npm/v/datadog-metrics.svg?style=flat-square
[npm-url]: https://npmjs.org/package/datadog-metrics
[npm-downloads]: https://img.shields.io/npm/dm/datadog-metrics.svg?style=flat-square
[travis-image]: https://img.shields.io/travis/dbader/node-datadog-metrics/master.svg?style=flat-square
[travis-url]: https://travis-ci.org/dbader/node-datadog-metrics
[wiki]: https://github.com/yourname/yourproject/wiki
