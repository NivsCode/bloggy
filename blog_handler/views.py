from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Comment
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import PostForm, CommentForm

class AuthorMixin(object):
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(author=self.request.user)

class AuthorEditMixin(object):
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class AuthorPostMixin(AuthorMixin, LoginRequiredMixin):
    model = Post
    success_url = reverse_lazy('home')

class AuthorPostEditMixin(AuthorPostMixin, AuthorEditMixin):
    template_name = 'posts/form.html'

class PostCreateView(AuthorPostEditMixin, CreateView):
    form_class = PostForm
    success_url = reverse_lazy('home')

class PostUpdateView(AuthorPostEditMixin, UpdateView):
    fields = ['title', 'content', 'status',]

class PostDeleteView(AuthorPostMixin, DeleteView):
    template_name = 'posts/delete.html'

class PostListView(ListView):
    model = Post
    queryset = Post.drafts.all()
    context_object_name = 'posts'
    template_name = 'posts/list.html'
    
class PostDetailView(DetailView):
    model = Post
    context_object_name = 'posts'
    template_name = 'posts/post_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        
        comment_form = CommentForm()
        post = get_object_or_404(Post, slug=slug)
        comments = post.comment_set.filter(parent_comment=None)
        
        context['post'] = post
        context['comments'] = comments
        context['form'] = comment_form
        return context
        
    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        self.object = self.get_object()
        context = super().get_context_data(**kwargs)
        
        post = Post.objects.filter(slug=self.kwargs.get('slug')).first()
        comments = post.comment_set.all()
        
        context['post'] = post
        context['comments'] = comments
        context['form'] = form

        if form.is_valid():
            content = form.cleaned_data['content']
            parent_comment = comments.filter(id=form.cleaned_data['parent_comment_id']).first()
            author = request.user if request.user.is_authenticated else None
            Comment.objects.create(
                content = content,
                author = author,
                post = post,
                parent_comment = parent_comment
            )
            context['form'] = CommentForm()
            return self.render_to_response(context=context)
        
        return self.render_to_response(context=context)
