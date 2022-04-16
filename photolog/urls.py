"""URL's"""

from django.urls import path
from . import views
from .views import AddPostView

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path(
        'add_post/', AddPostView.as_view(), name='add_post'
    ),
    path(
        'edit_post/<int:pk>', views.UpdatePostView.as_view(), name='edit_post'
    ),
    path('delete_post/<int:pk>', views.DeletePostView.as_view(),
         name='delete_post'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
