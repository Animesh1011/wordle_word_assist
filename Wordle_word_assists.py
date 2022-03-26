#!/usr/bin/env python
# coding: utf-8




#pip english-words





with open(r'C:\Users\USER\Downloads\myfile.txt') as word_file:
    valid_words = set(word_file.read().split())





#wordle_word_assists

def wordle_word_assists(startswith='',endswith='',contain_in_position='',doesnotinclude='',contain_not_in_pos='',repetitive_letter='',length_of_word=5):
    
    final_word_list = [x for x in valid_words if len(x) == length_of_word]
    
    #doesnotinclude
    
    #check if any letter present in other filter.
    letters_with_number = contain_not_in_pos + contain_in_position + repetitive_letter
    letters_without_number = ''.join(filter(lambda x : not x.isdigit(),letters_with_number))
    total_input_letters = set(startswith+endswith+letters_without_number)
    
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
                
    #anyposition
    contain_in_position_list = [(contain_in_position[x],contain_in_position[x+1]) for x in range(0,len(contain_in_position),2)]
    if contain_in_position_list:
        for tuples in contain_in_position_list:
            for word in final_word_list[:]:
                if word[int(tuples[0])-1]!=tuples[1]:
                    final_word_list.remove(word)
                
    #endswith
    if endswith:
        for word in final_word_list[:]:
            if word[-1]!=endswith:
                final_word_list.remove(word)
                
    repetitive_list = [(repetitive_letter[x],repetitive_letter[x+1]) for x in range(0,len(repetitive_letter),2)]
    if repetitive_list:
        for tuples in repetitive_list:
            for word in final_word_list[:]:
                if word.count(tuples[1])<int(tuples[0]):
                    final_word_list.remove(word)
    return final_word_list





print(wordle_word_assists(length_of_word = 5,contain_not_in_pos='',repetitive_letter='',startswith='',contain_in_position='',endswith='',doesnotinclude=''))







