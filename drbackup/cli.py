from api import MessageDownloader
from api import DraugiemException
import getpass 
import sys

def main():
    print "Enter email"
    email = raw_input()
    print "Enter password"
    password = getpass.getpass()
    try:
        downloader = MessageDownloader(email, password)
    except DraugiemException:
        print "invalid username/password"
        sys.exit(1)
    def progress_show(current, total):
        sys.stdout.write("%3d of %d\r" % (current, total))
        sys.stdout.flush()
    print "downloading inbox"
    downloader.get_messages(type = 'in', progress_callback = progress_show)
    print "downloading outbox"
    downloader.get_messages(type = 'out', progress_callback = progress_show)

if __name__ == "__main__":
    main()
