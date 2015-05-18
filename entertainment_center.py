import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story about toys that come to life when no humans are looking.",
                        "http://www.impawards.com/1995/posters/toy_story_ver1.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                        )

movies = []
fresh_tomatoes.open_movies_page(movies)