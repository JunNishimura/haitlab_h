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

def recommend(request):
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
            return HttpResponse('error to open pickle file')
    else:
        return HttpResponse('error to get post request')

def category(request):
    context = {
        'title': 'category',
    }
    return render(request, 'recommendation/category.html', context)

def category_result(request, genre):
    if request.method == 'GET':
        try:
            pickle_path = BASE_DIR + '\machine_learning\\genres_df.pickle'
            with open(pickle_path, 'rb') as f:
                genres_df = pickle.load(f)
                
                # function to return top 10 anime names as list in the given genre.
                genre_top10 = lambda g: genres_df[genres_df['genre'].str.contains(g)].sort_values('weighted_rating', ascending=False)['name'][:10].tolist()
                context = {
                    'title': 'category_result',
                    'genre': genre,
                    'top10': dict(zip(range(1, 11, 1), genre_top10(genre))), # key: order, value: anime name
                }
                return render(request, 'recommendation/category_result.html', context)
        except expression as e:
            print(e)
            return HttpResponse('error to open a pickle file')
    return HttpResponse('error to get GET request')