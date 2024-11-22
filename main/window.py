from tkinter import *
import customtkinter
from PIL import Image,ImageTk


global O_pic
global X_pic
global Empty_pic


O_pic = customtkinter.CTkImage(light_image=Image.open("O_PIC.png"),size=(43,43))
X_pic = customtkinter.CTkImage(light_image=Image.open("X_PIC.png"),size=(43,43))
Empty_pic = customtkinter.CTkImage(light_image=Image.open("EMPTY_PIC.png"),size=(43,43))
PVP = customtkinter.CTkImage(light_image=Image.open("PVP.png"),size=(80,40))
PVC = customtkinter.CTkImage(light_image=Image.open("PVC.png"),size=(80,40))




root = customtkinter.CTk()
w = root.winfo_screenwidth()
h = root.winfo_screenheight()

root.geometry("%dx%d+%d+%d" % (w,h,0,0))
BACK_GROUND = customtkinter.CTkImage(light_image=Image.open("BACKGROUND.png"),size=(w,h))

root.title("Tic-Tac-Toe")

#root.config(bg="#8E064C")

bg_LABEL = customtkinter.CTkLabel(root,text="",width = w,height = h, image = BACK_GROUND)
bg_LABEL.place(x = 0,y= 0)


#Buttons

button01 = customtkinter.CTkButton(root,width=85,height=75,text="",corner_radius=10,bg_color="#1d62fd",fg_color="#487ced",state=ACTIVE,image= Empty_pic)
button02 = customtkinter.CTkButton(root,width=85,height=75,text="",corner_radius=10,bg_color="#1d62fd",fg_color="#487ced",state=ACTIVE,image= Empty_pic)
button03 = customtkinter.CTkButton(root,width=85,height=75,text="",corner_radius=10,bg_color="#1d62fd",fg_color="#487ced",state=ACTIVE,image= Empty_pic)

button04 = customtkinter.CTkButton(root,width=85,height=75,text="",corner_radius=10,bg_color="#1d62fd",fg_color="#487ced",state=ACTIVE,image= Empty_pic)
button05 = customtkinter.CTkButton(root,width=85,height=75,text="",corner_radius=10,bg_color="#1d62fd",fg_color="#487ced",state=ACTIVE,image= Empty_pic)
button06 = customtkinter.CTkButton(root,width=85,height=75,text="",corner_radius=10,bg_color="#1d62fd",fg_color="#487ced",state=ACTIVE,image= Empty_pic)

button07 = customtkinter.CTkButton(root,width=85,height=75,text="",corner_radius=10,bg_color="#1d62fd",fg_color="#487ced",state=ACTIVE,image= Empty_pic)
button08 = customtkinter.CTkButton(root,width=85,height=75,text="",corner_radius=10,bg_color="#1d62fd",fg_color="#487ced",state=ACTIVE,image= Empty_pic)
button09 = customtkinter.CTkButton(root,width=85,height=75,text="",corner_radius=10,bg_color="#1d62fd",fg_color="#487ced",state=ACTIVE,image= Empty_pic)

button10 = customtkinter.CTkButton(root,text="",width=80, height=40,corner_radius=1,bg_color="#1d62fd",fg_color="#1d62fd",state=ACTIVE,image=PVP)
button11 = customtkinter.CTkButton(root,text="↻",font=("Kelvatica",40),text_color="#FFFFFF",width=40,height=40,corner_radius=1,fg_color="#1d62fd",bg_color="#1d62fd",hover_color="#1d62fd")

#placing

button01.place(x = 475 , y = 320)
button02.place(x = 570 , y = 320)
button03.place(x = 665 , y = 320)
button04.place(x = 475 , y = 405)
button05.place(x = 570 , y = 405)
button06.place(x = 665 , y = 405)
button07.place(x = 475 , y = 490)
button08.place(x = 570 , y = 490)
button09.place(x = 665 , y = 490)

button10.place(x = 460, y = 85)
button11.place(x = 740, y = 80)



WhosMove = StringVar()
WhosMove.set("X's MOVE")
WhosMove_LABEL = customtkinter.CTkLabel(root,textvariable = WhosMove,font = ("Arial",25),width = 250,height = 50,bg_color="#1d62fd",fg_color="#1d62fd",text_color="#FFFFFF")
WhosMove_LABEL.place(x = 485, y = 210)



move = 0
moves = [[0,0,0],[0,0,0],[0,0,0]]

def CheckWinner(arr):    
    for i in range(3):
        if arr[i][0] == arr[i][1] == arr[i][2] != 0:
            return arr[i][0]
        
    for j in range(3):
        if arr[0][j] == arr[1][j] == arr[2][j] != 0:
            return arr[0][j]
        
    if arr[0][2] == arr[1][1] == arr[2][0] != 0:
        return arr[0][2]
    
    if arr[0][0] == arr[1][1] == arr[2][2] != 0:
        return arr[0][0] 

    for i in range(3):
        for j in range(3):
            if arr[i][j] == 0:
                return 2
            
    return 0
    

def freeze():
    button01.configure(state =DISABLED)
    button02.configure(state =DISABLED)
    button03.configure(state =DISABLED)
    button04.configure(state =DISABLED)
    button05.configure(state =DISABLED)
    button06.configure(state =DISABLED)
    button07.configure(state =DISABLED)
    button08.configure(state =DISABLED)
    button09.configure(state =DISABLED)


def reset():
    global move
    move = 0
    button01.configure(state =ACTIVE,image = Empty_pic)
    button02.configure(state =ACTIVE,image = Empty_pic)
    button03.configure(state =ACTIVE,image = Empty_pic)
    button04.configure(state =ACTIVE,image = Empty_pic)
    button05.configure(state =ACTIVE,image = Empty_pic)
    button06.configure(state =ACTIVE,image = Empty_pic)
    button07.configure(state =ACTIVE,image = Empty_pic)
    button08.configure(state =ACTIVE,image = Empty_pic)
    button09.configure(state =ACTIVE,image = Empty_pic)
    
    for i in range(3):
        for j in range(3):
            moves[i][j] = 0

    WhosMove.set("X's MOVE")


CHECK_PVP = True
def Change():
    global CHECK_PVP
    if CHECK_PVP:
        button10.configure(image = PVC)
        CHECK_PVP = False
        
    else:
        button10.configure(image = PVP)
        CHECK_PVP = True


def minmax(arr,depth,isMaxing):
    if CheckWinner(arr) == 1: # X wins human wins
        return -10 - depth
    elif CheckWinner(arr) == -1: # O wins AI wins
        return  10 - depth
    elif CheckWinner(arr) == 0:
        return 0

    
    if isMaxing:
        BEST_SCORE = -1000
        for i in range(3):
            for j in range(3):
                if arr[i][j] == 0:
                    #Recursive 
                    arr[i][j] = -1
                    BEST_SCORE = max(BEST_SCORE,minmax(arr,depth+1,False))
                    #Backtraking
                    arr[i][j] = 0

        return BEST_SCORE
    
    else:
        BEST_SCORE = 1000
        for i in range(3):
            for j in range(3):
                if arr[i][j] == 0:
                    arr[i][j] = 1
                    BEST_SCORE = min(BEST_SCORE,minmax(arr,depth+1,True))

                    arr[i][j] = 0

        return BEST_SCORE



def BestMove(arr):
    Best_score = -1000
    best_move = None

    for i in range(3):
        for j in range(3):
            if arr[i][j] == 0:
                arr[i][j] = -1 #puts O and finds scores
                new_score = minmax(arr,0,False)
                arr[i][j] = 0

                if new_score > Best_score:
                    best_move = (i,j)
                    Best_score = new_score

    return best_move



def ButtonPressed(x,y):
    global moves
    global move
    if CHECK_PVP:
        butt(x,y)
    
    else:
        butt(x,y)
        if CheckWinner(moves) != 2:
            return
        

        m,n = BestMove(moves)
        butt(m,n)
        if CheckWinner(moves) != 2:
            return
        
        
        


        


def butt(x,y):
    global move
    if move % 2 == 0:
        moves[x][y] = 1
        WhosMove.set("O's MOVE")
    else:
        moves[x][y] = -1
        WhosMove.set("X's MOVE")

    if x == 0:
        if y == 0:
            button01.configure(image = X_pic) if move % 2 == 0 else button01.configure(image = O_pic)
            button01.configure(state = DISABLED)
            move = move + 1


        elif y == 1:
            button02.configure(image = X_pic) if move % 2 == 0 else button02.configure(image = O_pic)
            button02.configure(state = DISABLED)
            move = move + 1
        
        else:
            button03.configure(image = X_pic) if move % 2 == 0 else button03.configure(image = O_pic)
            button03.configure(state = DISABLED)
            move = move + 1

    elif x == 1:
        if y == 0:
            button04.configure(image = X_pic) if move % 2 == 0 else button04.configure(image = O_pic)
            button04.configure(state = DISABLED)
            move = move + 1

        elif y == 1:
            button05.configure(image = X_pic) if move % 2 == 0 else button05.configure(image = O_pic)
            button05.configure(state = DISABLED)
            move = move + 1
        
        else:
            button06.configure(image = X_pic) if move % 2 == 0 else button06.configure(image = O_pic)
            button06.configure(state = DISABLED)
            move = move + 1
        
    else:
        if y == 0:
            button07.configure(image = X_pic) if move % 2 == 0 else button07.configure(image = O_pic)
            button07.configure(state = DISABLED)
            move = move + 1
    
        elif y == 1:
            button08.configure(image = X_pic) if move % 2 == 0 else button08.configure(image = O_pic)
            button08.configure(state = DISABLED)
            move = move + 1
        
        else:
            button09.configure(image = X_pic) if move % 2 == 0 else button09.configure(image = O_pic)
            button09.configure(state = DISABLED)
            move = move + 1


    if CheckWinner(moves) == 1:
        WhosMove.set("X WINS!")
        freeze()
    elif CheckWinner(moves) == -1:
        WhosMove.set("O WINS!")
        freeze()
    elif CheckWinner(moves) == 0:
        WhosMove.set("DRAW !")






button01.configure(command = lambda: ButtonPressed(0,0))
button02.configure(command = lambda: ButtonPressed(0,1))
button03.configure(command = lambda: ButtonPressed(0,2))

button04.configure(command = lambda: ButtonPressed(1,0))
button05.configure(command = lambda: ButtonPressed(1,1))
button06.configure(command = lambda: ButtonPressed(1,2))

button07.configure(command = lambda: ButtonPressed(2,0))
button08.configure(command = lambda: ButtonPressed(2,1))
button09.configure(command = lambda: ButtonPressed(2,2))

button10.configure(command = lambda: Change())

button11.configure(command = lambda: reset())


root.mainloop()


