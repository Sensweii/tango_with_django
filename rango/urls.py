from django.urls import path
from django.conf.urls import include

from rango import views

app_name = 'rango'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('category/<slug:category_name_slug>/add_page/', views.add_page, name='add_page'),
    path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),
    path('add_category/', views.add_category, name='add_category'),
    path('goto/', views.goto_url, name='goto'),
]
