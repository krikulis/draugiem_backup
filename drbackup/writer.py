from string import Template

def stringify_user(user):
    return u"%s %s" % (user['name'], user['surname'])
class Writer(object):
    def __init__(self, filename):
        self.handle = open(filename, "w")

    def start(self, user):
        html = u'''<!html >
                  <head>
                  <title>Sarakste ar $user</title>
                  <meta http-equiv="Content-Type
                  </head>
                  <body>
                    <h1>$user</h1>
                '''
        html = Template(html).substitute(user = stringify_user(user))
        self.handle.write(html.encode("utf-8"))
    def write(self, message,):
        html = u'''<div>$type $user</div>
                  <div>$time</div>
                  <div>$subject</div>

                  <div>$text</div>'''
        if message['type'] == 'in':
            type = u'no'
        else:
            type = u'kam'
        html = Template(html).substitute(user = stringify_user(message['user']),
                                        time = message['timestamp'],
                                        subject = message['title'],
                                        text = message['text'],
                                        type = type)

        self.handle.write(html.encode("utf-8"))
    def end(self):
        html = '''</body></html>'''
        self.handle.write(html)
        self.handle.close()

