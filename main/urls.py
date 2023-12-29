from django.urls import path
from .views import IndexView, ItemView, ContactsView

app_name = 'main'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product/<int:pk>', ItemView.as_view(), name='product_details'),
]