from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone

def index(request):
    return render(request, 'index.html')

# list of vendors/ create a new vendor
class VendorListCreateView(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        if not queryset.exists():
            return Response({"message": "No vendors found"}, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.data, status=status.HTTP_200_OK)


# retrieve details/update a specific vendor/ delete vendor
class VendorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    lookup_url_kwarg = 'vendor_id'
    lookup_field = 'id'
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

# list of purchase orders/create a new purchase order
class PurchaseOrderListCreateView(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        if not queryset.exists():
            return Response({"message": "No purchase order found"}, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.data, status=status.HTTP_200_OK)


# retrieve details/ update a specific purchase order/ delete purchase order
class PurchaseOrderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    lookup_url_kwarg = 'po_id'
    lookup_field = 'id'
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


# retrieve performance details of specific vendor
class VendorPerformanceRetrieveView(generics.RetrieveAPIView):
    queryset = VendorPerformance.objects.all()
    serializer_class = VendorPerformanceSerializer
    lookup_url_kwarg = 'vendor_id'
    lookup_field = 'vendor__id'
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


# Acknowledge the receipt of a purchase order
class AcknowledgeUpdate(generics.UpdateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = AcknowledgeSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.validated_data['acknowledgment_date'] = timezone.now()
        super().perform_update(serializer)
        return Response(serializer.data)