'''
Created on Oct 18, 2013

@author: boatkrap
'''
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response

from pumbaa import forms, models

@view_config(route_name='forums.comments.comment', 
             permission='member')
@view_config(route_name='forums.comments.replies',
             permission='member')
def comment(request):
    title = request.matchdict.get('title')
    topic_id = request.matchdict.get('topic_id')
    form = forms.topics.Comment(request.POST)

    if len(request.POST) > 0 and form.validate():
        message = form.data.get('message')
        
    else:
        return HTTPFound(location=request.route_path('forums.topics.view', topic_id=topic_id, title=title))
    
    topic = models.Topic.objects.with_id(topic_id)
    comment = models.Comment(message=message, 
                             author=request.user, 
                             status='publish',
                             ip_address=request.environ.get('REMOTE_ADDR'))

    topic.comments.append(comment)
    topic.save()
    
    return HTTPFound(location=request.route_path('forums.topics.view', topic_id=topic_id, title=title))