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

the_matrix = media.Movie("The Matrix",
                         "How would you know the difference between the dream world and the real world?",
                         "http://www.impawards.com/1999/posters/matrix_ver1.jpg",
                         "https://www.youtube.com/watch?v=m8e-FF8MsqU"
                         )

eternal_sunshine = media.Movie("Eternal Sunshine of the Spotless Mind",
                               "Without our memories will we be the same?",
                               "https://infinitecrescendo.files.wordpress.com/2014/03/"
                               "eternal-sunshine-of-the-spotless-mind-poster.jpg",
                               "https://www.youtube.com/watch?v=lnSgSe2GzDc"
                               )

lotr_two_towers = media.Movie("Lord of the Rings: The Two Towers",
                              "Sequel to Lord of the Rings: The Fellowship of the Ring",
                              "http://img4.wikia.nocookie.net/__cb20150203041214/lotr/images/9/98/The_two_tower.jpg",
                              "https://www.youtube.com/watch?v=LbfMDwc4azU")

star_wars = media.Movie("Star Wars",
                        "A long time ago in a galaxy far, far away...",
                        "http://pre01.deviantart.net/6628/th/pre/i/2013/057/3/8/star_wars_iv___"
                        "a_new_hope___movie_poster_by_nei1b-d5t3cw9.jpg",
                        "https://www.youtube.com/watch?v=1g3_CFmnU7k"
                        )

empire_strikes_back = media.Movie("Star Wars: The Empire Strikes Back",
                                  "After the destruction of the death star, the Empire seeks to annihilate the rebel"
                                  "alliance. Darth Vader relentlessly pursues the young jedi, Luke Skywalker.",
                                  "http://i.newsarama.com/images/i/000/138/527/original/"
                                  "star-wars-empire-strikes-back-poster.jpg?1415977989",
                                  "https://www.youtube.com/watch?v=mz_YWNhKOkM"
                                  )

# Package the movie instances into a List of movies.
movies = [transformers, the_matrix, eternal_sunshine, lotr_two_towers, star_wars, empire_strikes_back]

# Generate the html and open the browser to it.
fresh_tomatoes.open_movies_page(movies)