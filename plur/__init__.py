import typing as t

__all__ = (
    "DEFAULT_PLURALS",
    "plur",
)

DEFAULT_PLURALS = ("-s",)


def plur(
    word: str,
    *plurals: str,
    sep: str = " ",
    num_first: bool = True,
    zero: str = "",
) -> t.Callable[[t.Union[int, t.Sequence]], str]:
    """`plur()` returns a pluralizer

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
    plurals = plurals or DEFAULT_PLURALS
    zero = zero or plurals[-1]
    words = zero, word, *plurals

    def pluralizer(count: t.Union[int, t.Sequence]) -> str:
        n = len(count) if isinstance(count, t.Sequence) else count
        i = min(n, len(words) - 1)
        p = words[i]
        if p.startswith("-"):
            p = word + p[1:]

        return f"{n}{sep}{p}" if num_first else f"{p}{sep}{n}"

    return pluralizer
