<%inherit file="/forums/base/base.mako"/>
<%! from pumbaa import models %>
<%block name="title">${photo_album.name}</%block>
<%block name="description">${photo_album.description}</%block>
<%block name="where_am_i">
<li><a href="${request.route_path('photos.photo_albums.index')}">Photo Albums</a></li>
<li><a href="${request.route_path('photos.photo_albums.view', photo_album_id=photo_album.id)}">${photo_album.name}</a></li>
</%block>
<%block name="panel_title">${photo_album.name}</%block>

<div style="padding: 5px;">
	<p class="text-primary">
		${photo_album.description}
	</p>
</div>

% for photo in photo_album.photos:
	<a href="${request.route_path('photos.photo_albums.photo_view', photo_album_id=photo_album.id, photo_id=photo.image.filename)}" >
		<img class="img-thumbnail" width="200px" alt="${photo.caption}" src="${request.route_path('photos.thumbnail', photo_album_id=photo_album.id, photo_id=photo.id)}" />
	</a>
% endfor

<%block name="more_body">
<%include file="/base/comments.mako", args="item=photo_album" />
</%block>