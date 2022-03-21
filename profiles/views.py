from django.views.generic import DetailView
from django.contrib.auth.models import User
from feed.models import Post


class ProfileDetailView(DetailView):
    template_name = "profiles/detail.html"
    model = User
    context_object_name = "user"
    slug_field = "username"
    slug_url_kwarg = "username"

    def get_context_data(self, **kwargs):

        user =  self.get_object()
        context =  super().get_context_data(**kwargs)
        context['total_post']= Post.objects.filter(author=user).count()
        return context