from app import app, db
from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    IntegerField,
    FloatField,
    SubmitField,
    BooleanField,
    DateTimeField,
    SelectField,
)
from wtforms.validators import DataRequired, Optional
from wtforms import ValidationError
from app.models import *


# New - Tile
class NewTileForm(FlaskForm):
    tile_id = IntegerField("tile_id", validators=[DataRequired()])
    tile_pos_east = FloatField("tile_pos_east", validators=[Optional()])
    tile_pos_north = FloatField("tile_pos_north", validators=[Optional()])
    tile_altitude = FloatField("tile_pos_altitude", validators=[Optional()])
    beamformer_id = IntegerField("beamformer_id", validators=[Optional()])
    submit = SubmitField("Add New Tile")
    # Custom Validation - Active tile_id must be unique
    def validate_tile_id(self, field):
        if Tile.query.filter(Tile.tile_id==field.data).filter(Tile.endtime==9e99).first():
            raise ValidationError('Active tile_id already exists.')


# Update - Tile
class UpdateTileForm(FlaskForm):
    tile_id = IntegerField("tile_id", render_kw={'readonly': True})
    tile_pos_east = FloatField("tile_pos_east", validators=[Optional()])
    tile_pos_north = FloatField("tile_pos_north", validators=[Optional()])
    tile_altitude = FloatField("tile_pos_altitude", validators=[Optional()])
    beamformer_id = IntegerField("beamformer_id", validators=[Optional()])
    submit = SubmitField("Update")


# New - Beamformer
class NewBeamformerForm(FlaskForm):
    beamformer_id = IntegerField("beamformer_id", validators=[DataRequired()])
    gain_y = FloatField("gain_y", validators=[Optional()])
    gain_x = FloatField("gain_x", validators=[Optional()])
    submit = SubmitField("Add New Beamformer")
    # Custom Validation - Active beamformer_id must be unique
    def validate_beamformer_id(self, field):
        if Beamformer.query.filter(Beamformer.beamformer_id==field.data).filter(Beamformer.endtime==9e99).first():
            raise ValidationError('Active beamformer_id already exists.')


# Update - Beamformer
class UpdateBeamformerForm(FlaskForm):
    beamformer_id = IntegerField("beamformer_id", render_kw={'readonly': True})
    gain_y = FloatField("gain_y", validators=[Optional()])
    gain_x = FloatField("gain_x", validators=[Optional()])
    submit = SubmitField("Update")


# New - Cable
class NewCableForm(FlaskForm):
    name = StringField("name", validators=[DataRequired()])
    type = StringField("type", validators=[Optional()])
    eleclength = FloatField("eleclength", validators=[Optional()])
    physlength = FloatField("physlength", validators=[Optional()])
    flavor = SelectField("flavor:", validators=[Optional()])
    submit = SubmitField("Add New Cable")
    # Custom Validation - Active name must be unique
    def validate_name(self, field):
        if Cable.query.filter(Cable.name==field.data).filter(Cable.endtime==9e99).first():
            raise ValidationError('Active name already exists.')


# Update - Cable
class UpdateCableForm(FlaskForm):
    name = StringField("name", render_kw={'readonly': True})
    type = StringField("type", validators=[Optional()])
    eleclength = FloatField("eleclength", validators=[Optional()])
    physlength = FloatField("physlength", validators=[Optional()])
    flavor = SelectField("flavor:", validators=[Optional()])
    submit = SubmitField("Update")


# New - Receiver
class NewReceiverForm(FlaskForm):
    receiver_id = IntegerField("receiver_id", validators=[DataRequired()])
    sbc_name = StringField("sbc_name", validators=[Optional()])
    fibre_length = FloatField("fibre_length", validators=[Optional()])
    active = BooleanField("active?", default=False)
    receiver_slot1 = IntegerField("receiver_slot1", validators=[Optional()])
    tile1 = IntegerField("tile1", validators=[Optional()])
    beamformer_id1 = IntegerField("beamformer_id1", validators=[Optional()])
    cable_name1 = StringField("cable_name1", validators=[Optional()])
    receiver_slot2 = IntegerField("receiver_slot2", validators=[Optional()])
    tile2 = IntegerField("tile2", validators=[Optional()])
    beamformer_id2 = IntegerField("beamformer_id2", validators=[Optional()])
    cable_name2 = StringField("cable_name2", validators=[Optional()])
    receiver_slot3 = IntegerField("receiver_slot3", validators=[Optional()])
    tile3 = IntegerField("tile3", validators=[Optional()])
    beamformer_id3 = IntegerField("beamformer_id3", validators=[Optional()])
    cable_name3 = StringField("cable_name3", validators=[Optional()])
    receiver_slot4 = IntegerField("receiver_slot4", validators=[Optional()])
    tile4 = IntegerField("tile4", validators=[Optional()])
    beamformer_id4 = IntegerField("beamformer_id4", validators=[Optional()])
    cable_name4 = StringField("cable_name4", validators=[Optional()])
    receiver_slot5 = IntegerField("receiver_slot5", validators=[Optional()])
    tile5 = IntegerField("tile5", validators=[Optional()])
    beamformer_id5 = IntegerField("beamformer_id5", validators=[Optional()])
    cable_name5 = StringField("cable_name5", validators=[Optional()])
    receiver_slot6 = IntegerField("receiver_slot6", validators=[Optional()])
    tile6 = IntegerField("tile6", validators=[Optional()])
    beamformer_id6 = IntegerField("beamformer_id6", validators=[Optional()])
    cable_name6 = StringField("cable_name6", validators=[Optional()])
    receiver_slot7 = IntegerField("receiver_slot7", validators=[Optional()])
    tile7 = IntegerField("tile7", validators=[Optional()])
    beamformer_id7 = IntegerField("beamformer_id7", validators=[Optional()])
    cable_name7 = StringField("cable_name7", validators=[Optional()])
    receiver_slot8 = IntegerField("receiver_slot8", validators=[Optional()])
    tile8 = IntegerField("tile8", validators=[Optional()])
    beamformer_id8 = IntegerField("beamformer_id8", validators=[Optional()])
    cable_name8 = StringField("cable_name8", validators=[Optional()])
    submit = SubmitField("Add New Receiver")
    # Custom Validation - Active receiver_id must be unique
    def validate_receiver_id(self, field):
        if Receiver.query.filter(Receiver.receiver_id==field.data).filter(Receiver.endtime==9e99).first():
            raise ValidationError('Active receiver_id already exists.')


# Update - Receiver
class UpdateReceiverForm(FlaskForm):
    receiver_id = IntegerField("receiver_id", render_kw={'readonly': True})
    sbc_name = StringField("sbc_name", validators=[Optional()])
    fibre_length = FloatField("fibre_length", validators=[Optional()])
    active = BooleanField("active?")
    receiver_slot1 = IntegerField("receiver_slot1", validators=[Optional()])
    tile1 = IntegerField("tile1", validators=[Optional()])
    beamformer_id1 = IntegerField("beamformer_id1", validators=[Optional()])
    cable_name1 = StringField("cable_name1", validators=[Optional()])
    receiver_slot2 = IntegerField("receiver_slot2", validators=[Optional()])
    tile2 = IntegerField("tile2", validators=[Optional()])
    beamformer_id2 = IntegerField("beamformer_id2", validators=[Optional()])
    cable_name2 = StringField("cable_name2", validators=[Optional()])
    receiver_slot3 = IntegerField("receiver_slot3", validators=[Optional()])
    tile3 = IntegerField("tile3", validators=[Optional()])
    beamformer_id3 = IntegerField("beamformer_id3", validators=[Optional()])
    cable_name3 = StringField("cable_name3", validators=[Optional()])
    receiver_slot4 = IntegerField("receiver_slot4", validators=[Optional()])
    tile4 = IntegerField("tile4", validators=[Optional()])
    beamformer_id4 = IntegerField("beamformer_id4", validators=[Optional()])
    cable_name4 = StringField("cable_name4", validators=[Optional()])
    receiver_slot5 = IntegerField("receiver_slot5", validators=[Optional()])
    tile5 = IntegerField("tile5", validators=[Optional()])
    beamformer_id5 = IntegerField("beamformer_id5", validators=[Optional()])
    cable_name5 = StringField("cable_name5", validators=[Optional()])
    receiver_slot6 = IntegerField("receiver_slot6", validators=[Optional()])
    tile6 = IntegerField("tile6", validators=[Optional()])
    beamformer_id6 = IntegerField("beamformer_id6", validators=[Optional()])
    cable_name6 = StringField("cable_name6", validators=[Optional()])
    receiver_slot7 = IntegerField("receiver_slot7", validators=[Optional()])
    tile7 = IntegerField("tile7", validators=[Optional()])
    beamformer_id7 = IntegerField("beamformer_id7", validators=[Optional()])
    cable_name7 = StringField("cable_name7", validators=[Optional()])
    receiver_slot8 = IntegerField("receiver_slot8", validators=[Optional()])
    tile8 = IntegerField("tile8", validators=[Optional()])
    beamformer_id8 = IntegerField("beamformer_id8", validators=[Optional()])
    cable_name8 = StringField("cable_name8", validators=[Optional()])
    delete_connection1 = BooleanField("delete_connection1", default=False)
    delete_connection2 = BooleanField("delete_connection2", default=False)
    delete_connection3 = BooleanField("delete_connection3", default=False)
    delete_connection4 = BooleanField("delete_connection4", default=False)
    delete_connection5 = BooleanField("delete_connection5", default=False)
    delete_connection6 = BooleanField("delete_connection6", default=False)
    delete_connection7 = BooleanField("delete_connection7", default=False)
    delete_connection8 = BooleanField("delete_connection8", default=False)
    submit = SubmitField("Update Receiver")


# Delete - Receiver
class DeleteReceiverForm(FlaskForm):
    delete_receiver = BooleanField("delete receiver?", default=False)
    submit = SubmitField("Delete Receiver")


# Update - Flag
class UpdateFlagForm(FlaskForm):
    starttime = IntegerField("starttime")
    stoptime = IntegerField("stoptime")
    tile_id = IntegerField("tile_id", validators=[DataRequired()])
    creator = StringField("creator", validators=[DataRequired()])
    comment = StringField("comment", validators=[Optional()])
    resolved = BooleanField("Resolved?", default=False)
    submit = SubmitField("Update")


# New - Flag
class NewFlagForm(FlaskForm):
    starttime = IntegerField("starttime")
    stoptime = IntegerField("stoptime")
    tile_id = IntegerField("tile_id", validators=[DataRequired()])
    creator = StringField("creator", validators=[DataRequired()])
    comment = StringField("comment", validators=[Optional()])
    submit = SubmitField("Add New Flag")


# Save - Configuration
class SaveConfigForm(FlaskForm):
    configuration_name = StringField("configuration_name",
                                     validators=[DataRequired()])
    submit = SubmitField("Save")
    # Custom Validation - configuration_name must be unique
    def validate_configuration_name(self, field):
        if Configuration.query.filter(Configuration.configuration_name == field.data).first():
            raise ValidationError('Configuration name already exists.')


# Retrieve - Configuration
class RetrieveConfigForm(FlaskForm):
    config_id = IntegerField("config_id", validators=[DataRequired()])
    configuration_name = StringField("configuration_name",
                                     validators=[DataRequired()])
    submit = SubmitField("Retrieve Configuration")
    