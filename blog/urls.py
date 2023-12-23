from django.urls import path

from blog.views import BlogCreateView, BlogUpdateView, BlogListView, BlogDetailView, BlogDeleteView

app_name = 'blog'

urlpatterns = [
    path('create/', BlogCreateView.as_view(), name='create'),
    path('', BlogListView.as_view(), name='list'),
    path('edit/<slug:slug>/', BlogUpdateView.as_view(), name='edit'),
    path('detail/<slug:slug>/', BlogDetailView.as_view(), name='detail'),
    path('delete/<slug:slug>/', BlogDeleteView.as_view(), name='delete'),
]
