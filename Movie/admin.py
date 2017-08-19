from django.contrib import admin

from .models import Film, Actor, Genre
# Register your models here.

#class Film_Admin(admin.ModelAdmin):
#	fieldset = [("Film Detail", {"field":["Title","Description","Year","Actor","Type"]})
#	]
	
#def Film_Actor(self, obj):
#	return obj.list_actor()

#def Film_Genre(self, obj):
#	return obj.list_genre()

	
#list_display = ("Title","Description","Year","Actor","Type")


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
	list_display = ("Title","Description","Year")
	list_editable = ("Description","Year",)
	list_filter = ("Title","Description","Year")
	search_fields = ("Title","Description","Year",)

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
	list_display = ("Actor_name",)
	#list_editable = ("Actor_name",)
	list_filter = ("Actor_name",)
	search_fields = ("Actor_name",)

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
	list_display = ("Type",)
	list_filter = ("Type",)
	search_fields = ("Type",)




#admin.site.register(Film)
#admin.site.register(Actor)
#admin.site.register(Genre)