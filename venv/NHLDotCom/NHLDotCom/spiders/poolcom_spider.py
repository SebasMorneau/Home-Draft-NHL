from scrapy import Spider
from scrapy.selector import Selector

from NHLDotCom.items import NhldotcomItem


class poolcomSpider(Spider):
    name = "poolcom"
    allowed_domains = ["lepool.com"]
    start_urls = [
        "https://www.lepool.com/nhl/predictions",
    ]

    def parse(self, response):
        players_name = Selector(response).xpath(
            '//div[@class="div-name-in-table"]//div[2]//div')

        for player_name in players_name:
            item = NhldotcomItem()
            item['title'] = player_name.xpath(
                './/a/@href'
            ).extract()[0]

            yield item
