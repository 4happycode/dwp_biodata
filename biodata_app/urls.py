from django.urls import path
from .views import user_form_view, thank_you_view, user_list_view, user_detail_view, user_update_view

urlpatterns = [
    path('', user_form_view, name='user_form_view'),
    path('thank-you/', thank_you_view, name='thank_you'),
    path('list/', user_list_view, name='user_list'),
    path('users/<int:user_id>/', user_detail_view, name='user_detail'),
    path('user/update/<int:user_id>/', user_update_view, name='user_update_view'),
]
