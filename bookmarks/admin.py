from django.contrib import admin
from bookmarks.models import Bookmark, SharedBookmark, Tag, Link

class BookmarkAdmin(admin.ModelAdmin):
	list_display = ('title', 'link','user')
	list_filter = ('user', )
	ordering = ('title', )
	search_fields = ('title', )

admin.site.register(Bookmark, BookmarkAdmin)
admin.site.register(SharedBookmark)
admin.site.register(Tag)
admin.site.register(Link)
