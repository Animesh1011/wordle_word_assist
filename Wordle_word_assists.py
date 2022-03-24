#!/usr/bin/env python
# coding: utf-8
#wordle_word_assists

with open(r'C:\Users\USER\Downloads\words_alpha.txt') as word_file:
    valid_words = set(word_file.read().split())

def wordle_word_assists(startswith='',second_position='',middle_position='',fourth_position='',endswith='',doesnotinclude='',contain_not_in_pos='',repetitive_letter='',length_of_word=5):
    
    five_word_list = [x for x in valid_words if len(x) == length_of_word]
    final_word_list = five_word_list
    
    #doesnotinclude
    
    #check if any letter present in other filter.
    letters_without_number = ''.join(filter(lambda x : not x.isdigit(),contain_not_in_pos))
    total_input_letters = set(startswith+second_position+middle_position+fourth_position+endswith+letters_without_number)
    
    for letter in total_input_letters:
        if letter in doesnotinclude:
            doesnotinclude = doesnotinclude.replace(letter,'')
    doesnotinclude_list = [x for x in doesnotinclude]
    
    if doesnotinclude_list:
        for letter in doesnotinclude_list:
            for word in final_word_list[:]:
                if letter in word:
                    final_word_list.remove(word)
                    
    #contains_but_not_in_nth_position
    contain_not_in_pos_list = [(contain_not_in_pos[x],contain_not_in_pos[x+1]) for x in range(0,len(contain_not_in_pos),2)]
    if contain_not_in_pos_list:
        include_list = []
        for tuples in contain_not_in_pos_list:
            for word in final_word_list[:]:
                if word[int(tuples[0])-1]==tuples[1]:
                    final_word_list.remove(word)
                    if tuples[1] not in include_list:
                        include_list.append(tuples[1])
                    
        for letter in include_list:
            for word in final_word_list[:]:
                if letter not in word:
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
                
    repetitive_list = [(repetitive_letter[x],repetitive_letter[x+1]) for x in range(0,len(repetitive_letter),2)]
    if repetitive_list:
        for tuples in repetitive_list:
            for word in final_word_list[:]:
                if word.count(tuples[1])<int(tuples[0]):
                    final_word_list.remove(word)
    return final_word_list


print(wordle_word_assists(length_of_word = 5,contain_not_in_pos='',repetitive_letter='',startswith='',second_position='',middle_position='',fourth_position='',endswith='',doesnotinclude=''))




