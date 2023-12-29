from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView

from .models import Product, Contact


#
#
# def index(request):
#     product_list = Product.objects.order_by('pk')[:5]
#     context = {
#         'object_list': product_list,
#         'title': 'Главная страница'
#     }
#     return render(request, 'main/index.html', context)
#
#
# def show_item(request, pk):
#     item = get_object_or_404(Product, pk=pk)
#     context = {
#         'item': item,
#         'title': item
#     }
#     return render(request, 'main/item.html', context)
#
#
# def contacts(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         message = request.POST.get('message')
#         print(f'{name} ({email}): {message}')
#     contact_list = [{
#         'name': contact.name,
#         'phone': contact.phone,
#         'address': contact.address,
#         'email': contact.email
#     } for contact in Contact.objects.all()]
#     return render(request, "main/contacts.html", {'title': 'Контакты', 'contacts': contact_list})

class IndexView(ListView):
    model = Product
    template_name = 'main/index.html'
    context_object_name = 'object_list'
    ordering = ['pk']
    extra_context = {'title': 'Главная страница'}
    paginate_by = 5


class ItemView(DetailView):
    model = Product
    template_name = 'main/item.html'
    context_object_name = 'item'
    extra_context = {'title': 'Наш крутой продукт'}




class ContactsView(ListView):
    template_name = 'main/contacts.html'
    form_class = Contact
    success_url = reverse_lazy('contacts')
    extra_context = {'title': 'Контакты'}
    queryset = Contact.objects.all()

    def form_valid(self, form):
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
