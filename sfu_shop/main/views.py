from django.shortcuts import render

# Create your views here.

def index(request):
    context = {}
    return render(request=request, 
                  template_name='main/index.html',
                  context=context)
