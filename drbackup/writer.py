from string import Template
import datetime

def stringify_user(user):
    return u"%s %s" % (user['name'], user['surname'])
class Writer(object):
    def __init__(self, filename):
        self.handle = open(filename, "w")

    def start(self, user):
        html = u'''<!html >
                  <head>
                  <title>Sarakste ar $user</title>
                  <meta http-equiv="Content-Type" value="text/html; charset=utf-8" />
                  </head>
                  <body>
                    <h1>$user</h1>
                '''
        self.user = stringify_user(user)
        html = Template(html).substitute(user = self.user)
        self.handle.write(html.encode("utf-8"))
    def write(self, message,):
        html = u'''<div>$type $user</div>
                  <div>$time</div>
                  <div>$subject</div>

                  <div>$text</div>'''
        if message['type'] == 'inbox':
            type = u'no'
            message['user'] = stringify_user(message['user'])
        else:
            type = u'kam'
            message['user'] = self.user
        html = Template(html).substitute(user = message['user'],
                                        time = datetime.datetime.fromtimestamp(int(message['timestamp'])).isoformat(),
                                        subject = message['title'],
                                        text = message['text'],
                                        type = type)

        self.handle.write(html.encode("utf-8"))
    def end(self):
        html = '''</body></html>'''
        self.handle.write(html)
        self.handle.close()

