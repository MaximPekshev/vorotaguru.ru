from django.urls import path
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from .views import show_index_page, show_private_client_page, show_corporate_client_page
from .views import show_category, show_contact, show_services, show_portfolio, show_about, show_calculator

urlpatterns = [

	path('',        		show_index_page, name='show_index_page'),
	path('private-client/', 	show_private_client_page, name='show_private_client_page'),
	path('corporate-client/', 	show_corporate_client_page, name='show_corporate_client_page'),
	path('category/<str:cpu_slug>/', 	show_category, name='show_category'),
	path('about/', 	show_about, name='show_about'),
	path('contact/', 	show_contact, name='show_contact'),
	path('services/', 	show_services, name='show_services'),
	path('portfolio/', 	show_portfolio, name='show_portfolio'),
	path('calculator/', 	show_calculator, name='show_calculator'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()


