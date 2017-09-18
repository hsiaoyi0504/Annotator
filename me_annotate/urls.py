"""me_annotate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r"^completed/(?P<paper_name>.+)", views.completed, name="completed"),
    url(r'^db/', views.dump_db, name='dump_db'),
    url(r'^admin/', admin.site.urls),
    url(r'^annotator/', include("annotator.urls")),
    url(r"^demo/", views.DemoView.as_view(), name="demo"),
    url(r"^paper_annotate/(?P<paper_name>.+)", views.paper_annotate, name="paper_annotate"),
]
