from scrapy.crawler import CrawlerProcess
from quotes_spider import QuotesSpider


def handler(event, context):
    message = 'Hello {} {}!'.format(event['first_name'],
                                    event['last_name'])

    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
        'FEED_FORMAT': 'json',
        'ITEM_PIPELINES': {'__main__.Pipeline': 1}
    })
    process.crawl(QuotesSpider)
    process.start()
    return {
        'message': message
    }

results = []
class Pipeline(object):
    def process_item(self, item, spider):
        print('process pipeline ', item)
        results.append(dict(item))

def main():
    handler({'first_name': 'f', 'last_name': 'l'}, None)

if __name__ == '__main__':
    main()