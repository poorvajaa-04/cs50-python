import getpass
import re

COMMON_PASSWORDS = {
    "password", "123456", "123456789", "12345678", "qwerty", "admin", "welcome", "letmein", "password123", "admin123", "iloveyou", "monkey",
    "dragon", "football", "abc123",
}

KEYBOARD_PATTERNS = [ "qwerty", "asdf", "zxcv", "qwert", "asdfg", "zxcvb",]

def main():
    print("=" * 50)
    print("       PASSWORD STRENGTH ANALYZER")
    print("=" * 50)

    password = getpass.getpass("Enter password: ")

    print("\nAnalyzing...")

    analysis = analyze_password(password)
    score = calculate_score(analysis)
    strength = classify_strength(score)
    recommendations = generate_recommendations(analysis)

    display_report(analysis, score, strength, recommendations)

def analyze_password(password):    #Analyze the basic characteristics and predictability of a password.

    analysis = {
        "length": len(password),
        "uppercase": bool(re.search(r"[A-Z]", password)),
        "lowercase": bool(re.search(r"[a-z]", password)),
        "numbers": bool(re.search(r"[0-9]", password)),
        "symbols": bool(re.search(r"[^A-Za-z0-9]", password)),
        "patterns": detect_patterns(password),
        "common_password": check_common_password(password),
    }

    return analysis

def detect_patterns(password):  #  Detect predictable patterns in a password 
                                #  Sequential numbers, reverse number sequences, alphabetic sequences, reverse alphabetic sequences, repeated characters, repeated chunks, keyboard patterns.

    patterns = []

    if not password:
        return patterns

    lower_password = password.lower()

    sequences = [ "012", "123","234", "345", "456", "567", "678", "789", "abc","bcd", "cde","def","efg", "fgh","ghi", "hij", "ijk", "jkl", 
                  "klm", "lmn", "mno", "nop", "opq", "pqr", "qrs", "rst", "stu", "tuv", "uvw", "vwx", "wxy", "xyz" ]

    reverse_sequences = [
        sequence[::-1]
        for sequence in sequences
    ]

    if any(sequence in lower_password for sequence in sequences):
        if any(char.isdigit() for char in password):
            patterns.append("sequential_numbers")
        else:
            patterns.append("alphabetic_sequence")

    if any(sequence in lower_password for sequence in reverse_sequences):
        if any(char.isdigit() for char in password):
            patterns.append("reverse_sequence")
        else:
            patterns.append("reverse_alphabetic_sequence")

    if re.search(r"(.)\1{2,}", password):
        patterns.append("repeated_characters")

    for chunk_length in range(1, len(password) // 2 + 1):
        if len(password) % chunk_length == 0:
            chunk = password[:chunk_length]
            repetitions = len(password) // chunk_length

            if repetitions >= 2 and chunk * repetitions == password:
                patterns.append("repeated_chunks")
                break

    if any(pattern in lower_password for pattern in KEYBOARD_PATTERNS):
        patterns.append("keyboard_pattern")

    return patterns

def check_common_password(password): # Check whether a password appears in the built-in collection of commonly used passwords

    return password.lower() in COMMON_PASSWORDS

def calculate_score(analysis): # Calculate a password security score from 0 to 100.
                               # Positive points: Password length, Character diversity
                               # Negative points: Common password, Predictable patterns
    score = 0

    length = analysis["length"]

    if length >= 8:
        score += 20

    if length >= 12:
        score += 15

    if length >= 16:
        score += 15

    if length >= 20:
        score += 10

    if analysis["lowercase"]:
        score += 10

    if analysis["uppercase"]:
        score += 10

    if analysis["numbers"]:
        score += 10

    if analysis["symbols"]:
        score += 10

    for pattern in analysis["patterns"]:
        if pattern == "sequential_numbers":
            score -= 10

        elif pattern == "reverse_sequence":
            score -= 10

        elif pattern == "alphabetic_sequence":
            score -= 10

        elif pattern == "reverse_alphabetic_sequence":
            score -= 10

        elif pattern == "repeated_characters":
            score -= 10

        elif pattern == "repeated_chunks":
            score -= 15

        elif pattern == "keyboard_pattern":
            score -= 15

    if analysis["common_password"]:
        score -= 40

    score = max(0, min(100, score))

    return score

def classify_strength(score):   # Convert a numerical score into a strength category

    if score <= 19:
        return "VERY WEAK"

    elif score <= 39:
        return "WEAK"

    elif score <= 59:
        return "MODERATE"

    elif score <= 79:
        return "STRONG"

    return "VERY STRONG"

def generate_recommendations(analysis):  # Generate human-readable recommendations based on the password analysis.

    recommendations = []

    if analysis["length"] < 12:
        recommendations.append(
            "Use at least 12–16 characters."
        )

    if not analysis["uppercase"]:
        recommendations.append(
            "Consider adding uppercase letters."
        )

    if not analysis["lowercase"]:
        recommendations.append(
            "Consider adding lowercase letters."
        )

    if not analysis["numbers"]:
        recommendations.append(
            "Consider adding numbers."
        )

    if not analysis["symbols"]:
        recommendations.append(
            "Consider adding special characters."
        )

    if analysis["common_password"]:
        recommendations.append(
            "This password is commonly used. Choose something unique."
        )

    if any(
        pattern in analysis["patterns"]
        for pattern in [
            "sequential_numbers",
            "reverse_sequence",
            "alphabetic_sequence",
            "reverse_alphabetic_sequence",
        ]
    ):
        recommendations.append(
            "Avoid predictable sequences such as 1234 or abcd."
        )

    if any(
        pattern in analysis["patterns"]
        for pattern in [
            "repeated_characters",
            "repeated_chunks",
        ]
    ):
        recommendations.append(
            "Avoid repeated characters or repeated patterns."
        )

    if "keyboard_pattern" in analysis["patterns"]:
        recommendations.append(
            "Avoid common keyboard patterns such as qwerty or asdf."
        )

    if not recommendations:
        recommendations.extend(
            [
                "Excellent password length.",
                "Good character diversity.",
                "No obvious predictable patterns.",
                "Password does not appear to be common.",
            ]
        )

    return recommendations

def display_report(analysis, score, strength, recommendations):  # Display the analysis results without displaying the actual password.

    print("\nPASSWORD ANALYSIS")
    print("-" * 30)

    print("Length:", analysis["length"])
    print("Uppercase:", analysis["uppercase"])
    print("Lowercase:", analysis["lowercase"])
    print("Numbers:", analysis["numbers"])
    print("Symbols:", analysis["symbols"])
    print("Common password:", analysis["common_password"])
    print("Patterns:", analysis["patterns"])

    print("\nScore:", score, "/100")
    print("Strength:", strength)

    print("\nRecommendations:")
    for recommendation in recommendations:
        print("-", recommendation)

if __name__ == "__main__":
    main()