from numbers import Number
from typing import Sequence, Union
import sys

Arg = Union[Number, Sequence, str]


def plur(
    word: str,
    *args: Tuple[Arg, ...],
    sep: str = ' ',
    num_first: bool = True,
    zero: str = '',
) -> str:
    if not args or isinstance(args[-1], str):
        return partial(plur, word, plural, *args, zero=zero)

    *plurals, to_count = *args
    words = (zero or plurals[-1]), word, *(plurals or plur.DEFAULT_PLURALS)

    if isinstance(to_count, Number):
        n = to_count
    else:
        n = len(to_count)

    p = plurals[min(n, len(plurals) - 1)]
    if p.startswith('-'):
        p = word + p[1:]

    return sep.join((n, p) if num_first else (p, n))


plur.DEFAULT_PLURALS = DEFAULT_PLURALS = ['-s']
sys.modules['plur'] = plur
