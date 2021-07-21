import scrapy


class Dc2019Item(scrapy.Item):
    candidate_code = scrapy.Field()
    district_code = scrapy.Field()
    district_c = scrapy.Field()
    district_e = scrapy.Field()
    candidate_num = scrapy.Field()
    name_c = scrapy.Field()
    name_e = scrapy.Field()
    alias_c = scrapy.Field()
    alias_e = scrapy.Field()
    age = scrapy.Field()
    affiliation_c = scrapy.Field()
    affiliation_e = scrapy.Field()
    count = scrapy.Field()
    win = scrapy.Field()
