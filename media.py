import webbrowser


# The movie class serves as a data container for movie information to be used
# in movie tiles on the movie trailer website.

class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, duration):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.duration = duration  # minutes

    def show_trailer(self):
        """
        Opens the user's browser to the movie's trailer.
        """
        webbrowser.open(self.trailer_youtube_url)
