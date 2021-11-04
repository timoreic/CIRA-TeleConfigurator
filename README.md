# CIRA-TeleConfigurator

---

## Project Description
### About
This is the repo for the ISYS3001/ISYS3002 Project, Semester 2, 2021. This application forms a new front-end web application that manages the MWA telescope configurations for CIRA. Their website can be found [here](https://astronomy.curtin.edu.au/).
### Technologies
This project is based almost entirely on the Python framework [Flask](https://flask.palletsprojects.com/en/2.0.x/). This framework allows the dynamic manipulation of HTML through the use of the Jinja2 engine as well as traditional JavaScript. Considerations were made towards making a Flask API and a seperate React (or similar JS framework) front-end, but was decided against as this would increase the projects complexity.
### Goals for the future
- Add sort feedback arrows in database columns
- Improve the applications styling / implement styling guides
- Improve documentation and commenting
### Known issues and challenges
- gpstime --> datetime conversion does not work on Safari based browsers. [Moments.js](https://momentjs.com/) could offer a solution
- PyTest is restricted by current project implementation. Look [here](https://flask.palletsprojects.com/en/2.0.x/testing/#the-application) for more details and comparisons

---

## Table of Contents
- [Project Contributers](https://github.com/Clark1e9/CIRA-TeleConfigurator#project-contributors)
- [How to Contribute to this repo](https://github.com/Clark1e9/CIRA-TeleConfigurator#how-to-contribute-to-this-repo)
- [Starting the Flask Application](https://github.com/Clark1e9/CIRA-TeleConfigurator#starting-the-flask-application)
- [Deployment](https://github.com/Clark1e9/CIRA-TeleConfigurator#deployment)

---

## Project Contributors

Timo Reichelt - Team Leader

Christopher Woods - Scrum Master

Scott Stewart - Documentation Manager

Nicholas Clarke - Quality Manager

---

## How to Contribute to this repo

> _Note: This assumes that you are using VSCode as your Developer Environment_

### 1. Install the VSCode extension [GitHub Pull Requests and Issues](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github)

### 2. Clone the repo locally

- View -> command palette -> `git:clone` -> clone from GitHub -> `CIRA-TeleConfigurator`
- Follow the prompts to save the repo to a local folder

## 3. Stage and commit changes

- Once finished working on a file (or multiple files), you stage your changes for a commit. This gives a developer the option to _not_ commit every file they have changed.
- When commiting your work, please leave a decent comment such as "Refactored code _x, y, z_" or "Added _x_ function". This allows everyone to review work or easily rewind aspects of the project to the correct place
  > If you run into a Git issue to do with a local account follow the tip in this message that was posted in [discord](https://discord.com/channels/872377564130328577/872377722142347265/875320028176715776)

---

## Starting the Flask Application
These steps can be followed if testing the application on your own machine or a server. This implementation is not recommended for production use as it is relatively insecure without HTTPS or strong server securities.
> This guide assumes the use of a BASH shell (Linux, MacOS or WSL)

### 1. Clone the repo to the device
> See above for instructions on how to clone using VSCode.

   *or*

Use this command in your terminal: `git clone https://github.com/Clark1e9/CIRA-TeleConfigurator.git`

### 2. Install the virtual environment and dependencies

The repo should contain a script called 'installenv.sh'. Start this script to create and install all the project dependencies by executing `./installenv.sh`. If this doesn't run try compiling the script with `chmod +x installenv.sh` and try again.

  *or*

Start an empty virtual environment: `virtualenv env`.
Then start the environment: `. env/bin/activate` or `source env/bin/activate`.
Then install the requirements: `pip install -r requirements`.

  *or*

Try the big magic bullet that might be able to do everything:

       virtualenv env && source env/bin/activate && pip install -r requirements.txt
       
### 3. Configure the application
Most of the applications configurations are managed by two files: 'config.py' and '.flaskenv'. The key configuration options are set below:

  #### Secret key - config.py
  The secret key is meant to be a secure string used by Flask modules such as WTF-Forms to improve application security. As currently set, This key can be set as an Flask environment variable (see [here](https://flask.palletsprojects.com/en/2.0.x/config/) for more info and environment options) or as a plain string in the 'config.py' file. This key should not be uplocommited to this repository and distributed only when necessary.

  #### Database URI - config.py
  This is the address used by the Flask module SQLAlchemy to access the database tables outlined in 'models.py'. The first parameter is used for accessing database servers. Connections should follow this format: <db type>://<user>:<password>@<hostname>/<db name>.
  
  To connect to a local postgress server the connection would look something as follows: `postgresql://mwa:password1@127.0.0.1/mwa`.

  The second parameter accepts a local database connection with the default name of 'app.db'. This can be changed to any name as necesary. This option is only used if the first option is null or fails.

  #### Development Environment - .flaskenv
  By setting the flask environment to development, the flask server will attempt to hot reload everytime it detects changes to python files. This can be helpful during development but should be avoided in production envronments. The project default is currently `FLASK_ENV=development` but can be changed by deleting or commenting out the line.
  
  #### LAN connectivity - .flaskenv
  If wanting to share the application with other users on a local network then the HOST environment variable should be added. This can be done with `HOST=0.0.0.0` to the .flaskenv file. Other users could then connect with the computer's or server;s local IP address port 5000. This would also allow for sharing over the internet with port forwarding but this isnt recommended. 

### 4. Start the Flask application

Start the application with `flask run`. This will load the configurations set earlier. The default connection if running on a personal computer will be 'http://localhost:5000'.

---

## Deployment
  Deployment of the application was out of scope for the intial project. However, Flask recommends running a wsgi gateway behind a Apache web server. Check the [Flask documentation](https://flask.palletsprojects.com/en/2.0.x/deploying/) for more details and options.
