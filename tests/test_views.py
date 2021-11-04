def test_home_page(app):
    '''
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    '''

    response = app.get('/')
    assert response.status_code == 200 

def test_tile_page_request(app):
    '''
    GIVEN a Flask application
    WHEN the '/tile' page is requested (GET)
    THEN check that the response is valid
    '''
    response = app.get('/tile')
    assert response.status_code == 200

def test_tile_page_post(app):
    '''
    GIVEN a Flask application
    WHEN the '/tile' page is requested (POST)
    THEN check that the response is valid
    '''
    response = app.get('/tile')
    assert response.status_code == 405

