"""
Models
"""

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField

STATUS = ((0, "Draft"), (1, "Published"))


# pylint: disable=no-member

class Account(models.Model):
    """The main user model containing information for all user types"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    slug = AutoSlugField(max_length=200, unique=True)
    bio = models.CharField(max_length=300, blank=False)
    friends = models.ManyToManyField("Account", blank=True)

    def __str__(self):
        return str(self.user.username)


class Friend(models.Model):
    """ Model for following users """
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL,
                                related_name='to', on_delete=models.CASCADE)
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  related_name='from_user',
                                  on_delete=models.CASCADE)

    def __str__(self):
        # pylint: disable=consider-using-f-string
        return "From {}, to {}".format(self.from_user, self.to_user)


class Post(models.Model):
    """
    Model for making posts in the feed
    """
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")
    featured_image = models.ImageField(upload_to="images/")
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = RichTextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        """Sets absolute URL"""
        return reverse('home')

    class Meta:
        """ordering by date posted - newest first"""
        ordering = ["-created_on"]

    def number_of_likes(self):
        """Returns number of likes"""
        return self.likes.count()


class Comment(models.Model):
    """ Model for commenting in posts detail view """
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=100)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """ordering by date posted - newest first"""
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
