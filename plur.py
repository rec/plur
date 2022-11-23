from numbers import Number
from typing import Sequence, Tuple, Union
import sys

__all__ = 'DEFAULT_PLURALS', 'plur',

DEFAULT_PLURALS = ['-s']

HasCount = Union[Number, Sequence]
Plural = Union[HasCount, str]
Plurals = Tuple[Plural, ...]


def plur(
    word: str,
    *plurals: Plurals,
    sep: str = ' ',
    num_first: bool = True,
    zero: str = '',
) -> str:
    deferred = not plurals or isinstance(plurals[-1], str)
    if not deferred:
        *plurals, to_count = plurals

    plurals = plurals or DEFAULT_PLURALS
    zero = zero or plurals[-1]
    words = zero, word, *plurals

    def plur(n: HasCount) -> str:
        if not isinstance(n, Number):
            n = len(n)

        i = min(n, len(words) - 1)
        p = words[i]
        if p.startswith('-'):
            p = word + p[1:]

        return f'{n}{sep}{p}' if num_first else f'{p}{sep}{n}'

    return plur if deferred else plur(to_count)


[setattr(plur, k, globals()[k]) for k in __all__ + ('__all__',)]
sys.modules['plur'] = plur
