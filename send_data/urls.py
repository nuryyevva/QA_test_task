from django.contrib import admin
from django.urls import include, path
from rest_framework.schemas import get_schema_view
from rest_framework.authtoken.views import obtain_auth_token

from users.views import RegistrationUserView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth", include("rest_framework.urls")),
    path("auth/", include("djoser.urls")),
    path("api/", include("api.urls")),
    path("registration/", RegistrationUserView.as_view(), name="registration"),
    path('token/', obtain_auth_token),
    path('token-jwt/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token-jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path(
        "openapi",
        get_schema_view(
            title="Send Packages",
            description="API for sending packages.",
            version="1.0.0",
        ),
        name="openapi-schema",
    ),
]
