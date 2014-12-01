from django.contrib import admin
# from django.utils import timezone

# from .models import Post



# def make_published(modeladmin, request, queryset):
#     queryset.update(status=PUBLISHED)
#     for q in queryset:
#         q.published_date_time = timezone.now()
#         q.save()
# make_published.short_description = "Mark selected posts as %s" % PUBLISHED



# class PostAdmin(admin.ModelAdmin):
#     fields = ['slug', 'created_by']
#     list_display = ['slug', 'created_by', 'published_date_time']
#     actions = [make_published]

#     def save_model(self, request, obj, form, change):
#         if not change:
#             # object was created by the user submitting the form
#             obj.created_by = request.user
#         obj.save()



# admin.site.register(Post, PostAdmin)
