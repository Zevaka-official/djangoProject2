from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView

from blog.models import Blog


class BlogCreateView(CreateView, PermissionRequiredMixin):
    model = Blog
    fields = ('title', 'content', 'preview', 'is_published', "email_author")
    success_url = reverse_lazy('blog:list')
    permission_required = ('blog.add_blog',)


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True).order_by('-date_created')
        return queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset=queryset)
        self.object.views_count += 1
        self.object.save()
        if self.object.views_count == 100 and self.object.email_author:
            # print(f"УРАААААААААА!{self.object.views_count} просмотров!")
            send_mail(
                "Test.title 1111",
                "Test.message 11111",
                None,
                [self.object.email_author],
                fail_silently=False,
            )
        return self.object


class BlogDeleteView(DeleteView, PermissionRequiredMixin):
    model = Blog
    success_url = reverse_lazy('blog:list')
    permission_required = ('blog.delete_blog',)


class BlogUpdateView(UpdateView, PermissionRequiredMixin):
    model = Blog
    fields = ('title', 'content', 'preview', 'is_published', "email_author")
    permission_required = ('blog.update_blog',)

    def form_valid(self, form):
        if form.is_valid():
            saved_object = form.save()
            return redirect('blog:detail', slug=saved_object.slug)
