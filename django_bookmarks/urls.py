import os.path
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from bookmarks.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

site_media = os.path.join(os.path.dirname(__file__), '..','site_media')

urlpatterns = patterns('',
    # Browsing
    (r'^$', main_page),
    (r'^popular/$', popular_page),
    (r'^user/(\w+)/$', user_page),
    (r'tag/([^\s]+)/$', tag_page),
    (r'tag/$', tag_cloud_page),
    (r'^search/$', search_page),
    (r'^bookmark/(\d+)/$', bookmark_page),
    
    # Comments
    (r'^comments/', include('django.contrib.comments.urls')),
    
    # Ajax
    (r'^ajax/tag/autocomplete/$', ajax_tag_autocomplete),
    
    #Session management
    (r'^login/$', 'django.contrib.auth.views.login'),
    (r'^logout/$', logout_page),
    (r'^register/$', register_page),
    (r'^register/success/$', direct_to_template,
     { 'template': 'registration/register_success.html' }),
    
    #Mdedia files
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
       { 'document_root': site_media }),
                       
    #Account management
    (r'^save/$', bookmark_save_page),
    (r'^vote/$', bookmark_vote_page),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    #Friends
    (r'^friends/(\w+)/$', friends_page),
    (r'^friend/add/$', friend_add),
)
