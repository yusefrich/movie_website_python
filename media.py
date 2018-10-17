import webbrowser


class Movie():
    # contructor for the movie
    # add here any value that is showed in the website
    def __init__(self,
                 movie_title,
                 movie_storyline,
                 porter_image,
                 trailer_youtube,
                 movie_imdb_url):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = porter_image
        self.trailer_youtube_url = trailer_youtube
        self.imdb_url = movie_imdb_url

    # shows movie trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    # shows imdb page
    def show_imdb_info(self):
        webbrowser.open(self.imdb_url)
