from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView, DeleteView

from .forms import ProductForm
from .models import Product, Contact


class IndexView(ListView):
    model = Product
    template_name = 'main/index.html'
    context_object_name = 'object_list'
    ordering = ['pk']
    extra_context = {'title': 'Главная страница'}
    paginate_by = 10


class ItemView(DetailView):
    model = Product
    template_name = 'main/item.html'
    context_object_name = 'item'
    extra_context = {'title': 'Наш крутой продукт'}


class ContactsView(FormView):
    template_name = 'main/contacts.html'
    form_class = Contact
    success_url = reverse_lazy('contacts')
    extra_context = {'title': 'Контакты'}

    def form_valid(self, form):
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            send_mail(
                f'Сообщение от {name} ({email})',
                message,
                email,
                ['youremail@example.com'],
                fail_silently=False,
            )
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contacts'] = Contact.objects.all()
        return context


class ItemCreate(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('main:index')


class ItemUpdate(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('main:index')

    def form_valid(self, form):
        saved_object = form.save()
        return redirect('main:product_details', pk=saved_object.id)


class ItemDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('main:index')
