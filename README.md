# custom app by sebastien morneau

NHL Home Draft

## GET Scrapy for Pyhton

Looking for a website to extract the nhl player

```
https://www.lepool.com/nhl/predictions
```

```python
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
```
