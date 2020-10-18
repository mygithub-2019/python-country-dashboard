from django.shortcuts import render
import requests
from django.http import request
# Create your views here.
countries = []

def newsHome(request):
    response = requests.get("https://newsapi.org/v2/everything?q=bitcoin&apiKey=47e090b9a860449fbafc5b7e06e7b528")
    responseJSON = response.json()
    articles = responseJSON['articles']
    print(articles[0])
    image = 'https://restcountries.eu/data/ind.svg'
    return render(request, 'news/index.html', {'articles': articles, 'image': image})

def getDateFormat(date):
    return date[0:10]

def getTimeFormat(date):
    return date[11:19]

def formatDateDataSource(newsArticles):
    for country in newsArticles:
        publishedAt = country['publishedAt']
        country['date'] = getDateFormat(publishedAt)
        country['time'] = getTimeFormat(publishedAt)
    return newsArticles

def countryDashboard(request):
    response = requests.get("https://restcountries.eu/rest/v2/all")
    responseJSON = response.json()
    return render(request, 'news/country_dashboard.html', {'countries': responseJSON, 'isLoading': True})

def countryDetail(request, code):
    #cinfo = code
    cinfo = getCountryInfo(code)
    news = getCountryNews(code[0:2])
    latestNewsArticles = formatDateDataSource(news['articles'])
    return render(request, 'news/country_detail.html', {'country': cinfo, 'news': latestNewsArticles})

def getCountryInfo(code):
    response = requests.get("https://restcountries.eu/rest/v2/all")
    countries = response.json()
    # for country in countries:
    #     print(country)
    #     return countries[0]
    for cnty in countries:
        if(code == cnty['alpha3Code']):
            return cnty

def getCountryNews(code):
    url = "http://newsapi.org/v2/top-headlines?country=" + code + "&apiKey=47e090b9a860449fbafc5b7e06e7b528"
    countryNews = requests.get(url)
    return countryNews.json()



def searchCounty(inputString):
    list = [{'name': 'john'}, {'name': 'peter'}, {'name': 'mike'}, {'name': 'john2'}]
    for item in list:
        if item['name'].find('joh', 0, 3) > -1:
            print(item)
