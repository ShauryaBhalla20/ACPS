from django.shortcuts import render
from .forms import handle
import json
import requests
from .models import user_handles, problem

def signupuser(request):
    if(request.method == 'GET'):
        return render(request, 'sheet/signupuser.html', {'form': handle()})
    else:
        
        user = request.POST['handle']
        min_rating = request.POST['min_rating']
        max_rating = request.POST['max_rating']
        
        url = f'https://codeforces.com/api/user.status?handle={user}'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}

        response = requests.get(url, headers=headers)

        data_json = response.json()

        if data_json['status'] == "OK":
            user_obj = user_handles(handle=user)
            user_obj.save()
            ac = {}
            nac = {}
            for i in data_json['result']:
                j = i['problem']
                s = str(j['contestId'])+str(j['index'])
                if i['verdict'] == "OK":
                    ac[s] = 1
                else:
                    nac[s] = 1
            
            problems = problem.objects.filter(rating__gte=min_rating, rating__lte=max_rating)
            
            return render(request, 'sheet/currentsheet.html', {'data_json': data_json, 'user': user, 'min_rating': min_rating, 'max_rating': max_rating, 'form': handle(), 'ac': ac, 'nac': nac, 'problems': problems})
        else:
            error = "Invalid Codeforces Handle!"
            return render(request, 'sheet/signupuser.html', {'form': handle(), 'error': error})