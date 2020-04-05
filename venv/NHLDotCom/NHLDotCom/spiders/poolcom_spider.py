from scrapy import Spider
from scrapy.selector import Selector

from NHLDotCom.items import NhldotcomItem

import os


class poolcomSpider(Spider):
    name = "poolcom"
    allowed_domains = ["lepool.com"]
    start_urls = [
        "https://www.lepool.com/nhl/print/tous-les-joueurs/2019-2020/predictions",
    ]

    if os.path.exists("items.json"):
        os.remove("items.json")
    else:
        print("The file does not exist")

    def parse(self, response):
        players_name = Selector(response).xpath(
            '//*[@class="table-players table-players-tous-les-joueurs"]//tr')

        for player_name in players_name[1:]:
            item = NhldotcomItem()
            item['player'] = player_name.xpath(
                'normalize-space(.//td[2]/div/div[2]/div/text())'
            ).extract()[0]
            item['position'] = player_name.xpath(
                './/td[2]/div/div/div/@data-content'
            ).extract()[0]
            if item['position'] == 'Attaquant'or item['position'] == 'Défenseur':
                item['goals'] = player_name.xpath(
                    'normalize-space(.//td[5]/text()[last()])'
                ).extract()[0]
                item['assists'] = player_name.xpath(
                    'normalize-space(.//td[6]/text()[last()])'
                ).extract()[0]
            if item['position'] == 'Gardien':
                item['vic'] = player_name.xpath(
                    'normalize-space(.//td[7]/text()[last()])'
                ).extract()[0]
                item['dp'] = player_name.xpath(
                    'normalize-space(.//td[9]/text()[last()])'
                ).extract()[0]
                item['bl'] = player_name.xpath(
                    'normalize-space(.//td[10]/text()[last()])'
                ).extract()[0]

            yield item
