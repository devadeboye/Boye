from django.shortcuts import render

from website.models import Category, Project

def index(request):
    """ view function for homepage sites """

    context={
        
    }
    # render the page in the html template index.html
    return render(request, 'index.html', context=context)
