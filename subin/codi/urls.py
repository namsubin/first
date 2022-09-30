from django.urls import path
from codi import views

app_name='codi'
urlpatterns = [
    path('', views.CategoryLV.as_view(), name='index'),
    path('category', views.CategoryLV.as_view(), name='category_list'),
    path('category/<int:pk>/', views.CategoryDV.as_view(), name='category_detail'),
    path('codi/<int:pk>/', views.CodiDV.as_view(), name='codi_detail'),

    path('category/add/', views.CategoryCV.as_view(),name='category_add'),
    path('category/change/', views.CategoryChangeLV.as_view(), name='category_change'),
    path('category/<int:pk>/update/', views.CategoryUV.as_view(), name='category_update'),
    path('category/<int:pk>/delete/', views.CategoryDelV.as_view(), name='category_delete'),
    
    path('codi/add/', views.CodiCV.as_view(),name='codi_add'),
    path('codi/change/', views.CodiChangeLV.as_view(), name='codi_change'),
    path('codi/<int:pk>/update/', views.CodiUV.as_view(), name='codi_update'),
    path('codi/<int:pk>/delete/', views.CodiDelV.as_view(), name='codi_delete'),
]
