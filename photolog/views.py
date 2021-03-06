"""Views"""

from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import CommentForm
from .models import Post


# pylint: disable=no-member
# pylint: disable=unused-argument

# home page
class PostList(generic.ListView):
    """
    This class creates the post list
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


# post detail page
class PostDetail(View):
    """
    This creates the post view
    """
    def get(self, request, slug, *args, **kwargs):
        """
        Displays post details in the view
        """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """
        Submits form content to the database
        """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )


# post likes
class PostLike(View):
    """
    Likes on a post
    """
    def post(self, request, slug, *args, **kwargs):
        """
        Submits to view
        """
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


# Adding a post
class AddPostView(LoginRequiredMixin, CreateView):
    """Adds post"""
    model = Post
    template_name = 'add_post.html'
    fields = ('title', 'content', 'featured_image')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# editing a post
class UpdatePostView(UpdateView):
    """
    Post update view
    """
    model = Post
    template_name = 'edit_post.html'
    fields = ('title', 'content', 'featured_image')


# delete a post
class DeletePostView(DeleteView):
    """Deletes post"""
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
