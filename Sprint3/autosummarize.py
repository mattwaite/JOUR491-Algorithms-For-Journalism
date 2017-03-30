import os

link = "http://journalstar.com/sports/huskers/mens-basketball/morrow-says-decision-to-transfer-from-nu-is-sacrifice-i/article_be9e1192-b890-56d1-a0d1-4d26b83099f7.html"

summarizers = ["lex-rank", "luhn", "edmundson", "lsa", "text-rank", "sum-basic", "kl"]

for summary in summarizers:
    print("%s >>>>>>>>>>>>" % summary)
    os.system("sumy %s --length=3 --url=%s" % (summary, link))
