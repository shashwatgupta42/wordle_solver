import math
import pickle

output_file = open("first_attempt_data_.dat", "ab")
colors = ["green", "yellow", 0] #0 for green, 1 for yellow, 2 for grey
combinations = []

# word lists 
f = open("wordle_words.txt", "r")
possible_words = []
for x in f:
    possible_words.append((x[0:5]).upper())   #possible words list (contains all words - 12953)
'''
g = open("wordle_words.txt", "r")
wordle_words = []
for y in g:
    wordle_words.append((y[0:5]).upper())     #wordle words list (contains only possible words - 2309)
'''

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

print(principal_data)
pickle.dump(principal_data, output_file)
output_file.close()