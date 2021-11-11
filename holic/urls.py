
from django.urls import path
from holic import views
urlpatterns = [
    
    path('',views.Index,name='home'),
    path('search',views.Serach,name='search'),
]
