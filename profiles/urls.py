from django.urls import path
from .views import ProfileDetailView


app_name = "profile"

urlpatterns = [
    path("<str:username>" , ProfileDetailView.as_view() , name="detail")
]
