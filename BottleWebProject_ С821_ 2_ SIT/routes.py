"""
Routes and views for the bottle application.
"""

from bottle import route, view
from datetime import datetime

@route('/')
@route('/home')
@view('index')
def home():
    """Renders the home page."""
    return dict(
        year=datetime.now().year
    )

@route('/method1')
@view('method1')
def contact():
    """Renders the contact page."""
    return dict(
        title='Method 1',
        message='Thats method 1.',
        year=datetime.now().year
    )

@route('/method2')
@view('method2')
def contact():
    """Renders the contact page."""
    return dict(
        title='Method 2',
        message='Thats method 2.',
        year=datetime.now().year
    )

@route('/method3')
@view('method3')
def contact():
    """Renders the contact page."""
    return dict(
        title='Method 3',
        message='Thats method 3.',
        year=datetime.now().year
    )

@route('/about')
@view('about')
def about():
    """Renders the about page."""
    return dict(
        title='About',
        message='Your application description page.',
        year=datetime.now().year
    )
