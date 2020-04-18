from django.db import models

# Create your models here.
class Folder(models.Model):
    name = models.CharField(max_length = 100, null = False)
    parent = models.ForeignKey("self", related_name = 'folder_parent', on_delete = models.CASCADE, null = True)

class File(models.Model):
    name = models.CharField(max_length = 100, null = False, unique = True)
    parent = models.ForeignKey(Folder, related_name = 'file_parent', on_delete = models.CASCADE, null = True)
    content = models.TextField(null = False)