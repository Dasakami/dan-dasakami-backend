from django.db import models
from cloudinary_storage.storage import MediaCloudinaryStorage

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=500)
    slug = models.SlugField(max_length=500, unique=True)
    content = models.TextField(null=True, blank=True)
    cover = models.ImageField(upload_to='help_article_images/', blank=True, null=True, storage=MediaCloudinaryStorage())
    tags = models.ManyToManyField(Tag, blank=True, related_name='articles')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

class Contact(models.Model):
    TYPE_CHOICES = [
        ('feedback', 'Отзыв'),
        ('question', 'Вопрос'),
        ('collaboration', 'Сотрудничество')
    ]

    name = models.CharField(max_length=128, blank=True)
    email = models.EmailField()
    subject = models.CharField(max_length=400)
    message = models.TextField()
    contact_type = models.CharField(max_length=50, choices=TYPE_CHOICES, default='feedback')
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)  # отмечаем прочитано или нет

    def __str__(self):
        return f'Сообщение от {self.name or "Аноним"}'
    
    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class ProjectCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    STATUS_CHOICES = [
        ('not_started', 'Не начато'),
        ('in_progress', 'В процессе'),
        ('completed', 'Завершено'),
    ]

    title = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    cover = models.ImageField(upload_to='projects/', blank=True, null=True, storage=MediaCloudinaryStorage())
    github = models.URLField(max_length=500, null=True, blank=True)
    link = models.URLField(max_length=500, null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='not_started')
    tech_stack = models.JSONField(default=list, blank=True)
    category = models.ForeignKey(ProjectCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name='projects')
    is_featured = models.BooleanField(default=False)
    the_best = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='projects/', storage=MediaCloudinaryStorage())
    caption = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.project.title} - {self.caption or "Image"}'


class Skill(models.Model):
    name = models.CharField(max_length=50, unique=True)
    icon = models.ImageField(upload_to='skills/', blank=True, null=True, storage=MediaCloudinaryStorage())  # иконка технологии
    proficiency = models.IntegerField(default=50)  # 0-100%, например

    def __str__(self):
        return self.name
