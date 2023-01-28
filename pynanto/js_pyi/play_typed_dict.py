from __future__ import annotations

from typing import TypedDict, NotRequired


class Movie(TypedDict):
    name: str
    year: int = 10


class SuperMovie(TypedDict, Movie):
    stars: NotRequired[int]


Point2D = TypedDict('Point2D', {
    """cosa e' """
    'x': int,
    'y': int,
    'label': str
})


def main():
    movie: Movie = {'name': 'Blade Runner', 'year': 1982}
    movi2: Movie = {}
    smov: SuperMovie = {'name': 'Blade Runner', 'year': 1982, 'stars': 123}
    point: Point2D = {'x': 42}


if __name__ == '__main__':
    main()
