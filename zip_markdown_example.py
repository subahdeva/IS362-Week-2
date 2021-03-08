#!/usr/bin/env python
# coding: utf-8

# In[3]:


import markdown

## create a list
email_list = {'George Costanza': ['george.costanza@email.com', 'art.vandelay@email.com', 'georgie@email.com'],
              'Cosmo Kramer': ['cosmo.kramer@email.com', 'penny.packer@email.com', 'drvannostrand@email.com'],
              'Jerry Seinfeld': ['jerry.seinfeld@email.com', 'tim.watley@email.com', 'jseinfeld@email.com']
             }
## create a file named md and then iterate through each key/value 
## pair and extract/save to name variable and then iterate through the 
with open('emails.md', 'bw+') as f:
    for name, email in email_list.items():
        f.write('# {}\n'.format(name).encode('utf-8'))
        for email in email:
            f.write('* {}\n'.format(email).encode('utf-8'))
    f.seek(0)
    markdown.markdownFromFile(input=f, output='emails.html')


# In[24]:





# In[ ]:




