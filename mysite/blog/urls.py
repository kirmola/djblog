from django.urls import path
from blog.views import PostView


urlpatterns = [
    path("<slug:slug>/", PostView.as_view(), name="post_detail")
]