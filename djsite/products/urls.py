from .models import *
from django.urls import path, include, re_path
from .views import *

urlpatterns = [
    path("api/v1/auth/", include("djoser.urls")),
    re_path(r"^auth/", include("djoser.urls.authtoken")),
    path("api/v1/productlist/",ProductListAPIView.as_view(), name="products"),
    path("api/v1/available/", AvailableProductsAPIView.as_view(), name="available")
]