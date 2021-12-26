from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    #  поля которые отображаются в админке
    list_display = ('id', 'user', 'title', 'description', 'complete', 'create')
    #  поля которые будут ссылками в админке
    list_display_links = ('id', "user")
    #  возможность менять поля через админку
    list_editable = ('title', 'description', 'complete')
    #  возможность фильтровать по полям в админке
    list_filter = ('user', 'create')
    #  поля только для чтения
    readonly_fields = ('create',)

    #  панель для сохранения на верху страницы в админке
    save_on_top = True


admin.site.register(Task, TaskAdmin)
