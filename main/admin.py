from django.contrib import admin
from .models import Article, ProjectCategory, Project,ProjectImage,Skill,Tag

admin.site.register(Article)
admin.site.register(Skill)
admin.site.register(Tag)
admin.site.register(ProjectCategory)
admin.site.register(ProjectImage)
admin.site.register(Project)