from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

#import a package that looks for a variable called urlpatterns (a list). The package checks if the clients side url matches what's inside the list. If it matches, then it follows that path, then goes to the views py file
from . import views     #access our views

urlpatterns=[
    url(r'^$', views.initial, name='initial'),        #use of carets. $- anything before the url s considered. r means when a request is made
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^location/(\w+)', views.specific_location, name='specific_location')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)