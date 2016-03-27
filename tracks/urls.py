from django.conf.urls import url
from .models import Track
from .views import Track_View

urlpatterns = [
    url(r'^$', Track_View.as_view(), name ="tracks"),
]
