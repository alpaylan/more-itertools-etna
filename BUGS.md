# more-itertools — Injected Bugs

Pure-Python iterator utilities — bug fixes mined from upstream history.

Total mutations: 8

## Bug Index

| # | Variant | Name | Location | Injection | Fix Commit |
|---|---------|------|----------|-----------|------------|
| 1 | `exactly_n_negative_input_adeda34_1` | `exactly_n_negative_input` | `more_itertools/more.py` | `patch` | `adeda34bd11ff636f5f19238cf422a73e1455483` |
| 2 | `iterate_func_stop_iteration_cd0a3a8_1` | `iterate_func_stop_iteration` | `more_itertools/more.py` | `patch` | `cd0a3a87d231033db06a3c222fe893025e398a86` |
| 3 | `last_reversed_truthy_check_cca3294_1` | `last_reversed_truthy_check` | `more_itertools/more.py` | `patch` | `cca32949f12d473fd823e37a5530c30d2faa1332` |
| 4 | `numeric_range_negative_step_slice_a51da82_1` | `numeric_range_negative_step_slice` | `more_itertools/more.py` | `patch` | `a51da8244b6f9ec59ec05f81f1555f943d9506b2` |
| 5 | `numeric_range_reversed_empty_edb3346_1` | `numeric_range_reversed_empty` | `more_itertools/more.py` | `patch` | `edb3346f835ca917efbfda5e2d6664ab952da369` |
| 6 | `product_index_iterator_input_cf186b5_1` | `product_index_iterator_input` | `more_itertools/more.py` | `patch` | `cf186b5de4797602fef76c3391da2d110b88a954` |
| 7 | `split_after_maxsplit_empty_9245cd0_1` | `split_after_maxsplit_empty` | `more_itertools/more.py` | `patch` | `9245cd04c043d0d646497934df72549943d5f868` |
| 8 | `split_before_empty_buffer_2e81a56_1` | `split_before_empty_buffer` | `more_itertools/more.py` | `patch` | `2e81a562fbaccc996c19c069090a53f52ec894fe` |

## Property Mapping

| Variant | Property | Witness(es) |
|---------|----------|-------------|
| `exactly_n_negative_input_adeda34_1` | `ExactlyNRejectsNegative` | `witness_exactly_n_rejects_negative_case_basic` |
| `iterate_func_stop_iteration_cd0a3a8_1` | `IterateStopsOnStopIteration` | `witness_iterate_stops_on_stop_iteration_case_basic` |
| `last_reversed_truthy_check_cca3294_1` | `LastWithNoneReversed` | `witness_last_with_none_reversed_case_basic` |
| `numeric_range_negative_step_slice_a51da82_1` | `NumericRangeSliceNegativeStep` | `witness_numeric_range_slice_negative_step_case_basic` |
| `numeric_range_reversed_empty_edb3346_1` | `NumericRangeReversedHandlesEmpty` | `witness_numeric_range_reversed_handles_empty_case_basic` |
| `product_index_iterator_input_cf186b5_1` | `ProductIndexAcceptsIterator` | `witness_product_index_accepts_iterator_case_basic` |
| `split_after_maxsplit_empty_9245cd0_1` | `SplitAfterMaxsplitNoEmpty` | `witness_split_after_maxsplit_no_empty_case_basic` |
| `split_before_empty_buffer_2e81a56_1` | `SplitBeforeEmptyIterableNoEmpty` | `witness_split_before_empty_iterable_no_empty_case_basic` |

## Framework Coverage

| Property | proptest | quickcheck | crabcheck | hegel |
|----------|---------:|-----------:|----------:|------:|
| `ExactlyNRejectsNegative` | ✓ | ✓ | ✓ | ✓ |
| `IterateStopsOnStopIteration` | ✓ | ✓ | ✓ | ✓ |
| `LastWithNoneReversed` | ✓ | ✓ | ✓ | ✓ |
| `NumericRangeSliceNegativeStep` | ✓ | ✓ | ✓ | ✓ |
| `NumericRangeReversedHandlesEmpty` | ✓ | ✓ | ✓ | ✓ |
| `ProductIndexAcceptsIterator` | ✓ | ✓ | ✓ | ✓ |
| `SplitAfterMaxsplitNoEmpty` | ✓ | ✓ | ✓ | ✓ |
| `SplitBeforeEmptyIterableNoEmpty` | ✓ | ✓ | ✓ | ✓ |

## Bug Details

### 1. exactly_n_negative_input

- **Variant**: `exactly_n_negative_input_adeda34_1`
- **Location**: `more_itertools/more.py` (inside `exactly_n`)
- **Property**: `ExactlyNRejectsNegative`
- **Witness(es)**:
  - `witness_exactly_n_rejects_negative_case_basic` — exactly_n([True, False], -2) must return False, not raise.
- **Source**: internal — Fix bug for negative inputs to exactly_n(). Optimize code.
  > ``exactly_n(it, n)`` was implemented as ``ilen(islice(filter(pred, it), n + 1)) == n``. For ``n <= -2`` this passes a negative ``stop`` to ``islice`` which raises ``ValueError``. The fix returns ``False`` directly for ``n < 0``.
- **Fix commit**: `adeda34bd11ff636f5f19238cf422a73e1455483` — Fix bug for negative inputs to exactly_n(). Optimize code.
- **Invariant violated**: For any iterable and any ``n < 0``, ``exactly_n(iterable, n)`` returns ``False`` and does not raise.
- **How the mutation triggers**: The mutation reverts ``exactly_n`` to its prior one-line ``islice``-based implementation. With ``n <= -2`` the call ``islice(..., n + 1)`` has a negative ``stop`` argument and raises ``ValueError``.

### 2. iterate_func_stop_iteration

- **Variant**: `iterate_func_stop_iteration_cd0a3a8_1`
- **Location**: `more_itertools/more.py` (inside `iterate`)
- **Property**: `IterateStopsOnStopIteration`
- **Witness(es)**:
  - `witness_iterate_stops_on_stop_iteration_case_basic` — f(3) raises StopIteration; iterate must stop after yielding [0, 1, 2, 3].
- **Source**: [#707](https://github.com/more-itertools/more-itertools/pull/707) — Issue #707: fix iterate() to enable func to raise StopIteration
  > Under PEP 479, a ``StopIteration`` raised inside a generator is converted to ``RuntimeError``. The bare ``while True: yield start; start = func(start)`` body in ``iterate`` therefore corrupted ``StopIteration`` raised from ``func``. The fix wraps the loop in ``with suppress(StopIteration):``.
- **Fix commit**: `cd0a3a87d231033db06a3c222fe893025e398a86` — Issue #707: fix iterate() to enable func to raise StopIteration
- **Invariant violated**: ``iterate(func, start)`` yields ``start, func(start), func(func(start)), ...`` and stops cleanly when ``func`` raises ``StopIteration`` (no ``RuntimeError`` leak).
- **How the mutation triggers**: The mutation removes the ``with suppress(StopIteration):`` wrapper around the loop. Any ``StopIteration`` raised by ``func`` is converted to ``RuntimeError`` by PEP 479.

### 3. last_reversed_truthy_check

- **Variant**: `last_reversed_truthy_check_cca3294_1`
- **Location**: `more_itertools/more.py` (inside `last`)
- **Property**: `LastWithNoneReversed`
- **Witness(es)**:
  - `witness_last_with_none_reversed_case_basic` — Custom iterable with __reversed__ = None over [1, 2, 3].
- **Source**: internal — fix last() when __reversed__ is None
  > ``last`` checked ``hasattr(iterable, '__reversed__')`` to decide whether to call ``reversed()``. Python's protocol allows a class to opt out of ``reversed()`` by setting ``__reversed__ = None``, which still satisfies ``hasattr``, but ``reversed()`` then raises ``TypeError``. The fix uses ``getattr(iterable, '__reversed__', None)`` truthiness.
- **Fix commit**: `cca32949f12d473fd823e37a5530c30d2faa1332` — fix last() when __reversed__ is None
- **Invariant violated**: For any non-empty iterable ``it``, ``last(it)`` returns the same value as the last element produced by ``iter(it)`` — even when ``it`` declares ``__reversed__ = None``.
- **How the mutation triggers**: The mutation reverts to ``hasattr(iterable, '__reversed__')``. For an iterable whose class sets ``__reversed__ = None`` (the official opt-out marker), the buggy branch calls ``reversed(iterable)`` which raises ``TypeError``.

### 4. numeric_range_negative_step_slice

- **Variant**: `numeric_range_negative_step_slice_a51da82_1`
- **Location**: `more_itertools/more.py` (inside `numeric_range.__getitem__`)
- **Property**: `NumericRangeSliceNegativeStep`
- **Witness(es)**:
  - `witness_numeric_range_slice_negative_step_case_basic` — numeric_range(0, 10, 2)[::-1] should equal [8, 6, 4, 2, 0].
- **Source**: internal — Fix numeric_range slicing with negative step returning empty range
  > ``numeric_range.__getitem__`` did not normalise default ``start``/``stop`` for slices with a negative step direction, so ``nr[::-1]`` returned an empty range. The fix delegates to ``slice.indices`` and reconstructs the slice from the corrected indices.
- **Fix commit**: `a51da8244b6f9ec59ec05f81f1555f943d9506b2` — Fix numeric_range slicing with negative step returning empty range
- **Invariant violated**: For any valid ``numeric_range`` ``nr``, ``list(nr[::-1])`` equals ``list(nr)[::-1]``.
- **How the mutation triggers**: The mutation reverts ``__getitem__`` to defaulting ``start`` to ``self._start`` and ``stop`` to ``self._stop`` regardless of step sign. With a negative slice step the resulting range is empty because ``start`` and ``stop`` are not swapped.

### 5. numeric_range_reversed_empty

- **Variant**: `numeric_range_reversed_empty_edb3346_1`
- **Location**: `more_itertools/more.py` (inside `numeric_range.__reversed__`)
- **Property**: `NumericRangeReversedHandlesEmpty`
- **Witness(es)**:
  - `witness_numeric_range_reversed_handles_empty_case_basic` — Empty range numeric_range(0, 0, 1).
- **Source**: internal — Fix empty ranges in numeric_range.__reversed__
  > ``numeric_range.__reversed__`` calls ``self._get_by_index(-1)``, which raises ``IndexError`` for an empty range. The fix wraps the call in a ``try/except`` and returns ``iter([])`` on empty ranges.
- **Fix commit**: `edb3346f835ca917efbfda5e2d6664ab952da369` — Fix empty ranges in numeric_range.__reversed__
- **Invariant violated**: For any valid (start, stop, step), ``list(reversed(numeric_range(start, stop, step)))`` equals ``list(numeric_range(start, stop, step))[::-1]`` and never raises.
- **How the mutation triggers**: The mutation removes the empty-range guard; ``__reversed__`` calls ``self._get_by_index(-1)`` which raises ``IndexError`` whenever the range is empty (``start == stop``).

### 6. product_index_iterator_input

- **Variant**: `product_index_iterator_input_cf186b5_1`
- **Location**: `more_itertools/more.py` (inside `product_index`)
- **Property**: `ProductIndexAcceptsIterator`
- **Witness(es)**:
  - `witness_product_index_accepts_iterator_case_basic` — iter([2, 3, 1]) over three range(5) pools.
- **Source**: internal — Fix product_index() with iterator input
  > ``product_index`` validated arity with ``len(element) != len(args)``. ``len(element)`` raises ``TypeError`` for bare iterators (e.g. generators); the fix uses the materialised tuples ``len(elements) != len(pools)`` instead.
- **Fix commit**: `cf186b5de4797602fef76c3391da2d110b88a954` — Fix product_index() with iterator input
- **Invariant violated**: For any element-iterable that produces a tuple equal to a list ``L``, ``product_index(elem_iter, *pools)`` returns the same value as ``product_index(L, *pools)``.
- **How the mutation triggers**: The mutation reverts the arity check to ``len(element) != len(pools)``. When ``element`` is a bare iterator, ``len(element)`` raises ``TypeError`` before any product index is computed.

### 7. split_after_maxsplit_empty

- **Variant**: `split_after_maxsplit_empty_9245cd0_1`
- **Location**: `more_itertools/more.py` (inside `split_after`)
- **Property**: `SplitAfterMaxsplitNoEmpty`
- **Witness(es)**:
  - `witness_split_after_maxsplit_no_empty_case_basic` — split_after([0], pred=x==0, maxsplit=1) must not yield a trailing [].
- **Source**: [#658](https://github.com/more-itertools/more-itertools/pull/658) — Fix issue 658 for split_after
  > When ``maxsplit == 1`` and the predicate matched the final element, ``split_after`` reached its ``yield list(it)`` branch with the iterator already exhausted — yielding a trailing ``[]`` chunk. The fix only yields if the trailing chunk is non-empty.
- **Fix commit**: `9245cd04c043d0d646497934df72549943d5f868` — Fix issue 658 for split_after
- **Invariant violated**: ``split_after`` never yields an empty chunk for any input, predicate, or ``maxsplit`` value.
- **How the mutation triggers**: The mutation reverts to ``yield list(it)`` immediately when ``maxsplit == 1``. If the predicate just matched the final item, ``it`` is exhausted and the buggy branch yields ``[]``.

### 8. split_before_empty_buffer

- **Variant**: `split_before_empty_buffer_2e81a56_1`
- **Location**: `more_itertools/more.py` (inside `split_before`)
- **Property**: `SplitBeforeEmptyIterableNoEmpty`
- **Witness(es)**:
  - `witness_split_before_empty_iterable_no_empty_case_basic` — split_before([], pred) must yield no chunks.
- **Source**: internal — Fix split_before for an empty collections.
  > ``split_before`` unconditionally yielded the buffer after the loop, producing a trailing empty list when the input was empty. The fix gates the yield on ``if buf:``.
- **Fix commit**: `2e81a562fbaccc996c19c069090a53f52ec894fe` — Fix split_before for an empty collections.
- **Invariant violated**: ``split_before([], pred)`` yields no chunks; in particular it never yields an empty list.
- **How the mutation triggers**: The mutation removes the ``if buf:`` guard before the trailing ``yield buf``. When the input iterable is empty, ``buf`` is empty and the generator yields a stray ``[]``.
