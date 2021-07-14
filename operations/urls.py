from django.urls import path
from . import views
urlpatterns = [
    path('',views.form_init,name="index"),
    path('save/',views.save_form,name="save"),
    path('del/',views.delete_data,name="del"),
    path('edit/',views.edit_data,name="edit"),

]
