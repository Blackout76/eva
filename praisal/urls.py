from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<code_praisal>\w{8})$', views.appraisement, name="appraisement"),
    url(r'^', views.praisal, name="praisal"),
]