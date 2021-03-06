<%inherit file="/manager/base/base.mako"/>

<%block name="title">New Photo Albums</%block>
<%block name="where_am_i">
	${parent.where_am_i()}
	<li><a href="${request.route_path('manager.pages.index')}">Photo Albums</a></li>
	<li><a href="${request.current_route_path()}">New page</a></li>
</%block>

<%block name="panel_title">New Photo Albums</%block>
<form action="${request.current_route_path()}" method="post">
	<div class="form-group${' has-error' if form.name.errors else ''}">
	    <label for="title" class="control-label${' has-error' if form.name.errors else ''}">Name</label>
	    % if form.name.errors:
			<span class="text-danger">${form.name.errors[0]}</span>
		% endif
	    ${form.name(class_='form-control', placeholder='Enter photo album name')}
	</div>
	<div class="form-group${' has-error' if form.description.errors else ''}">
	    <label for="title" class="control-label${' has-error' if form.description.errors else ''}">Description</label>
	    % if form.description.errors:
			<span class="text-danger">${form.description.errors[0]}</span>
		% endif
	    ${form.description(class_='form-control', placeholder='Enter photo album name')}
	</div>
	<div class="form-group">
		<button type="submit" class="btn btn-primary">Create photo album</button>
	</div>
</form>
