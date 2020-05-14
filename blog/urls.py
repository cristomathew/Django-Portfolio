from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.list, name="list"),
    path('<int:pk>', views.detail, name="detail")
]