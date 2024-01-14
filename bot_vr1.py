import math
import operator
import pickle

colors = ["green", "yellow", 0] #0 for green, 1 for yellow, 2 for grey
combinations = []

#binary file containing the entropies for first attempt. Calculated by initial_entropy_calc.py srcipt
first_attempt_file = open("first_attempt_data.dat", "rb") 

# word lists 
f = open("wordle_words.txt", "r") 
possible_words = []
for x in f:
    possible_words.append((x[0:5]).upper())   #possible words list 

g = open("wordle_words.txt", "r")
wordle_words = []
for y in g:
    wordle_words.append((y[0:5]).upper())     #wordle words list (contains only possible words - 2309)

for i in colors:
    for j in colors:
        for k in colors:
            for l in colors:
                for m in colors:
                    combinations.append([i,j,k,l,m])

def color_boxes(curr, win_char_list):
    colors = [0,0,0,0,0] # "#" to only declare a non empty list
    curr_temp = curr[:]
    win_char_list_temp = win_char_list[:]

    if curr != [1,1,1,1,1]:
        if curr_temp[0] not in win_char_list_temp and curr_temp[1] not in win_char_list_temp and curr_temp[2] not in win_char_list_temp and curr_temp[3] not in win_char_list_temp and curr_temp[4] not in win_char_list_temp:
            colors = ["#","#","#","#","#"]
    for i in range(0,5):
        if curr_temp[i] == win_char_list_temp[i]:
            colors[i] = "green"
            curr_temp[i] = 0
            win_char_list_temp[i] = 0 

    for j in range(0,5):
        if curr_temp[j] != 0:
            if curr_temp[j] in win_char_list_temp:
                colors[j] = "yellow"
                win_char_list_temp[win_char_list_temp.index(curr_temp[j])] = 0
                curr_temp[j] = 0


    return colors

#data for first attempt
first_attempt_data = pickle.load(first_attempt_file)
sorted_first_attempt = sorted(first_attempt_data.items(), key=operator.itemgetter(1))
for i in sorted_first_attempt:
    print(i[0], ":", i[1])

def find_entropy(possible_words):
    principal_data = {}
    on_word = 0
    for i in possible_words:
        all_func_val = []
        win_char_list = []
        for letters in i:
            win_char_list.append(letters)
        #print(win_char_list)
        for j in combinations:
            valid_words = 0
            #print(j)
            for k in possible_words:
                curr = []
                for letters_k in k:
                    curr.append(letters_k)
                #print(curr)
                color_boxes_out = color_boxes(curr, win_char_list)
                if color_boxes_out == j:
                    valid_words += 1
                    #print(k)

            #print(valid_words)
            probability = valid_words/len(possible_words)
            if probability != 0:
                func_val = (probability) * (math.log(1/probability, 2))
                all_func_val.append(func_val)
        entropy = sum(all_func_val)
        principal_data[i] = entropy
        on_word += 1
        print(on_word)

    return principal_data

def give_words(prev_input, words_list, colour_output):
    give_words_ouput = []
    prev_input_list = []
    for j in prev_input:
        prev_input_list.append(j)
    for i in words_list:
        win_list = []
        for letters in i:
            win_list.append(letters)
        if color_boxes(prev_input_list, win_list) == colour_output:
            give_words_ouput.append(i)
    return give_words_ouput


for attempts in range(5):
    prev_input = (input("Enter last input:")).upper()
    if prev_input == "WON":
        break
    colour_output = eval(input("Enter colors: "))
    give_words_output = give_words(prev_input, possible_words, colour_output)
    possible_words.clear()
    possible_words = give_words_output[:]
    print(give_words_output)
    find_entropy_output = find_entropy(possible_words)
    sorted_find_entropy_output = sorted(find_entropy_output.items(), key=operator.itemgetter(1))
    for i in sorted_find_entropy_output:
        print(i[0], ":", i[1])


first_attempt_file.close()
f.close()
g.close()