from django.urls import path
from rango import views
from rango.views import AboutView, AddCategoryView, ProfileView

app_name = 'rango'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('category/<slug:category_name_slug>/add_page/', views.add_page, name='add_page'),
    path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('goto/', views.goto_url, name='goto'),
    path('register_profile/', views.register_profile, name='register_profile'),
    path('profile/<username>', ProfileView.as_view(), name='profile'),
    path('profiles/', views.list_profiles, name='list_profiles'),
    path('like/', views.like_category, name='like_category'),
    path('suggest/', views.suggest_category, name='suggest_category'),
    path('add/', views.auto_add_page, name='auto_add_page'),
    path('terms/', views.terms, name='terms_page'),
]
