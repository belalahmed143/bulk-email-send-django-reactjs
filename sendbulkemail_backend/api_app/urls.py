from django.urls import path
from .views import *


urlpatterns = [
    # path('', email_send)
    path('send-bulk-email/', BulkEmailSendAPI.as_view())
]