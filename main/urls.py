from django.urls import path
from .views import (
    ArticleListViews, ArticleDetailViews, ProjectCategoryViews, 
    ProjectDetailView, SkillListViews, TagViews, ProjectListViews, ContactsViews
)

urlpatterns = [
    path('article_list/', ArticleListViews.as_view(), name='article_list'),
    path('article/<int:id>/', ArticleDetailViews.as_view(), name='article_detail'),
    path('skills/', SkillListViews.as_view(), name='skills'),
    path('tags/', TagViews.as_view(), name='tags'),
    path('projects/', ProjectListViews.as_view(), name='projects'),
    path('project/<int:id>', ProjectDetailView.as_view(), name='project'),
    path('project_categories/', ProjectCategoryViews.as_view(), name='project_categories'),
    path('contacts/', ContactsViews.as_view(), name='contacts'),
]
