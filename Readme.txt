I. Counting the frequency of Words

In this assignment, you will write a function named word_distribution that takes a string as an input and returns a dictionary containing the frequency of each word in the text. Your function should convert all words to lower case and should remove punctuation that occurs at the end of a word. 
For example if the argument to the function is: 
 
text_string = “Hello. How are you? Please say hello if you don’t love me!”
your function should return (note that dictionaries are unordered and you may see a different ordering of keys in what your function returns):
 
{‘hello’: 2, ‘how’:1, ‘are’:1, ‘you’:2, ’please’:1, “don’t”: 1, 'say':1, 'if':1, 'love':1,'me':1}
 
For the purposes of this assignment, you can assume that words have at most one punctuation symbol at the end or one punctuation symbol at the beginning and ignore punctuation that appears anywhere else. For example:
text_string = "That's when I saw Jane (John's sister)!"
should return:
 {"that's":1, "when":1,"i":1,"saw":1,"jane":1, "(john's":1, "sister)":1}
Though sister) is not really a word, we'll accept it for the purposes of this assignment. Don't try to remove more than 1 punctuation symbol at the end of the words, because it would be rejected by the grader.
 
Notes:
 
1. word.split() splits a string on spaces and returns a list. Note that this will concatenate punctuation with words. For the above example, you will get:
[‘Hello.’,’How’,’are’,’you?’,…]
2. word = word.lower() converts a string into lower case. 
3. x.isalpha() returns True if a character is a letter of the alphabet and False otherwise