from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index',views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),


    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    # path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('donate', views.donate, name='donate'),
    # path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
]