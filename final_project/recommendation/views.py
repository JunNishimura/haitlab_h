from django.shortcuts import render

# Create your views here.
def index(request):
    context = {

    }
    return render(request, 'recommendation/index.html', context)

def select(request):
    context = {
        'title': 'select',
    }
    return render(request, 'recommendation/select.html', context)

def result(request):
    context = {
        'title': 'result'
    }
    return render(request, 'recommendation/result.html', context)