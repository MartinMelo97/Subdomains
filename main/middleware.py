from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Tienda
from .views import Detail
#class SubdomainTiendaMiddleware(object):

#para django 1.10
from django.utils.deprecation import MiddlewareMixin

class SubdomainTiendaMiddleware(MiddlewareMixin):
	def process_request(self, request):
		host_parts = request.get_host().split('.') #nos traemos la url y la seccionamos
		print(request.get_host())
		if len(host_parts) > 2 and host_parts[0] != "www":
			tienda = get_object_or_404(Tienda, slug=host_parts[0])
			print(tienda.nombre)
			tienda_url = reverse('detail', args=[tienda.slug])
			template_name = "main/detail.html"
			context = {'object':tienda}
			return render(request, template_name, context)
			#url = '{}://{}{}'.format(request.scheme, '.'.join(host_parts[1:]), tienda_url)
			#return redirect(url)
