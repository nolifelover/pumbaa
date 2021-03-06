<%inherit file="/admin/base/base.mako"/>
<%block name="where_am_i">
	${parent.where_am_i()}
	<li><a href="${request.current_route_path()}">Forums</a></li>
</%block>
<%block name="panel_title">Forums</%block>
<ul class="list-inline">
	<li><a href="${request.route_path('admin.forums.create')}">new forums</a></li>
</ul>
<ul class="list-group">
	% for forum in forums:
    <li class="list-group-item">
    	<a href="${request.route_path('forums.view', name=forum.name)}">${forum.name}</a> : 
    	<a href="${request.route_path('admin.forums.edit', forum_id=forum.id)}">edit</a>
    	<a href="${request.route_path('admin.forums.delete', forum_id=forum.id)}">delete</a>
    </li>
    % endfor
</ul>