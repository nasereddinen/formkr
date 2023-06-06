from django.urls import re_path
from django.urls import path
from . import views 
urlpatterns = [
   path("form_view/<int:form_definition_id>/", views._form_detail_view, name="form_designer_form_view"),
]
