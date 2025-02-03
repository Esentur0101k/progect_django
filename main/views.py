from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,"index.html")

def home(request):
    name  = "esentur"
    surname  = "kasymbekow"
    context = {
        "name":name,
        "surname":surname

    }
    return  render(request,'home.html',context)






