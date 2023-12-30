from django.urls import path
from . import views
urlpatterns = [
   
    path('home/',views.index,name='index'),
    path('post_detail/<int:pk>',views.post_detail,name='post-detail'),
    path('post_edit/<int:pk>',views.post_edit,name='post-edit'),
    path('post_delete/<int:pk>/delete/',views.post_delete,name='post-delete')
]