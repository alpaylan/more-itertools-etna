"""Hypothesis strategies for the more-itertools ETNA workload.

CrossHair-compatible: only ``st.integers``, ``st.lists``, ``st.tuples``.
"""
from __future__ import annotations

from hypothesis import strategies as st


_INT = st.integers(min_value=-50, max_value=50)
_SMALL_INT = st.integers(min_value=0, max_value=4)
_NONZERO_STEP = st.integers(min_value=-10, max_value=10).filter(lambda x: x != 0)


def strategy_numeric_range_reversed_handles_empty():
    return st.tuples(_INT, _INT, _NONZERO_STEP)


def strategy_numeric_range_slice_negative_step():
    return st.tuples(_INT, _INT, _NONZERO_STEP)


def strategy_last_with_none_reversed():
    # Non-empty list of integers; property discards on empty.
    return st.lists(_INT, min_size=1, max_size=10)


def strategy_split_before_empty_iterable_no_empty():
    # Property only triggers on empty list; force the items to be empty.
    # Hypothesis will spend its time on the (target) value, which doesn't
    # matter — the property passes for empty `items` regardless.
    return st.tuples(st.lists(_INT, max_size=0), _INT)


def strategy_split_after_maxsplit_no_empty():
    return st.tuples(
        st.lists(_INT, max_size=10),
        _INT,
        st.integers(min_value=1, max_value=5),
    )


def strategy_exactly_n_rejects_negative():
    return st.tuples(
        st.lists(st.booleans(), max_size=10),
        st.integers(min_value=-5, max_value=-1),
    )


def strategy_iterate_stops_on_stop_iteration():
    return st.tuples(
        st.integers(min_value=-5, max_value=20),
        st.integers(min_value=-5, max_value=20),
    )


def strategy_product_index_accepts_iterator():
    return st.lists(_SMALL_INT, min_size=3, max_size=3)
