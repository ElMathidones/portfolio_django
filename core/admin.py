from django.contrib import admin
from core.models import Projeto

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('titulo',)}
