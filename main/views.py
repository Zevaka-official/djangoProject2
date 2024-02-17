from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.mail import send_mail
from django.forms import inlineformset_factory
from django.http import Http404
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView, DeleteView

from .forms import ProductForm, ModeratorProductForm, VersionForm
from .models import Product, Contact, ProductVersion


class IndexView(ListView):
    model = Product
    template_name = 'main/index.html'
    context_object_name = 'object_list'
    ordering = ['pk']
    extra_context = {'title': 'Главная страница'}
    paginate_by = 10


class ItemDetailView(DetailView):
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


class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('main:index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class ItemUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('main:index')

    def form_valid(self, form):
        saved_object = form.save()
        self.object.owner = self.request.user
        return redirect('main:product_details', pk=saved_object.id)

    def get_form_class(self):
        if not self.request.user.is_superuser and self.request.user.has_perm('main.set_published'):
            return ModeratorProductForm
        return ProductForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Изменение товара'
        if self.request.user == self.object.owner or self.request.user.is_superuser:
            VersionFormset = inlineformset_factory(Product, ProductVersion, form=VersionForm, extra=1)
            if self.request.method == 'POST':
                context['formset'] = VersionFormset(self.request.POST, instance=self.object)
            else:
                context['formset'] = VersionFormset(instance=self.object)
        return context

    def test_func(self):
        obj = self.get_object()
        return (obj.owner == self.request.user
                or self.request.user.has_perms(['main.change_product'])
                or self.request.user.is_superuser)

    def handle_no_permission(self):
        raise Http404('У вас нет прав для изменения этой страницы')


@method_decorator(login_required, name='dispatch')
class ItemDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('main:index')
    permission_required = 'main.delete_product'
