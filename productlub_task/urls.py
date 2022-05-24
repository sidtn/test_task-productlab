from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from wildberries_products.views import UploadExelViewSet, main_page

router = routers.DefaultRouter()
router.register(r"upload", UploadExelViewSet, basename="upload")
print(router.urls)

urlpatterns = [
    path("", main_page),
    path("admin/", admin.site.urls),
    path("api/v1/", include(router.urls))
]
