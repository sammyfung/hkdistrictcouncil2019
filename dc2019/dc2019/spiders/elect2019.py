import scrapy, re
from dc2019.items import Dc2019Item


class Elect2019Spider(scrapy.Spider):
    name = 'elect2019'
    allowed_domains = ['elections.gov.hk']
    start_urls = ['https://www.elections.gov.hk/dc2019/chi/results_hk.html', 'https://www.elections.gov.hk/dc2019/eng/results_hk.html']
    db = {}
    items = []

    def parse(self, response):
        records = response.xpath('//table[contains(@id, "table-district-member")]/tr')
        last_dcode = ''
        last_district = ''

        for i in records:
            dcode = i.xpath('td[1]/text()').extract()
            if re.search('/chi/', response.url):
                chinese = True
            else:
                chinese = False
            if len(dcode) > 0:
                record = {}
                if not re.search('^[1-9]', dcode[0]):
                    last_dcode = dcode[0]
                    record['candidate_num'] = 1
                    if chinese:
                        record['district_c'] = i.xpath('td[2]/text()').extract()[0]
                        last_district = record['district_c']
                        name_c = i.xpath('td[4]/text()').extract()
                    else:
                        record['district_e'] = i.xpath('td[2]/text()').extract()[0]
                        last_district = record['district_e']
                        name_e = i.xpath('td[4]/text()').extract()
                    count = i.xpath('td[5]/text()').extract()[0]
                else:
                    record['candidate_num'] = int(dcode[0])
                    if chinese:
                        record['district_c'] = last_district
                        name_c = i.xpath('td[2]/text()').extract()
                    else:
                        record['district_e'] = last_district
                        name_e = i.xpath('td[2]/text()').extract()
                    count = i.xpath('td[3]/text()').extract()[0]
                record['district_code'] = last_dcode
                record['candidate_code'] = last_dcode + '-' + '%s' % record['candidate_num']
                if chinese:
                    if len(name_c) > 1:
                        record['alias_c'] = re.sub('[()]', '', name_c[1])
                    else:
                        record['alias_c'] = ''
                    record['name_c'] = name_c[0]
                else:
                    if len(name_e) > 1:
                        record['alias_e'] = re.sub('[()]', '', name_e[1])
                    else:
                        record['alias_e'] = ''
                    record['name_e'] = name_e[0]
                if re.search('\*', count):
                    record['win'] = True
                else:
                    record['win'] = False
                record['count'] = int(re.sub('[,*  註Note]', '', count))
                try:
                    if chinese:
                        self.db[record['candidate_code']]['district_c'] = record['district_c']
                        self.db[record['candidate_code']]['name_c'] = record['name_c']
                        self.db[record['candidate_code']]['alias_c'] = record['alias_c']
                    else:
                        self.db[record['candidate_code']]['district_e'] = record['district_e']
                        self.db[record['candidate_code']]['name_e'] = record['name_e']
                        self.db[record['candidate_code']]['alias_e'] = record['alias_e']
                except:
                    self.db[record['candidate_code']] = record
                try:
                    assert self.db[record['candidate_code']]['affiliation_c']
                except:
                    url_chi = 'https://www.elections.gov.hk/dc2019/pdf/intro_to_can/%s_CHN.html' % record['candidate_code']
                    url_chi = re.sub('-', '_', url_chi)
                    yield scrapy.Request(url_chi, self.parse_candidate)
                try:
                    assert self.db[record['candidate_code']]['affiliation_e']
                except:
                    url_eng = 'https://www.elections.gov.hk/dc2019/pdf/intro_to_can/%s_ENG.html' % record['candidate_code']
                    url_eng = re.sub('-', '_', url_eng)
                    yield scrapy.Request(url_eng, self.parse_candidate)
                try:
                    item = Dc2019Item()
                    item['candidate_code'] = self.db[record['candidate_code']]['candidate_code']
                    item['district_code'] = self.db[record['candidate_code']]['district_code']
                    item['district_c'] = self.db[record['candidate_code']]['district_c']
                    item['district_e'] = self.db[record['candidate_code']]['district_e']
                    item['candidate_num'] = self.db[record['candidate_code']]['candidate_num']
                    item['name_c'] = self.db[record['candidate_code']]['name_c']
                    item['name_e'] = self.db[record['candidate_code']]['name_e']
                    item['alias_c'] = self.db[record['candidate_code']]['alias_c']
                    item['alias_e'] = self.db[record['candidate_code']]['alias_e']
                    item['age'] = self.db[record['candidate_code']]['age']
                    item['affiliation_c'] = self.db[record['candidate_code']]['affiliation_c']
                    item['affiliation_e'] = self.db[record['candidate_code']]['affiliation_e']
                    item['count'] = self.db[record['candidate_code']]['count']
                    item['win'] = self.db[record['candidate_code']]['win']
                    self.items.append(item)
                except:
                    pass

        return self.items


    def parse_candidate(self, response):
        candidate_code = re.sub('.*/', '', response.url)
        candidate_code = re.sub('_(CHN|ENG)\.html', '', candidate_code)
        candidate_code = re.sub('_', '-', candidate_code)
        self.db[candidate_code]['age'] = int(response.xpath('//div/p[3]/span[2]/text()').extract()[0])
        affiliation = response.xpath('//div/p[5]/span[2]/text()').extract()[0]
        if re.search('_CHN.html$', response.url):
            if re.search('候選人並未提供有關資料', affiliation):
                self.db[candidate_code]['affiliation_c'] = affiliation
            else:
                self.db[candidate_code]['affiliation_c'] = ''
        else:
            if re.search('Relevant information has not been provided by the candidate', affiliation):
                self.db[candidate_code]['affiliation_e'] = affiliation
            else:
                self.db[candidate_code]['affiliation_e'] = ''

        try:
            item = Dc2019Item()
            item['candidate_code'] = self.db[candidate_code]['candidate_code']
            item['district_code'] = self.db[candidate_code]['district_code']
            item['district_c'] = self.db[candidate_code]['district_c']
            item['district_e'] = self.db[candidate_code]['district_e']
            item['candidate_num'] = self.db[candidate_code]['candidate_num']
            item['name_c'] = self.db[candidate_code]['name_c']
            item['name_e'] = self.db[candidate_code]['name_e']
            item['alias_c'] = self.db[candidate_code]['alias_c']
            item['alias_e'] = self.db[candidate_code]['alias_e']
            item['age'] = self.db[candidate_code]['age']
            item['affiliation_c'] = self.db[candidate_code]['affiliation_c']
            item['affiliation_e'] = self.db[candidate_code]['affiliation_e']
            item['count'] = self.db[candidate_code]['count']
            item['win'] = self.db[candidate_code]['win']
            self.items.append(item)
        except:
            pass

        return self.items
