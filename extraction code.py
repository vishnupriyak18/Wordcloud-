#!/usr/bin/env python
# coding: utf-8

# In[1]:


import PyPDF2
pdfFile=open('work.pdf','rb')
pdfReader=PyPDF2.PdfFileReader(pdfFile)
print(pdfReader.numPages)
pageObj=pdfReader.getPage(0)
print(pageObj.extractText())
pdfFile.close()


# In[ ]:




