__author__ = 'Administrator'

import scrapy
from Lotto_Scrapy.items import LottoItem


class LottoSpider(scrapy.Spider):
    name = "lotto"
    allowed_domains = ["http://www.nlotto.co.kr/"]
    start_urls = [
        "http://www.nlotto.co.kr/lotto645Confirm.do?method=byWin&drwNo=678"
    ]

    def start_requests(self):
        urls = 'http://www.nlotto.co.kr/lotto645Confirm.do?method=byWin&drwNo='
        for i in range(1, 679):
            url = urls + str(i)
            yield scrapy.Request(url, self.parse)

    def parse(self, response):
        try:
            nums = response.xpath('//div[@class="lotto_win_number mt12"]/p/img/@alt').extract()
            if len(nums) == 7:
                lotto = LottoItem()
                lotto['round'] = response.url.split('=')[2].encode('utf-8')
                lotto['num1'] = nums[0].encode('utf-8')
                lotto['num2'] = nums[1].encode('utf-8')
                lotto['num3'] = nums[2].encode('utf-8')
                lotto['num4'] = nums[3].encode('utf-8')
                lotto['num5'] = nums[4].encode('utf-8')
                lotto['num6'] = nums[5].encode('utf-8')
                lotto['specialNum'] = nums[6].encode('utf-8')
                yield lotto
        except Exception as e:
            print e
