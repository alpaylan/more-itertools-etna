"""Property functions for the more-itertools ETNA workload.

Each property is pure, total, deterministic. Returns PropertyResult.
"""
from __future__ import annotations

from typing import Tuple, List

from more_itertools import (
    exactly_n,
    iterate,
    last,
    numeric_range,
    product_index,
    split_after,
    split_before,
    take,
)

from ._result import PASS, DISCARD, PropertyResult, fail


# ---------------------------------------------------------------------------
# NumericRangeReversedHandlesEmpty (variant: numeric_range_reversed_empty_edb3346_1)
# ---------------------------------------------------------------------------
def property_numeric_range_reversed_handles_empty(
    args: Tuple[int, int, int],
) -> PropertyResult:
    """``reversed(numeric_range(start, stop, step))`` must not raise on an empty range.

    Bug (edb3346): ``__reversed__`` calls ``self._get_by_index(-1)`` which
    raises ``IndexError`` when the range is empty. The fix wraps the call
    in a ``try/except`` and returns ``iter([])`` for empty ranges.
    """
    start, stop, step = args
    if step == 0:
        return DISCARD
    try:
        nr = numeric_range(start, stop, step)
    except ValueError:
        return DISCARD

    expected_forward = list(nr)
    expected_reversed = list(reversed(expected_forward))

    try:
        got = list(reversed(nr))
    except IndexError as e:
        return fail(
            f"reversed(numeric_range({start!r}, {stop!r}, {step!r})) raised "
            f"IndexError: {e}; expected {expected_reversed!r}"
        )

    if got != expected_reversed:
        return fail(
            f"reversed(numeric_range({start!r}, {stop!r}, {step!r})) = {got!r}; "
            f"expected {expected_reversed!r}"
        )
    return PASS


# ---------------------------------------------------------------------------
# NumericRangeSliceNegativeStep (variant: numeric_range_negative_step_slice_a51da82_1)
# ---------------------------------------------------------------------------
def property_numeric_range_slice_negative_step(
    args: Tuple[int, int, int],
) -> PropertyResult:
    """``numeric_range(...)[::-1]`` must equal ``list(reversed(numeric_range(...)))``.

    Bug (a51da82): ``numeric_range.__getitem__`` did not handle negative
    slice steps; ``nr[::-1]`` returned an empty range instead of the
    reversed sequence. The fix delegates to ``slice.indices`` to normalise
    indices accounting for step direction.
    """
    start, stop, step = args
    if step == 0:
        return DISCARD
    try:
        nr = numeric_range(start, stop, step)
    except ValueError:
        return DISCARD

    expected = list(nr)[::-1]
    sliced = nr[::-1]
    got = list(sliced)
    if got != expected:
        return fail(
            f"numeric_range({start!r}, {stop!r}, {step!r})[::-1] = {got!r}; "
            f"expected {expected!r}"
        )
    return PASS


# ---------------------------------------------------------------------------
# LastWithNoneReversed (variant: last_reversed_truthy_check_cca3294_1)
# ---------------------------------------------------------------------------
class _IterableWithNoneReversed:
    """Iterable that exposes ``__reversed__ = None`` to opt out of ``reversed()``.

    ``hasattr(obj, '__reversed__')`` returns ``True`` for this class, but
    Python's official protocol treats ``None`` as "explicitly unsupported";
    the bug-fix idiom uses ``getattr(..., None)`` truthiness instead.
    """

    __reversed__ = None

    def __init__(self, items: Tuple[int, ...]) -> None:
        self._items = items

    def __iter__(self):
        return iter(self._items)


def property_last_with_none_reversed(args: List[int]) -> PropertyResult:
    """``last`` must return the final element even when ``__reversed__`` is ``None``.

    Bug (cca3294): ``hasattr(iterable, '__reversed__')`` returns ``True`` for
    objects whose ``__reversed__`` attribute is set to ``None`` (the official
    "I don't support reversed()" marker). The buggy branch then calls
    ``reversed(obj)`` which raises ``TypeError``. The fix checks
    ``getattr(iterable, '__reversed__', None)`` for truthiness instead.
    """
    items = args
    if not items:
        return DISCARD
    obj = _IterableWithNoneReversed(tuple(items))
    expected = items[-1]
    try:
        got = last(obj)
    except (TypeError, ValueError) as e:
        return fail(
            f"last(IterableWithNoneReversed({items!r})) raised "
            f"{type(e).__name__}: {e}"
        )
    if got != expected:
        return fail(
            f"last(IterableWithNoneReversed({items!r})) = {got!r}; "
            f"expected {expected!r}"
        )
    return PASS


# ---------------------------------------------------------------------------
# SplitBeforeEmptyIterableNoEmpty (variant: split_before_empty_buffer_2e81a56_1)
# ---------------------------------------------------------------------------
def property_split_before_empty_iterable_no_empty(
    args: Tuple[List[int], int],
) -> PropertyResult:
    """``split_before`` on an empty iterable must yield nothing.

    Bug (2e81a56): the unconditional ``yield buf`` after the loop yielded a
    trailing empty list when the input iterable was empty. The fix only
    yields the buffer if it is non-empty.
    """
    items, target = args
    if items:
        return DISCARD
    pred = lambda x: x == target
    got = list(split_before(items, pred))
    if got:
        return fail(
            f"split_before([], pred) = {got!r}; expected []"
        )
    return PASS


# ---------------------------------------------------------------------------
# SplitAfterMaxsplitNoEmpty (variant: split_after_maxsplit_empty_9245cd0_1)
# ---------------------------------------------------------------------------
def property_split_after_maxsplit_no_empty(
    args: Tuple[List[int], int, int],
) -> PropertyResult:
    """``split_after`` with ``maxsplit`` must not yield a trailing empty list.

    Bug (9245cd0): when ``maxsplit == 1`` and the predicate matched the
    final element of the iterable, the buggy code yielded ``list(it)`` —
    which was empty because the iterator was exhausted — producing a
    trailing ``[]`` chunk. The fix only yields the trailing chunk if it
    is non-empty.
    """
    items, target, maxsplit = args
    if maxsplit < 1:
        return DISCARD
    pred = lambda x: x == target
    got = list(split_after(items, pred, maxsplit=maxsplit))
    for chunk in got:
        if not chunk:
            return fail(
                f"split_after({items!r}, pred=lambda x: x=={target!r}, "
                f"maxsplit={maxsplit!r}) = {got!r}; "
                f"contains an empty trailing chunk"
            )
    return PASS


# ---------------------------------------------------------------------------
# ExactlyNRejectsNegative (variant: exactly_n_negative_input_adeda34_1)
# ---------------------------------------------------------------------------
def property_exactly_n_rejects_negative(
    args: Tuple[List[int], int],
) -> PropertyResult:
    """``exactly_n(iterable, n)`` with negative ``n`` must return ``False``,
    not raise.

    Bug (adeda34): the original implementation used
    ``ilen(islice(filter(predicate, iterable), n + 1)) == n``. For
    ``n <= -2`` this passes a negative stop to ``islice``, which raises
    ``ValueError``. The fix returns ``False`` directly for ``n < 0``.
    """
    items, n = args
    if n >= 0:
        return DISCARD
    try:
        got = exactly_n(items, n)
    except ValueError as e:
        return fail(
            f"exactly_n({items!r}, n={n!r}) raised ValueError: {e}; "
            f"expected False"
        )
    if got is not False:
        return fail(
            f"exactly_n({items!r}, n={n!r}) = {got!r}; expected False"
        )
    return PASS


# ---------------------------------------------------------------------------
# IterateStopsOnStopIteration (variant: iterate_func_stop_iteration_cd0a3a8_1)
# ---------------------------------------------------------------------------
def property_iterate_stops_on_stop_iteration(
    args: Tuple[int, int],
) -> PropertyResult:
    """``iterate(func, start)`` must stop cleanly when ``func`` raises
    ``StopIteration``.

    Bug (cd0a3a8): a bare ``while True: yield start; start = func(start)``
    loop allowed ``StopIteration`` from ``func`` to leak as a
    ``RuntimeError`` under PEP 479. The fix wraps the loop in
    ``with suppress(StopIteration):``.
    """
    start, threshold = args
    if threshold < start:
        return DISCARD
    distance = threshold - start
    if distance > 50:
        return DISCARD

    def f(x: int) -> int:
        if x >= threshold:
            raise StopIteration
        return x + 1

    expected = list(range(start, threshold + 1))
    try:
        got = take(distance + 5, iterate(f, start))
    except RuntimeError as e:
        return fail(
            f"iterate(f, {start!r}) leaked StopIteration as RuntimeError: {e}"
        )
    if got != expected:
        return fail(
            f"iterate(f, {start!r}) yielded {got!r}; expected {expected!r}"
        )
    return PASS


# ---------------------------------------------------------------------------
# ProductIndexAcceptsIterator (variant: product_index_iterator_input_cf186b5_1)
# ---------------------------------------------------------------------------
def property_product_index_accepts_iterator(args: List[int]) -> PropertyResult:
    """``product_index`` must accept an iterator as ``element``.

    Bug (cf186b5): the implementation called ``len(element)`` to validate
    arity, which raises ``TypeError`` on bare iterators. The fix checks
    ``len(elements)`` (the materialised tuple) instead.
    """
    indices = args
    if len(indices) != 3:
        return DISCARD
    if any(i < 0 or i >= 5 for i in indices):
        return DISCARD

    pools = ([0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4])
    expected = product_index(list(indices), *pools)
    try:
        got = product_index(iter(indices), *pools)
    except TypeError as e:
        return fail(
            f"product_index(iter({indices!r}), *pools) raised TypeError: {e}"
        )
    if got != expected:
        return fail(
            f"product_index(iter({indices!r}), *pools) = {got!r}; "
            f"expected {expected!r}"
        )
    return PASS
