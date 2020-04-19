from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from markdown import markdown
from .forms import *
from .models import *

# Folders = ['Help', 'I need', 'Somebody', 'HELP', 'No just anybody']
Files = ['file1', 'file2', 'file3', 'file4', 'file5']

# Create your views here.
def index(request):
    Folders = Folder.objects.filter(parent = None)
    Files = File.objects.filter(parent = None)
    return render(request, 'main/info.html', {'text': markdown('*HEEEEEEEEEELP*'), 'folders': Folders, 'files': Files, 'parent' : False})

def folder(request, FolderName):
    # Parent = Folder.get(name = FolderName)
    Parent = get_object_or_404(Folder, name = FolderName)
    Folders = Folder.objects.filter(parent = Parent)
    Files = File.objects.filter(parent = Parent)
    return render(request, 'main/info.html', {'text': markdown('FOLDER'), 'folders': Folders, 'files': Files, 'parent': Parent.parent})

def files(request, FileName):
    Folders = Folder.objects.filter(parent = None)
    Files = File.objects.filter(parent = None)
    req_file = get_object_or_404(File, name = FileName, parent = None)
    return render(request, 'main/info.html', {'text': markdown(req_file.content), 'folders': Folders, 'files': Files, 'file': req_file, 'parent': req_file.parent})

def finf(request, FolderName, FileName):
    Parent = get_object_or_404(Folder, name = FolderName)
    Folders = Folder.objects.filter(parent = Parent)
    Files = File.objects.filter(parent = Parent)
    print(FileName)
    req_file = get_object_or_404(File, name = FileName, parent = Parent)
    return render(request, 'main/info.html', {'text': markdown(req_file.content), 'folders': Folders, 'files': Files, 'file': req_file, 'parent': req_file.parent})

def new_folder(request):
    if (request.method == 'POST'):
        form = FolderForm(request.POST)
        if (form.is_valid()):
            print(form.cleaned_data['name'])
            newFolder = Folder()
            newFolder.name = form.cleaned_data['name']
            newFolder.parent = form.cleaned_data['parent']
            newFolder.save()
            return HttpResponseRedirect('/')
    else:
        form = FolderForm()
    
    return render(request, 'main/add_folder.html', { 'form':form })

def new_file(request):
    if (request.method == 'POST'):
        form = FileForm(request.POST)
        if (form.is_valid()):
            print(form.cleaned_data['name'])
            newFile = File()
            newFile.name = form.cleaned_data['name']
            newFile.parent = form.cleaned_data['parent']
            newFile.content = form.cleaned_data['content']
            newFile.save()
            return HttpResponseRedirect('/')
    else:
        form = FileForm()
    
    return render(request, 'main/add_file.html', { 'form':form })
