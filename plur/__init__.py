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
    """ `plur()` pluralizes nouns.

      word:
          The root word for a single item

      plurals:
           Zero or more plurals.  If none are given, '-s' is used

      sep:
           The separator string between the number and the noun

      num_first:
           A boolean saying whether the number is written first or second

      zero:
           If there is a special case for zero items, it goes here
    """
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


if __name__ != '__main__':
    [setattr(plur, k, globals()[k]) for k in __all__ + ('__all__',)]
    sys.modules[__name__] = plur
