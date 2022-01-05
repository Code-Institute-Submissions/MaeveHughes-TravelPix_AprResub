from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.db.models.signals import post_save
from django.conf import settings
from autoslug import AutoSlugField
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

class Account(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.png', upload_to='profile_pics')
	slug = AutoSlugField(max_length=200, unique=True)
	bio = models.CharField(max_length=300, blank=False)
	friends = models.ManyToManyField("Account", blank=True)

	def __str__(self):
		return str(self.user)

class Friend(models.Model):
	to_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='to', on_delete=models.CASCADE)
	from_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='from_user', on_delete=models.CASCADE)

	def __str__(self):
		return "From {}, to {}".format(self.from_user, self.to_user)

class Post(models.Model):
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=100)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
