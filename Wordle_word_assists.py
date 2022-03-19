#!/usr/bin/env python
# coding: utf-8




#!pip install english-words



from english_words import english_words_lower_alpha_set





#wordle_word_assists

def wordle_word_assists(startswith='',second_position='',middle_position='',fourth_position='',endswith='',include='',doesnotinclude='',contain_not_in_pos=''):
    #variable decralation
    startswith = startswith
    second_position = second_position
    middle_position = middle_position
    fourth_position = fourth_position
    endswith = endswith
    include = include
    doesnotinclude = doesnotinclude
    contain_not_in_pos = contain_not_in_pos
    
    five_word_list = [x for x in english_words_lower_alpha_set if len(x) == 5]
    final_word_list = five_word_list
    
    #doesnotinclude
    doesnotinclude_list = [x for x in doesnotinclude]
    if doesnotinclude_list:
        for letter in doesnotinclude_list:
            for word in final_word_list[:]:
                if letter in word:
                    final_word_list.remove(word)
    
    #include
    include_list = [x for x in include]
    if include_list:
        for letter in include_list:
            for word in final_word_list[:]:
                if letter not in word:
                    final_word_list.remove(word)
                    
    #contains_but_not_in_nth_position
    contain_not_in_pos_list = [(contain_not_in_pos[x],contain_not_in_pos[x+1]) for x in range(0,len(contain_not_in_pos),2)]
    if contain_not_in_pos_list:
        for tuples in contain_not_in_pos_list:
            for word in final_word_list[:]:
                if word[int(tuples[0])-1]==tuples[1]:
                    final_word_list.remove(word)
                    
    #startswith
    if startswith:
        for word in final_word_list[:]:
            if word[0]!=startswith:
                final_word_list.remove(word)
                
    #second_position
    if second_position:
        for word in final_word_list[:]:
            if word[1]!=second_position:
                final_word_list.remove(word)
                
    #middle_position
    if middle_position:
        for word in final_word_list[:]:
            if word[2]!=middle_position:
                final_word_list.remove(word)
                
    #fourth_position
    if fourth_position:
        for word in final_word_list[:]:
            if word[3]!=fourth_position:
                final_word_list.remove(word)
                
    #endswith
    if endswith:
        for word in final_word_list[:]:
            if word[4]!=endswith:
                final_word_list.remove(word)
    return final_word_list


print(wordle_word_assists(contain_not_in_pos='',startswith='',second_position='',middle_position='',fourth_position='',endswith='',include='',doesnotinclude=''))




