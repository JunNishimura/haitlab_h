from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from final_project.settings import BASE_DIR
import pickle
import pandas as pd

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

def candidates(request):
    result = ''
    if request.method == 'POST':
        animeTitle = request.POST.get('animeTitle')
        try:
            pickle_path = BASE_DIR + '\machine_learning\\item_sim_df.pickle'
            with open(pickle_path, 'rb') as f:
                item_sim_df = pickle.load(f)
                candidates = item_sim_df.sort_values(by=animeTitle, ascending=False).index[1:11]
                candidates = candidates.tolist()
                return JsonResponse({'animeTitle': animeTitle, 
                                     'candidates': candidates})

        except:
            print('Error to open a file')
        return HttpResponse('error to get open pickle file')
    else:
        return HttpResponse('error to get post request')


def search_result(request):
    pass

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