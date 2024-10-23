class Solution:
  def compress(self, chars: List[str]) -> int:
    length = 0
    i = 0

    while i < len(chars):
      c = chars[i]
      counter = 0
      while i < len(chars) and chars[i] == c:
        counter += 1
        i += 1
      chars[length] = c
      length += 1
      if counter > 1:
        for c in str(counter):
          chars[length] = c
          length += 1

    return length