from api import MessageDownloader
from api import DraugiemException
import getpass 
import sys
import os 
from writer import Writer

def main():
    print "Welcome to draugiem.lv message downloader "
    sys.stdout.write("Email: ")
    sys.stdout.flush()
    email = raw_input()
    password = getpass.getpass()
    try:
        downloader = MessageDownloader(email, password)
    except DraugiemException:
        print "invalid username/password"
        sys.exit(1)
    def progress_show(current, total):
        sys.stdout.write("%3d of %d\r" % (current, total))
        sys.stdout.flush()
    print "[1/x] downloading inbox"
    downloader.get_messages(type = 'in', progress_callback = progress_show)
    print "[2/x] downloading outbox"
    downloader.get_messages(type = 'out', progress_callback = progress_show)
    print "[3/x] sorting messages"
    msgs =  downloader.get_all_messages()
    sys.stdout.write("Enter path: ")
    sys.stdout.flush()
    path = raw_input()
    if not os.path.exists(path):
        os.mkdir(path)
    print "[4/x] writing"
    for user in msgs:
        w = Writer(os.path.join(path, "%s.html" % (downloader.get_user_info(user).replace("/", ""))))

        w.start(downloader.users[user])
        for item in msgs[user]:
            w.write(item)
        w.end()
    
if __name__ == "__main__":
    main()
