from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_list, name='create_list'),  # ← вот эта строка
    path('list/<uuid:list_uuid>/', views.view_list, name='view_list'),
    path('item/<int:item_id>/toggle/', views.toggle_item, name='toggle_item'),
    path('item/<int:item_id>/delete/', views.delete_item, name='delete_item'),
]
