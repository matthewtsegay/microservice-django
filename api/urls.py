from django.urls import path, include # type: ignore

urlpatterns = [
    path('api/users/', include('users.urls')),  
    path('api/registrations/', include('registration.urls')), 
    path('api/courses/', include('course_catalog.urls')), 
    path('api/payments/', include('payments.urls')),
]
