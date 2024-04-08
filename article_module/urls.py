
from django.urls import path,re_path
from . import views
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('',views.ArticleListView.as_view(),name='article_list'),
    path('cat/<cat>', views.ArticleListView.as_view(), name='article_categories_list'),
    path('search/', views.search, name='search'),
    path('<slug:slug>/',views.ArticleDetailView.as_view(),name='article_detail'),

]