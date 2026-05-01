# more-itertools — ETNA Tasks

Total tasks: 32

## Task Index

| Task | Variant | Framework | Property | Witness |
|------|---------|-----------|----------|---------|
| 001 | `exactly_n_negative_input_adeda34_1` | proptest | `ExactlyNRejectsNegative` | `witness_exactly_n_rejects_negative_case_basic` |
| 002 | `exactly_n_negative_input_adeda34_1` | quickcheck | `ExactlyNRejectsNegative` | `witness_exactly_n_rejects_negative_case_basic` |
| 003 | `exactly_n_negative_input_adeda34_1` | crabcheck | `ExactlyNRejectsNegative` | `witness_exactly_n_rejects_negative_case_basic` |
| 004 | `exactly_n_negative_input_adeda34_1` | hegel | `ExactlyNRejectsNegative` | `witness_exactly_n_rejects_negative_case_basic` |
| 005 | `iterate_func_stop_iteration_cd0a3a8_1` | proptest | `IterateStopsOnStopIteration` | `witness_iterate_stops_on_stop_iteration_case_basic` |
| 006 | `iterate_func_stop_iteration_cd0a3a8_1` | quickcheck | `IterateStopsOnStopIteration` | `witness_iterate_stops_on_stop_iteration_case_basic` |
| 007 | `iterate_func_stop_iteration_cd0a3a8_1` | crabcheck | `IterateStopsOnStopIteration` | `witness_iterate_stops_on_stop_iteration_case_basic` |
| 008 | `iterate_func_stop_iteration_cd0a3a8_1` | hegel | `IterateStopsOnStopIteration` | `witness_iterate_stops_on_stop_iteration_case_basic` |
| 009 | `last_reversed_truthy_check_cca3294_1` | proptest | `LastWithNoneReversed` | `witness_last_with_none_reversed_case_basic` |
| 010 | `last_reversed_truthy_check_cca3294_1` | quickcheck | `LastWithNoneReversed` | `witness_last_with_none_reversed_case_basic` |
| 011 | `last_reversed_truthy_check_cca3294_1` | crabcheck | `LastWithNoneReversed` | `witness_last_with_none_reversed_case_basic` |
| 012 | `last_reversed_truthy_check_cca3294_1` | hegel | `LastWithNoneReversed` | `witness_last_with_none_reversed_case_basic` |
| 013 | `numeric_range_negative_step_slice_a51da82_1` | proptest | `NumericRangeSliceNegativeStep` | `witness_numeric_range_slice_negative_step_case_basic` |
| 014 | `numeric_range_negative_step_slice_a51da82_1` | quickcheck | `NumericRangeSliceNegativeStep` | `witness_numeric_range_slice_negative_step_case_basic` |
| 015 | `numeric_range_negative_step_slice_a51da82_1` | crabcheck | `NumericRangeSliceNegativeStep` | `witness_numeric_range_slice_negative_step_case_basic` |
| 016 | `numeric_range_negative_step_slice_a51da82_1` | hegel | `NumericRangeSliceNegativeStep` | `witness_numeric_range_slice_negative_step_case_basic` |
| 017 | `numeric_range_reversed_empty_edb3346_1` | proptest | `NumericRangeReversedHandlesEmpty` | `witness_numeric_range_reversed_handles_empty_case_basic` |
| 018 | `numeric_range_reversed_empty_edb3346_1` | quickcheck | `NumericRangeReversedHandlesEmpty` | `witness_numeric_range_reversed_handles_empty_case_basic` |
| 019 | `numeric_range_reversed_empty_edb3346_1` | crabcheck | `NumericRangeReversedHandlesEmpty` | `witness_numeric_range_reversed_handles_empty_case_basic` |
| 020 | `numeric_range_reversed_empty_edb3346_1` | hegel | `NumericRangeReversedHandlesEmpty` | `witness_numeric_range_reversed_handles_empty_case_basic` |
| 021 | `product_index_iterator_input_cf186b5_1` | proptest | `ProductIndexAcceptsIterator` | `witness_product_index_accepts_iterator_case_basic` |
| 022 | `product_index_iterator_input_cf186b5_1` | quickcheck | `ProductIndexAcceptsIterator` | `witness_product_index_accepts_iterator_case_basic` |
| 023 | `product_index_iterator_input_cf186b5_1` | crabcheck | `ProductIndexAcceptsIterator` | `witness_product_index_accepts_iterator_case_basic` |
| 024 | `product_index_iterator_input_cf186b5_1` | hegel | `ProductIndexAcceptsIterator` | `witness_product_index_accepts_iterator_case_basic` |
| 025 | `split_after_maxsplit_empty_9245cd0_1` | proptest | `SplitAfterMaxsplitNoEmpty` | `witness_split_after_maxsplit_no_empty_case_basic` |
| 026 | `split_after_maxsplit_empty_9245cd0_1` | quickcheck | `SplitAfterMaxsplitNoEmpty` | `witness_split_after_maxsplit_no_empty_case_basic` |
| 027 | `split_after_maxsplit_empty_9245cd0_1` | crabcheck | `SplitAfterMaxsplitNoEmpty` | `witness_split_after_maxsplit_no_empty_case_basic` |
| 028 | `split_after_maxsplit_empty_9245cd0_1` | hegel | `SplitAfterMaxsplitNoEmpty` | `witness_split_after_maxsplit_no_empty_case_basic` |
| 029 | `split_before_empty_buffer_2e81a56_1` | proptest | `SplitBeforeEmptyIterableNoEmpty` | `witness_split_before_empty_iterable_no_empty_case_basic` |
| 030 | `split_before_empty_buffer_2e81a56_1` | quickcheck | `SplitBeforeEmptyIterableNoEmpty` | `witness_split_before_empty_iterable_no_empty_case_basic` |
| 031 | `split_before_empty_buffer_2e81a56_1` | crabcheck | `SplitBeforeEmptyIterableNoEmpty` | `witness_split_before_empty_iterable_no_empty_case_basic` |
| 032 | `split_before_empty_buffer_2e81a56_1` | hegel | `SplitBeforeEmptyIterableNoEmpty` | `witness_split_before_empty_iterable_no_empty_case_basic` |

## Witness Catalog

- `witness_exactly_n_rejects_negative_case_basic` — exactly_n([True, False], -2) must return False, not raise.
- `witness_iterate_stops_on_stop_iteration_case_basic` — f(3) raises StopIteration; iterate must stop after yielding [0, 1, 2, 3].
- `witness_last_with_none_reversed_case_basic` — Custom iterable with __reversed__ = None over [1, 2, 3].
- `witness_numeric_range_slice_negative_step_case_basic` — numeric_range(0, 10, 2)[::-1] should equal [8, 6, 4, 2, 0].
- `witness_numeric_range_reversed_handles_empty_case_basic` — Empty range numeric_range(0, 0, 1).
- `witness_product_index_accepts_iterator_case_basic` — iter([2, 3, 1]) over three range(5) pools.
- `witness_split_after_maxsplit_no_empty_case_basic` — split_after([0], pred=x==0, maxsplit=1) must not yield a trailing [].
- `witness_split_before_empty_iterable_no_empty_case_basic` — split_before([], pred) must yield no chunks.
