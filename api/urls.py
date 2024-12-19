from django.urls import path, include

urlpatterns = [
    path('v1/users/', include('users.urls')),  
    path('v1/registrations/', include('registration.urls')), 
    path('v1/courses/', include('course_catalog.urls')), 
    path('v1/payments/', include('payments.urls')),
]
