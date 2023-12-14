from django.urls import path

from .views import index, contacts, show_item

app_name = 'main'


urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>', show_item ,name='product_details'),

]
