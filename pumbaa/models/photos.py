'''
Created on Nov 9, 2013

'''

import mongoengine as me

import datetime
import bson

from . import forums

LICENSE = [
         'COPYRIGHT',
         'CC-BY-NC-ND',
         'CC-BY-ND',
         'CC-BY-NC',
         'CC-BY-SA',
         'CC-BY-NC-SA',
         'CC-BY'
         ]

class Photo(me.EmbeddedDocument):
    id = me.ObjectIdField(required=True, default=bson.ObjectId)
    
    caption = me.StringField(default='')
    
    created_date = me.DateTimeField(required=True, default=datetime.datetime.now)
    updated_date = me.DateTimeField(required=True, default=datetime.datetime.now)

    image = me.ImageField(collection_name='images',
                          size=(1024, 786, True),
                          thumbnail_size=(320, 240, True),
                          )
    comments = me.ListField(me.EmbeddedDocumentField(forums.Comment))
    license = me.StringField(required=True, default='COPYRIGHT', choices=LICENSE)
    
    def get_album(self):
        album = PhotoAlbum.objects(photos__id = self.id).first()
        return album
    
class PhotoAlbum(me.Document):
    meta = {'collection' : 'photo_albums'}
    
    name = me.StringField(required=True)
    description = me.StringField(default='')
    photos = me.ListField(me.EmbeddedDocumentField(Photo))
    status = me.StringField(required=True, default='draft')
    """ status: draft, publish, delete """
    
    created_date = me.DateTimeField(required=True, default=datetime.datetime.now)
    published_date = me.DateTimeField(required=True, default=datetime.datetime.now)
    updated_date = me.DateTimeField(required=True, default=datetime.datetime.now)
    
    
    comments = me.ListField(me.EmbeddedDocumentField(forums.Comment))

    def get_photo(self, photo_id):
        for photo in self.photos:
            if photo.image.filename == photo_id:
                return photo
            if str(photo.id) == photo_id:
                return photo
    
    def get_photo_index(self, photo_id):
        this_photo = None
        for i in range(0, len(self.photos)):
            photo = self.photos[i]
            if photo.image.filename == photo_id:
                this_photo = photo
            if str(photo.id) == photo_id:
                this_photo = photo
                
            if this_photo is not None:
                previous_ = None
                next_ = None

                if i-1 >= 0:
                    previous_ = self.photos[i-1]
                if i+1 < len(self.photos):
                    next_ = self.photos[i+1]

                return this_photo, previous_, next_