import webbrowser


# This class defines the movies and its attributes
class Movie():
    # The constructor method defines the inputs and the outputs for the class
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

# The function opens the youtube trailer for the selected movies
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)



