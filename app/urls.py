from django.urls import path
from .import views

urlpatterns = [
    path('cakes/', views.CakeCreateListCreateView.as_view()),
    path('cakes/<int:id>/', views.CakeRetrieveUpdateDestroyView.as_view()),
    path('cakes/', views.CategoryCreateListCreateView.as_view()),
    path('cakes/<int:id>/', views.CategoryRetrieveUpdateDestroyView.as_view()),
    path('cakes/', views.ShapeCreateListCreateView.as_view()),
    path('cakes/<int:id>/', views.ShapeRetrieveUpdateDestroyView.as_view()),
    path('cakes/', views.WeightCreateListCreateView.as_view()),
    path('cakes/<int:id>/', views.WeightRetrieveUpdateDestroyView.as_view())
]
