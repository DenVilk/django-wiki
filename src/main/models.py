from django.db import models

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