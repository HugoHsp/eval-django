from django.contrib import admin

from lesFiches.models import MovieCard


@admin.register(MovieCard)
class MovieCardAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date_sortie', 'realisateur', 'view_note')

    @admin.display(empty_value="pas de note")
    def view_note(self, obj):
        if obj.note < 5:
            color = 'red'
        else:
            color = 'green'
            return format_html("<span style=color:{} >{} </span >".format(color,
                                                                          obj.note))
