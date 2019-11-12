# -*- coding: utf-8 -*-
import scrapy


from scrapy_splash import SplashRequest
import regex


class ImmoSpider(scrapy.Spider):
    name = "immospider"

    start_urls = ["https://www.willhaben.at/iad/immobilien/grundstuecke/grundstueck-angebote?rows=5&areaId=6"]

    def parse(self, response):
        for offer_id in response.xpath("//a/@data-ad-link"):
            url = "https://www.willhaben.at/iad/finncode/result?finncode={}".format(offer_id.extract())

            yield SplashRequest(url, self.parse_offer, args={'wait': 2})
    
    def parse_offer(self, response):
        
        

        return {
            "id": response.xpath("//span[@id='advert-info-whCode']/text()").extract()[0].split(":")[1].strip(),
            "title": response.xpath("//h1[contains(@class, header)]/text()").extract()[0].split("\n")[1].strip(),
            "desciption": "".join(response.xpath('//*[contains(@itemprop, "description")]/text()').extract()),
            **self.parse_address(response.xpath('//*[contains(@itemprop, "Address")]/text()').extract())
        }
        
    def parse_address(self, raw_address):
        
        self.log(raw_address)

        return {
            "country": "AT",
            "city": regex.findall("([\p{L}\s]+)", raw_address[-3])[0].strip(),
            "post_code": raw_address[-3].split(" ")[0],
            "street": regex.findall("([\p{L}\s]+)", raw_address[-4])[0].strip() if len(raw_address) >= 4 else None,
            "house_number": regex.sub("([\p{L}'\s]+)", "", raw_address[-4]) if len(raw_address) >= 4 else None
        }

