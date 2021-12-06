from django.urls import path
from .import views
urlpatterns = [
    path('', views.create_view, name="create_view"),
    path('list_view/', views.list_view, name="list_view"),
    path('list_view/<id>/', views.detail_view, name="detail_view"),
    path('update_view/<id>/', views.update_view, name="update_view"),
    path('delete_view/<id>/', views.delete_view, name="delete_view"),
]
