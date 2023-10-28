import re
from typing import Generator

from gedcom5.gedcom import GEDCOM
from gedcom5.tag import Tag

YEAR = re.compile(r"\b\d{3,4}\b")


def walk(gedcom: GEDCOM) -> Generator[Tag, None, None]:
    for child in gedcom:
        yield from _walk_inner(child)


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


def _walk_inner(tag: Tag) -> Generator[Tag, None, None]:
    yield tag
    for child in tag:
        yield from _walk_inner(child)
