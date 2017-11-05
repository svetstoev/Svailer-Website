# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 15:09:51 2017

@author: Svetlozar Stoev
"""
import media
import fresh_tomatoes

#  Create instances of the Movie class assigning information to its attributes
rocky = media.Movie("Rocky",
                    "Rocky Balboa, a small-time boxer, gets a supremely\
                     rare chance to fight heavy-weight champion Apollo\
                     Creed in a bout in which he strives to go\
                     the distance for his self-respect.",
                    "https://upload.wikimedia.org/wikipedia/en/1/18/Rocky_poster.jpg",
                    "https://www.youtube.com/watch?v=7RYpJAUMo2M")

devils_advocate = media.Movie("The Devil's Advocate",
                              "An exceptionally adept Florida lawyer\
                               is offered a job to work in New York City for\
                               a high-end law firm with a high-end\
                               boss - the biggest opportunity of his\
                               career to date.",
                              "https://upload.wikimedia.org/wikipedia/en/3/3f/Devilsadvocate.jpg",
                              "https://www.youtube.com/watch?v=CkNfxHw5wo8")

southpaw = media.Movie("Southpaw",
                       "A story of a boxer who lost everything\
                        but fought to get back on his feet in order\
                        to support his little daughter.",
                       "https://upload.wikimedia.org/wikipedia/en/8/89/Southpaw_poster.jpg",
                       "https://www.youtube.com/watch?v=Mh2ebPxhoLs")

john_wick = media.Movie("John Wick",
                        "An ex-hitman comes out of retirement to track\
                         down the gangsters that took everything from him.",
                        "https://upload.wikimedia.org/wikipedia/en/9/98/John_Wick_TeaserPoster.jpg",
                        "https://www.youtube.com/watch?v=RllJtOw0USI")

i_want_you = media.Movie("I Want You",
                         "Starts with the return of H to his hometown\
                          where reconnecting with the past means struggle\
                          and also a new love.",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BMzdiNDkyNjUtMDcwNC00YWYyLTk2NTMtMWJiZGFiYTg0NTYwXkEyXkFqcGdeQXVyMTA0MjU0Ng@@._V1_.jpg",
                         "https://www.youtube.com/watch?v=X_jZHkOYSIg")

fast_furious = media.Movie("The Fast and the Furious",
                           "Los Angeles police officer Brian O'Connor\
                            must decide where his loyalty really lies\
                            when he becomes enamored with the street racing\
                            world he has been sent undercover to destroy.",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BNzlkNzVjMDMtOTdhZC00MGE1LTkxODctMzFmMjkwZmMxZjFhXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,672,1000_AL_.jpg",
                           "https://www.youtube.com/watch?v=ZsJz2TJAPjw")

blind_side = media.Movie("The Blind Side",
                         "The story of Michael Oher, a homeless and\
                          traumatized boy who became an All American football\
                          player and first round NFL draft pick with\
                          the help of a caring woman and her family.",
                         "https://upload.wikimedia.org/wikipedia/en/6/60/Blind_side_poster.jpg",
                         "https://www.youtube.com/watch?v=gvqj_Tk_kuM")

#  Create a list of all instances
movies = [rocky,
          devils_advocate,
          southpaw,
          john_wick,
          i_want_you,
          fast_furious,
          blind_side]

#  Feed the above list to a function which opens and creates the web page
fresh_tomatoes.open_movies_page(movies)
