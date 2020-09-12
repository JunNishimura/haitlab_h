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

def search(request):
    context = {
        'title': 'search',
    }
    return render(request, 'recommendation/search.html', context)

def search_result(request):
    context = {
        'title': 'search_result',
    }
    return render(request, 'recommendation/search_result.html', context)

def category(reqeust):
    context = {
        'title': 'category',
    }
    return render(request, 'recommendation/category.html', context)

def category_result(request):
    context = {
        'title': 'category_result'
    }
    return render(request, 'recommendation/category_result.html', context)