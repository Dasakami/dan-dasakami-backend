from rest_framework import serializers
from .models import Article, Project, ProjectCategory, ProjectImage, Skill, Tag, Contact

# ----------------------
# Статьи
# ----------------------
class ArticleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id','title', 'slug', 'content', 'cover', 'created_at', 'updated_at', 'is_featured', 'tags']
        depth = 1  # чтобы теги подтягивались автоматически


# ----------------------
# Теги
# ----------------------
class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


# ----------------------
# Навыки
# ----------------------
class SkillSerializers(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name', 'icon', 'proficiency']


# ----------------------
# Категории проектов
# ----------------------
class ProjectCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = ProjectCategory
        fields = ['id', 'name']


# ----------------------
# Изображения проекта
# ----------------------
class ProjectImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = ['id', 'image', 'caption', 'created_at']


# ----------------------
# Проекты (с галереей и категорией)
# ----------------------
class ProjectSerializers(serializers.ModelSerializer):
    category = ProjectCategorySerializers(read_only=True)
    images = ProjectImageSerializers(many=True, read_only=True)  # подтягиваем все фото
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Project
        fields = [
            'id', 'title', 'description', 'link', 'github', 'cover',
            'status', 'is_featured', 'the_best', 'tech_stack',
            'category', 'images', 'created_at', 'updated_at'
        ]


# ----------------------
# Контакты
# ----------------------
class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message', 'type']
