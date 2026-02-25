
vowels = ['a', 'e', 'i', 'o', 'u']
phrase = "I love python"

def count_vowels(phrase):
    count = 0
    for char in phrase:
        if char.lower() in vowels:
            count += 1
    return count

vowel_count = count_vowels(phrase)
print(f"The number of vowels in the phrase is: {vowel_count}")
