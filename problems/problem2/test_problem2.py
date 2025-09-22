from solution import longest_common_prefix

def test_case1():
    assert longest_common_prefix(["flower", "flow", "flight"]) == "fl"

def test_case2():
    assert longest_common_prefix(["dog", "racecar", "car"]) == ""

def test_case3():
    assert longest_common_prefix(["abcd", "abc"]) == "abc"

def test_case4():
    assert longest_common_prefix(["interspecies", "interstellar", "interstate", "internet"]) == "inter"
