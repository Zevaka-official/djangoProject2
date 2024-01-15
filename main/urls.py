from django.urls import path
from .views import IndexView, ItemView, ContactsView, ItemCreate

app_name = 'main'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product/<int:pk>', ItemView.as_view(), name='product_details'),
    path('product/create', ItemCreate.as_view(), name='product_create'),
]