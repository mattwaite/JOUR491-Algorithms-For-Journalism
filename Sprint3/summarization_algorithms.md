# Summarization algorithms

There are a number of algorithms that will attempt to automate summarizing a body of text. We're going to try seven of them. 

Using the [sumy library](https://github.com/miso-belica/sumy) in Python, we're going to summarize 70 news stories -- 10 each -- seven ways into three paragraph summaries. You are going to then evaluate those 10 stories summarized into three paragraphs seven different ways. You are going to rate them on a three point scale:

1. Can be used as a summary of the story as is.
2. Needs editing to be used as a summary.
3. Cannot be used at all. 

You are going to create a data file of your summaries. Your data file must include the url, the summarization algorithm used, and the rating. An example:

http://www.omaha.com/news/metro/police-officer-tells-omaha-couple-to-run-after-attack-on/article_3a1a457e-0f36-11e7-b1e6-0faa143160f8.html, Luhn, 2
http://www.omaha.com/news/metro/police-officer-tells-omaha-couple-to-run-after-attack-on/article_3a1a457e-0f36-11e7-b1e6-0faa143160f8.html, Lex-Rank, 1

We will use this to make tools that can improve a news organization's Alexa Flash Briefing.
