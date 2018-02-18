# posts/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='posts'),
    path('<int:pk>/edit/',
         views.PostUpdateView.as_view(), name='post_edit'),  # new
    path('<int:pk>/',
         views.PostDetailView.as_view(), name='post_detail'),  # new
    path('<int:pk>/delete/',
         views.PostDeleteView.as_view(), name='post_delete'),  # new
    path('new/', views.PostCreateView.as_view(), name='post_new'),
]
