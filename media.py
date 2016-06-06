# -*- coding: utf-8 -*-
"""
Created on Sun Jun 05 19:20:29 2016

@author: Fish
"""

class Movie():
    """
    This a Movie class for gouping all the information for a movie
    And could add necessary methods
    """
    
    def __init__(self, trailer_youtube_url , title,poster_image_url):
        
        """
        This is the constructor .
        It requires to input youtube trailer URL, movie name, poster image url.
        It can be call using instance.* for each relevant element.
        
        """
        self.trailer_youtube_url = trailer_youtube_url 
        self.title = title
        self.poster_image_url = poster_image_url
        
        
