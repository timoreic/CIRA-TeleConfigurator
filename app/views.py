from flask import Flask, render_template, redirect, request, url_for, flash
from app import app, db
from app.models import *
from app.forms import *
from sqlalchemy.sql import func
from datetime import datetime


# Index - Homepage
@app.route("/")
def index():
    """Index displays the home page of the website

    :return function: This fuction renders the template index.html.
    """
    return render_template("index.html")


# Tile - Table
@app.route("/tile", methods=["GET", "POST"])
def tile():
    """Displays the tile_info table on the Tile Page of the website. This fuction uses a POST method to check if there is a POST request. This request allows the data within the form into the database.
        If the fuction finds that there is no valid POST request then it defaults to the GET function and fills the page with the data from the database as is.

    responses:
      200:
        description: Renders the template tile.html
      500:
        description: Internal Server Error
    """
    # Get offset value (GPS to Unix)
    offset = getOffset()
    # POST
    if request.method == "POST":
        # Get time gps values from form
        time = request.form.get("time")
        time_float = request.form.get("time_float")
        # Check if time is a number
        if time_float != "NaN":
            time_float = float(time_float)
        # Show default if not a number
        if time_float == "NaN":
            return redirect("/tile")
        # Seach for time
        elif time_float != "NaN":
            tiles = (Tile.query.filter(Tile.begintime <= time_float).filter(
                Tile.endtime >= time_float).order_by(Tile.tile_id))
            return render_template(
                "tile.html",
                tiles=tiles,
                offset=offset,
                time=time,
                time_float=time_float,
            )
        # Error
        else:
            return render_template("500.html")
    # GET
    else:
        currentTime = datetime.today().strftime("%Y-%m-%dT%H:%M:%S")
        currentGPStime = db.session.query(func.public.gpsnow()).first()
        currentGPStime = currentGPStime[0]
        tiles = Tile.query.filter_by(endtime=9e99).order_by(Tile.tile_id)
        return render_template(
            "tile.html",
            tiles=tiles,
            offset=offset,
            time=currentTime,
            time_float=currentGPStime,
        )


# Tile - Update Entry
@app.route("/tile/<int:tile_id>/<float:begintime>", methods=["GET", "POST"])
def updateTile(tile_id, begintime):
    """Displays the tile to update in the UpdateTileForm that is defined in forms.py. This fuction uses a POST method to check if there is a POST request. This request allows the data within the form into the database.
        If the fuction finds that there is no valid POST request then it defaults to the GET function and fills the page with the data from the database as is.

    parameters:
      - name: tile_id
        in: path
        type: int
        required: true
        description: Tile id
      - name: begintime
        in: path
        type: float
        required: true
        description: Tile begintime

    responses:
      200:
        description: Renders the template updateTile.html
      404:
        description: Tile not found
    """
    tile_to_update = Tile.query.get_or_404([tile_id, begintime])
    form = UpdateTileForm()
    # POST & form submitted successfully
    if request.method == "POST" and form.validate_on_submit():
        # Set stoptime of old entry to gpsnow
        tile_to_update.endtime = func.public.gpsnow()
        db.session.add(tile_to_update)
        db.session.commit()
        # Add new Tile entry with updated values
        updatedTile = Tile(
            tile_id=form.tile_id.data,
            begintime=func.public.gpsnow(),
            endtime=9e99,
            tile_pos_east=form.tile_pos_east.data,
            tile_pos_north=form.tile_pos_north.data,
            tile_altitude=form.tile_altitude.data,
            beamformer_id=form.beamformer_id.data,
        )
        db.session.add(updatedTile)
        db.session.commit()
        return redirect("/tile")
    # GET
    else:
        return render_template("/updateTile.html",
                               form=form,
                               tile_to_update=tile_to_update)


# Tile - Add New Entry
@app.route("/tile/addNew", methods=["GET", "POST"])
def newTile():
    """Displays the NewTileForm that is defined in forms.py. This fuction uses a POST method to check if there is a POST request. This request allows the data within the form into the database.
        If the fuction finds that there is no valid POST request then it defaults to the GET function and fills the page with the data from the database as is.

    responses:
      200:
        description: Renders the template newTile.html
    """
    form = NewTileForm()
    # POST & form submitted successfully
    if request.method == "POST" and form.validate_on_submit():
        newTile = Tile(
            tile_id=form.tile_id.data,
            begintime=func.public.gpsnow(),
            endtime=9e99,
            tile_pos_east=form.tile_pos_east.data,
            tile_pos_north=form.tile_pos_north.data,
            tile_altitude=form.tile_altitude.data,
            beamformer_id=form.beamformer_id.data,
        )
        db.session.add(newTile)
        db.session.commit()
        return redirect("/tile")
    # GET
    else:
        return render_template("/newTile.html", form=form)


# Beamformer - Table
@app.route("/beamformer", methods=["GET", "POST"])
def beamformer():
    """Displays the beamformer_info table on the beamformer page of the website. This fuction uses a POST method to check if there is a POST request. This request allows the data within the form into the database.
      If the fuction finds that there is no valid POST request then it defaults to the GET function and fills the page with the data from the database as is.

    responses:
      200:
        description: Renders the template beamformer.html
      500:
        description: Internal Server Error
    """
    # Get offset value (GPS to Unix)
    offset = getOffset()
    # POST
    if request.method == "POST":
        # Get time gps values from form
        time = request.form.get("time")
        time_float = request.form.get("time_float")
        # Check if time is a number
        if time_float != "NaN":
            time_float = float(time_float)
        # Show default
        if time_float == "NaN":
            return redirect("/beamformer")
        # Seach for time
        elif time_float != "NaN":
            beamformers = (Beamformer.query.filter(
                Beamformer.begintime <= time_float).filter(
                    Beamformer.endtime >= time_float).order_by(
                        Beamformer.beamformer_id))
            return render_template(
                "beamformer.html",
                beamformers=beamformers,
                offset=offset,
                time=time,
                time_float=time_float,
            )
        # Error
        else:
            return render_template("500.html")
    # GET
    else:
        currentTime = datetime.today().strftime("%Y-%m-%dT%H:%M:%S")
        currentGPStime = db.session.query(func.public.gpsnow()).first()
        currentGPStime = currentGPStime[0]
        beamformers = Beamformer.query.filter_by(endtime=9e99).order_by(
            Beamformer.beamformer_id)
        return render_template(
            "beamformer.html",
            beamformers=beamformers,
            offset=offset,
            time=currentTime,
            time_float=currentGPStime,
        )


# Beamformer - Update Entry
@app.route("/beamformer/<int:beamformer_id>/<float:begintime>",
           methods=["GET", "POST"])
def updateBeamformer(beamformer_id, begintime):
    """Displays the beamformer to update in the UpdateBeamformerForm that is defined in forms.py. This fuction uses a POST method to check if there is a POST request. This request allows the data within the form into the database.
        If the fuction finds that there is no valid POST request then it defaults to the GET function and fills the page with the data from the database as is.

    parameters:
      - name: beamformer_id
        in: path
        type: int
        required: true
        description: Beamformer id
      - name: begintime
        in: path
        type: float
        required: true
        description: Beamformer begintime

    responses:
      200:
        description: Renders the template updateBeamformer.html
      404:
        description: Beamformer not found
    """
    beamformer_to_update = Beamformer.query.get_or_404(
        [beamformer_id, begintime])
    form = UpdateBeamformerForm()
    # POST & form submitted successfully
    if request.method == "POST" and form.validate_on_submit():
        # Set stoptime of old entry to gpsnow
        beamformer_to_update.endtime = func.public.gpsnow()
        db.session.add(beamformer_to_update)
        db.session.commit()
        # Add new Beamformer entry with updated values
        updatedBeamformer = Beamformer(
            beamformer_id=form.beamformer_id.data,
            begintime=func.public.gpsnow(),
            endtime=9e99,
            gain_y=form.gain_y.data,
            gain_x=form.gain_x.data,
        )
        db.session.add(updatedBeamformer)
        db.session.commit()
        return redirect("/beamformer")
    # GET
    else:
        return render_template(
            "/updateBeamformer.html",
            form=form,
            beamformer_to_update=beamformer_to_update,
        )


# Beamformer - Add New Entry
@app.route("/beamformer/addNew", methods=["GET", "POST"])
def newBeamformer():
    """Displays the NewBeamformerForm that is defined in forms.py. This fuction uses a POST method to check if there is a POST request. This request allows the data within the form into the database.
        If the fuction finds that there is no valid POST request then it defaults to the GET function and fills the page with the data from the database as is.

    responses:
      200:
        description: Renders the template newBeamformer.html
    """
    form = NewBeamformerForm()
    # POST & form submitted successfully
    if request.method == "POST" and form.validate_on_submit():
        newBeamformer = Beamformer(
            beamformer_id=form.beamformer_id.data,
            begintime=func.public.gpsnow(),
            endtime=9e99,
            gain_y=form.gain_y.data,
            gain_x=form.gain_x.data,
        )
        db.session.add(newBeamformer)
        db.session.commit()
        return redirect("/beamformer")
    # GET
    else:
        return render_template("/newBeamformer.html", form=form)


# Cable - Table
@app.route("/cable", methods=["GET", "POST"])
def cable():
    """Displays the cable_info table on the cable page of the website. This fuction uses a POST method to check if there is a POST request. This request allows the data within the form into the database.
      If the fuction finds that there is no valid POST request then it defaults to the GET function and fills the page with the data from the database as is.

    responses:
      200:
        description: Renders the template cable.html
      500:
        description: Internal Server Error
    """
    # Get offset value (GPS to Unix)
    offset = getOffset()
    # POST
    if request.method == "POST":
        # Get time gps values from form
        time = request.form.get("time")
        time_float = request.form.get("time_float")
        # Check if time is a number
        if time_float != "NaN":
            time_float = float(time_float)
        # Show default
        if time_float == "NaN":
            return redirect("/cable")
        # Seach for time
        elif time_float != "NaN":
            cables = (Cable.query.filter(Cable.begintime <= time_float).filter(
                Cable.endtime >= time_float).order_by(Cable.name))
            return render_template(
                "cable.html",
                cables=cables,
                offset=offset,
                time=time,
                time_float=time_float,
            )
        # Error
        else:
            return render_template("500.html")
    # GET
    else:
        currentTime = datetime.today().strftime("%Y-%m-%dT%H:%M:%S")
        currentGPStime = db.session.query(func.public.gpsnow()).first()
        currentGPStime = currentGPStime[0]
        cables = Cable.query.filter_by(endtime=9e99).order_by(Cable.name)
        return render_template(
            "cable.html",
            cables=cables,
            offset=offset,
            time=currentTime,
            time_float=currentGPStime,
        )


# Cable - Update Entry
@app.route("/cable/<name>/<float:begintime>", methods=["GET", "POST"])
def updateCable(name, begintime):
    """Displays the cable to update in the UpdateCableForm that is defined in forms.py. This fuction uses a POST method to check if there is a POST request. This request allows the data within the form into the database.
        If the fuction finds that there is no valid POST request then it defaults to the GET function and fills the page with the data from the database as is.

    parameters:
      - name: name
        in: path
        type: string
        required: true
        description: Cable name
      - name: begintime
        in: path
        type: float
        required: true
        description: Cable begintime

    responses:
      200:
        description: Renders the template updateCable.html
      404:
        description: Cable not found
    """
    cable_to_update = Cable.query.get_or_404([name, begintime])
    form = UpdateCableForm()
    flavorObjects = Flavor.query.all()
    flavors = [""]
    for flavor in flavorObjects:
        flavors.append(flavor.flavor)
    form.flavor.choices = flavors
    # POST & form submitted successfully
    if request.method == "POST" and form.validate_on_submit():
        # Set stoptime of old entry to gpsnow
        cable_to_update.endtime = func.public.gpsnow()
        db.session.add(cable_to_update)
        db.session.commit()
        # Add new Cable entry with updated values
        updatedCable = Cable(
            name=form.name.data,
            begintime=func.public.gpsnow(),
            endtime=9e99,
            type=form.type.data,
            eleclength=form.eleclength.data,
            physlength=form.physlength.data,
            flavor=form.flavor.data,
        )
        db.session.add(updatedCable)
        db.session.commit()
        return redirect("/cable")
    # GET
    else:
        return render_template("/updateCable.html",
                               form=form,
                               cable_to_update=cable_to_update)


# Cable - Add New Entry
@app.route("/cable/addNew", methods=["GET", "POST"])
def newCable():
    """Displays the NewCableForm that is defined in forms.py. This fuction uses a POST method to check if there is a POST request. This request allows the data within the form into the database.
        If the fuction finds that there is no valid POST request then it defaults to the GET function and fills the page with the data from the database as is.

    responses:
      200:
        description: Renders the template newCable.html
    """
    form = NewCableForm()
    flavorObjects = Flavor.query.all()
    flavors = [""]
    for flavor in flavorObjects:
        flavors.append(flavor.flavor)
    form.flavor.choices = flavors
    # POST & form submitted successfully
    if request.method == "POST" and form.validate_on_submit():
        newCable = Cable(
            name=form.name.data,
            begintime=func.public.gpsnow(),
            endtime=9e99,
            type=form.type.data,
            eleclength=form.eleclength.data,
            physlength=form.physlength.data,
            flavor=form.flavor.data,
        )
        db.session.add(newCable)
        db.session.commit()
        return redirect("/cable")
    # GET
    else:
        return render_template("/newCable.html", form=form)


# Receiver - Table
@app.route("/receiver", methods=["GET", "POST"])
def receiver():
    """Displays the receiver_info table on the receiver page of the website. This fuction uses a POST method to check if there is a POST request. This request allows the data within the form into the database.
      If the fuction finds that there is no valid POST request then it defaults to the GET function and fills the page with the data from the database as is.

    responses:
      200:
        description: Renders the template receiver.html
      500:
        description: Internal Server Error
    """
    # Get offset value (GPS to Unix)
    offset = getOffset()
    # POST
    if request.method == "POST":
        # Get time gps values from form
        time = request.form.get("time")
        time_float = request.form.get("time_float")
        # Check if time is a number
        if time_float != "NaN":
            time_float = float(time_float)
        # Show default
        if time_float == "NaN":
            return redirect("/receiver")
        # Seach for time
        elif time_float != "NaN":
            receivers = (Receiver.query.filter(
                Receiver.begintime <= time_float).filter(
                    Receiver.endtime >= time_float).order_by(
                        Receiver.receiver_id))
            connections = (Connection.query.filter(
                Connection.begintime <= time_float).filter(
                    Connection.endtime >= time_float).order_by(
                        Connection.receiver_slot))
            return render_template(
                "receiver.html",
                receivers=receivers,
                connections=connections,
                offset=offset,
                time=time,
                time_float=time_float,
            )
        # Error
        else:
            return render_template("500.html")
    # GET
    else:
        currentDatetime = datetime.today().strftime("%Y-%m-%dT%H:%M:%S")
        currentGPStime = db.session.query(func.public.gpsnow()).first()
        currentGPStime = currentGPStime[0]
        receivers = Receiver.query.filter_by(endtime=9e99).order_by(
            Receiver.receiver_id)
        connections = Connection.query.filter_by(endtime=9e99).order_by(
            Connection.receiver_slot)
        return render_template(
            "receiver.html",
            receivers=receivers,
            connections=connections,
            offset=offset,
            time=currentDatetime,
            time_float=currentGPStime,
        )


# Receiver - Update Entry
@app.route("/receiver/<int:receiver_id>/<float:begintime>",
           methods=["GET", "POST"])
def updateReceiver(receiver_id, begintime):
    """Displays the receiver to update in the UpdateReceiverForm that is defined in forms.py. This fuction uses a POST method to check if there is a POST request. This request allows the data within the form into the database.
        If the fuction finds that there is no valid POST request then it defaults to the GET function and fills the page with the data from the database as is.

    parameters:
      - name: receiver id
        in: path
        type: int
        required: true
        description: receiver id
      - name: size
        in: query
        type: float
        description: receiver begintime

    responses:
      200:
        description: Renders the template updateReceiver.html
      404:
        description: Receiver not found
    """
    receiver_to_update = Receiver.query.get_or_404([receiver_id, begintime])
    connections_to_update = (Connection.query.filter_by(
        endtime=9e99).filter_by(receiver_id=receiver_id).order_by(
            Connection.receiver_slot).all())
    form = UpdateReceiverForm()
    deleteReceiverForm = DeleteReceiverForm()
    numConnections = len(connections_to_update)
    # POST & UpdateReceiverForm submitted successfully
    if request.method == "POST" and form.validate_on_submit():
        deactivateConfigs()
        # Set stoptime of old entries (receiver and all connections) to gpsnow
        receiver_to_update.endtime = func.public.gpsnow()
        for connection in connections_to_update:
            connection.endtime = func.public.gpsnow()
            db.session.add(connection)
        db.session.add(receiver_to_update)
        # Add new receiver with updated values
        newReceiver = Receiver(
            receiver_id=form.receiver_id.data,
            begintime=func.public.gpsnow(),
            endtime=9e99,
            sbc_name=form.sbc_name.data,
            fibre_length=form.fibre_length.data,
            active=form.active.data,
        )
        db.session.add(newReceiver)
        # Add connection1
        if form.tile1.data != None and form.delete_connection1.data == False:
            newConnection1 = Connection(
                tile=form.tile1.data,
                begintime=func.public.gpsnow(),
                endtime=9e99,
                receiver_id=form.receiver_id.data,
                receiver_slot=form.receiver_slot1.data,
                beamformer_id=form.beamformer_id1.data,
                cable_name=form.cable_name1.data,
            )
            db.session.add(newConnection1)
        # Add connection2
        if form.tile2.data != None and form.delete_connection2.data == False:
            newConnection2 = Connection(
                tile=form.tile2.data,
                begintime=func.public.gpsnow(),
                endtime=9e99,
                receiver_id=form.receiver_id.data,
                receiver_slot=form.receiver_slot2.data,
                beamformer_id=form.beamformer_id2.data,
                cable_name=form.cable_name2.data,
            )
            db.session.add(newConnection2)
        # Add connection3
        if form.tile3.data != None and form.delete_connection3.data == False:
            newConnection3 = Connection(
                tile=form.tile3.data,
                begintime=func.public.gpsnow(),
                endtime=9e99,
                receiver_id=form.receiver_id.data,
                receiver_slot=form.receiver_slot3.data,
                beamformer_id=form.beamformer_id3.data,
                cable_name=form.cable_name3.data,
            )
            db.session.add(newConnection3)
        # Add connection4
        if form.tile4.data != None and form.delete_connection4.data == False:
            newConnection4 = Connection(
                tile=form.tile4.data,
                begintime=func.public.gpsnow(),
                endtime=9e99,
                receiver_id=form.receiver_id.data,
                receiver_slot=form.receiver_slot4.data,
                beamformer_id=form.beamformer_id4.data,
                cable_name=form.cable_name4.data,
            )
            db.session.add(newConnection4)
        # Add connection5
        if form.tile5.data != None and form.delete_connection5.data == False:
            newConnection5 = Connection(
                tile=form.tile5.data,
                begintime=func.public.gpsnow(),
                endtime=9e99,
                receiver_id=form.receiver_id.data,
                receiver_slot=form.receiver_slot5.data,
                beamformer_id=form.beamformer_id5.data,
                cable_name=form.cable_name5.data,
            )
            db.session.add(newConnection5)
        # Add connection6
        if form.tile6.data != None and form.delete_connection6.data == False:
            newConnection6 = Connection(
                tile=form.tile6.data,
                begintime=func.public.gpsnow(),
                endtime=9e99,
                receiver_id=form.receiver_id.data,
                receiver_slot=form.receiver_slot6.data,
                beamformer_id=form.beamformer_id6.data,
                cable_name=form.cable_name6.data,
            )
            db.session.add(newConnection6)
        # Add connection7
        if form.tile7.data != None and form.delete_connection7.data == False:
            newConnection7 = Connection(
                tile=form.tile7.data,
                begintime=func.public.gpsnow(),
                endtime=9e99,
                receiver_id=form.receiver_id.data,
                receiver_slot=form.receiver_slot7.data,
                beamformer_id=form.beamformer_id7.data,
                cable_name=form.cable_name7.data,
            )
            db.session.add(newConnection7)
        # Add connection8
        if form.tile8.data != None and form.delete_connection8.data == False:
            newConnection8 = Connection(
                tile=form.tile8.data,
                begintime=func.public.gpsnow(),
                endtime=9e99,
                receiver_id=form.receiver_id.data,
                receiver_slot=form.receiver_slot8.data,
                beamformer_id=form.beamformer_id8.data,
                cable_name=form.cable_name8.data,
            )
            db.session.add(newConnection8)
        db.session.commit()
        return redirect("/receiver")
    # POST & deleteReceiverForm submitted successfully
    elif request.method == "POST" and deleteReceiverForm.validate_on_submit():
        # Set stoptime of old entries (receiver and all connections) to gpsnow
        receiver_to_update.endtime = func.public.gpsnow()
        for connection in connections_to_update:
            connection.endtime = func.public.gpsnow()
            db.session.add(connection)
        db.session.add(receiver_to_update)
        db.session.commit()
        return redirect("/receiver")
    # GET
    else:
        return render_template(
            "/updateReceiver.html",
            form=form,
            deleteReceiverForm=deleteReceiverForm,
            receiver_to_update=receiver_to_update,
            connections_to_update=connections_to_update,
            numConnections=numConnections,
        )


# Receiver - Add New Entry
@app.route("/receiver/addNew", methods=["GET", "POST"])
def newReceiver():
    """Displays the NewReceiverForm that is defined in forms.py. This fuction uses a POST method to check if there is a POST request. This request allows the data within the form into the database.
        If the fuction finds that there is no valid POST request then it defaults to the GET function and fills the page with the data from the database as is.

    responses:
      200:
        description: Renders the template newReceiver.html
    """
    form = NewReceiverForm()
    # POST & form submitted successfully
    if request.method == "POST" and form.validate_on_submit():
        deactivateConfigs()
        # Add new receiver
        newReceiver = Receiver(
            receiver_id=form.receiver_id.data,
            begintime=func.public.gpsnow(),
            endtime=9e99,
            sbc_name=form.sbc_name.data,
            fibre_length=form.fibre_length.data,
            active=form.active.data,
        )
        db.session.add(newReceiver)
        # Add connection1
        if form.tile1.data != None:
            newConnection1 = Connection(
                tile=form.tile1.data,
                begintime=func.public.gpsnow(),
                endtime=9e99,
                receiver_id=form.receiver_id.data,
                receiver_slot=1,
                beamformer_id=form.beamformer_id1.data,
                cable_name=form.cable_name1.data,
            )
            db.session.add(newConnection1)
        # Add connection2
        if form.tile2.data != None:
            newConnection2 = Connection(
                tile=form.tile2.data,
                begintime=func.public.gpsnow(),
                endtime=9e99,
                receiver_id=form.receiver_id.data,
                receiver_slot=2,
                beamformer_id=form.beamformer_id2.data,
                cable_name=form.cable_name2.data,
            )
            db.session.add(newConnection2)
        # Add connection3
        if form.tile3.data != None:
            newConnection3 = Connection(
                tile=form.tile3.data,
                begintime=func.public.gpsnow(),
                endtime=9e99,
                receiver_id=form.receiver_id.data,
                receiver_slot=3,
                beamformer_id=form.beamformer_id3.data,
                cable_name=form.cable_name3.data,
            )
            db.session.add(newConnection3)
        # Add connection4
        if form.tile4.data != None:
            newConnection4 = Connection(
                tile=form.tile4.data,
                begintime=func.public.gpsnow(),
                endtime=9e99,
                receiver_id=form.receiver_id.data,
                receiver_slot=4,
                beamformer_id=form.beamformer_id4.data,
                cable_name=form.cable_name4.data,
            )
            db.session.add(newConnection4)
        # Add connection5
        if form.tile5.data != None:
            newConnection5 = Connection(
                tile=form.tile5.data,
                begintime=func.public.gpsnow(),
                endtime=9e99,
                receiver_id=form.receiver_id.data,
                receiver_slot=5,
                beamformer_id=form.beamformer_id5.data,
                cable_name=form.cable_name5.data,
            )
            db.session.add(newConnection5)
        # Add connection6
        if form.tile6.data != None:
            newConnection6 = Connection(
                tile=form.tile6.data,
                begintime=func.public.gpsnow(),
                endtime=9e99,
                receiver_id=form.receiver_id.data,
                receiver_slot=6,
                beamformer_id=form.beamformer_id6.data,
                cable_name=form.cable_name6.data,
            )
            db.session.add(newConnection6)
        # Add connection7
        if form.tile7.data != None:
            newConnection7 = Connection(
                tile=form.tile7.data,
                begintime=func.public.gpsnow(),
                endtime=9e99,
                receiver_id=form.receiver_id.data,
                receiver_slot=7,
                beamformer_id=form.beamformer_id7.data,
                cable_name=form.cable_name7.data,
            )
            db.session.add(newConnection7)
        # Add connection8
        if form.tile8.data != None:
            newConnection8 = Connection(
                tile=form.tile8.data,
                begintime=func.public.gpsnow(),
                endtime=9e99,
                receiver_id=form.receiver_id.data,
                receiver_slot=8,
                beamformer_id=form.beamformer_id8.data,
                cable_name=form.cable_name8.data,
            )
            db.session.add(newConnection8)
        db.session.commit()
        return redirect("/receiver")
    # GET
    else:
        return render_template("/newReceiver.html", form=form)


# Flags - Table
@app.route("/flags", methods=["GET", "POST"])
def flags():
    """Displays the tile_flags table on the flags page of the website. This fuction uses a POST method to check if there is a POST request. This request allows the data within the form into the database.
      If the fuction finds that there is no valid POST request then it defaults to the GET function and fills the page with the data from the database as is.

    responses:
      200:
        description: Renders the template tile.html
      500:
        description: Internal Server Error
    """
    # Get offset value (GPS to Unix)
    offset = getOffset()
    # POST
    if request.method == "POST":
        # Get time gps values from form
        time = request.form.get("time")
        time_float = request.form.get("time_float")
        # Check if time is a number
        if time_float != "NaN":
            time_float = float(time_float)
        # Show default
        if time_float == "NaN":
            return redirect("/flags")
        # Seach for time
        elif time_float != "NaN":
            flags1 = (Flags.query.filter(Flags.starttime <= time_float).filter(
                Flags.stoptime >= time_float).order_by(Flags.tile_id))
            flags2 = (Flags.query.filter(Flags.starttime <= time_float).filter(
                Flags.stoptime == None).order_by(Flags.tile_id))
            flags = flags1.union(flags2)
            return render_template(
                "flags.html",
                flags=flags,
                offset=offset,
                time=time,
                time_float=time_float,
            )
        # Error
        else:
            return render_template("500.html")
    # GET
    else:
        currentTime = datetime.today().strftime("%Y-%m-%dT%H:%M:%S")
        currentGPStime = db.session.query(func.public.gpsnow()).first()
        currentGPStime = currentGPStime[0]
        flags = Flags.query.filter_by(stoptime=None).order_by(Flags.tile_id)
        return render_template(
            "flags.html",
            flags=flags,
            offset=offset,
            time=currentTime,
            time_float=currentGPStime,
        )


# Flags - Update Entry
@app.route("/flags/<int:tile_id>/<int:starttime>", methods=["GET", "POST"])
def updateFlags(tile_id, starttime):
    """Displays the flag to update in the UpdateFlagForm that is defined in forms.py. This fuction uses a POST method to check if there is a POST request. This request allows the data within the form into the database.
      If the fuction finds that there is no valid POST request then it defaults to the GET function and fills the page with the data from the database as is.

    parameters:
      - name: tile_id
        in: path
        type: int
        required: true
        description: Flags tile id
      - name: starttime
        in: path
        type: int
        required: true
        description: Flag starttime

    responses:
      200:
        description: Renders the template updateFlag.html
    """
    flag_to_update = (Flags.query.filter(Flags.tile_id == tile_id).filter(
        Flags.starttime == starttime).first())
    form = UpdateFlagForm()
    # POST & form submitted successfully
    if request.method == "POST" and form.validate_on_submit():
        if form.resolved.data == True:
            flag_to_update.stoptime = func.public.gpsnow()
            db.session.add(flag_to_update)
            db.session.commit()
            return redirect("/flags")
        else:
            # Set stoptime of old entry to gpsnow
            flag_to_update.stoptime = func.public.gpsnow()
            db.session.add(flag_to_update)
            db.session.commit()
            # Add a new entry with the updated values
            updatedFlag = Flags(
                starttime=func.public.gpsnow(),
                tile_id=form.tile_id.data,
                creator=form.creator.data,
                comment=form.comment.data,
            )
            db.session.add(updatedFlag)
            db.session.commit()
            return redirect("/flags")
    # GET
    else:
        return render_template("/updateFlags.html",
                               form=form,
                               flag_to_update=flag_to_update)


# Flags - Add New Entry
@app.route("/flags/addNew", methods=["GET", "POST"])
def newFlag():
    """Displays the NewFlagForm that is defined in forms.py. This fuction uses a POST method to check if there is a POST request. This request allows the data within the form into the database.
        If the fuction finds that there is no valid POST request then it defaults to the GET function and fills the page with the data from the database as is.

    responses:
      200:
        description: Renders the template newFlag.html
    """
    form = NewFlagForm()
    # POST & form submitted successfully
    if request.method == "POST" and form.validate_on_submit():
        newFlag = Flags(
            starttime=func.public.gpsnow(),
            tile_id=form.tile_id.data,
            creator=form.creator.data,
            comment=form.comment.data,
        )
        db.session.add(newFlag)
        db.session.commit()
        return redirect("/flags")
    # GET
    else:
        return render_template("/newFlag.html", form=form)


# Configuration - Table
@app.route("/configuration")
def configuration():
    """Displays the configuration_info table on the configuration page of the website. This fuction uses a POST method to check if there is a POST request. This request allows the data within the form into the database.
        If the fuction finds that there is no valid POST request then it defaults to the GET function and fills the page with the data from the database as is.

    responses:
      200:
        description: Renders the template configuration.html
      500:
        description: Internal Server Error
    """
    # Get offset value (GPS to Unix)
    offset = getOffset()
    configurations = Configuration.query.order_by(
        Configuration.config_id).all()
    return render_template("configuration.html",
                           configurations=configurations,
                           offset=offset)


# Configuration - Add New Entry
@app.route("/configuration/addNew", methods=["GET", "POST"])
def newConfiguration():
    """Displays the SaveConfigForm that is defined in forms.py. This fuction uses a POST method to check if there is a POST request. This request allows the data within the form into the database.
        If the fuction finds that there is no valid POST request then it defaults to the GET function and fills the page with the data from the database as is.

    responses:
      200:
        description: Renders the template newConfiguration.html
    """
    form = SaveConfigForm()
    # POST & form submitted successfully
    if request.method == "POST" and form.validate_on_submit():
        deactivateConfigs()
        # Add new configuration
        newConfig = Configuration(
            configuration_name=form.configuration_name.data,
            active=True,
            refrence_time=func.public.gpsnow(),
        )
        db.session.add(newConfig)
        # Create new tile_connection entries (newConfig.reference_time = newConnection.begintime)
        currentTime = newConfig.refrence_time
        connections = Connection.query.filter_by(endtime=9e99).order_by(
            Connection.receiver_slot)
        for connection in connections:
            connection.endtime = func.public.gpsnow()
            newConnection = Connection(
                tile=connection.tile,
                begintime=currentTime,
                endtime=9e99,
                receiver_id=connection.receiver_id,
                receiver_slot=connection.receiver_slot,
                beamformer_id=connection.beamformer_id,
                cable_name=connection.cable_name,
            )
            db.session.add(connection)
            db.session.add(newConnection)
        db.session.commit()
        return redirect("/configuration")
    # GET
    else:
        return render_template("/newConfiguration.html", form=form)


# Configuration - Retrieve Configuration
@app.route("/configuration/<int:config_id>/<configuration_name>",
           methods=["GET", "POST"])
def retrieveConfiguration(config_id, configuration_name):
    """Displays the configuration_info table and the RetrieveConfigForm that is defined in forms.py. This fuction uses a POST method to check if there is a POST request. This request allows the data within the form into the database.
        If the fuction finds that there is no valid POST request then it defaults to the GET function and fills the page with the data from the database as is.

    responses:
      200:
        description: Renders the template retrieveConfiguration.html
    """
    form = RetrieveConfigForm()
    configuration_to_retrieve = Configuration.query.filter(
        Configuration.config_id == config_id).first()
    connections = Connection.query.filter_by(
        begintime=configuration_to_retrieve.refrence_time).order_by(
            Connection.receiver_id)
    # POST & form submitted successfully
    if request.method == "POST" and form.validate_on_submit():
        deactivateConfigs()
        configuration_to_retrieve.active = True
        connections_to_deactivate = (Connection.query.filter_by(
            endtime=9e99).order_by(Connection.receiver_slot).all())
        connections_to_activate = (Connection.query.filter_by(
            begintime=configuration_to_retrieve.refrence_time).order_by(
                Connection.receiver_slot).all())
        # Deactivate current connections
        for connection in connections_to_deactivate:
            connection.endtime = func.public.gpsnow()
            db.session.add(connection)
        # Activate new connections
        currentTime = func.public.gpsnow()
        for connection in connections_to_activate:
            newConnection = Connection(
                tile=connection.tile,
                begintime=currentTime,
                endtime=9e99,
                receiver_id=connection.receiver_id,
                receiver_slot=connection.receiver_slot,
                beamformer_id=connection.beamformer_id,
                cable_name=connection.cable_name,
            )
            db.session.add(newConnection)
        db.session.commit()
        return redirect("/configuration")
    # GET
    else:
        return render_template(
            "retrieveConfiguration.html",
            connections=connections,
            configuration_to_retrieve=configuration_to_retrieve,
            form=form,
        )


# Error - 404
@app.errorhandler(404)
def page_not_found(e):
    """Displays a 404 error message - page not found.

    responses:
      200:
        description: Renders the template 404.html
    """
    return render_template("404.html"), 404


# Error - 500
@app.errorhandler(500)
def internal_server_error(e):
    """Displays a 500 error message - internal server error.

    responses:
      200:
        description: Renders the template 500.html
    """
    return render_template("500.html"), 500


# Function - Deactivate all configurations
def deactivateConfigs():
    """This function gets all configurations in the database and deactivates them."""
    configurations = Configuration.query.all()
    for configuration in configurations:
        configuration.active = False


# Function - Get offset value (GPS to Unix)
def getOffset():
    """This function gets the offset value (GPS to Unix) from the database.

    :return offset: offset value (GPS to Unix)
    :type offset: float
    """
    # Get the current offset value from the database
    offsetObject = db.engine.execute(
        "select extract(epoch from timestamp_gps(gpsnow())) - gpsnow();")
    # Extract the value from the LegacyCursorResult object
    offset = offsetObject.first()[0]
    # Return offset
    return offset
