from django.urls import path
from .views import *

app_name = 'crudapp'

urlpatterns = [
	path('home/', ClientHomeView.as_view(), 
		name='clienthome'),
	path('list/', ClientListView.as_view(), name='clientlist'),
	path('demo/<int:pk>/detail/', ClientDemoDetailView.as_view(), name='clientdemodetail'),
	path('demo/create/', DemoCreateView.as_view(), name='democreate'),
	path('demo/<int:pk>/update/', DemoUpdateView.as_view(), name='demoupdate'),
	path('demo/<int:pk>/delete/', DemoDeleteView.as_view(), name='demodelete'),

]
