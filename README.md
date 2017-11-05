# Svailer-Website

Svailer is a Movie Trailer Website containing the names and posters of a number of my favorite movies and subsequently displays their corresponding trailers once the user clicks on the poster image.

**1. Initial requirements**

In order to make use of the project, the user should have a Python- version 3.5.2 installed on their PC, so that they can compile and run the codes included in the current repository.

**2. Getting started**

In order to view the website the user needs to go through the following steps:
- Open and run the file called `entertainment_center.py`
- A web page should open up in your browser
- Click on the poster images and watch the accompanying them movie trailers
- Enjoy! :)

**3. Repository constituents**

- `media.py` - it consists of the class which creates the attributes to the different movies (i.e. title, story line, poster image, trailer video)
- `entertainment_center.py` - this is our main file, it creates different movie instances using the class from `media.py` and then feeds them into a function call from `fresh_tomatoes.py` in order to display our web page. Once you run it, an HTML file called `fresh_tomatoes.html` would be created in the same directory 
- `fresh_tomatoes.py` - it creates the HTML and opens the browser, using the movies specified in `entertainment_center.py` as inputs
- `README.md` - the file that you are currently reading

**4. License**

The files included in this repository are covered under the MIT license.

**5. Author**

Svetlozar Stoev
