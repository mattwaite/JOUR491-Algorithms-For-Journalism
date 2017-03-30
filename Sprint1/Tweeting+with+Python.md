
# Tweeting with Python

The mayor's press releases are online in a boring HTML table. We could automate checking it for our favorite topic: The flu. And, whenever it found flu related reports, it would tweet it. Here's what that looks like.

First import Beautiful Soup, the Python 3 url handling bits with urlopen and Twython.


```python
from bs4 import BeautifulSoup
from urllib.request import urlopen
from twython import Twython
```

Now set up your Twitter access per the Twython documentation. These keys are mine. Do not use them.


```python
API_KEY = 'YOURKEY'
API_SECRET = 'YOURSECRET'
ACCESS_TOKEN = 'YOURTOKEN'
ACCESS_TOKEN_SECRET = 'YOURTOKENSECRET'
```

Now we create a Twython twitter object that can access Twitter on our behalf.


```python
twitter = Twython(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
```

Now we get our data. We request the page from the mayor's website and then parse it.


```python
response = urlopen("http://www.lincoln.ne.gov/city/mayor/media/")
html = response.read()
```


```python
soup = BeautifulSoup(html, "html.parser")
```

This is simple, and for demonstration purposes, but it's a simple loop. You first narrow down the block of HTML you need -- in this case, all the links are in an Unordered List unironically called "art." Then, I start another loop where I find the links in each list item. Then I give my condition -- in this case, only Tweet about influenza -- and the create the tweet. I have the actual Tweeting part commented out.


```python
for link in soup.find_all("ul", class_="art"):
    for url in link.find_all('a'):
        if "Influenza" in url.contents[0]:
            tweet = "Influenza news alert: %s %s" % (url.contents[0], "http://www.lincoln.ne.gov"+url['href'])
            print(tweet)
            #twitter.update_status(status=tweet) 
```

    Influenza news alert: Health Department Reports Influenza Increase http://www.lincoln.ne.gov/city/mayor/media/2017/011317.htm

