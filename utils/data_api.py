"""
This module imports Task 1's loader + index builder and exposes a minimal,
stable API for the rest of the team.

Public functions:
    init_index(force: bool = False) -> None
    is_operational(name: str) -> bool
    get_station_id(name: str) -> int | None
    get_station_name(station_id: int) -> str | None

Notes:
- Uses the CLRS hashtable built by task1.module_wrapper.
- Assumes station lookup keys are the normalised station names.
"""

from __future__ import annotations
from typing import Optional, Tuple, List

from task1.data_extract import read_csv_file
from task1.module_wrapper import build_index_from_rows


def _norm(s: str) -> str:
    """Normalise a station name exactly like Task 1 (trim, collapse spaces, casefold)."""
    return " ".join((s or "").strip().split()).casefold()

def _unwrap(node_or_obj):
    """If the CLRS search returns a linked-list node, unwrap its .data; otherwise return the object."""
    return getattr(node_or_obj, "data", node_or_obj)

_HT = None
_BY_ID: List[object] | None = None


def init_index(force: bool = False) -> None:
    """Build the global index once (idempotent). Call before using other functions."""
    global _HT, _BY_ID
    if _HT is not None and _BY_ID is not None and not force:
        return
    station_rows, edge_rows = read_csv_file()
    _HT, _BY_ID = build_index_from_rows(station_rows, edge_rows)


def is_operational(name: str) -> bool:
    """True if the station exists in the index. """
    if _HT is None or _BY_ID is None:
        init_index()
    return _HT.search(_norm(name)) is not None

def get_station_id(name: str) -> Optional[int]:
    """Return the integer station id for a given name, or None if not found. """
    if _HT is None or _BY_ID is None:
        init_index()
    hit = _HT.search(_norm(name))
    if hit is None:
        return None
    rec = _unwrap(hit)
    return getattr(rec, "id", None)

def get_station_name(station_id: int) -> Optional[str]:
    """Return the station name for a given id, or None if out of range."""
    if _BY_ID is None or _HT is None:
        init_index()
    if station_id < 0 or station_id >= len(_BY_ID):
        return None
    rec = _BY_ID[station_id]
    return getattr(rec, "name", None)


__all__ = [
    "init_index",
    "is_operational",
    "get_station_id",
    "get_station_name",
]