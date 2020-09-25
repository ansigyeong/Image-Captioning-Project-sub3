from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('point/reward/', views.point_reward),
    path('point/list/', views.point_list),
    path('daily/', views.daily),
    path('userwithdraw/', views.userdelete),
]