from django.shortcuts import render, redirect
from .models import Notes
from .forms import NotesForm
from django.contrib import messages
# Create your views here.


def index(request):
    note=Notes.objects.all()
    return render(request, "index.html",context={'note':note})

def new_note(request):
    if request.method == "POST":
        data=request.POST
        title=data.get('title')
        text=data.get('notes')
        Notes.objects.create(
            title=title,
            text=text
        )
        return redirect('index')
    return render(request, "new_note.html")

def update(request,id):
    queryset=Notes.objects.get(id=id)
    if request.method=="POST":
        data=request.POST
        title=data.get('title')
        text=data.get('notes')
        
        queryset.title=title
        queryset.text=text
        queryset.save()
        return redirect('index')
    con={'note':queryset}
    return render(request,"update.html",con)

def delete(request,id):
    queryset=Notes.objects.get(id=id)
    if request.method=="POST":
        queryset.delete()
        messages.info(request, "The note has been deleted")
    con={'note':queryset}
    return render(request,"delete.html",con)

def note_dtl(request,id):
    queryset=Notes.objects.get(id=id)
    con={'note':queryset}
    return render(request,"note_dtl.html",con)

def search_text(request):
    if request.method=="POST":
        txt=request.POST['search']
        notes=Notes.objects.filter(title__icontains=txt) | Notes.objects.filter(text__icontains=txt)
        if notes is None:
            messages.info("Data not Found !!")
        return render(request,"search.html",context={'notes':notes})          
    return redirect('index')
    