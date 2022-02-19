
from django.urls import path
from .views import ArticleListView, ArticleDetail, CategoryList, AuthorList
app_name = 'myapp'
urlpatterns = [
     path('', ArticleListView.as_view(), name='home1'), 
     path('page/<int:page>', ArticleListView.as_view(), name='home1'), 
     path('article/<slug:slug>', ArticleDetail.as_view(), name='detail'),
     path('category/<slug:slug>', CategoryList.as_view(), name='category'),
     path('category/<slug:slug>/page/<int:page>', CategoryList.as_view(), name='category'),
     path('author/<slug:username>', AuthorList.as_view(), name='author'),
     path('author/<slug:username>/page/<int:page>', AuthorList.as_view(), name='author') 
]

