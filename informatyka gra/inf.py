from cProfile import label
from distutils import command
import tkinter as tk
from tkinter import font
import requests
from hashlib import new
from importlib.metadata import EntryPoint, entry_points
from tkinter import *
from turtle import window_height, window_width
from PIL import ImageTk,Image
import pygame
import random
import time
import logging

w=Tk()
w.geometry('900x500')
w.configure(bg='#262626')
w.resizable(0,0)
w.title('OKEJ')
w.iconbitmap('SUS.ico')

pygame.mixer.init()
def play():
      pygame.mixer.music.load("barka.mp3")
      pygame.mixer.music.play()

def pause():
    pygame.mixer.music.pause()

pygame.mixer.init()
def play2():
      pygame.mixer.music.load("masno.mp3")
      pygame.mixer.music.play()
    
def play3():
      pygame.mixer.music.load("louda.mp3")
      pygame.mixer.music.play()


new_window = ''
def openwindow():
      global new_window
      new_window = Toplevel(w)
      new_window.geometry("600x500")
      new_window.iconbitmap('kk.ico')
      new_window.title("kalkulator")
      new_window.resizable(False,False)
      def buttonadd(number):
          current = entry.get()
          entry.delete(0, END)
          entry.insert(0, str(current) + str(number))


      def buttonclear():
          entry.delete(0, END)


      def  buttonclick():
          first_nuber = entry.get()
          global f_num
          f_num = int(first_nuber)
          entry.delete(0, END)

      def buttonequale():
          secondnumber = entry.get()
          entry.delete(0, END)
          entry.insert(0, f_num + int(secondnumber))

    
      
      label = Label(new_window, bg='#262626')
      label.place(relheight=1, relwidth=1)


      entry = Entry(new_window, width=35, borderwidth=5, )
      entry.grid(column=0, row=0, columnspan=3, padx=10, pady=10)



      Buttton1 = Button(new_window, text="1",padx=40, pady=20,command=lambda: buttonadd(1),bg='#12c4c0')
      Buttton1.grid(row=3, column=0)

      Buttton2 = Button(new_window, text="2",padx=40, pady=20,command=lambda: buttonadd(2),bg='#12c4c0')
      Buttton2.grid(row=3, column=1)

      Buttton3 = Button(new_window, text="3",padx=40, pady=20,command=lambda: buttonadd(3),bg='#12c4c0')
      Buttton3.grid(row=3, column=2)



      Buttton4 = Button(new_window, text="4",padx=40, pady=20,command=lambda: buttonadd(4),bg='#12c4c0')
      Buttton4.grid(row=2, column=0)

      Buttton5 = Button(new_window, text="5",padx=40, pady=20,command=lambda: buttonadd(5),bg='#12c4c0')
      Buttton5.grid(row=2, column=1)

      Buttton6 = Button(new_window, text="6",padx=40, pady=20,command=lambda: buttonadd(6),bg='#12c4c0')
      Buttton6.grid(row=2, column=2)



      Buttton7 = Button(new_window, text="7",padx=40, pady=20,command=lambda: buttonadd(7),bg='#12c4c0')
      Buttton7.grid(row=1, column=0)

      Buttton8 = Button(new_window, text="8",padx=40, pady=20,command=lambda: buttonadd(8),bg='#12c4c0')
      Buttton8.grid(row=1, column=1)

      Buttton9= Button(new_window, text="9",padx=40, pady=20,command=lambda: buttonadd(9),bg='#12c4c0')
      Buttton9.grid(row=1, column=2)



      Buttton0 = Button(new_window, text="0",padx=40, pady=20,command=lambda: buttonadd(0),bg='#12c4c0')
      Buttton0.grid(row=4, column=0)

      ButttonADD = Button(new_window, text="+",padx=39, pady=20, command=buttonclick, bg='#12c4c0')
      ButttonADD.grid(row=5, column=2, columnspan=2)

      Butttonrówna = Button(new_window, text="=",padx=40, pady=20,command= buttonequale,bg='#12c4c0')
      Butttonrówna.grid(row=4, column=0)

      Butttonclear = Button(new_window, text="Clear",padx=79, pady=20,command= buttonclear,bg='#12c4c0')
      Butttonclear.grid(row=4, column=1, columnspan=2)


          
def weatherapp():
    HEIGHT = 500
    WIDTH = 600
    


    def formar_response(weather):
        name = (weather['name'])
        desc = (weather['weather'][0]['description'])
        temp = (weather['main']['temp'])

        return str(name) + ' ' + str(desc) + ' '+ str(temp)
    


    
    def get_weather(city):

        weather_key= '344d83fba8d4e06f64eb7cf6629e48a6'
        url = 'https://api.openweathermap.org/data/2.5/weather'
        params = {'APPID': weather_key, 'q': city, 'units': 'metric' }
        response = requests.get(url, params=params)
        weather = response.json()

        label['text'] = formar_response(weather)


    root = Tk()

    canvas = Canvas(root, height=HEIGHT, width=WIDTH)
    canvas.pack()


    
    background_label = Label(root, bg='#262626')
    background_label.place(x=0,y=0,relwidth=1, relheight=1)




    frame = Frame(root, bg='#12c4c0', bd=5)
    frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

    entry = Entry(frame, font=40)
    entry.place(relwidth=0.65, relheight=1)

    button = Button(frame, text="Znajdz pogodę", font=40, command=lambda: get_weather(entry.get()))
    button.place(relx=0.7, relheight=1, relwidth=0.3)

    lower_frame = Frame(root, bg='#12c4c0', bd=10, )
    lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


    label = Label(lower_frame, font=100,)
    label.place(relheight=1, relwidth=1)

    
snake_window = ''
def snakewindow():
    pygame.init()
    
 
    white = (255, 255, 255)
    yellow = (255, 255, 102)
    black = (0, 0, 0)
    red = (213, 50, 80)
    green = (0, 255, 0)
    blue = (50, 153, 213)
 
    dis_width = 600
    dis_height = 400
 
    dis = pygame.display.set_mode((dis_width, dis_height))
    pygame.display.set_caption('Wąż')

    
    
 
    clock = pygame.time.Clock()
 
    snake_block = 10
    snake_speed = 15
 
    font_style = pygame.font.SysFont("bahnschrift", 25)
    score_font = pygame.font.SysFont("comicsansms", 35)
 
 
    def Your_score(score):
        value = score_font.render("Twój wynik: " + str(score), True,'#12c4c0' )
        dis.blit(value, [0, 0])
 
 
 
    def our_snake(snake_block, snake_list):
        for x in snake_list:
            pygame.draw.rect(dis, '#12c4c0', [x[0], x[1], snake_block, snake_block])
 
 
    def message(msg, color):
        mesg = font_style.render(msg, True, color)
        dis.blit(mesg, [dis_width / 6, dis_height / 3])
 
 
    def gameLoop():
        game_over = False
        game_close = False
 
        x1 = dis_width / 2
        y1 = dis_height / 2
 
        x1_change = 0
        y1_change = 0
 
        snake_List = []
        Length_of_snake = 1
 
        foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
 
        while not game_over:
 
            while game_close == True:
                dis.fill('#262626')
                message("Przegrałeś jesteś naiwny i głupi",'#12c4c0' )
                Your_score(Length_of_snake - 1)
                pygame.display.update()
 
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_c:
                            gameLoop()
 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_change = -snake_block
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = snake_block
                        y1_change = 0
                    elif event.key == pygame.K_UP:
                        y1_change = -snake_block
                        x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        y1_change = snake_block
                        x1_change = 0
 
            if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                game_close = True
            x1 += x1_change
            y1 += y1_change
            dis.fill('#262626')
            pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
            snake_Head = []
            snake_Head.append(x1)
            snake_Head.append(y1)
            snake_List.append(snake_Head)
            if len(snake_List) > Length_of_snake:
                del snake_List[0]
 
            for x in snake_List[:-1]:
                if x == snake_Head:
                    game_close = True
 
            our_snake(snake_block, snake_List)
            Your_score(Length_of_snake - 1)
 
            pygame.display.update()
 
            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                Length_of_snake += 1
 
            clock.tick(snake_speed)
 
        pygame.quit()
        quit()

         
    gameLoop()

 



    

    
def toggle_win():
    f1=Frame(w,width=300,height=500,bg='#12c4c0')
    f1.place(x=0,y=0)


    #buttons
    def bttn(x,y,text,bcolor,fcolor,cmd):
     
        def on_entera(e):
            myButton1['background'] = bcolor #ffcc66
            myButton1['foreground']= '#262626'  #000d33

        def on_leavea(e):
            myButton1['background'] = fcolor
            myButton1['foreground']= '#262626'

        myButton1 = Button(f1,text=text,
                       width=42,
                       height=2,
                       fg='#262626',
                       border=0,
                       bg=fcolor,
                       activeforeground='#262626',
                       activebackground=bcolor,            
                        command=cmd)
                      
        myButton1.bind("<Enter>", on_entera)
        myButton1.bind("<Leave>", on_leavea)

        myButton1.place(x=x,y=y)


    bttn(0,117,'POGODA','#0f9d9a','#12c4c0',weatherapp)
    bttn(0,154,'W Ą Ż','#0f9d9a','#12c4c0',snakewindow)
    bttn(0,191,'KALKULATOR','#0f9d9a','#12c4c0',openwindow)
    bttn(0,228,'PRZESTAŃ SŁUCHAĆ BARKI','#0f9d9a','#12c4c0',pause)
    bttn(0,265,'SŁUCHANIE BARKI','#0f9d9a','#12c4c0',play)


    #
    def dele():
        f1.destroy()

    global img2
    img2 = ImageTk.PhotoImage(Image.open("close.png"))

    Button(f1,
           image=img2,
           border=0,
           command=dele,
           bg='#12c4c0',
           activebackground='#12c4c0').place(x=5,y=10)
    

img1 = ImageTk.PhotoImage(Image.open("open.png"))

Button(w,image=img1,
       command=toggle_win,
       border=0,
       bg='#262626',
       activebackground='#262626').place(x=5,y=10)

w.mainloop()