from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name = "about"),
    path('projects/',views.projects, name="projects"),
    path('login/',views.user_login, name="login"),
    path('logout/',views.user_logout, name="logout"),
    path('about/contactme/',views.contact_me, name="contact_me"),

]