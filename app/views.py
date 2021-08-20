from django.shortcuts import render

# Create your views here.
def loopingfun(args):
    d={"name" : "Forloop"}
    return render(args,'loop.html', d)
    