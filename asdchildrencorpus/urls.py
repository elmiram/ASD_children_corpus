from django.conf.urls import patterns, include, url
from django.contrib import admin
from TestCorpus.views import Index, Search, Statistics, PopUp
from news.views import NewsView, SectionView
from annotator.admin import learner_admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'learner_corpus.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^myadmin/', include(learner_admin.urls)),

    url(r'^admin/', include(learner_admin.urls)),
    url(r'^(news)$', NewsView.as_view(), name='news'),
    url(r'^(search)/$', Search.as_view(), name='main.search'),
    url(r'^(help)$', Index.as_view(), name='main.static'),
    url(r'^$', SectionView.as_view(), name='start_page'),
    url(r'^search/(gramsel|lex|errsel)$', PopUp.as_view(), name='popup'),
    url(r'^(stats)/$', Statistics.as_view(), name='main.stats'),
    url(r'^document-annotations', include('annotator.urls')),
    (r'^i18n/', include('django.conf.urls.i18n')),
    )
