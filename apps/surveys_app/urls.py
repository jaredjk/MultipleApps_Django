from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.survey),
    url(r'^/new$', views.new)

]