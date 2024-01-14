import pygame 
import random as rn
pygame.init()
res = (820, 820) #screen dimensions
screen = pygame.display.set_mode(res)
run = True
win = 0
pygame.display.set_caption('Wordle Bot')

white = (255, 255, 255)
black = (0,0,0)
green = (121, 167, 107)
yellow = (197, 181, 101)
grey = (122, 124, 126)
main_box_dim = (400, 480) #dimensions of the parent box
main_box_pos = ((res[0]-main_box_dim[0])/2, (res[1]-main_box_dim[1])/2) #starting coordinates of the parent box
pygame.draw.rect(screen, white , pygame.Rect(main_box_pos[0],main_box_pos[1],main_box_dim[0],main_box_dim[1]), 2) #drawing the parent box

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

# word lists 
f = open("possible_words.txt", "r")
possible_words = []
for x in f:
    possible_words.append((x[0:5]).upper())   #possible words list (contains all words - 12953)

g = open("wordle_words.txt", "r")
wordle_words = []
for y in g:
    wordle_words.append((y[0:5]).upper())     #wordle words list (contains only possible words - 2309)

#select a random winning word
random_digit = rn.randint(0, len(wordle_words)-1)
win_word = wordle_words[random_digit]
win_char_list = []
for i in win_word:
    win_char_list.append(i)
print(win_char_list)

pygame.display.flip()

row_1 = [[], "open"]
row_2 = [[], "open"]
row_3 = [[], "open"]
row_4 = [[], "open"]
row_5 = [[], "open"]
row_6 = [[], "open"]

def listen():
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            return("quit")
        if events.type == pygame.KEYDOWN and win == 0:
            if events.key == pygame.K_a:
                return("A")
            if events.key == pygame.K_b:
                return("B")
            if events.key == pygame.K_c:
                return("C")
            if events.key == pygame.K_d:
                return("D")
            if events.key == pygame.K_e:
                return("E")
            if events.key == pygame.K_f:
                return("F")
            if events.key == pygame.K_g:
                return("G")
            if events.key == pygame.K_h:
                return("H")
            if events.key == pygame.K_i:
                return("I")
            if events.key == pygame.K_j:
                return("J")
            if events.key == pygame.K_k:
                return("K")
            if events.key == pygame.K_l:
                return("L")
            if events.key == pygame.K_m:
                return("M")
            if events.key == pygame.K_n:
                return("N")
            if events.key == pygame.K_o:
                return("O")
            if events.key == pygame.K_p:
                return("P")
            if events.key == pygame.K_q:
                return("Q")
            if events.key == pygame.K_r:
                return("R")
            if events.key == pygame.K_s:
                return("S")
            if events.key == pygame.K_t:
                return("T")
            if events.key == pygame.K_u:
                return("U")
            if events.key == pygame.K_v:
                return("V")
            if events.key == pygame.K_w:
                return("W")
            if events.key == pygame.K_x:
                return("X")
            if events.key == pygame.K_y:
                return("Y")
            if events.key == pygame.K_z:
                return("Z")
            if events.key == pygame.K_RETURN:
                return("enter")
            if events.key == pygame.K_BACKSPACE:
                return("backspace")

row_color = 0 #row that needs to be coloured
curr = [1,1,1,1,1] #1 is a random value here just to declare a non empty list

#function to arrange the entered data
def listprint(key, row_color, curr):

    if row_1[1] == "open":
        if len(row_1[0]) < 5 and key != "enter" and key != "backspace":
            row_1[0].append(key)
        elif key == "backspace" and row_1[1] == "open" and len(row_1[0]) != 0:
            del row_1[0][-1]
        elif key == "enter" and len(row_1[0]) == 5 and row_1[1] == "open" and ''.join(row_1[0]) in possible_words:
            row_1[1] = "closed"
            row_color = 1
            curr = row_1[0][:]
        elif key == "enter" and len(row_1[0]) == 5 and row_1[1] == "open" and ''.join(row_1[0]) not in possible_words:
            print("Invalid Word")


    elif row_1[1] == "closed" and row_2[1] == "open":
        if len(row_2[0]) < 5 and key != "enter" and key != "backspace":
            row_2[0].append(key)
        elif key == "backspace" and row_2[1] == "open" and len(row_2[0]) != 0:
            del row_2[0][-1]
        elif key == "enter" and len(row_2[0]) == 5 and row_2[1] == "open" and ''.join(row_2[0]) in possible_words:
            row_2[1] = "closed"
            row_color = 2
            curr = row_2[0][:]
        elif key == "enter" and len(row_2[0]) == 5 and row_2[1] == "open" and ''.join(row_2[0]) not in possible_words:
            print("Invalid Word")

    elif row_1[1] == "closed" and row_2[1] == "closed" and row_3[1] == "open":
        if len(row_3[0]) < 5 and key != "enter" and key != "backspace":
            row_3[0].append(key)
        elif key == "backspace" and row_3[1] == "open" and len(row_3[0]) != 0:
            del row_3[0][-1]
        elif key == "enter" and len(row_3[0]) == 5 and row_3[1] == "open" and ''.join(row_3[0]) in possible_words:
            row_3[1] = "closed"
            row_color = 3
            curr = row_3[0][:]
        elif key == "enter" and len(row_3[0]) == 5 and row_3[1] == "open" and ''.join(row_3[0]) not in possible_words:
            print("Invalid Word")

    elif row_1[1] == "closed" and row_2[1] == "closed" and row_3[1] == "closed" and row_4[1] == "open":
        if len(row_4[0]) < 5 and key != "enter" and key != "backspace":
            row_4[0].append(key)
        elif key == "backspace" and row_4[1] == "open" and len(row_4[0]) != 0:
            del row_4[0][-1]
        elif key == "enter" and len(row_4[0]) == 5 and row_4[1] == "open" and ''.join(row_4[0]) in possible_words:
            row_4[1] = "closed"
            row_color = 4
            curr = row_4[0][:]
        elif key == "enter" and len(row_4[0]) == 5 and row_4[1] == "open" and ''.join(row_4[0]) not in possible_words:
            print("Invalid Word")

    elif row_1[1] == "closed" and row_2[1] == "closed" and row_3[1] == "closed" and row_4[1] == "closed" and row_5[1] == "open":
        if len(row_5[0]) < 5 and key != "enter" and key != "backspace":
            row_5[0].append(key)
        elif key == "backspace" and row_5[1] == "open" and len(row_5[0]) != 0:
            del row_5[0][-1]
        elif key == "enter" and len(row_5[0]) == 5 and row_5[1] == "open" and ''.join(row_5[0]) in possible_words:
            row_5[1] = "closed"
            row_color = 5
            curr = row_5[0][:]
        elif key == "enter" and len(row_5[0]) == 5 and row_5[1] == "open" and ''.join(row_5[0]) not in possible_words:
            print("Invalid Word")

    elif row_1[1] == "closed" and row_2[1] == "closed" and row_3[1] == "closed" and row_4[1] == "closed" and row_5[1] == "closed" and row_6[1] == "open":
        if len(row_6[0]) < 5 and key != "enter" and key != "backspace":
            row_6[0].append(key)
        elif key == "backspace" and row_6[1] == "open" and len(row_6[0]) != 0:
            del row_6[0][-1]
        elif key == "enter" and len(row_6[0]) == 5 and row_6[1] == "open" and ''.join(row_6[0]) in possible_words:
            row_6[1] = "closed"
            row_color = 6
            curr = row_6[0][:]
        elif key == "enter" and len(row_6[0]) == 5 and row_6[1] == "open" and ''.join(row_6[0]) not in possible_words:
            print("Invalid Word")
    return row_color, curr


#function to display entered on the game window
def display_data(data):
    text_x = main_box_pos[0] + (main_box_dim[0]/10)
    text_y = main_box_pos[1] + (main_box_dim[1]/12)
    for i in data:
        for j in i[0]:
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

color_dict = {} #to store output colors corresponding to respective rows

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


while run:
    key_press = listen()
    if key_press != None and key_press != "quit":
        #print(key_press)
        listprint_out = listprint(key_press, row_color, curr)
        entered_data = [row_1, row_2, row_3, row_4, row_5, row_6]

        screen.fill(black) #black fill to update
        retain_color(color_dict, main_box_pos, main_box_dim)
        if key_press == "enter":
            color_out = color_boxes(listprint_out[1], listprint_out[0], win_char_list, main_box_dim, main_box_pos)
            if color_out != None:
                print(color_out[0])
                color_dict[color_out[1]] = color_out[0]
                if color_out[0] == ["green", "green","green","green","green"]:
                    win = 1
            #print(color_dict)
        draw_boxes(main_box_dim, main_box_pos, white) #small box draw

        display_data(entered_data)
        #for i in entered_data:
           #print(i)


    pygame.display.update()
    if key_press == "quit":
        pygame.quit()
        run = False

    
    
