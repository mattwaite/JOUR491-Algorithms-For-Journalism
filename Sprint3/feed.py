import feedparser, re

links = feedparser.parse('http://www.omaha.com/search/?mode=article&q=&t=article&l=200&d=&d1=1+year+ago&d2=&s=priority&sd=desc&k=news&f=atom&fulltext=odcmobile&altf=mrss&ips=600')

linkfile = open('links.txt', 'a')

for post in links.entries:
    if not re.search("/opinion/", post.link):
        if not re.search("/columnists/", post.link):
            linkfile.write(post.link+'\n')
        else:
            pass
    else:
        pass
