import os

link = "http://www.omaha.com/news/metro/police-officer-tells-omaha-couple-to-run-after-attack-on/article_3a1a457e-0f36-11e7-b1e6-0faa143160f8.html"

summarizers = ["lex-rank", "luhn", "edmundson", "lsa", "text-rank", "sum-basic", "kl"]

for summary in summarizers:
    print("%s >>>>>>>>>>>>" % summary)
    os.system("sumy %s --length=3 --url=%s" % (summary, link))
