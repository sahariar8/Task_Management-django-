from django.urls import path
from tasks import views

urlpatterns = [
    path('manager-dashboard/', views.manager_dashboard),  # Admin dashboard for the task management system
    path('user-dashboard/', views.user_dashboard), 
    path('test/',views.test) # user dashboard for the task management system
]
