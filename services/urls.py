from django.urls import path
from . import views 
app_name  = 'service'



urlpatterns = [
    path('complaint/create/', views.ComplaintCreateView.as_view(),name='create_complaint'),
    path('complaint/detail/<int:pk>/', views.ComplaintDetailView.as_view(),name='complaint_detail'),
    path('complaint/list/', views.ComplaintListView.as_view(),name='complaints'),
    path('complaint/delete/<int:pk>/', views.CancelComplaint.as_view(),name='cancel_complaint'), 
    path('complaint/update/<int:pk>/', views.ComplaintUpdateView.as_view(),name='complaint_update'), 
    


]
