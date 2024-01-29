from django.urls import path

from api.views import PackageDetail, PackageList

app_name = "api"

urlpatterns = [
    path("v1/package/", PackageList.as_view(), name="package"),
    path("v1/package/<int:pk>/", PackageDetail.as_view(), name="detail"),
]
