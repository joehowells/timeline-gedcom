import re

import pandas as pd

YEAR = re.compile(r"\b\d{3,4}\b")


def year(date: str) -> int | None:
    """
    Returns the year from date if it exists.

    >>> year("")
    >>> year("12 July 927")
    927
    >>> year("1 Jan 1970")
    1970
    """
    if match := YEAR.search(date):
        return int(match.group())
    else:
        return None
