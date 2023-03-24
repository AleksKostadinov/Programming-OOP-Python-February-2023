from project.user import User
from project.movie_specification.movie import Movie


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def __find_user(self, name):
        for u in self.users_collection:
            if u.username == name:
                return u

    def __check_if_user_exists(self, name):
        for u in self.users_collection:
            if u.username == name:
                return True
        return False

    def __check_if_movie_exists(self, title):
        for t in self.movies_collection:
            if t.title == title:
                return True
        return False

    # def __check_if_user_liked_movie(self, name, title):
    #     user = self.__find_user(name)
    #     for m in user.movies_liked:
    #         if m.title == title:
    #             return True
    #     return False

    def register_user(self, username: str, age: int):
        new_user = User(username, age)
        if self.__check_if_user_exists(username):
            raise Exception("User already exists!")

        self.users_collection.append(new_user)
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie):
        user = self.__find_user(username)
        if not self.__check_if_user_exists(username):
            raise Exception("This user does not exist!")
        elif self.__check_if_movie_exists(movie.title):
            raise Exception("Movie already added to the collection!")
        elif not username == movie.owner.username:
            raise Exception(f'{username} is not the owner of the movie {movie.title}!')
        else:
            self.movies_collection.append(movie)
            user.movies_owned.append(movie)
            return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        if not self.__check_if_movie_exists(movie.title):
            raise Exception(f'The movie {movie.title} is not uploaded!')
        elif not username == movie.owner.username:
            raise Exception(f'{username} is not the owner of the movie {movie.title}!')
        else:
            # for attr, new_value in kwargs.items():
            #     if attr == "title":
            #         movie.title = new_value
            #     elif attr == "year":
            #         movie.year = new_value
            #     elif attr == "age_restriction":
            #         movie.age_restriction = new_value
            for attr, new_value in kwargs.items():
                setattr(movie, attr, new_value)
            return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        user = self.__find_user(username)
        if not self.__check_if_movie_exists(movie.title):
            raise Exception(f'The movie {movie.title} is not uploaded!')
        elif not username == movie.owner.username:
            raise Exception(f'{username} is not the owner of the movie {movie.title}!')
        else:
            self.movies_collection.remove(movie)
            user.movies_owned.remove(movie)
            return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        user = self.__find_user(username)
        if username == movie.owner.username:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")
        # elif self.__check_if_user_liked_movie(username, movie):
        elif movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")
        else:
            movie.likes += 1
            user.movies_liked.append(movie)
            return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        user = self.__find_user(username)
        if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")
        else:
            movie.likes -= 1
            user.movies_liked.remove(movie)
            return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if not self.movies_collection:
            return 'No movies found.'
        else:
            result = []
            for movie in sorted(self.movies_collection, key=lambda x: (-x.year, x.title)):
                result.append(movie.details())
            return '\n'.join(result)

    def __str__(self):
        if not self.users_collection:
            users = "No users."
        else:
            users = ', '.join(u.username for u in self.users_collection)

        if not self.movies_collection:
            movies = 'No movies.'
        else:
            movies = ', '.join(m.title for m in self.movies_collection)

        return f'All users: {users}\nAll movies: {movies}'

