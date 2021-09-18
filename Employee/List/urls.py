from django.urls import path
from List import views

app_name = 'List'

urlpatterns = [
    path('add', views.index, name="add"),
    path('show', views.show, name="show"),
    path('payment/<pk>/', views.change, name="change"),
    path('pdf', views.render_pdf_view, name="pdf"),

]
