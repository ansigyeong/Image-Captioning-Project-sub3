from django.urls import path
from . import views

app_name = 'english'

urlpatterns = [
    path('vocabulary/', views.vocabulary),
    path('speaking/', views.speaking),
    path('imagecaption/', views.do_captioning),
]