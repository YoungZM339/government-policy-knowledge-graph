"""
URL configuration for government_policy_knowledge_graph project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("index/", views.search),
    path("search/", views.search, name="search"),
    path("qa_system/", views.qa_system, name="qa_system"),
    path("all_relation/", views.all_relation, name="all_relation"),
    path("edit_relation/", views.edit_relation, name="edit_relation"),
    path("display_policy_content/", views.display_policy_content, name="display_policy_content"),
    path("get_profile/", views.get_profile),
    path("qa_system_answer/", views.qa_system_answer),
    path("search_name/", views.search_name),
    path("search_all_objects/", views.search_all_objects),
    path("add_relation/", views.add_relation),
    path("del_relation/", views.del_relation),
    path("admin/", admin.site.urls),
]
