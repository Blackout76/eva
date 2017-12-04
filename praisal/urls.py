from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name="create_praisal"),
    url(r'^(?P<code_praisal>\w{8})$', views.view_praisal, name="view_praisal")
]