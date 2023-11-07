from django.urls import path
from . import views
urlpatterns = [
    path('home/',views.base,name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
