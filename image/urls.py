from django.conf.urls import url
from . import views
urlpatterns=[
url(r'^$',views.photo_of_today,name = 'photoToday'),
url(r'^search/', views.search_results, name='search_results'),
url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_photos,name = 'pastPhotos'),
]
