#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

 


def random_color_func(word=None, font_size=None, position=None, orientation=None, font_path=None, random_state=None):
    h = int(360.0 * 45.0 / 255.0)
    s = int(100.0 * 255.0 / 255.0)
    l = int(100.0 * float(random_state.randint(60, 120)) / 255.0)

 

    return "hsl({}, {}%, {}%)".format(h, s, l)

 

file_content=open ("work.pdf").read()

 

wordcloud = WordCloud(font_path = r'C:\Windows\Fonts\Verdana.ttf',
                            stopwords = STOPWORDS,
                            background_color = 'black',
                            width = 1200,
                            height = 1000,
                            color_func = random_color_func
                            ).generate(file_content)

 

plt.imshow(wordcloud)
plt.axis('off')
plt.show()


# In[ ]:




