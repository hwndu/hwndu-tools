import datetime
from feedgen.feed import FeedGenerator
import math

def get_milli():
    m = int((datetime.datetime.utcnow() - datetime.datetime(1970, 1, 1)).total_seconds() * 1000)
    return float(m)

def generate_time():
    delta = (get_milli()-1484902680000.0)/86400000.0
    day = math.floor(delta)
    period = ""
    pointdelta = delta - day
    if pointdelta < 0.3:
        period = "Morning"
    elif pointdelta < 0.58:
        period = "Afternoon"
    elif pointdelta < 0.71:
        period = "Evening"
    else:
        period = "Night"
    time_string = "It is currently Day %d (%s)." % (day, period)
    return time_string

def main():
    # Create the feed
    fg = FeedGenerator()
    fg.id('https://github.com/hwndu/hwndu-tools/blob/master/rss.xml')
    fg.title('Hacky Time Feed')
    fg.author( {'name':'Hwndindu','email':'hwndu@fuckoff.org'} )
    fg.description("Hacky Time Feed")
    fg.link( href='https://github.com/hwndu/hwndu-tools', rel='alternate' )

    fg.language('en')

    # Create the time entry
    fe = fg.add_entry()
    fe.id('https://github.com/hwndu/hwndu-tools/blob/master/rss.xml')
    fe.title('There is a new day when the clock hits 3:58 AM (ET).')
    fe.content('')
    fe.summary(generate_time())
    fe.link(href='https://youtu.be/dQw4w9WgXcQ', rel='alternate')
    fe.author(name='Hwndindu', email='hwndu@fuckoff.org')

    # Write the feed to file
    fg.rss_file('rss.xml')



if __name__ == "__main__":
    main()
