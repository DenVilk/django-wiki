from django.shortcuts import render
from markdown import markdown

Folders = ['Help', 'I need', 'Somebody', 'HELP', 'No just anybody']
Files = ['file1', 'file2', 'file3', 'file4', 'file5']

# Create your views here.
def index(request):
    # folders = ['Help', 'I need', 'Somebody', 'HELP', 'No just anybody']
    # files = ['file1', 'file2', 'file3', 'file4', 'file5']
    return render(request, 'main/info.html', {'text': markdown('*HEEEEEEEEEELP*'), 'folders': Folders, 'files': Files})

def folder(request, Folder):
    return render(request, 'main/info.html', {'text': markdown('FOLDER'), 'folders': Folders, 'files': Files})

def files(request, File):
    return render(request, 'main/info.html', {'text': markdown('FILE'), 'folders': Folders, 'files': Files})

def finf(request, Folder, File):
    return render(request, 'main/info.html', {'text': markdown('FILE IN FOLDER'), 'folders': Folders, 'files': Files})