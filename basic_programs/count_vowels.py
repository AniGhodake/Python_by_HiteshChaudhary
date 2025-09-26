
def countVowels(s):
    vowels = "aeiouAEIOU"
    count = 0

    for ch in s:
        if ch in vowels:
            count = count + 1
    return count


ans = countVowels("aeiou aeiou AEIOU")
print(ans)