import pytest
from fizz_buzz import fizzbuzz


def test_fizzbuzz_given_1_returns_1():
    assert fizzbuzz(1) == 1


def test_fizzbuzz_given_2_returns_2():
    assert fizzbuzz(2) == 2


def test_fizzbuzz_given_3_returns_fizz():
    assert fizzbuzz(3) == "fizz"


def test_fizzbuzz_given_5_returns_buzz():
    assert fizzbuzz(5) == "buzz"


def test_fizzbuzz_given_6_returns_fizz():
    assert fizzbuzz(6) == "fizz"


def test_fizzbuzz_given_9_returns_fizz():
    assert fizzbuzz(9) == "fizz"


def test_fizzbuzz_given_10_returns_buzz():
    assert fizzbuzz(10) == "buzz"


def test_fizzbuzz_given_15_returns_fizzbuzz():
    assert fizzbuzz(15) == "fizzbuzz"


def test_fizzbuzz_given_20_returns_buzz():
    assert fizzbuzz(20) == "buzz"


def test_fizzbuzz_given_30_returns_fizzbuzz():
    assert fizzbuzz(30) == "fizzbuzz"


def test_fizzbuzz_given_45_returns_fizzbuzz():
    assert fizzbuzz(45) == "fizzbuzz"


def test_fizzbuzz_given_100_returns_buzz():
    assert fizzbuzz(100) == "buzz"
