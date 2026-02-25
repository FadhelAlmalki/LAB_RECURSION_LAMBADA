'''
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
'''
def count_vowels(phrase):
    if not phrase:
        return 0
    first_char = phrase[0].lower()
    if first_char in ['a', 'e', 'i', 'o', 'u']:
        return 1 + count_vowels(phrase[1:])
    else:
        return count_vowels(phrase[1:])

phrase = "I love python"
vowel_count = count_vowels(phrase)
print(f"The number of vowels in the phrase is: {vowel_count}")

