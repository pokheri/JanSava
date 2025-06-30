
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace='accounts')), 
    path('services/',include('services.urls',namespace='service')),
    
    path('', include('dash.urls', namespace='dash')), 
    
    

]
