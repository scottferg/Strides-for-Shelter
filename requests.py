import cgi
import os

from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db

class Entry( db.Model ):
    author = db.UserProperty( )
    content = db.StringProperty( multiline = True )
    date = db.DateTimeProperty( auto_now_add = True )

class MainPage( webapp.RequestHandler ):
    def get( self ):

        template_values = { }

        path = os.path.join( os.path.dirname( __file__ ), 'templates/main.html' )
        self.response.out.write( template.render( path, template_values ) )

class News( webapp.RequestHandler ):
    def get ( self ):
        entries = entry.all( ).order( '-date' ).fetch( 10 )

        template_values = {
            'entries': entries,
        }

        path = os.path.join( os.path.dirname( __file__ ), 'templates/news.html' )
        self.response.out.write( template.render( path, template_values ) )

    def post( self ):
        entry = Entry( )

        if users.get_current_user( ):
            entry.author = users.get_current_user( )
        
        entry.content = self.request.get( 'content' )
        entry.put( )
        self.redirect( '/' )

class Signup( webapp.RequestHandler ):
    def get( self ):
    
        template_values = { }

        path = os.path.join( os.path.dirname( __file__ ), 'templates/signup.html' )
        self.response.out.write( template.render( path, template_values ) )

class About( webapp.RequestHandler ):
    def get( self ):

        template_values = { }

        path = os.path.join( os.path.dirname( __file__ ), 'templates/about.html' )
        self.response.out.write( template.render( path, template_values ) )

class Sponsors( webapp.RequestHandler ):
    def get( self ):

        template_values = { }

        path = os.path.join( os.path.dirname( __file__ ), 'templates/sponsors.html' )
        self.response.out.write( template.render( path, template_values ) )

class Contact( webapp.RequestHandler ):
    def get( self ):

        template_values = { }

        path = os.path.join( os.path.dirname( __file__ ), 'templates/contact.html' )
        self.response.out.write( template.render( path, template_values ) )

application = webapp.WSGIApplication( [( '/', MainPage ),
                                       ( '/news', News ),
                                       ( '/signup', Signup ),
                                       ( '/about', About ),
                                       ( '/sponsors', Sponsors ),
                                       ( '/contact', Contact )],
                                       debug = True )

def main( ):
    run_wsgi_app( application )

if __name__ == "__main__":
    main( )
