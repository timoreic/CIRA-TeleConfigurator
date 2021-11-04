from app import app, db


class Tile(db.Model):
    __tablename__ = "tile_info"
    tile_id = db.Column(db.Integer, primary_key=True)
    begintime = db.Column(db.Float, primary_key=True)
    endtime = db.Column(db.Float, nullable=True)
    tile_pos_east = db.Column(db.Float, nullable=True)
    tile_pos_north = db.Column(db.Float, nullable=True)
    tile_altitude = db.Column(db.Float, nullable=True)
    beamformer_id = db.Column(db.Integer, nullable=True)


class Beamformer(db.Model):
    __tablename__ = "beamformer_info"
    beamformer_id = db.Column(db.Integer, primary_key=True)
    begintime = db.Column(db.Float, primary_key=True)
    endtime = db.Column(db.Float, nullable=True)
    gain_y = db.Column(db.Float, nullable=True)
    gain_x = db.Column(db.Float, nullable=True)


class Cable(db.Model):
    __tablename__ = "cable_info"
    name = db.Column(db.String, primary_key=True)
    begintime = db.Column(db.Float, primary_key=True)
    endtime = db.Column(db.Float)
    type = db.Column(db.String, nullable=True)
    eleclength = db.Column(db.Float, nullable=True)
    physlength = db.Column(db.Float, nullable=True)
    flavor = db.Column(db.String, nullable=True)


class Receiver(db.Model):
    __tablename__ = "receiver_info"
    receiver_id = db.Column(db.Integer, primary_key=True)
    begintime = db.Column(db.Float, primary_key=True)
    endtime = db.Column(db.Float, nullable=True)
    active = db.Column(db.Boolean, nullable=True)
    creator = db.Column(db.String, default="mwa")
    modtime = db.Column(db.DateTime, nullable=True)
    sbc_name = db.Column(db.String, nullable=True)
    fibre_length = db.Column(db.Float, nullable=True)


class Connection(db.Model):
    __tablename__ = "tile_connection"
    tile = db.Column(db.Integer, primary_key=True)
    begintime = db.Column(db.Float, primary_key=True)
    endtime = db.Column(db.Float, nullable=True)
    receiver_id = db.Column(db.Integer, nullable=True)
    receiver_slot = db.Column(db.Integer, nullable=True)
    wire_length = db.Column(db.Float, nullable=True)
    beamformer_id = db.Column(db.Integer, nullable=True)
    cable_name = db.Column(db.String, nullable=True)


class Flags(db.Model):
    __tablename__ = "tile_flags"
    starttime = db.Column(db.Integer, primary_key=True)
    stoptime = db.Column(db.Integer, nullable=True)
    tile_id = db.Column(db.Integer, primary_key=True)
    creator = db.Column(db.String)
    comment = db.Column(db.String)


class Configuration(db.Model):
    __tablename__ = "configuration_info"
    config_id = db.Column(db.Integer, primary_key=True)
    configuration_name = db.Column(db.String, unique=True)
    active = db.Column(db.Boolean)
    refrence_time = db.Column(db.Float)


class Flavor(db.Model):
    __tablename__ = "cable_flavor"
    flavor = db.Column(db.String, primary_key=True)
