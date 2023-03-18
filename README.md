# Quora_Question_Pairs
Over 100 million people visit Quora every month, so it's no surprise that many people ask similarly worded questions. Multiple questions with the same intent can cause seekers to spend more time finding the best answer to their question, and make writers feel they need to answer multiple versions of the same question. Quora values canonical questions because they provide a better experience to active seekers and writers, and offer more value to both of these groups in the long term.

![alt text](https://github.com/pradeep-1995/Quora_Question_Pairs/blob/b693a43ab492ee1885d52a250c01b3ea8669ad83/website.JPG "image title")


### **Basic Features** 
- **q1_len** length of question 1 is number of letters in it.

- **q2_len** length of question 2 is number of letters in it.

- **q1_num_words** Number of words in questions 1

- **q2_num_words** Number of words in questions 2

- **words_common** Number of words common in both questions1 and questions2

- **words_total** Total number of unique words used in both questions1 and questions2

- **words_share** It is the ratio of words_common and words_total in each questions sets both 1 and 2

- Bow **counter_vectorizer** coloumns Here we take maximun used 3000 words.

### **Advanced Features**
#### **1. Token Features**

**cwc_min** *This is the ratio of the number of common words to the length of the smaller question.*

**cwc_max** *This is the ratio of the number of common words to the length of the larger question.*

**csc_min** *This is the ratio of the number of common stop words to the smaller stop word count among the two questions.*

**csc_max** *This is the ratio of the number of common stop words to the larger stop word count among the two questions.*

**ctc_min** *This is the ratio of the number of common tokens to the smaller token count among the two questions*

**ctc_max** *This is the ratio of the number of common tokens to the larger token count among the two questions*

**last_word_eq** *1 if the last word in the two questions is same, otherwise 0.*

**first_word_eq** *1 if the first word in the two questions is same, otherwise 0.*

#### **2. Length Based Features**

**mean_len** *Mean of the length of the two questions (By number of words).*

**abs_len_diff** *Absolute difference between the length of the two questions (By number of words).*

**longest_substr_ratio** *Ratio of the length of the longest substring among the two questions to the length of the smaller question.*

#### **3. Fuzzy Features**

 It provides a variety of functions for comparing two strings and computing a measure of similarity or distance between them.

**fuzz_ratio** *fuzz_ratio score from fuzzywuzzy*

**fuzz_partial_ratio** *fuzz_partial_ratio from fuzzywuzzy*

**token_sort_ratio** *token_sort_ratio from fuzzywuzzy*

**token_set_ratio** *token_set_ratio from fuzzywuzzy*
