
from django.urls import path
from holic import views
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
    
    path('ok',views.Index,name='home'),
    path('',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('search',views.Serach,name='search'),
    path('vikash',views.vik,name='vikash')
    # path('', views.Signin, name='signin'),

]
