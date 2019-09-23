from django.shortcuts import render

from website.models import Category, Project

def index(request):
    """ view function for homepage of the site """

    context={
        
    }
    # render the page in the html template index.html
    return render(request, 'index.html', context=context)


def services(request):
    """ view for the service page of the site """

    context = {

    }
    return render(request, 'services.html', context=context)

def portfolio(request):
    """ view that display the portfolio page """
    project = Project.objects.all()
    contex = {
        'project':project
    }
    return render(request, 'portfolio.html', context=contex)