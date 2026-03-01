def find_anagrams(word, candidates):
    result = []
    word_lower = word.lower()
    word_sorted = sorted(word_lower)
    for candidate in candidates:
        candidate_lower = candidate.lower()
        if candidate_lower != word_lower and sorted(candidate_lower) == word_sorted:
            result.append(candidate)
    return result

print(find_anagrams("listen", ["enlists", "google", "inlets", "banana"]))