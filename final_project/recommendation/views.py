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

def search(request):
    context = {
        'title': 'search',
    }
    return render(request, 'recommendation/search.html', context)

def candidates(request):
    if request.method == 'GET':
        keyword = request.GET.get('keyword')
        try:
            pickle_path = BASE_DIR + '\machine_learning\\anime_title_df.pickle'
            with open(pickle_path, 'rb') as f:
                anime_title_df = pickle.load(f)
                candidates = anime_title_df[anime_title_df['name'].str.contains(keyword)]['name'].tolist() #検索キーワードを含むアニメタイトルをリストにして返す
                return JsonResponse({'candidates': candidates})
        except:
            print('Error to open a file')
            return HttpResponse('error to get open pickle file')
    else:
        return HttpResponse('error to get post request')

def recommendation(request):
    if request.method == 'POST':
        animeTitle = request.POST.get('animeTitle')
        try:
            pickle_path = BASE_DIR + '\machine_learning\\item_sim_df.pickle'
            with open(pickle_path, 'rb') as f:
                item_sim_df = pickle.load(f)
                recommendation = item_sim_df.sort_values(by=animeTitle, ascending=False).index[1:11].tolist()
                return JsonResponse({'recommendation': recommendation})
        except:
            print('Error to open a file')
            return HttpResponse('error to get open pickle file')
    else:
        return HttpResponse('error to get post request')

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