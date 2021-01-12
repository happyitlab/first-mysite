from django.urls import path
from . import views


urlpatterns = [
    # path('', views.index),
    path('', views.PostList.as_view()),
    # path('<int:pk>/', views.post_detail),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('category/<str:slug>/', views.PostListByCategory.as_view()),
    path('tag/<str:slug>/', views.PostListByTag.as_view()),
    path('search/<str:q>/', views.PostSearch.as_view()),
]


