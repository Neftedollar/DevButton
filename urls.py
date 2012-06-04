from django.conf.urls import patterns, include, url
from dummy.views import any_other_web_page,indexPage,showIP

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       ('^$', indexPage),
                       ('^my-ip/$',showIP),
                        url(r'^admin/', include(admin.site.urls)),
                       ('.+', any_other_web_page),


    # Examples:
    # url(r'^$', 'OriginalSite.views.home', name='home'),
    # url(r'^OriginalSite/', include('OriginalSite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

)