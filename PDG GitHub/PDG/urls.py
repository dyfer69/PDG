from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth import logout
from django.contrib.auth.views import logout

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'PDG.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^$', 'AnalizadorSistemas.views.home', name='home'),
                       url(r'^actualizar/', 'AnalizadorSistemas.views.actualizar', name='actualizar'),
                       url(r'^login/', 'django.contrib.auth.views.login', {'template_name':'login.html'}, name= 'login'),
                       url(r'^cerrar/$', 'django.contrib.auth.views.logout',  {'next_page': 'home'}, name= 'logout'),
                       url(r'^exportar/', 'AnalizadorSistemas.views.exportar', name='exportar'),
                       url(r'^variables/', 'AnalizadorSistemas.views.variables', name='variables'),
                       url(r'^subir/', 'AnalizadorSistemas.views.subir', name='subir'),
                       url(r'^admin/', include(admin.site.urls)),

                       )
