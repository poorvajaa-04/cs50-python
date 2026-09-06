from project import (
    analyze_password,
    detect_patterns,
    check_common_password,
    calculate_score,
    classify_strength,
    generate_recommendations,
)


def test_analyze_password():
    result = analyze_password("Password123!")
    assert result["length"] == 12
    assert result["uppercase"]
    assert result["lowercase"]
    assert result["numbers"]
    assert result["symbols"]


def test_detect_patterns():
    assert "sequential_numbers" in detect_patterns("1234")
    assert "repeated_characters" in detect_patterns("aaaa")
    assert detect_patterns("Xk9!mQ2") == []


def test_check_common_password():
    assert check_common_password("password")
    assert check_common_password("PASSWORD")
    assert not check_common_password("Xk9!mQ2")


def test_calculate_score():
    weak = analyze_password("123")
    strong = analyze_password("StrongPassword9!")
    assert calculate_score(strong) > calculate_score(weak)


def test_classify_strength():
    assert classify_strength(10) == "VERY WEAK"
    assert classify_strength(30) == "WEAK"
    assert classify_strength(50) == "MODERATE"
    assert classify_strength(70) == "STRONG"
    assert classify_strength(90) == "VERY STRONG"


def test_generate_recommendations():
    result = generate_recommendations(analyze_password("abc"))
    assert len(result) > 0