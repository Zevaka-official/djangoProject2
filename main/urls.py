from django.urls import path

from .views import IndexView, ItemDetailView, ContactsView, ItemCreateView, ItemUpdateView, ItemDeleteView

app_name = 'main'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product/<int:pk>', ItemDetailView.as_view(), name='product_details'),
    path('product/create', ItemCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update', ItemUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete', ItemDeleteView.as_view(), name='product_delete'),
]
