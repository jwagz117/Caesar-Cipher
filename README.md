## Caesar Cipher Crack
### Jack Wagner

A Caesar Cipher is a method to encode messages by shifting the entire alphabet by an unknown value.  For example, a shift of 7 means that a --> h, b --> i, and so on.  

*caesarCrack.py* takes a user inputted string and makes an output file of all 26 Caesar shift possibilities.  Then, it runs through each line in the output file and assigns a score based on how many words in the line are real English words.  The line with the highest score is outputted as the decoded Message


See *testPoss.txt* for the output file that contains all the possibilities when the following string was entered:

`ftue ue m omqemd oubtqd`

The above string is `this is a caesar cipher` with a shift of 12.


##Sample output:##


````
What is your encoded message?     ftue ue m omqemd oubtqd
1: 1
2: 1
3: 1
4: 1
5: 1
6: 1
7: 1
8: 1
9: 1
10: 1
11: 1
12: 4
13: 1
14: 1
15: 1
16: 1
17: 1
18: 1
19: 1
20: 2
21: 1
22: 1
23: 1
24: 1
25: 1
Decoded Message: this is a caesar cipher 


Process finished with exit code 0
````
