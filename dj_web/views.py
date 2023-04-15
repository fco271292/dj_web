from django.http import HttpResponse
from datetime import datetime
from datetime import date
import json
from django.http import JsonResponse

def hello(request):
    return HttpResponse(f"HI {datetime.now()}")

def goodbye(request):
    return HttpResponse(f"BYE {datetime.now().second}")

def calculate_age(request, year):
    current_year = datetime.now().year
    age =  current_year - year
    object = {'year': year, 'current_year': current_year, 'age':age}
    return HttpResponse(json.dumps(object), content_type = "application/json")

def current_time(request):
    current_time = date.today()
    data = {'current_time': current_time, 'year': current_time.year, 'month': current_time.month, 'day': current_time.day}
    return JsonResponse(data)