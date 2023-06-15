from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = (
    [
        path("admin/", admin.site.urls),
        path("", include("books.urls", namespace="books")),
        path('accounts/', include('registration.backends.default.urls')),

        path("sitemap.xml", TemplateView.as_view(template_name="sitemap.xml", content_type="text/xml")),
        path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
        path("ServiceWorker.js", TemplateView.as_view(template_name="ServiceWorker.js", content_type="application/javascript")),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)

admin.site.site_header = "Ebooks Administration"
admin.site.site_title = "Ebooks Admin Portal"
admin.site.index_title = "Welcome to Ebooks Admin Portal"
