from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class Dc2019Pipeline:
    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter['candidate_code'] in self.ids_seen:
            raise DropItem(f"Duplicate item found: {item!r}")
        else:
            self.ids_seen.add(adapter['candidate_code'])
            return item
        #return item