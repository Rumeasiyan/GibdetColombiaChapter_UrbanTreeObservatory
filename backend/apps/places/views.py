from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Country, Department, Municipality, Place
from .serializers import (
    CountrySerializer,
    DepartmentSerializer,
    MunicipalitySerializer,
    PlaceSerializer,
)


class CountryViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint for Country model."""

    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name"]
    ordering_fields = ["name"]
    ordering = ["name"]


class DepartmentViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint for Department model."""

    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = ["name"]
    filterset_fields = ["country"]
    ordering_fields = ["name", "country__name"]
    ordering = ["name"]


class MunicipalityViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint for Municipality model."""

    queryset = Municipality.objects.all()
    serializer_class = MunicipalitySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = ["name"]
    filterset_fields = {
        "department": ["exact"],
        "department__country": ["exact"],
    }
    ordering_fields = ["name", "department__name"]
    ordering = ["name"]


class PlaceViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint for Place model."""

    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = ["site", "populated_center"]
    filterset_fields = {
        "municipality": ["exact"],
        "municipality__department": ["exact"],
        "municipality__department__country": ["exact"],
        "zone": ["exact"],
        "subzone": ["exact"],
    }
    ordering_fields = [
        "site",
        "municipality__name",
        "municipality__department__name",
        "zone",
        "subzone",
    ]
    ordering = ["site"]
