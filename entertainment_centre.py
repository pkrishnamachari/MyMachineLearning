# imports the file to render the webpage through the open_movies_function
import fresh_tomatoes
# imports the media class defining the Movie class
import media

# Define the parameters for my favourite movies: Gladiator, Descendents 2,
# Forrest Gump and Lego Movie

gladiator = media.Movie(
                        "Gladiator",
                        "A story of a Roman general who becomes a gladiator "
                        "to restore the Roman empire",
                        "https://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=owK1qxDselE"
                        )

descendents = media.Movie(
                        "Descendents 2", "Story of good winning over evil",
                        "https://upload.wikimedia.org/wikipedia/en/f/f1/Descendants_2.jpeg",  # NOQA
                        "https://www.youtube.com/watch?v=-iwE57nUG80"
                        )

forrest_gump = media.Movie(
                        "Forrest Gump",
                        "A story of a small town boy who went on to do "
                        "extraordinary things in life",
                        "https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=bLvqoHBptjg"
                        )

lego_movie = media.Movie(
                        "Lego Movie", "A Lego mini figure turns to a "
                        " superhero and helps fight the resistance group",
                        "https://i0.wp.com/media2.slashfilm.com/slashfilm/wp/wp-content/images/The-Lego-Movie-poster-header.jpg",  # NOQA
                         "https://www.youtube.com/watch?v=fZ_JOBCLF-I"
                        )

# Define the movie array and call the open_movies_page function

movies = [gladiator, descendents, forrest_gump, lego_movie]
fresh_tomatoes.open_movies_page(movies)

