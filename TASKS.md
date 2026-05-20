# more-itertools — ETNA Tasks

Total tasks: 16

## Task Index

| Task | Variant | Framework | Property | Witness |
|------|---------|-----------|----------|---------|
| 001 | `exactly_n_negative_input_adeda34_1` | hypothesis | `ExactlyNRejectsNegative` | `witness_exactly_n_rejects_negative_case_basic` |
| 002 | `exactly_n_negative_input_adeda34_1` | crosshair | `ExactlyNRejectsNegative` | `witness_exactly_n_rejects_negative_case_basic` |
| 003 | `iterate_func_stop_iteration_cd0a3a8_1` | hypothesis | `IterateStopsOnStopIteration` | `witness_iterate_stops_on_stop_iteration_case_basic` |
| 004 | `iterate_func_stop_iteration_cd0a3a8_1` | crosshair | `IterateStopsOnStopIteration` | `witness_iterate_stops_on_stop_iteration_case_basic` |
| 005 | `last_reversed_truthy_check_cca3294_1` | hypothesis | `LastWithNoneReversed` | `witness_last_with_none_reversed_case_basic` |
| 006 | `last_reversed_truthy_check_cca3294_1` | crosshair | `LastWithNoneReversed` | `witness_last_with_none_reversed_case_basic` |
| 007 | `numeric_range_negative_step_slice_a51da82_1` | hypothesis | `NumericRangeSliceNegativeStep` | `witness_numeric_range_slice_negative_step_case_basic` |
| 008 | `numeric_range_negative_step_slice_a51da82_1` | crosshair | `NumericRangeSliceNegativeStep` | `witness_numeric_range_slice_negative_step_case_basic` |
| 009 | `numeric_range_reversed_empty_edb3346_1` | hypothesis | `NumericRangeReversedHandlesEmpty` | `witness_numeric_range_reversed_handles_empty_case_basic` |
| 010 | `numeric_range_reversed_empty_edb3346_1` | crosshair | `NumericRangeReversedHandlesEmpty` | `witness_numeric_range_reversed_handles_empty_case_basic` |
| 011 | `product_index_iterator_input_cf186b5_1` | hypothesis | `ProductIndexAcceptsIterator` | `witness_product_index_accepts_iterator_case_basic` |
| 012 | `product_index_iterator_input_cf186b5_1` | crosshair | `ProductIndexAcceptsIterator` | `witness_product_index_accepts_iterator_case_basic` |
| 013 | `split_after_maxsplit_empty_9245cd0_1` | hypothesis | `SplitAfterMaxsplitNoEmpty` | `witness_split_after_maxsplit_no_empty_case_basic` |
| 014 | `split_after_maxsplit_empty_9245cd0_1` | crosshair | `SplitAfterMaxsplitNoEmpty` | `witness_split_after_maxsplit_no_empty_case_basic` |
| 015 | `split_before_empty_buffer_2e81a56_1` | hypothesis | `SplitBeforeEmptyIterableNoEmpty` | `witness_split_before_empty_iterable_no_empty_case_basic` |
| 016 | `split_before_empty_buffer_2e81a56_1` | crosshair | `SplitBeforeEmptyIterableNoEmpty` | `witness_split_before_empty_iterable_no_empty_case_basic` |

## Witness Catalog

- `witness_exactly_n_rejects_negative_case_basic` — exactly_n([True, False], -2) must return False, not raise.
- `witness_iterate_stops_on_stop_iteration_case_basic` — f(3) raises StopIteration; iterate must stop after yielding [0, 1, 2, 3].
- `witness_last_with_none_reversed_case_basic` — Custom iterable with __reversed__ = None over [1, 2, 3].
- `witness_numeric_range_slice_negative_step_case_basic` — numeric_range(0, 10, 2)[::-1] should equal [8, 6, 4, 2, 0].
- `witness_numeric_range_reversed_handles_empty_case_basic` — Empty range numeric_range(0, 0, 1).
- `witness_product_index_accepts_iterator_case_basic` — iter([2, 3, 1]) over three range(5) pools.
- `witness_split_after_maxsplit_no_empty_case_basic` — split_after([0], pred=x==0, maxsplit=1) must not yield a trailing [].
- `witness_split_before_empty_iterable_no_empty_case_basic` — split_before([], pred) must yield no chunks.
