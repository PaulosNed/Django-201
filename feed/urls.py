from django.urls import path

from feed.views import HomeView, MakeNewPost, PostDetaiView

app_name="feed"
urlpatterns = [
    path("" , HomeView.as_view(), name="index"),
    path("detail/<int:pk>", PostDetaiView.as_view(), name="detail"),
    path("create/", MakeNewPost.as_view(), name="create")
]