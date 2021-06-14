## Useful Python Snippits

** Output all punctuation **
> https://www.geeksforgeeks.org/string-punctuation-in-python/
    > Make sure to import string library function inorder to use string.punctuation
    > !"#$%&'()*+, -./:;<=>?@[\]^_`{|}~

** Remove punctuation from a string
> https://www.geeksforgeeks.org/python-remove-punctuation-from-string/
    > Prefer to use the regex method here:
    >> # Python3 code to demonstrate working of
    >> # Removing punctuations in string
    >> # Using regex
    >> import re
    >> 
    >> # initializing string
    >> test_str = "Gfg, is best : for ! Geeks ;"
    >> 
    >> # printing original string
    >> print("The original string is : " + test_str)
    >> 
    >> # Removing punctuations in string
    >> # Using regex
    >> res = re.sub(r'[^\w\s]', '', test_str)
    >> 
    >> # printing result
    >> print("The string after punctuation filter : " + res)

!!! This might be super userfule
> http://www.localizingjapan.com/blog/2012/01/20/regular-expressions-for-japanese-text/
    * Unicode Hiragana \x3041-\x3096
    * Unicode Katakana \x30A0-\x30FF
    * Unicode Kanji \x3400-\x4DB5\x4E00-\x9FCB\xF900-\xFA6A
    * Unicode Radicals \x2E80-\x2FD5
    * Unicode Half Width \xFF5F-\xFF9F
    * Unicode Japanese Symbols \x3000-\x303F
