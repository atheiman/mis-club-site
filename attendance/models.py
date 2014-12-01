from django.db import models
# from django.contrib.auth.models import User



# class Post(models.Model):
#     title = models.CharField(max_length=100)
#     category = models.ForeignKey(Category, related_name="posts")
#     slug = models.SlugField(help_text="Only lowercase letters, numbers, underscores or hyphens.", max_length=100, unique=True)
#     preview = models.TextField(max_length=200)
#     content = models.TextField()
#     created_by = models.ForeignKey(User, related_name="created_posts")
#     published_date_time = models.DateTimeField(blank=True, null=True)

#     def save(self, *args, **kwargs):
#         # create slug as lowercase
#         self.slug = self.slug.lower()

#         # generate preview from the markdown content
#         self.preview = "%s..." % self.content[:197]

#         # save to db
#         super(Post, self).save(*args, **kwargs)

#     def __unicode__(self):
#         return self.slug
