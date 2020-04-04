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
            '//div[@class="div-name-in-table"]')

        for player_name in players_name:
            item = NhldotcomItem()
            item['name'] = player_name.xpath(
                './/div[2]/div/a/text()'
            ).extract()[0]
            item['position'] = player_name.xpath(
                './/div/div/@data-content'
            ).extract()[0]

            yield item
