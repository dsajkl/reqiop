from django.conf.urls import patterns, include, url


from ParerntApp import views


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
   # url(r'^$', 'Parentengagment.views.home', name='home'),
   # url(r'^Parentengagment/', include('Parentengagment.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),


	url(r'^$', 'ParerntApp.views.home', name = 'home'),

	url(r'^create/$', views.create),

	url(r'^create/create/$', views.create),

	url(r'^sendmail/$', views.sendmail),

)
