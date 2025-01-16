from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('pay/<int:registration_id>/', views.make_payment, name='make_payment'),
]
