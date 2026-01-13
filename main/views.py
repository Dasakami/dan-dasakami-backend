from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Article, Tag, Skill, ProjectCategory, Project, Contact
from .serializers import (
    ArticleSerializers,
    TagSerializers,
    SkillSerializers,
    ProjectCategorySerializers,
    ProjectSerializers,
    ContactSerializers
)
from django.contrib.auth.models import User

# ----------------------
# Статьи
# ----------------------
class ArticleListViews(generics.ListAPIView):
    serializer_class = ArticleSerializers
    permission_classes = [permissions.AllowAny]
    queryset = Article.objects.all().order_by('-created_at')


class ArticleDetailViews(generics.RetrieveAPIView):
    serializer_class = ArticleSerializers
    permission_classes = [permissions.AllowAny]
    queryset = Article.objects.all()
    lookup_field = 'id'  


class TagViews(generics.ListAPIView):
    serializer_class = TagSerializers
    permission_classes = [permissions.AllowAny]
    queryset = Tag.objects.all()

class SkillListViews(generics.ListAPIView):
    serializer_class = SkillSerializers
    permission_classes = [permissions.AllowAny]
    queryset = Skill.objects.all()


class ProjectCategoryViews(generics.ListAPIView):
    serializer_class = ProjectCategorySerializers
    permission_classes = [permissions.AllowAny]
    queryset = ProjectCategory.objects.all()

class ProjectListViews(generics.ListAPIView):
    serializer_class = ProjectSerializers
    permission_classes = [permissions.AllowAny]
    queryset = Project.objects.all().order_by('-created_at')


class ProjectDetailView(generics.RetrieveAPIView):
    serializer_class = ProjectSerializers
    permission_classes = [permissions.AllowAny]
    queryset = Project.objects.all()
    lookup_field = 'id'


class ContactsViews(generics.CreateAPIView):
    serializer_class = ContactSerializers
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {'message': 'Сообщение успешно отправлено'},
            status=status.HTTP_201_CREATED,
            headers=headers
        )
from django.http import JsonResponse
from django.contrib.auth import get_user_model

User = get_user_model()

def create_superuser(request):
    # Проверка, что пользователь уже есть
    if User.objects.filter(username='Dasakami', is_staff=True).exists():
        return JsonResponse({'message': 'User already exists'})

    # Создание суперюзера
    user = User.objects.create_superuser(username='Dasakami', password='h72ivh-19')
    
    return JsonResponse({'message': 'Superuser created'})