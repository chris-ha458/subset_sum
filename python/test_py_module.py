import dpss


def test_find_subset():
    assert dpss.find_subset([1, 2, 3, 4, 5], 6, 3) == [
        [1, 5], [2, 4], [1, 2, 3]]


def test_find_subset_fast_only_positive():
    assert dpss.find_subset_fast_only_positive([1, 2, 3, 4, 5], 10, 4) == [
        [1, 4, 5], [2, 3, 5], [1, 2, 3, 4]]


def test_sequence_matcher():
    assert dpss.sequence_matcher([3, 5, 7], [1, 5, -3, 4, 5, 3], 4) == \
        [
            [(3, [3]), (5, [5]), (7, [-3, 1, 4, 5])],
            [(3, [3]), (5, [1, 4]), (7, [-3, 5, 5])],
            [(3, [-3, 1, 5]), (5, [5]), (7, [3, 4])],
    ]


def test_sequence_matcher_m2m():
    assert dpss.sequence_matcher_m2m(
        [1980, 2980, 3500, 4000, 1050],
        [1950, 2900, 30, 80, 3300, 200, 3980, 1050, 20], 10) == \
        [[([1050], [1050]), ([1980], [30, 1950]), ([2980], [80, 2900]),
          ([3500], [200, 3300]), ([4000], [20, 3980])],
         [([1050, 1980, 2980], [80, 1950, 3980]), ([3500], [200, 3300]),
          ([4000], [20, 30, 1050, 2900])]]
