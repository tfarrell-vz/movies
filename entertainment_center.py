import fresh_tomatoes
import media

# Some of the strings were too long to remain singly-lined. Pay close attention to commas to differentiate arguments.
transformers = media.Movie("Transformers: The Movie",
                           "The Decepticons lead a strike against the Autobots only for both to discover "
                           "they have an even greater enemy: Unicron",
                           "https://upload.wikimedia.org/wikipedia/en/thumb/9/91/"
                           "Transformers-movieposter-west.jpg/220px-Transformers-movieposter-west.jpg",
                           "https://www.youtube.com/watch?v=4lo7JPLJUUU",
                           )



# Package the movie instances into a List of movies.
movies = [transformers]

# Generate the html and open the browser to it.
fresh_tomatoes.open_movies_page(movies)