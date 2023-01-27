from __future__ import annotations

from typing import TypedDict, NotRequired


class Movie(TypedDict):
    name: str
    year: int = 10


class SuperMovie(TypedDict, Movie):
    stars: NotRequired[int]


def main():
    movie: Movie = {'name': 'Blade Runner', 'year': 1982}
    smov: SuperMovie = {'name': 'Blade Runner', 'year': 1982, 'stars': 123}


if __name__ == '__main__':
    main()
