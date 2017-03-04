from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^new/$',
		views.New.as_view(),
		name="new"),

	url(r'^(?P<slug>[-\w]+)/$',
		views.Detail.as_view(),
		name="detail"),

	url(r'^',
		views.Main.as_view(),
		name="home")
]