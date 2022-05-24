from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from wildberries_products.views import UploadExelViewSet

router = routers.DefaultRouter()
router.register(r"upload", UploadExelViewSet, basename="upload")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(router.urls))
]
