from yatzy import Yatzy, Roll

# These unit tests can be run using the py.test framework
# available from http://pytest.org/


def test_chance_scores_sum_of_all_dice():
    assert 15 == Yatzy.chance(Roll(2, 3, 4, 5, 1))
    assert 16 == Yatzy.chance(Roll(3, 3, 4, 5, 1))


def test_yatzy_scores_50_if_all_dice_same_number_0_otherwise():
    assert 50 == Yatzy.yatzy(Roll(4, 4, 4, 4, 4))
    assert 50 == Yatzy.yatzy(Roll(6, 6, 6, 6, 6))
    assert 0 == Yatzy.yatzy(Roll(6, 6, 6, 6, 3))


def test_ones_scores_sum_dice_reading_1():
    assert 1 == Yatzy.ones(Roll(1, 2, 3, 4, 5))
    assert 2 == Yatzy.ones(Roll(1, 2, 1, 4, 5))
    assert 0 == Yatzy.ones(Roll(6, 2, 2, 4, 5))
    assert 4 == Yatzy.ones(Roll(1, 2, 1, 1, 1))


def test_twos_scores_sum_dice_reading_2():
    assert 4 == Yatzy.twos(Roll(1, 2, 3, 2, 6))
    assert 10 == Yatzy.twos(Roll(2, 2, 2, 2, 2))


def test_threes_scores_sum_dice_reading_3():
    assert 6 == Yatzy.threes(Roll(1, 2, 3, 2, 3))
    assert 12 == Yatzy.threes(Roll(2, 3, 3, 3, 3))


def test_fours_scores_sum_dice_reading_4():
    assert 12 == Yatzy.fours(Roll(4, 4, 4, 5, 5))
    assert 8 == Yatzy.fours(Roll(4, 4, 5, 5, 5))
    assert 4 == Yatzy.fours(Roll(4, 5, 5, 5, 5))


def test_fives_scores_sum_dice_reading_5():
    assert 10 == Yatzy.fives(Roll(4, 4, 4, 5, 5))
    assert 15 == Yatzy.fives(Roll(4, 4, 5, 5, 5))
    assert 20 == Yatzy.fives(Roll(4, 5, 5, 5, 5))


def test_sixes_scores_sum_dice_reading_6():
    assert 0 == Yatzy.sixes(Roll(4, 4, 4, 5, 5))
    assert 6 == Yatzy.sixes(Roll(4, 4, 6, 5, 5))
    assert 18 == Yatzy.sixes(Roll(6, 5, 6, 6, 5))


def test_pair_scores_sum_two_highest_matching_dice():
    assert 6 == Yatzy.pair(Roll(3, 4, 3, 5, 6))
    assert 10 == Yatzy.pair(Roll(5, 3, 3, 3, 5))
    assert 12 == Yatzy.pair(Roll(5, 3, 6, 6, 5))


def test_two_pairs_scores_sum_mathing_dice_if_two_disctinct_pairs_0_otherwise():
    assert 16 == Yatzy.two_pairs(Roll(3, 3, 5, 4, 5))
    assert 18 == Yatzy.two_pairs(Roll(3, 3, 6, 6, 6))
    assert 0 == Yatzy.two_pairs(Roll(3, 3, 6, 5, 4))


def test_three_of_a_kind_scores_sum_three_matching_dice_0_otherwise():
    assert 9 == Yatzy.three_of_a_kind(Roll(3, 3, 3, 4, 5))
    assert 15 == Yatzy.three_of_a_kind(Roll(5, 3, 5, 4, 5))
    assert 9 == Yatzy.three_of_a_kind(Roll(3, 3, 3, 3, 5))


def test_four_of_a_kind_scores_sum_four_matching_dice_0_otherwise():
    assert 12 == Yatzy.four_of_a_kind(Roll(3, 3, 3, 3, 5))
    assert 20 == Yatzy.four_of_a_kind(Roll(5, 5, 5, 4, 5))
    assert 12 == Yatzy.four_of_a_kind(Roll(3, 3, 3, 3, 3))
    assert 0 == Yatzy.four_of_a_kind(Roll(3, 3, 3, 2, 1))


def test_small_straight_scores_sum_of_dice_if_dice_reads_1_2_3_4_5():
    assert 15 == Yatzy.small_straight(Roll(1, 2, 3, 4, 5))
    assert 15 == Yatzy.small_straight(Roll(2, 3, 4, 5, 1))
    assert 0 == Yatzy.small_straight(Roll(1, 2, 2, 4, 5))


def test_large_straight_scores_sum_of_dice_if_dice_reads_2_3_4_5_6():
    assert 20 == Yatzy.large_straight(Roll(6, 2, 3, 4, 5))
    assert 20 == Yatzy.large_straight(Roll(2, 3, 4, 5, 6))
    assert 0 == Yatzy.large_straight(Roll(1, 2, 2, 4, 5))


def test_full_house_scores_sum_of_dice_if_three_of_a_kind_and_two_of_a_kind():
    assert 18 == Yatzy.full_house(Roll(6, 2, 2, 2, 6))
    assert 0 == Yatzy.full_house(Roll(2, 3, 4, 5, 6))
