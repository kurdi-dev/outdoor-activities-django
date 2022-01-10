from django.urls import path
from . import views
from django.http import HttpResponse

urlpatterns = [
    path('', views.home, name='home'),
    path('activity/create', views.create_activity, name='create_activity'),
    path('activity/update/<str:activity_id>', views.update_activity, name='update_activity'),
    path('activity/delete/<str:activity_id>', views.delete_activity, name='delete_activity'),
    path('activity/<str:activity_id>', views.activity, name='activity'),
]
