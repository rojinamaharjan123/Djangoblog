from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Demo
from .forms import DemoCreateForm
from django.urls import reverse_lazy

# Create your views here.
class ClientHomeView(TemplateView):
	template_name = 'home.html'


class ClientListView(ListView):
	template_name = 'list.html'
	model = Demo
	# queryset = Demo.objects.all()
	context_object_name = 'demolist'


class ClientDemoDetailView(DetailView):
	template_name = 'demodetail.html'
	model = Demo
	context_object_name = 'demodetail'


class DemoCreateView(CreateView):
	template_name = 'democreate.html'
	form_class = DemoCreateForm
	success_url = reverse_lazy('crudapp:clienthome')


class DemoUpdateView(UpdateView):
	template_name = 'democreate.html'
	form_class = DemoCreateForm
	model = Demo
	success_url = reverse_lazy('crudapp:clientlist')


class DemoDeleteView(DeleteView):
	template_name = 'demodelete.html'
	model = Demo
	success_url = "/list/"