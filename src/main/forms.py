from django import forms
from .models import *


class FolderForm(forms.Form):
    name = forms.CharField(label = 'Folder name')
    parent = forms.ModelChoiceField(label = 'Parent', queryset = Folder.objects.all(), required = False)

    def __init__(self, *args, **kwargs):
        super(FolderForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class':'form-control'})
        self.fields['parent'].widget.attrs.update({'class':'form-control custom-select'})


class FileForm(forms.Form):
    name = forms.CharField(label = 'File name')
    parent = forms.ModelChoiceField(label = 'Parent', queryset = Folder.objects.all(), required = False)
    content = forms.CharField(label = 'Content', widget = forms.Textarea())

    def __init__(self, *args, **kwargs):
        super(FileForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class':'form-control'})
        self.fields['parent'].widget.attrs.update({'class':'form-control custom-select'})
        self.fields['content'].widget.attrs.update({'class':'form-control new-content'})


class EditFileForm(forms.Form):
    content = forms.CharField(label = 'Content', widget = forms.Textarea())

    def __init__(self, *args, **kwargs):
        super(EditFileForm, self).__init__(*args, **kwargs)
        self.fields['content'].widget.attrs.update({'class':'form-control edit-form'})