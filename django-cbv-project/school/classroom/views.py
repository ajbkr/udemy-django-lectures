from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    FormView,
    ListView,
    TemplateView,
    UpdateView,
)

from classroom.forms import ContactForm
from classroom.models import Teacher


class HomeView(TemplateView):
    template_name = 'classroom/home.html'


class ThankYouView(TemplateView):
    template_name = 'classroom/thank_you.html'


class TeacherCreateView(CreateView):
    model = Teacher
    fields = '__all__'

    success_url = reverse_lazy('classroom:thank_you')


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'classroom/contact.html'

    success_url = reverse_lazy('classroom:thank_you')

    def form_valid(self, form):
        print(form.cleaned_data)

        return super().form_valid(form)


class TeacherListView(ListView):
    model = Teacher
    queryset = Teacher.objects.order_by('first_name')

    context_object_name = 'teacher_list'


class TeacherDetailView(DetailView):
    model = Teacher


class TeacherUpdateView(UpdateView):
    model = Teacher
    fields = '__all__'

    success_url = reverse_lazy('classroom:list_teachers')


class TeacherDeleteView(DeleteView):
    model = Teacher

    success_url = reverse_lazy('classroom:list_teachers')
