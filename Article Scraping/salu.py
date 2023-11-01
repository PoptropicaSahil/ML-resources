#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import feedparser
import random
import webbrowser


# In[2]:


website_list = ['https://newsletter.bringthedonuts.com/feed', "https://blackboxofpm.com/feed", 
               'https://hitenism.com/feed/', 'https://cdn.hackernoon.com/tagged/product-management/feed',
               'https://cdn.hackernoon.com/tagged/product-manager/feed', 'https://feedpress.me/elezea',
               'https://medium.com/feed/women-in-product-blogs', 'https://jaystansell.medium.com/feed',
               'https://www.producttalk.org/feed/' , 'https://www.producttalk.org/blog/feed/']


# In[ ]:


while True:
    feed_url = random.choice(website_list)
    blog_feed = feedparser.parse(feed_url)


    print(blog_feed.feed.title, blog_feed.feed.link,'{', len(blog_feed.entries),'}', '\n' )
#     print(blog_feed.feed.link)
#     print(f'{len(blog_feed.entries)} articles found')
    
    i = random.randint(0, len(blog_feed.entries))

    try:
        print('\tTITLE', blog_feed.entries[i].title)
        print('\tLINK', blog_feed.entries[i].link)
        print('\tAUTHOR', blog_feed.entries[i].author)
        print('\tDATE PUBLISHED', blog_feed.entries[i].published)
    except:
        pass

    try: 
        tags = [tag.term for tag in blog_feed.entries[0].tags]
        print('\tTAGS', tags)
    except:
        pass

    
    print("\nOPEN karna kya bhai? (Y/N)")
    ans = input("").lower()

    if ans == "y":
        webbrowser.open(blog_feed.entries[i].link)
        break
    elif ans == "n":
        print('\n')
        continue
    elif (ans == 'exit') or (ans == 'quit'):
        print('exited successfully!')
        break
    else:
        print("kuch bhi random enter nahi karneka bhai")
        pass
    
    print('\n\n')

