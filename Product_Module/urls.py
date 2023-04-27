from django.urls import path
from . import views

urlpatterns = [
    # path('', views.product_list, name='product-list'),

    path('', views.ProductListView.as_view(), name='Product_list_Url'),
    path('<cat>', views.ProductListView.as_view(), name='ProductCategory_list_Url'),
    path('Brands/<int:pk>', views.ProductListView.as_view(), name='ProductBrand_list_Url'),
    path('product_favorit', views.AddProductFavorite.as_view(), name='product_Favorite'),
    path('detail/<slug:slug>/', views.ProductDetailView.as_view(), name='product-detail'),
]


