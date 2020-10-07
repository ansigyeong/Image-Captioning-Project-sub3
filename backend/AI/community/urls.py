from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('notice/', views.notice_list),
    path('notice/check/', views.noticecheck),
    path('notice/create/', views.notice_create),
    path('notice/<int:notice_pk>/', views.notice_detail),
    path('notice/<int:notice_pk>/delete/', views.notice_delete),
    path('notice/<int:notice_pk>/update/', views.notice_update),


    path('suggestion/', views.suggestion_list),
    path('suggestion/create/', views.suggestion_create),
    path('suggestion/<int:suggestion_pk>/', views.suggestion_detail),
    path('suggestion/<int:suggestion_pk>/delete/', views.suggestion_delete),
    path('suggestion/<int:suggestion_pk>/update/', views.suggestion_update),
    path('suggestion/<int:suggestion_pk>/commentcreate/', views.commentcreate),
    path('suggestion/<int:suggestion_pk>/<int:comment_pk>/commentdelete/', views.commentdelete),
    
]