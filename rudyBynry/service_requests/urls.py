from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit_request, name='submit_request'),
    path('list/', views.request_list, name='request_list'),
    path('detail/<int:pk>/', views.request_detail, name='request_detail'),
    path('support-dashboard/', views.support_dashboard, name='support_dashboard'),
    path('update/<int:pk>/', views.update_request, name='update_request'),
]