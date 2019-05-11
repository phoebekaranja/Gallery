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
 View Function to present news from past days
def past_days_photos(request, past_date):

    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(photo_of_today)

    photo = Image.days_photo(date)
    return render(request, 'all-photos/past_rudi.html', {"date": date, 'photo':photo})
