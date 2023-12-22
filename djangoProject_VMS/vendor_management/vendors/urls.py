from django.urls import path
from .views import VendorListCreateView, VendorRetrieveUpdateDestroyView, PurchaseOrderListCreateView, PurchaseOrderRetrieveUpdateDestroyView, VendorPerformanceRetrieveView
from vendors import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # Vendor URLs
    path('', views.index, name='index'),
    path('api/vendors/', VendorListCreateView.as_view(), name='vendor-list-create'),
    path('api/vendors/<int:vendor_id>/', VendorRetrieveUpdateDestroyView.as_view(), name='vendor-retrieve-update-destroy'),

    # Purchase Order URLs
    path('api/purchase_orders/', PurchaseOrderListCreateView.as_view(), name='purchase-order-list-create'),
    path('api/purchase_orders/<int:po_id>/', PurchaseOrderRetrieveUpdateDestroyView.as_view(), name='purchase-order-retrieve-update-destroy'),

    # Vendor Performance URLs
    path('api/vendors/<int:vendor_id>/performance/', VendorPerformanceRetrieveView.as_view(), name='vendor-performance-retrieve'),

    path('api/purchase_orders/<int:pk>/acknowledge/', views.AcknowledgeUpdate.as_view()),
    path('apitoken/', obtain_auth_token),
]
