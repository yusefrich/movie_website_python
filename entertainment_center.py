import fresh_tomatoes
import media

#instantiation of my favorite movies classes
toy_story = media.Movie("toy story",
                        "Woody eh um boneco cowboy de bom coracao que pertence a um jovem chamado Andy.",
                        "https://upload.wikimedia.org/wikipedia/pt/d/dc/Movie_poster_toy_story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                        "https://www.imdb.com/title/tt0114709/")

avatar = media.Movie("avatar",
                    "No exuberante mundo alienigena de Pandora vivem os Na'vi, seres que parecem ser primitivos, mas sao altamente evoluidos.",
                    "https://upload.wikimedia.org/wikipedia/pt/thumb/b/b0/Avatar-Teaser-Poster.jpg/250px-Avatar-Teaser-Poster.jpg",
                    "https://www.youtube.com/watch?v=6ziBFh3V1aM",
                    "https://www.imdb.com/title/tt0499549/")

drive = media.Movie("Drive",
                    "Um habilidoso motorista, que eh duble em cenas de perseguicao em filmes de Hollywood, tambem usa seu talento no volante para ser piloto de fuga em assaltos",
                    "https://upload.wikimedia.org/wikipedia/pt/thumb/e/e6/Drive-P%C3%B4ster.jpg/250px-Drive-P%C3%B4ster.jpg",
                    "https://www.youtube.com/watch?v=KBiOF3y1W0Y",
                    "https://www.imdb.com/title/tt0780504/")


a_origem = media.Movie("A Origem",
                       "Don Cobb eh um ladrao que invade os sonhos das pessoas e rouba segredos do subconsciente.",
                       "https://upload.wikimedia.org/wikipedia/pt/thumb/7/74/A_origem_poster_portugues.jpg/250px-A_origem_poster_portugues.jpg",
                       "https://www.youtube.com/watch?v=HiixbtN-O24",
                       "https://www.imdb.com/title/tt1375666/")

whiplash = media.Movie("Whiplash",
                       "O jovem musico Andrew Neiman batalha para ser o melhor baterista de jazz de sua geracao.",
                       "https://upload.wikimedia.org/wikipedia/pt/thumb/c/cd/Whiplash_em_busca_da_perfeicao.png/240px-Whiplash_em_busca_da_perfeicao.png",
                       "https://www.youtube.com/watch?v=7d_jQycdQGo",
                       "https://www.imdb.com/title/tt2582802/")

pulp_fiction = media.Movie("Pulp Fiction",
                           "Os caminhos de varios criminosos se cruzam nestas tres historias de Quentin Tarantino.",
                           "https://upload.wikimedia.org/wikipedia/pt/thumb/8/82/Pulp_Fiction_cover.jpg/240px-Pulp_Fiction_cover.jpg",
                           "https://www.youtube.com/watch?v=s7EdQ4FqbhY",
                           "https://www.imdb.com/title/tt0110912/")

#storing all the movies into a array
movies = [toy_story, avatar, drive, a_origem, whiplash, pulp_fiction]
#generate and open web page
fresh_tomatoes.open_movies_page(movies)

#print(media.Movie.VALID_RATINGS)

