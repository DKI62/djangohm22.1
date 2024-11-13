from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import ProductListView, ProductDetailView, ContactView, BlogPostListView, BlogPostDetailView, \
    BlogPostCreateView, BlogPostUpdateView, BlogPostDeleteView, ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('blog/', BlogPostListView.as_view(), name='blogpost_list'),
    path('blog/create/', BlogPostCreateView.as_view(), name='blogpost_create'),
    path('blog/<slug:slug>/', BlogPostDetailView.as_view(), name='blogpost_detail'),
    path('blog/<slug:slug>/update/', BlogPostUpdateView.as_view(), name='blogpost_update'),
    path('blog/<slug:slug>/delete/', BlogPostDeleteView.as_view(), name='blogpost_delete'),
    path('product/add/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('product/<int:product_id>/add_version/', views.add_version, name='add_version'),
    path('product/<int:product_id>/edit_version/<int:version_id>/', views.edit_version, name='edit_version'),
    path('product/<int:product_id>/delete_version/<int:version_id>/', views.delete_version, name='delete_version'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
