'''
Created on Nov 10, 2013

@author: boatkrap
'''
from wtforms import Form
from wtforms import fields
from wtforms import validators

class PhotoAlbum(Form):
    name = fields.TextField('Name', validators=[validators.InputRequired()])
    description = fields.TextAreaField('Description')

class Photo(Form):
    image = fields.FileField('Image', )
    license = fields.SelectField('License', validators=[validators.InputRequired()])