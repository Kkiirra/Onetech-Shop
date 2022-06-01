from django.urls import path
from .views import home_page, product_detail, search_product, add_delete_wishlist

app_name = 'home'

urlpatterns = [
    path('home/', home_page, name='home_page'),
    path('wish_add/', add_delete_wishlist, name='wish_add'),
    path('search_product/', search_product, name='search_product'),
    path('item/<slug:slug>/', product_detail, name='product_detail'),
]
