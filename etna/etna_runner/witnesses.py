"""Concrete witnesses for the more-itertools ETNA workload.

Each ``witness_<snake>_case_<tag>`` is a no-arg function that calls
``property_<snake>`` with frozen inputs. On the base tree every witness
returns PASS; with the corresponding patch reverse-applied, the witness
returns fail(...).
"""
from __future__ import annotations

from . import properties
from ._result import PropertyResult


def witness_numeric_range_reversed_handles_empty_case_basic() -> PropertyResult:
    # Empty range: start == stop.
    return properties.property_numeric_range_reversed_handles_empty((0, 0, 1))


def witness_numeric_range_slice_negative_step_case_basic() -> PropertyResult:
    # numeric_range(0, 10, 2)[::-1] should be [8, 6, 4, 2, 0].
    return properties.property_numeric_range_slice_negative_step((0, 10, 2))


def witness_last_with_none_reversed_case_basic() -> PropertyResult:
    return properties.property_last_with_none_reversed([1, 2, 3])


def witness_split_before_empty_iterable_no_empty_case_basic() -> PropertyResult:
    # Empty iterable: split_before should yield nothing.
    return properties.property_split_before_empty_iterable_no_empty(([], 0))


def witness_split_after_maxsplit_no_empty_case_basic() -> PropertyResult:
    # split_after([0], pred=lambda x: x==0, maxsplit=1):
    #   buggy yields [[0], []]; fix yields [[0]].
    return properties.property_split_after_maxsplit_no_empty(([0], 0, 1))


def witness_exactly_n_rejects_negative_case_basic() -> PropertyResult:
    # n = -2 triggers ValueError under the buggy islice path.
    return properties.property_exactly_n_rejects_negative(([True, False], -2))


def witness_iterate_stops_on_stop_iteration_case_basic() -> PropertyResult:
    # f(0..2) returns x+1; f(3) raises StopIteration.
    return properties.property_iterate_stops_on_stop_iteration((0, 3))


def witness_product_index_accepts_iterator_case_basic() -> PropertyResult:
    # Element [2, 3, 1] in product(range(5), range(5), range(5)).
    return properties.property_product_index_accepts_iterator([2, 3, 1])
