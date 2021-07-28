_ZERO_TO_NINETEEN = ('Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven',
                     'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen')
_TENS = ('', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety', 'Hundred')
_THOUSANDS = ('', 'Thousand', 'Million', 'Billion')


def num_to_words(num):
    if num == 0:
        return _ZERO_TO_NINETEEN[0]
    ans = ""
    i = 0
    while num > 0:
        if num % 1000 != 0:
            ans = _num_to_word_helper(num % 1000) + _THOUSANDS[i] + " " + ans
            i += 1
            num //= 1000
    return ans.strip()


def _num_to_word_helper(num):
    if num == 0:
        return ""
    elif num < 20:
        return _ZERO_TO_NINETEEN[num] + " "
    elif num < 100:
        return _TENS[num // 10] + " " + _num_to_word_helper(num % 10)
    else:
        return _ZERO_TO_NINETEEN[num // 100] + " Hundred " + _num_to_word_helper(num % 100)


print(num_to_words(100))
print(num_to_words(512))
print(num_to_words(12345))
print(num_to_words(123456))
print(num_to_words(1234567))
print(num_to_words(8765))
