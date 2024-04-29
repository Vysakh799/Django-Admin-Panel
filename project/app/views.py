from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def basictable(request):
    return render(request,'basic-table.html')