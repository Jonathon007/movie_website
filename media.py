class Movie():
    """
    Args:
        param1: The movie's title.
        param2: The movie's poster image URL.
        param3: The movie's trailer on Youtube.
    Behavior:
        Assign movie's title, poster image URL and trailer on Youtube
        into different variables.
    Returns:
        Variables of movie's title, poster image URL and trailer on Youtube.
    """
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
