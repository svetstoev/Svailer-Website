"""
Created on Sat Oct 21 15:04:22 2017
# -*- coding: utf-8 -*-
@author: Fujitsu

"""

import webbrowser


class Movie():
    """ This class provides a way to store movie related information

    It has 4 attributes corresponding to the title ('movie title'),
    story line (movie_storyline), poster image ('poster_image_url) and
    youtube trailer ('trailer_youtube_url') of the movie"""

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
