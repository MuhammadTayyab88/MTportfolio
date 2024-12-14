from . import views as V
from django.urls import path
from .views import skills_view
urlpatterns = [
    # Generic View
    path("", V.layout_view, name="home"),
    path("contact/", V.contact_view, name="contact"),
    path('contact_success/',V.contact_success, name='contact_success'),
    path("download_cv/", V.download_cv, name="download_cv"), 
    path('skills/', skills_view, name='skills'),
]
