from django.db import models
from markdown import markdown
import requests

def md_to_gfm(text):
    headers = {'Content-Type': 'text/plain'}
    data = text.encode('utf-8')
    r = requests.post('https://api.github.com/markdown/raw', headers=headers, data=data)

    print(r.text)

    return r.text#.encode('utf-8')

# Create your models here.
class Folder(models.Model):
    name = models.CharField(max_length = 100, null = False, unique = True)
    parent = models.ForeignKey("self", related_name = 'folder_parent', on_delete = models.CASCADE, null = True, default = None, blank = True)

    def __str__(self):
        return self.name

class File(models.Model):
    name = models.CharField(max_length = 100, null = False, unique = True)
    parent = models.ForeignKey(Folder, related_name = 'file_parent', on_delete = models.CASCADE, null = True, default = None, blank = True)
    content = models.TextField(null = False)

    def __str__(self):
        return self.name

    def mark(self):
        return markdown(self.content)

    def gfm(self):
        return md_to_gfm(self.content)