from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.views.generic.detail import DetailView
from .models import Tienda
from django.utils.text import slugify

class Main(TemplateView):
	template_name = "main/home.html"

class New(CreateView):
	model = Tienda
	fields = ['nombre']
	template_name = "main/new.html"

	def form_valid(self, form):
		t = form.save(commit=False)
		t.user = self.request.user
		t.slug = slugify(t.nombre)

		self.object = t.save()
		return super(New, self).form_valid(form)

class Detail(DetailView):
	template_name = "main/detail.html"
	model = Tienda

