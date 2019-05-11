from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt
# Create your views here.
global category,location
location = ['Nairobi','Nakuru','Mombasa','Kisumu']
category = ['Food','Clothing','Travel','Fashion']
def photo_of_today(request):
    date = dt.date.today()
    photo = Image.todays_photo()
    return render(request,'all-photos/today_rudi.html',{'date': date, 'photo':photo,'category':category})
