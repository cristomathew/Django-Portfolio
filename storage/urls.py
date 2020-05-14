from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.private, name="private"),
    path('entertainment/', views.entertainment, name = "entertainment"),
    path('study/',views.study, name="study"),
    path('extra/',views.extra,name="extra"),
    path('entertainment/view/',views.ent_detail,name="ent_detail"),
    path('extra/view/',views.e_detail,name="e_detail"),
    path('study/view/',views.s_detail,name="s_detail"),

]