import datetime
from feedgen.feed import FeedGenerator

def get_milli():
    m = int((datetime.datetime.utcnow() - datetime.datetime(1970, 1, 1)).total_seconds() * 1000)
    return m

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
    fe.title('$")
    fe.content('')
    fe.summary(u'It is currently Day 15 (Morning)')
    fe.link(href='https://youtu.be/dQw4w9WgXcQ', rel='alternate')
    fe.author(name='Hwndindu', email='hwndu@fuckoff.org')

    # Write the feed to file
    fg.rss_file('rss.xml')



if __name__ == "__main__":
    main()
