import livestreamer
import sys
import datetime

def main():
    streams = livestreamer.streams("https://livestream.com/accounts/23093026/events/6897778/player")
    best = streams['best']
    best.swf = best.swf.replace("////", "//")
    fd = best.open()
    data = ""
    f = file(datetime.datetime.now().isoformat() + ".flv", 'w')
    while True:
        try:
            data = fd.read(1024)
            f.write(data)
        except IOError as err:
            f.close()
            sys.exit()

        if not data:
            f.close()
            sys.exit()




if __name__ == '__main__':
    main()
