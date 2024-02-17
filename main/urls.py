from django.urls import path
from django.views.decorators.cache import cache_page
from .views import IndexView, ItemDetailView, ContactsView, ItemCreateView, ItemUpdateView, ItemDeleteView, \
    CategoryListView

app_name = 'main'




urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product/<int:pk>', cache_page(60)(ItemDetailView.as_view()), name='product_details'),
    path('product/create', ItemCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update', ItemUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete', ItemDeleteView.as_view(), name='product_delete'),
    path('categories/', CategoryListView.as_view(), name='categories'),
]
