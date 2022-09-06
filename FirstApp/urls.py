from django.urls import path
from .views import home, about, contact, add_page, add_product, get_data, update_data, record_update, delete_product

urlpatterns = [
    path('Home', home, name='FAhome'),
    path('About', about, name='FAabout'),
    path('Contact', contact, name='FAcontact'),
    path("AddP", add_page, name='FAaddp'),
    path('Addproduct', add_product, name='Addproduct'),
    path('Data', get_data, name='display'),
    path('update/<int:id>', update_data, name='update'),
    path('update/RecordUpdate/<int:id>', record_update, name='RecordUpdate'),
    path('deleteproduct/<int:_id>', delete_product, name='deleteproduct')
]
