from flask import current_app
import pytest


"""
    This is meant to setup the PyTest framework to support regression testing.
    As of 17/10/2021 this doesnt work. 

            RuntimeError: Working outside of application context.

            This typically means that you attempted to use functionality that needed
            to interface with the current application object in some way. To solve
            this, set up an application context with app.app_context().  See the
            documentation for more information.

    See https://testdriven.io/blog/flask-pytest/ for some more info   
"""
@pytest.fixture
def app():
    app = current_app
    return app