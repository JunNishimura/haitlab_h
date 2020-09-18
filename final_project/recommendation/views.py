from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from final_project.settings import BASE_DIR, YOUTUBE_API_KEY
import pickle
import pandas as pd
from googleapiclient.discovery import build

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
                top10   = item_sim_df.sort_values(by=animeTitle, ascending=False).index[1:11].tolist()
                worst10 = item_sim_df.sort_values(by=animeTitle, ascending=True).index[1:11].tolist()
                return JsonResponse({'top10': top10,
                                    'worst10': worst10})
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
                genre_top10  = lambda g: genres_df[genres_df['genre'].str.contains(g)].sort_values('weighted_rating', ascending=False)['name'][:10].tolist()
                top10_animes = genre_top10(genre)

                # function to return worst 10 anime names as list in the given genre.
                genre_worst10 = lambda g: genres_df[genres_df['genre'].str.contains(g)].sort_values('weighted_rating', ascending=True)['name'][:10].tolist()
                worst10_animes = genre_worst10(genre)
                
                # get youtube link for each anime 
                # youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
                # youtube_links = []
                # for anime in top10_animes:
                #     # 各アニメを検索キーワードとした視聴回数の最も多いyoutubeリンクを取得する
                #     search_response = youtube.search().list(
                #         part='id,snippet',
                #         q=anime,
                #         order='viewCount',
                #         type='video',
                #     ).execute()
                #     link = 'https://www.youtube.com/watch?v=' + search_response['items'][0]['id']['videoId']
                #     youtube_links.append(link)

                context = {
                    'title': 'category_result',
                    'genre': genre,
                    'top10': dict(zip(range(1, 11, 1), top10_animes)), # key: order, value: anime name
                    'worst10': dict(zip(range(1, 11, 1), worst10_animes)),
                    # 'links': youtube_links,
                }
                return render(request, 'recommendation/category_result.html', context)
        except:
            return HttpResponse('error to open a pickle file')
    return HttpResponse('error to get GET request')