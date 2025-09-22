def maxVowels(self, s: str, k: int) -> int:
  temp = s[0:k]
  vowels = ['a', 'e', 'i', 'o', 'u']
  vowel = sum(1 for char in temp if char in vowels)
  max_vowel = vowel

  for i in range(1, len(s)-k+1):
    if s[i-1] in 'aeiou' :
      vowel -= 1

    if s[i+k-1] in 'aeiou' :
      vowel += 1

    if max_vowel < vowel :
      max_vowel = vowel

  return max_vowel


if __name__ == '__main__' :
  string = str(input())
  k = int(input())

  print(string, k)

  print(maxVowels(string, k))

  # error
  # 1. s[i] in 'aeiou' : vowel -=1 -> 새로 들어오는 모음인데 뺌