from django.shortcuts import render
import requests


# Create your views here.
def home(request):
    url = "https://dad-jokes.p.rapidapi.com/random/joke"

    headers = {
	"X-RapidAPI-Key": "230a41950bmshe03949cee1f69c0p15c6bajsnb9a493bf81b1",
	"X-RapidAPI-Host": "dad-jokes.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)
    context={'setup':response.json()['body'][0]['setup'],'punchline':response.json()['body'][0]['punchline']}
    return render(request,'base/home.html',context)

def search(request):
    keyword="1729"
    if request.method=='POST':
        keyword=request.POST.get("keyword")
    url = "https://numbersapi.p.rapidapi.com/"+keyword+"/math"
    print(url)
    querystring = {"fragment":"true","json":"true"}

    headers = {
	"X-RapidAPI-Key": "230a41950bmshe03949cee1f69c0p15c6bajsnb9a493bf81b1",
	"X-RapidAPI-Host": "numbersapi.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    context={'data':response.json()['text'],'number':keyword}
    return render(request,'base/searchpage.html',context)