from uuid import uuid4
import hashlib

class Item(object):
    def __init__(self, item_dict, feed):
        try:
            self.title = str(item_dict['title'])
        except:
            self.title = ""
        try:
            self.link = str(item_dict['link'])
        except:
            self.link = ""
        try:
            self.id = str(item_dict['id'])
        except:
            self.id = str(hashlib.sha256(self.link.encode('ASCII')).hexdigest())

        try:
            self.published = (item_dict['published'])
        except:
            self.published = ""
        try:
            self.updated = str(item_dict['updated'])
        except:
            self.updated = ""
        try:
            self.summary = str(item_dict['summary'])
        except:
            self.summary = ""
        try:
            self.content = str(item_dict['content'])
        except:
            self.content = ""
        self.feed = { 'title': feed.title, 'url': feed.url, 'name':
                feed.name, 'id': feed.id}
    def to_dict(self):
        return {
                '_id': uuid4().hex,
                'type': 'item',
                'schemaversion': 1,
                'feedId': self.feed['id'],
                'title': self.title,
                'link': self.link,
                'id': self.id,
                'published': self.published,
                'updated': self.updated,
                'summary': self.summary,
                'content':  self.content
                }
