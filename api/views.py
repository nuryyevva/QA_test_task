from django.db.models import Q
from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication, BasicAuthentication

from api.mixins import PaginationHandlerMixin
from api.models import Package
from api.paginators import BasicPagination
from api.serializers import PackageSerializer


class PackageList(APIView, PaginationHandlerMixin):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = BasicPagination

    def post(self, request, *args, **kwargs) -> Response:
        data_for_package = dict(request.data)
        data_for_package.update({"user": request.user.id})
        serializer = PackageSerializer(data=data_for_package)
        if serializer.is_valid():
            serializer.save()
            data = {"package": serializer.data}
            status_code = status.HTTP_201_CREATED
        else:
            data = {"error": serializer.errors}
            status_code = status.HTTP_400_BAD_REQUEST
        return Response(data, status=status_code)

    def get(self, request, *args, **kwargs) -> Response:
        packages = Package.objects.filter(user=request.user.id)
        page = self.paginate_queryset(packages)
        serializer = self.get_paginated_response(
            self.serializer_class(page, many=True).data
        )
        return Response(serializer.data, status=status.HTTP_200_OK)


class PackageDetail(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Package.objects.all()
    serializer_class = PackageSerializer

    def get(self, request, pk: int) -> Response:
        query = (
            Q(pk=pk, user_id=request.user.id)
            if request.user.is_staff is False
            else Q(pk=pk)
        )
        package = Package.objects.filter(query).first()
        if package is None:
            data = {
                "error": f"This user can't get package {pk}, because one is not author or such package not found."
            }
            status_code = status.HTTP_403_FORBIDDEN
        else:
            data = PackageSerializer(package).data
            status_code = status.HTTP_200_OK
        return Response(data, status=status_code)
