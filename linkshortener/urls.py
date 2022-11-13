from django.urls import path, re_path
from . import api
from .views import redirect_page


app_name = 'linkshortener'


urlpatterns = [
    path('create-link', api.LinkShortnerApi.as_view(), name="link_create"),
    re_path(r'redirect-page/(?P<slug>[-\w]+)/', redirect_page, name='single-product'),
]
