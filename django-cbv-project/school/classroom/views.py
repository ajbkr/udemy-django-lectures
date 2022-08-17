from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from classroom.forms import ContactForm


class HomeView(TemplateView):
    template_name = 'classroom/home.html'


class ThankYouView(TemplateView):
    template_name = 'classroom/thank_you.html'


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'classroom/contact.html'

    success_url = reverse_lazy('classroom:thank_you')

    def form_valid(self, form):
        print(form.cleaned_data)

        return super().form_valid(form)
