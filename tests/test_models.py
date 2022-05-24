"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
import pytest


@pytest.mark.parametrize(
    "test, expected, expect_raises",
    [
        ... # other test cases here, with None for expect_raises
        (
            [[-1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [[0, 0.67, 1], [0.67, 0.83, 1], [0.78, 0.89, 1]],
            ValueError,
        ),
        (
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [[0.33, 0.67, 1], [0.67, 0.83, 1], [0.78, 0.89, 1]],
            None,
        ),
    ])
def test_patient_normalise(test, expected, expect_raises):
    """Test normalisation works for arrays of one and positive integers."""
    from inflammation.models import patient_normalise
    if expect_raises is not None:
        with pytest.raises(expect_raises):
            npt.assert_almost_equal(patient_normalise(np.array(test)), np.array(expected), decimal=2)
    else:
        npt.assert_almost_equal(patient_normalise(np.array(test)), np.array(expected), decimal=2)



@pytest.mark.parametrize(
    "test, expected",
    [
        ([[1, 2], [3, 4], [5, 6]], [1, 2]),
        ([[10, 92], [3, 4], [5, 6]], [3, 4]),
    ])

def test_min_with_params(test, expected):
    from inflammation.models import daily_min
    npt.assert_array_equal(daily_min(np.array(test)), np.array(np.array(expected)))

def test_daily_min_string():
    from inflammation.models import daily_min

    with pytest.raises(TypeError):
        error_expected = daily_min([['Hell', 'Hell'], ['hell', 'f']])

def test_daily_mean_zeros():
    """Test that mean function works for an array of zeros."""
    from inflammation.models import daily_mean

    test_input = np.array([[0, 0],
                           [0, 0],
                           [0, 0]])
    test_result = np.array([0, 0])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)


def test_daily_mean_integers():
    """Test that mean function works for an array of positive integers."""
    from inflammation.models import daily_mean

    test_input = np.array([[1, 2],
                           [3, 4],
                           [5, 6]])
    test_result = np.array([3, 4])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)


def test_daily_min():
    """ Test the min. """
    from inflammation.models import daily_min

    test_input = np.array([[1, 2],
                          [3, 4],
                          [5, 6]])
    test_result = np.array([1, 2])
    npt.assert_array_equal(daily_min(test_input), test_result)

def test_daily_max():
    """ Test the max. """
    from inflammation.models import daily_max

    test_input = np.array([[1, 2],
                          [3, 40],
                          [5, 6]])
    test_result = np.array([5, 40])
    npt.assert_array_equal(daily_max(test_input), test_result)