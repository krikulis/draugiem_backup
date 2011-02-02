import urllib
import urllib2
import json 

DRAUGIEM_URL = 'https://api.draugiem.lv/json/' 
APP_KEY = '171f138ae5d7a472caa581e13cab9565'

class DraugiemException(Exception):
    def __init__(self, code):
        self.code = code

class MessageDownloader(object):
    def __init__(self, username, password):
        self.api_key = None
        self.login(username, password)
        self.inbox = []
        self.outbox = []
        self.users = {}
        self.total = 0
        self.current = 0
    def login(self, username, password):
        response = self.call(action = 'login',
                  email = username,
                  password = password)
        self.user_info = response['login']
        self.api_key = response['login']['apikey']

    def call(self, **kwargs):
        kwargs['app'] = APP_KEY
        if self.api_key:
            kwargs['apikey'] = self.api_key
        url = "%s?%s" % (DRAUGIEM_URL, urllib.urlencode(kwargs))
        response = urllib.urlopen(url).read()
        response = json.loads(response)
        ir 'error' in response:
            raise DraugiemException(response['error']['code'])
        return response
    def get_messages(self, type = 'in', progress_callback = None):
        page = 0 
        valid = True
        if type == 'in':
            li = self.inbox
        else:
            li = self.outbox
        while True:
            r = self.call(action = 'messages/list',
                                 box = type,
                                 limit = 20,
                                 page = page)
            if self.total == 0:
                self.total = r['total']
            if not 'users' in r:
                print r
                break
            if not len(r['users']):
                break
            for user in r['users']:
                self.users[user] = r['users'][user]
            messages = self.get_message_details(','.join(r['messages'].keys()), type)
            for msg in r['messages']:
                r['messages'][msg]['text'] = messages[msg]['text']
                li.append(r['messages'][msg])
            page += 1
            self.current += 20
            if progress_callback:
                progress_callback(self.current, self.total)
            
    def get_message_details(self, id, box):
        # ugly hack, causes 1 HTTP req per message 
        result = self.call(action = 'messages/read',
                           box = box,
                           ids = id)
        return result['messagedata']
    def pretify_inbox_msg(self, msg):
        return {'from' : self.users[msg['uid']],
                'to' : self.user_info,
                'title' : msg['subject'],
                'timestamp' : msg['created'],
                'text' : msg['text']}


