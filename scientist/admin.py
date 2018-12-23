from django.contrib import admin


# Register your models here.
from .models import Scientist


class ScientistModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'designation', 'born_and_died', 'famous_work_1', 'award_1']
    list_display_links = ['name', 'designation', 'born_and_died', 'famous_work_1', 'award_1']
    # list_editable = ['name']
    list_filter = ['name', 'created_at']
    search_fields = ['name', 'designation', 'famous_work_1', 'award_1', 'famous_book_1']

    class Meta:
        model = Scientist


admin.site.register(Scientist, ScientistModelAdmin)
