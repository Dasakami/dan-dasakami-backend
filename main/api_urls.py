from django.urls import path
from .views import ContactsViews, ArticleListViews, ArticleDetailViews

urlpatterns = [
    path('contacts/', ContactsViews.as_view(), name='contacts'),
    path('article_list/', ArticleListViews.as_view(), name='article_list'),
    path('article/<int:id>/', ArticleDetailViews.as_view(), name='article_detail'),

]
