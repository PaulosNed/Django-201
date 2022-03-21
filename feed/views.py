from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from feed.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(ListView):
    http_method_name = ["get"]
    template_name = "feed/home.html"
    model = Post
    context_object_name = "posts"
    queryset = Post.objects.all().order_by("-id")[0:30]

class PostDetaiView(DetailView):
    template_name="feed/detail.html"
    model = Post
    context_object_name = "post"

class MakeNewPost(LoginRequiredMixin , CreateView):
    template_name="feed/make_post.html"
    model = Post
    fields = ['text']
    success_url = "/"

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        return super().form_valid(form)
