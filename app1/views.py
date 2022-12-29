from django.shortcuts import render

# Create your views here.
def first(request):
    d={'name':'muni'}
    return render(request,'first.html',context=d)
def second(request):
    d={'name':'we have been friends for the 7 years'}
    return render(request,'second.html',context=d)  