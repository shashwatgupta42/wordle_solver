import pygame 
import operator
import random as rn
import math
import time
import pickle

#binary file containing the entropies for first attempt. Calculated by initial_entropy_calc.py script
first_attempt_file = open("first_attempt_data.dat", "rb") 

pygame.init()
res = (820, 820) #screen dimensions
screen = pygame.display.set_mode(res)
run = True

#variables to store winning and losing status
won = 0
lost = 0

games_played = 0

pygame.display.set_caption('Wordle Bot')
colors = ["green", "yellow", 0] #0 for green, 1 for yellow, 2 for grey
combinations = []

#data for first attempt
first_attempt_data = pickle.load(first_attempt_file)
sorted_first_attempt = sorted(first_attempt_data.items(), key=operator.itemgetter(1))

white = (255, 255, 255)
black = (0,0,0)
green = (121, 167, 107)
yellow = (197, 181, 101)
grey = (122, 124, 126)
blue = (74, 154, 233)
main_box_dim = (400, 480) #dimensions of the parent box
main_box_pos = ((res[0]-main_box_dim[0])/2, (res[1]-main_box_dim[1])/2) #starting coordinates of the parent box
pygame.draw.rect(screen, white , pygame.Rect(main_box_pos[0],main_box_pos[1],main_box_dim[0],main_box_dim[1]), 2) #drawing the parent box


#the following nested loop creates all permutations of colors
for i in colors:
    for j in colors:
        for k in colors:
            for l in colors:
                for m in colors:
                    combinations.append([i,j,k,l,m])


#function to draw boxes
def draw_boxes(main_box_dim, main_box_pos, white):
    small_box_dim = (main_box_dim[0]/5, main_box_dim[1]/6)
    small_x = main_box_pos[0] #small box init x
    small_y = main_box_pos[1] #small box init y
    boxes = 0
    for i in range(30):
        pygame.draw.rect(screen, white, pygame.Rect(small_x, small_y, small_box_dim[0], small_box_dim[1]), 2)
        boxes += 1
        small_x += main_box_dim[0]/5
        if boxes%5 == 0:
            small_x = main_box_pos[0]
            small_y += main_box_dim[1]/6

draw_boxes(main_box_dim, main_box_pos, white) #initial draw

#text font
font = pygame.font.Font('freesansbold.ttf', 32)
'''
# word lists 
f = open("possible_words.txt", "r")
possible_words = []
for x in f:
    possible_words.append((x[0:5]).upper())   #possible words list (contains all words - 12953)
'''
g = open("wordle_words.txt", "r")
wordle_words = []
for y in g:
    wordle_words.append((y[0:5]).upper())     #wordle words list (contains only possible words - 2309)

pygame.display.flip()

def listen():
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            return("quit")
        


#function to arrange the entered data
def listprint(suggestion, row_color, curr, row_1, row_2, row_3, row_4, row_5, row_6):

    if len(row_1) == 0:
        row_1 = suggestion[:]
        row_color = 1
        curr = row_1[:]

    elif len(row_1) == 5 and len(row_2) == 0:
        row_2 = suggestion[:]
        row_color = 2
        curr = row_2[:]

    elif len(row_1) == 5 and len(row_2) == 5 and len(row_3) == 0:
        row_3 = suggestion[:]
        row_color = 3
        curr = row_3[:]

    elif len(row_1) == 5 and len(row_2) == 5 and len(row_3) == 5 and len(row_4) == 0:
        row_4 = suggestion[:]
        row_color = 4
        curr = row_4[:]

    elif len(row_1) == 5 and len(row_2) == 5 and len(row_3) == 5 and len(row_4) == 5 and len(row_5) == 0:
        row_5 = suggestion[:]
        row_color = 5
        curr = row_5[:]

    elif len(row_1) == 5 and len(row_2) == 5 and len(row_3) == 5 and len(row_4) == 5 and len(row_5) == 5 and len(row_6) == 0:
        row_6 = suggestion[:]
        row_color = 6
        curr = row_6[:]

    return row_color, curr, row_1, row_2, row_3, row_4, row_5, row_6


#function to display entered data on the game window
def display_data(data):
    text_x = main_box_pos[0] + (main_box_dim[0]/10)
    text_y = main_box_pos[1] + (main_box_dim[1]/12)
    for i in data:
        for j in i:
            text = font.render(j, True, white, black)
            textRect = text.get_rect()
            textRect.center = (text_x, text_y)
            screen.blit(text, textRect)

            text_x += main_box_dim[0]/5
        text_y += main_box_dim[1]/6
        text_x = main_box_pos[0] + (main_box_dim[0]/10)

def color_boxes(curr, row_color, win_char_list, main_box_dim, main_box_pos):
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

    #**********************
    #NOTE:- 0 in the colors list represents grey

    if colors != [0,0,0,0,0]:
        x = main_box_pos[0]
        for k in colors:
            y = main_box_pos[1] + ((row_color-1)*(main_box_dim[1]/6))
            if k == "green":
                color_val = green[:]
            elif k == "yellow":
                color_val = yellow[:]
            elif k == 0 or k == "#":
                color_val = grey[:]
            pygame.draw.rect(screen, color_val, pygame.Rect(x, y, main_box_dim[0]/5, main_box_dim[1]/6), 15)
            x += main_box_dim[0]/5

        return colors, row_color


#************************** F.O.R   B.O.T ********************************

#following functions outputs colors for the bot
def color_boxes_bot(curr, win_char_list):
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

#following function calculates the entropy for the bot
def find_entropy(bot_words):
    principal_data = {}
    on_word = 0
    for i in bot_words:
        all_func_val = []
        win_char_list = []
        for letters in i:
            win_char_list.append(letters)
        #print(win_char_list)
        for j in combinations:
            valid_words = 0
            #print(j)
            for k in bot_words:
                curr = []
                for letters_k in k:
                    curr.append(letters_k)
                #print(curr)
                color_boxes_out = color_boxes_bot(curr, win_char_list)
                if color_boxes_out == j:
                    valid_words += 1
                    #print(k)

            #print(valid_words)
            probability = valid_words/len(bot_words)
            if probability != 0:
                func_val = (probability) * (math.log(1/probability, 2))
                all_func_val.append(func_val)
        entropy = sum(all_func_val)
        principal_data[i] = entropy
        on_word += 1
        #print(on_word)

    return principal_data

#following function gives word list that are valid for the game
def give_words(prev_input, words_list, colour_output):
    give_words_ouput = []
    prev_input_list = []
    for j in prev_input:
        prev_input_list.append(j)
    for i in words_list:
        win_list = []
        for letters in i:
            win_list.append(letters)
        if color_boxes_bot(prev_input_list, win_list) == colour_output:
            give_words_ouput.append(i)
    return give_words_ouput

#*********************** BOT SPECIFIC FUNCTIONS END **************************************




def retain_color(color_dict, main_box_pos, main_box_dim): #to retain the output colors after keypress
    for i in color_dict:
        x = main_box_pos[0]
        for k in color_dict[i]:
            y = main_box_pos[1] + ((i-1)*(main_box_dim[1]/6))
            if k == "green":
                color_val = green[:]
            elif k == "yellow":
                color_val = yellow[:]
            elif k == 0 or k == "#":
                color_val = grey[:]
            pygame.draw.rect(screen, color_val, pygame.Rect(x, y, main_box_dim[0]/5, main_box_dim[1]/6), 15)
            x += main_box_dim[0]/5

to_be_played = int(input("NO. OF GAMES TO BE PLAYED: "))
at_game = 0
while run:
    key_press = listen()
    if key_press == "quit":
        run = False
    if at_game != to_be_played and run != False:
        for games in range(1, (to_be_played+1)):
            at_game = games

            print("At Game: ", at_game)
            pygame.display.update()
            win = 0

            #initial suggestion
            suggestion = []
            
            for i in sorted_first_attempt[-1][0]:
                suggestion.append(i)

            #following words list is for the bot to operate on
            bot_words = wordle_words[:]
            
            #select a random winning word
            random_digit = rn.randint(0, len(wordle_words)-1)
            win_word = wordle_words[random_digit]
            win_char_list = []
            for i in win_word:
                win_char_list.append(i)
            #print(win_char_list)

            row_1 = []
            row_2 = []
            row_3 = []
            row_4 = []
            row_5 = []
            row_6 = []

            row_color = 0 #row that needs to be coloured
            curr = [1,1,1,1,1] #1 is a random value here just to declare a non empty list
            color_dict = {} #to store output colors corresponding to respective rows

            if win == 0 and run != False:
                for attempts in range(6):

                    listprint_out = listprint(suggestion, row_color, curr, row_1, row_2, row_3, row_4, row_5, row_6)
                    row_1 = listprint_out[2][:]
                    row_2 = listprint_out[3][:]
                    row_3 = listprint_out[4][:]
                    row_4 = listprint_out[5][:]
                    row_5 = listprint_out[6][:]
                    row_6 = listprint_out[7][:]

                    entered_data = [row_1, row_2, row_3, row_4, row_5, row_6]

                    screen.fill(black)

                    #to print the relevant text
                    at_game_text = font.render("At Game: "+str(at_game), True, white, black)
                    at_gameRect = at_game_text.get_rect()
                    at_gameRect.center = (res[0]/2, res[1]/10)
                    screen.blit(at_game_text, at_gameRect)

                    won_text = font.render("Won: "+str(won), True, white, black)
                    won_textRect = won_text.get_rect()
                    won_textRect.center = (res[0]/4, res[1]*(8.7/10))
                    screen.blit(won_text, won_textRect)

                    lost_text = font.render("Lost: "+str(lost), True, white, black)
                    lost_textRect = lost_text.get_rect()
                    lost_textRect.center = (res[0]*(3/4), res[1]*(8.7/10))
                    screen.blit(lost_text, lost_textRect)


                    retain_color(color_dict, main_box_pos, main_box_dim)

                    color_out = color_boxes(listprint_out[1], listprint_out[0], win_char_list, main_box_dim, main_box_pos)
                    if color_out != None:
                        color_dict[color_out[1]] = color_out[0]

                    draw_boxes(main_box_dim, main_box_pos, white)
                    display_data(entered_data)
                    pygame.display.update()

                    color_out_bot = color_boxes_bot(suggestion, win_char_list)
                    give_words_output = give_words(suggestion, bot_words, color_out_bot)
                    bot_words.clear()
                    bot_words = give_words_output[:]
                    #print(give_words_output)
                    find_entropy_output = find_entropy(bot_words)
                    sorted_find_entropy_output = sorted(find_entropy_output.items(), key=operator.itemgetter(1))
                    #for i in sorted_find_entropy_output:
                        #print(i[0], ":", i[1])
                    highest_entropy_words = [k for k,v in find_entropy_output.items() if v == sorted_find_entropy_output[-1][1]]
                    if len(highest_entropy_words) > 1:
                        suggested_word = rn.choice(highest_entropy_words)
                    else:
                        suggested_word = sorted_find_entropy_output[-1][0]
                    suggestion.clear()
                    for i in suggested_word:
                        suggestion.append(i)

                    if color_out[0] == ["green","green","green","green","green"]:
                        print("Game Status: WON")
                        win = 1
                        won += 1
                        break
                    elif len(row_6) == 5 and win == 0:
                        print("Game Status: LOST")
                        lost += 1
                        break
                    time.sleep(0.25)
            pygame.display.update()
            games_played += 1


            time.sleep(0.5)

    #final text print
    screen.fill(black)
    final_text = font.render("FINAL RESULTS", True, white, black)
    final_textRect = final_text.get_rect()
    final_textRect.center = (res[0]/2, res[1]/10)
    screen.blit(final_text, final_textRect)

    played_text = font.render("Games Played: "+str(games_played), True, white, black)
    played_textRect = played_text.get_rect()
    played_textRect.center = (res[0]/2, res[1]*(1/3))
    screen.blit(played_text, played_textRect)

    won_text = font.render("    "+"Won: "+str(won)+"    ", True, white, green)
    won_textRect = won_text.get_rect()
    won_textRect.center = (res[0]/2, (res[1]*(1/3))+50)
    screen.blit(won_text, won_textRect)

    lost_text = font.render("   "+"Lost: "+str(lost)+"  ", True, white, grey)
    lost_textRect = lost_text.get_rect()
    lost_textRect.center = (res[0]/2, (res[1]*(1/3))+100)
    screen.blit(lost_text, lost_textRect)

    percent_text = font.render("   "+"Winning percent: "+str((won/games_played)*100)+"%  ", True, white, blue)
    percent_textRect = percent_text.get_rect()
    percent_textRect.center = (res[0]/2, (res[1]*(1/3))+150)
    screen.blit(percent_text, percent_textRect)

    pygame.display.update()
    #break
print("\n")
print("********** FINAL RESULTS *************")
print("\n")
print("GAMES PLAYED: ", games_played)
print("GAMES WON: ", won)
print("GAMES LOST: ", lost)
print("\n")
print("WINNING PERCENTAGE: ", (won/games_played)*100, "%")
print("\n")

#f.close()
g.close()
first_attempt_file.close()