from solution import first_non_repeating

def test_case1():
    assert first_non_repeating("leetcode") == "l"

def test_case2():
    assert first_non_repeating("aabb") == "None"

def test_case3():
    assert first_non_repeating("abcabcde") == "d"

def test_case4():
    assert first_non_repeating("swiss") == "w"
