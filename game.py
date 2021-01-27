import pygame
pygame.init()
pygame.mixer.init()
print('Game may take some time to load, as there are many files')
from tkinter import *
app=Tk()
app.resizable(width=FALSE, height=FALSE)
current=1
bcurrent=1
revivecount=0
enemy=""
win_game=False
Fight=False
trancer_transin_frame=0
trancer_in_frame=0
trancer_gone_frame=0
trancer_out_frame=0
ashe_transin_frame=0
ashe_in_frame=0
ashe_gone_frame=0
ashe_out_frame=0
korino_transin_frame=0
korino_in_frame=0
korino_gone_frame=0
korino_out_frame=0
emperor_transin_frame=0
emperor_in_frame=0
emperor_gone_frame=0
emperor_out_frame=0
base_animation_frame=0
general_in_frame=0
animation_frame=0
sample=1
teen_frame=0
Fade=True
example=1
num=0
frame=0
speaker=""
stun=0
no_speakers=[0,1,2,3,4,5,6,12,17,26,31,40]
stop=False
quote_num=0
sample2=1
def variables():
    global current
    global bcurrent
    global revivecount
    global enemy
    global win_game
    global Fight
    global trancer_transin_frame
    global trancer_in_frame
    global trancer_gone_frame
    global trancer_out_frame
    global ashe_transin_frame
    global ashe_in_frame
    global ashe_gone_frame
    global ashe_out_frame
    global korino_transin_frame
    global korino_in_frame
    global korino_gone_frame
    global korino_out_frame
    global emperor_transin_frame
    global emperor_in_frame
    global emperor_gone_frame
    global emperor_out_frame
    global base_animation_frame
    global general_in_frame
    global animation_frame
    global teen_frame
    global Fade
    global example
    global num
    global frame
    global speaker
    global stun
    global no_speakers
    global stop
    global quote_num
    
    current=1
    bcurrent=1
    revivecount=0
    enemy=""
    win_game=False
    Fight=False
    trancer_transin_frame=0
    trancer_in_frame=0
    trancer_gone_frame=0
    trancer_out_frame=0
    ashe_transin_frame=0
    ashe_in_frame=0
    ashe_gone_frame=0
    ashe_out_frame=0
    korino_transin_frame=0
    korino_in_frame=0
    korino_gone_frame=0
    korino_out_frame=0
    emperor_transin_frame=0
    emperor_in_frame=0
    emperor_gone_frame=0
    emperor_out_frame=0
    base_animation_frame=0
    general_in_frame=0
    animation_frame=0
    teen_frame=0
    Fade=True
    example=1
    num=0
    frame=0
    speaker=""
    stun=0
    no_speakers=[0,1,2,3,4,5,6,12,17,26,31,40]
    stop=False
    quote_num=0
variables()
quote1="The year is 20XX..."
quote2="The world has been overtaken by Meka Emperor and his army."
quote3="A radical team of teenagers with attitude have started an uprising "
quote4="They are known as the Resistance X"
quote5="The group fed up with the technazis decided to raid and overthrow Meka Emperor."
quote6="They board the base of Meka Emperer and seek to destroy him"
#*Red Alert*
#-sirens play-
quote7="They are met by the general Wu Jia Li"
quote8="Gentlemen, you have fallen right into my trap!"
#*Shocked face* - !!!
quote9="You must fight The 3 CyberLords and I, if you wish to be graced with our Emperor:"
quote10="MEKA EMPEROR"
quote11="Your first opponent..."
quote12='Hello Gentlemen, I am Trancer, the master of RAVE-N'
quote13="-fight scene-"
#*fight scene*
quote14="Finally we defeated him"
quote15="Good job team."
quote16="Not so fast children."
quote17="I AM ASHE of the steam, prepare to be rocked!"
#*fight scene*
quote18="-fight scene-"
quote19="Finally we defeated him"
quote20="Good job team."
quote21="Not so fast childre-"
quote22="The last guy already said that!"
quote23="WAI-WHAT?!"
quote24="How dare he steal my li-..."
quote25="I am Korino master of SAO"
quote26="Prepare to fight!"
#*fake fight scene*
quote27="-fight scene-"
quote28="Wait wait wait!"
quote29="I forgot my weapon"
quote30="Oh here it is!"
quote31="NOW Prepare to fight"
#*Fight scene*
quote32="-fight scene-"
quote33="Tell my mother... she makes good sushi..."
#*Explodes*
quote34="Took you long enough."
quote35="Come join me, we can destroy the emperor and rule the world!"
quote36="A new age of Tyrany, of justice of chao-"
quote37="Fuhuhuhuhu"
quote38="You ungrateful rat! Burn in hell"
#stabs general
quote39="I am Meka Emperor, but you may call me god!"
quote40="Prepare to die!"
#*fight scene*
quote41="-fight scene-"
#End scene
quote42="The Teenagers defeated Meka Emperor and were forever remembered as heroes!"
quote43="Congratulations! You beat the game! Thanks for Playing!"
quote44="Press 'z' to advance text"
quotes=[quote1,quote2,quote3,quote4,quote5,quote6,quote7,quote8,quote9,quote10,quote11,quote12,quote13,quote14,quote15,quote16,quote17,quote18,quote19,quote20,quote21,quote22,
        quote23,quote24,quote25,quote26,quote27,quote28,quote29,quote30,quote31,quote32,quote33,quote34,quote35,quote36,quote37,quote38,quote39,quote40,quote41,quote42,quote43,quote44]
quote_sample=quotes[quote_num]
win_music=pygame.mixer.Sound('sounds/win.wav')
emperor_death=pygame.mixer.Sound('sounds/emperor_death.wav')
emperor_laser=pygame.mixer.Sound('sounds/emperor_laser.wav')
stab=PhotoImage(file="images/stab.gif")
intro=pygame.mixer.Sound('sounds/intro.wav')
general_start=pygame.mixer.Sound('sounds/general_start.wav')
general_cont=pygame.mixer.Sound('sounds/general_cont.wav')
boss_music=pygame.mixer.Sound('sounds/boss_music.wav')
punch_sound=pygame.mixer.Sound('sounds/punch.wav')
kick_sound=pygame.mixer.Sound('sounds/kick.wav')
emperor_music=pygame.mixer.Sound('sounds/emperor_music.wav')
heal_sound=pygame.mixer.Sound('sounds/heal.wav')
stab_sound=pygame.mixer.Sound('sounds/staby.wav')
#-------------------------------------------------------------------------------------------------------------------------------------------------------
animation1=PhotoImage(file='images/animation1.gif')
animation2=PhotoImage(file='images/animation2.gif')
animation3=PhotoImage(file='images/animation3.gif')
animation4=PhotoImage(file='images/animation4.gif')
animation5=PhotoImage(file='images/animation5.gif')
animation6=PhotoImage(file='images/animation6.gif')
animation7=PhotoImage(file='images/animation7.gif')
animation8=PhotoImage(file='images/animation8.gif')
animation9=PhotoImage(file='images/animation9.gif')
animation10=PhotoImage(file='images/animation10.gif')
animation11=PhotoImage(file='images/animation11.gif')
animation12=PhotoImage(file='images/animation12.gif')
animation13=PhotoImage(file='images/animation13.gif')
animation14=PhotoImage(file='images/animation14.gif')
animation15=PhotoImage(file='images/animation15.gif')

animation=[animation1,animation2,animation3,animation4,animation5,animation6,animation7,animation8,animation9,animation10,
            animation11,animation12,animation13,animation14,animation15]
#-------------------------------------------------------------------------------------------------------------------------------------------------------

background = Label(app, image=animation1,height='500',width='500')
death_back=PhotoImage(file='images/death_back.gif')
death_background = Label(app, image=death_back,height='500',width='500')
background.place(x=0, y=0, relwidth=1, relheight=1)

#-----------------------------------------------------------------------------------------------
base_animation1=PhotoImage(file='images/Base_Animation1.gif')
base_animation2=PhotoImage(file='images/Base_Animation2.gif')
base_animation3=PhotoImage(file='images/Base_Animation3.gif')
base_animation4=PhotoImage(file='images/Base_Animation4.gif')
base_animation5=PhotoImage(file='images/Base_Animation5.gif')
base_animation6=PhotoImage(file='images/Base_Animation6.gif')
base_animation7=PhotoImage(file='images/Base_Animation7.gif')
base_animation8=PhotoImage(file='images/Base_Animation8.gif')
base_animation9=PhotoImage(file='images/Base_Animation9.gif')
base_animation10=PhotoImage(file='images/Base_Animation10.gif')
base_animation11=PhotoImage(file='images/Base_Animation11.gif')
base_animation=[base_animation1,base_animation2,base_animation3,base_animation4,base_animation5,base_animation6,base_animation7,base_animation8,
                base_animation9,base_animation10,base_animation11]
#-------------------------------------------------------------------------------------------------------------------------------------------------------
general_in1=PhotoImage(file='images/general_in1.gif')
general_in2=PhotoImage(file='images/general_in2.gif')
general_in3=PhotoImage(file='images/general_in3.gif')
general_in4=PhotoImage(file='images/general_in4.gif')
general_in5=PhotoImage(file='images/general_in5.gif')
general_in6=PhotoImage(file='images/general_in6.gif')
general_in7=PhotoImage(file='images/general_in7.gif')
general_in8=PhotoImage(file='images/general_in8.gif')
general_in9=PhotoImage(file='images/general_in9.gif')
general_in10=PhotoImage(file='images/general_in10.gif')
general_in11=PhotoImage(file='images/general_in11.gif')
general_in12=PhotoImage(file='images/general_in12.gif')
general_in13=PhotoImage(file='images/general_in13.gif')
general_in14=PhotoImage(file='images/general_in14.gif')
general_in15=PhotoImage(file='images/general_in15.gif')
general_in16=PhotoImage(file='images/general_in16.gif')
general_in=[general_in1,general_in2,general_in3,general_in4,general_in5,general_in6,general_in7,general_in8,general_in9,general_in10,
            general_in11,general_in12,general_in13,general_in14,general_in15,general_in16]

#-------------------------------------------------------------------------------------------------------------------------------------------------------
teen_1=PhotoImage(file='images/teen_1.gif')
teen_2=PhotoImage(file='images/teen_2.gif')
teen_3=PhotoImage(file='images/teen_3.gif')
teen_4=PhotoImage(file='images/teen_4.gif')
teen_5=PhotoImage(file='images/teen_5.gif')
teen_6=PhotoImage(file='images/teen_6.gif')
teen_7=PhotoImage(file='images/teen_7.gif')
teen_8=PhotoImage(file='images/teen_8.gif')
teen_9=PhotoImage(file='images/teen_9.gif')
teen_10=PhotoImage(file='images/teen_10.gif')
teen_11=PhotoImage(file='images/teen_11.gif')


teen=[teen_1,teen_2,teen_3,teen_4,teen_5,teen_6,teen_7,teen_8,teen_9,teen_10,
            teen_11]
#-------------------------------------------------------------------------

hp0=PhotoImage(file='images/hp0.gif')
hp1=PhotoImage(file='images/hp1.gif')
hp2=PhotoImage(file='images/hp2.gif')
hp3=PhotoImage(file='images/hp3.gif')
hp4=PhotoImage(file='images/hp4.gif')
hp5=PhotoImage(file='images/hp5.gif')
hp6=PhotoImage(file='images/hp6.gif')
hp7=PhotoImage(file='images/hp7.gif')
hp8=PhotoImage(file='images/hp8.gif')
hp9=PhotoImage(file='images/hp9.gif')
hp10=PhotoImage(file='images/hp10.gif')
hp11=PhotoImage(file='images/hp11.gif')
hp12=PhotoImage(file='images/hp12.gif')
hp13=PhotoImage(file='images/hp13.gif')
hp14=PhotoImage(file='images/hp14.gif')
hp15=PhotoImage(file='images/hp15.gif')
hp16=PhotoImage(file='images/hp16.gif')
hp17=PhotoImage(file='images/hp17.gif')
hp18=PhotoImage(file='images/hp18.gif')
hp19=PhotoImage(file='images/hp19.gif')
hp20=PhotoImage(file='images/hp20.gif')

hp=[hp0,hp1,hp2,hp3,hp4,hp5,hp6,hp7,hp8,hp9,hp10,hp11,hp12,hp13,hp14,hp15,
    hp16,hp17,hp18,hp19,hp20]
hp_current=hp[current]

#-------------------------------------------------------------------------
bhp0=PhotoImage(file='images/bhp0.gif')
bhp1=PhotoImage(file='images/bhp1.gif')
bhp2=PhotoImage(file='images/bhp2.gif')
bhp3=PhotoImage(file='images/bhp3.gif')
bhp4=PhotoImage(file='images/bhp4.gif')
bhp5=PhotoImage(file='images/bhp5.gif')
bhp6=PhotoImage(file='images/bhp6.gif')
bhp7=PhotoImage(file='images/bhp7.gif')
bhp8=PhotoImage(file='images/bhp8.gif')
bhp9=PhotoImage(file='images/bhp9.gif')
bhp10=PhotoImage(file='images/bhp10.gif')
bhp11=PhotoImage(file='images/bhp11.gif')
bhp12=PhotoImage(file='images/bhp12.gif')
bhp13=PhotoImage(file='images/bhp13.gif')
bhp14=PhotoImage(file='images/bhp14.gif')
bhp15=PhotoImage(file='images/bhp15.gif')
bhp16=PhotoImage(file='images/bhp16.gif')
bhp17=PhotoImage(file='images/bhp17.gif')
bhp18=PhotoImage(file='images/bhp18.gif')
bhp19=PhotoImage(file='images/bhp19.gif')
bhp20=PhotoImage(file='images/bhp20.gif')
bhp21=PhotoImage(file='images/bhp21.gif')
bhp22=PhotoImage(file='images/bhp22.gif')
bhp23=PhotoImage(file='images/bhp23.gif')
bhp24=PhotoImage(file='images/bhp24.gif')
bhp25=PhotoImage(file='images/bhp25.gif')
bhp26=PhotoImage(file='images/bhp26.gif')
bhp27=PhotoImage(file='images/bhp27.gif')
bhp28=PhotoImage(file='images/bhp28.gif')
bhp29=PhotoImage(file='images/bhp29.gif')
bhp30=PhotoImage(file='images/bhp30.gif')
bhp30=PhotoImage(file='images/bhp30.gif')
bhp31=PhotoImage(file='images/bhp31.gif')
bhp32=PhotoImage(file='images/bhp32.gif')
bhp33=PhotoImage(file='images/bhp33.gif')
bhp34=PhotoImage(file='images/bhp34.gif')
bhp35=PhotoImage(file='images/bhp35.gif')
bhp36=PhotoImage(file='images/bhp36.gif')
bhp37=PhotoImage(file='images/bhp37.gif')
bhp38=PhotoImage(file='images/bhp38.gif')
bhp39=PhotoImage(file='images/bhp39.gif')
bhp40=PhotoImage(file='images/bhp40.gif')
bhp=[bhp0,bhp1,bhp2,bhp3,bhp4,bhp5,bhp6,bhp7,bhp8,bhp9,bhp10,bhp11,bhp12,bhp13,bhp14,bhp15,
    bhp16,bhp17,bhp18,bhp19,bhp20,bhp21,bhp22,bhp23,bhp24,bhp25,bhp26,bhp27,bhp28,bhp29,
    bhp30,bhp31,bhp32,bhp33,bhp34,bhp35,bhp36,bhp37,bhp38,bhp39,bhp40]
bhp_current=bhp[bcurrent]

action_image=PhotoImage(file='images/back3.gif')
button=PhotoImage(file='images/back2.gif')


ashe_in1=PhotoImage(file='images/ashe_in1.gif')
ashe_in2=PhotoImage(file='images/ashe_in2.gif')
ashe_in3=PhotoImage(file='images/ashe_in3.gif')
ashe_in4=PhotoImage(file='images/ashe_in4.gif')
ashe_in5=PhotoImage(file='images/ashe_in5.gif')
ashe_in=[ashe_in1,ashe_in2,ashe_in3,ashe_in4,ashe_in5]

ashe_transin1=PhotoImage(file='images/ashe_transin_1.gif')
ashe_transin2=PhotoImage(file='images/ashe_transin_2.gif')
ashe_transin3=PhotoImage(file='images/ashe_transin_3.gif')
ashe_transin4=PhotoImage(file='images/ashe_transin_4.gif')
ashe_transin5=PhotoImage(file='images/ashe_transin_5.gif')
ashe_transin6=PhotoImage(file='images/ashe_transin_6.gif')
ashe_transin7=PhotoImage(file='images/ashe_transin_7.gif')
ashe_transin=[ashe_transin1,ashe_transin2,ashe_transin3,ashe_transin4,ashe_transin5,ashe_transin6,ashe_transin7]

ashe_out1=PhotoImage(file='images/ashe_out1.gif')
ashe_out2=PhotoImage(file='images/ashe_out2.gif')
ashe_out3=PhotoImage(file='images/ashe_out3.gif')
ashe_out4=PhotoImage(file='images/ashe_out4.gif')
ashe_out5=PhotoImage(file='images/ashe_out5.gif')
ashe_out6=PhotoImage(file='images/ashe_out6.gif')
ashe_out7=PhotoImage(file='images/ashe_out7.gif')
ashe_out=[ashe_out1,ashe_out2,ashe_out3,ashe_out4,ashe_out5,ashe_out6,ashe_out7]

ashe_gone1=PhotoImage(file='images/Ashe_gone1.gif')
ashe_gone2=PhotoImage(file='images/Ashe_gone2.gif')
ashe_gone3=PhotoImage(file='images/Ashe_gone3.gif')
ashe_gone4=PhotoImage(file='images/Ashe_gone4.gif')
ashe_gone5=PhotoImage(file='images/Ashe_gone5.gif')
ashe_gone=[ashe_gone1,ashe_gone2,ashe_gone3,ashe_gone4,ashe_gone5]

trancer_in1=PhotoImage(file='images/trancer_in1.gif')
trancer_in2=PhotoImage(file='images/trancer_in2.gif')
trancer_in3=PhotoImage(file='images/trancer_in3.gif')
trancer_in4=PhotoImage(file='images/trancer_in4.gif')
trancer_in=[trancer_in1,trancer_in2,trancer_in3,trancer_in4]

trancer_transin1=PhotoImage(file='images/trancer_transin_1.gif')
trancer_transin2=PhotoImage(file='images/trancer_transin_2.gif')
trancer_transin3=PhotoImage(file='images/trancer_transin_3.gif')
trancer_transin4=PhotoImage(file='images/trancer_transin_4.gif')
trancer_transin5=PhotoImage(file='images/trancer_transin_5.gif')
trancer_transin6=PhotoImage(file='images/trancer_transin_6.gif')
trancer_transin7=PhotoImage(file='images/trancer_transin_7.gif')
trancer_transin=[trancer_transin1,trancer_transin2,trancer_transin3,trancer_transin4,trancer_transin5,trancer_transin6,trancer_transin7]

trancer_out1=PhotoImage(file='images/trancer_out1.gif')
trancer_out2=PhotoImage(file='images/trancer_out2.gif')
trancer_out3=PhotoImage(file='images/trancer_out3.gif')
trancer_out4=PhotoImage(file='images/trancer_out4.gif')
trancer_out5=PhotoImage(file='images/trancer_out5.gif')
trancer_out6=PhotoImage(file='images/trancer_out6.gif')
trancer_out7=PhotoImage(file='images/trancer_out7.gif')
trancer_out=[trancer_out1,trancer_out2,trancer_out3,trancer_out4,trancer_out5,trancer_out6,trancer_out7]

trancer_gone1=PhotoImage(file='images/trancer_gone1.gif')
trancer_gone2=PhotoImage(file='images/trancer_gone2.gif')
trancer_gone3=PhotoImage(file='images/trancer_gone3.gif')
trancer_gone4=PhotoImage(file='images/trancer_gone4.gif')

trancer_gone=[trancer_gone1,trancer_gone2,trancer_gone3,trancer_gone4]

korino_in1=PhotoImage(file='images/korino_in1.gif')
korino_in2=PhotoImage(file='images/korino_in2.gif')
korino_in3=PhotoImage(file='images/korino_in3.gif')
korino_in4=PhotoImage(file='images/korino_in4.gif')
korino_in5=PhotoImage(file='images/korino_in5.gif')
korino_in=[korino_in1,korino_in2,korino_in3,korino_in4,korino_in5]

korino_transin1=PhotoImage(file='images/korino_transin_1.gif')
korino_transin2=PhotoImage(file='images/korino_transin_2.gif')
korino_transin3=PhotoImage(file='images/korino_transin_3.gif')
korino_transin4=PhotoImage(file='images/korino_transin_4.gif')
korino_transin5=PhotoImage(file='images/korino_transin_5.gif')
korino_transin6=PhotoImage(file='images/korino_transin_6.gif')
korino_transin=[korino_transin1,korino_transin2,korino_transin3,korino_transin4,korino_transin5,korino_transin6]

korino_out1=PhotoImage(file='images/korino_out1.gif')
korino_out2=PhotoImage(file='images/korino_out2.gif')
korino_out3=PhotoImage(file='images/korino_out3.gif')
korino_out4=PhotoImage(file='images/korino_out4.gif')
korino_out5=PhotoImage(file='images/korino_out5.gif')
korino_out6=PhotoImage(file='images/korino_out6.gif')
korino_out7=PhotoImage(file='images/korino_out7.gif')
korino_out8=PhotoImage(file='images/korino_out8.gif')
korino_out9=PhotoImage(file='images/korino_out9.gif')
korino_out10=PhotoImage(file='images/korino_out10.gif')
korino_out11=PhotoImage(file='images/korino_out11.gif')
korino_out12=PhotoImage(file='images/korino_out12.gif')
korino_out13=PhotoImage(file='images/korino_out13.gif')
korino_out14=PhotoImage(file='images/korino_out14.gif')
korino_out15=PhotoImage(file='images/korino_out15.gif')
korino_out16=PhotoImage(file='images/korino_out16.gif')
korino_out17=PhotoImage(file='images/korino_out17.gif')
korino_out18=PhotoImage(file='images/korino_out18.gif')
korino_out19=PhotoImage(file='images/korino_out19.gif')
korino_out20=PhotoImage(file='images/korino_out20.gif')
korino_out21=PhotoImage(file='images/korino_out21.gif')

korino_out=[korino_out1,korino_out2,korino_out3,korino_out4,korino_out5,korino_out6,korino_out7,korino_out8,korino_out9,
                korino_out10,korino_out11,korino_out12,korino_out13,korino_out14,korino_out15,korino_out16,korino_out17,korino_out18,
                korino_out19,korino_out20,korino_out21]


korino_gone1=PhotoImage(file='images/korino_gone1.gif')
korino_gone2=PhotoImage(file='images/korino_gone2.gif')
korino_gone3=PhotoImage(file='images/korino_gone3.gif')
korino_gone4=PhotoImage(file='images/korino_gone4.gif')
korino_gone5=PhotoImage(file='images/korino_gone5.gif')
korino_gone=[korino_gone1,korino_gone2,korino_gone3,korino_gone4,korino_gone5]

emperor_in1=PhotoImage(file='images/emperor_in1.gif')
emperor_in2=PhotoImage(file='images/emperor_in2.gif')
emperor_in3=PhotoImage(file='images/emperor_in3.gif')
emperor_in4=PhotoImage(file='images/emperor_in4.gif')
emperor_in5=PhotoImage(file='images/emperor_in5.gif')
emperor_in6=PhotoImage(file='images/emperor_in6.gif')
emperor_in7=PhotoImage(file='images/emperor_in7.gif')
emperor_in8=PhotoImage(file='images/emperor_in8.gif')
emperor_in9=PhotoImage(file='images/emperor_in9.gif')
emperor_in10=PhotoImage(file='images/emperor_in10.gif')
emperor_in=[emperor_in1,emperor_in2,emperor_in3,emperor_in4,emperor_in5,emperor_in6,emperor_in7,emperor_in8,emperor_in9,emperor_in10]

emperor_transin1=PhotoImage(file='images/emperor_transin_1.gif')
emperor_transin2=PhotoImage(file='images/emperor_transin_2.gif')
emperor_transin3=PhotoImage(file='images/emperor_transin_3.gif')
emperor_transin4=PhotoImage(file='images/emperor_transin_4.gif')
emperor_transin5=PhotoImage(file='images/emperor_transin_5.gif')
emperor_transin6=PhotoImage(file='images/emperor_transin_6.gif')
emperor_transin7=PhotoImage(file='images/emperor_transin_7.gif')
emperor_transin8=PhotoImage(file='images/emperor_transin_8.gif')
emperor_transin9=PhotoImage(file='images/emperor_transin_9.gif')
emperor_transin=[emperor_transin1,emperor_transin2,emperor_transin3,emperor_transin4,emperor_transin5,emperor_transin6,emperor_transin7,emperor_transin8,emperor_transin9]

emperor_out1=PhotoImage(file='images/emperor_out_1.gif')
emperor_out2=PhotoImage(file='images/emperor_out_2.gif')
emperor_out3=PhotoImage(file='images/emperor_out_3.gif')
emperor_out4=PhotoImage(file='images/emperor_out_4.gif')
emperor_out5=PhotoImage(file='images/emperor_out_5.gif')
emperor_out6=PhotoImage(file='images/emperor_out_6.gif')
emperor_out7=PhotoImage(file='images/emperor_out_7.gif')
emperor_out8=PhotoImage(file='images/emperor_out_8.gif')
emperor_out9=PhotoImage(file='images/emperor_out_9.gif')
emperor_out10=PhotoImage(file='images/emperor_out_10.gif')
emperor_out11=PhotoImage(file='images/emperor_out_11.gif')
emperor_out12=PhotoImage(file='images/emperor_out_12.gif')
emperor_out13=PhotoImage(file='images/emperor_out_13.gif')
emperor_out14=PhotoImage(file='images/emperor_out_14.gif')
emperor_out15=PhotoImage(file='images/emperor_out_15.gif')
emperor_out16=PhotoImage(file='images/emperor_out_16.gif')
emperor_out=[emperor_out1,emperor_out2,emperor_out3,emperor_out4,emperor_out5,emperor_out6,emperor_out7,emperor_out8,emperor_out9,
             emperor_out10,emperor_out11,emperor_out12,emperor_out13,emperor_out14,emperor_out15,emperor_out16]

emperor_gone1=PhotoImage(file='images/emperor_gone_1.gif')
emperor_gone2=PhotoImage(file='images/emperor_gone_2.gif')
emperor_gone3=PhotoImage(file='images/emperor_gone_3.gif')
emperor_gone4=PhotoImage(file='images/emperor_gone_4.gif')
emperor_gone5=PhotoImage(file='images/emperor_gone_5.gif')
emperor_gone6=PhotoImage(file='images/emperor_gone_6.gif')
emperor_gone7=PhotoImage(file='images/emperor_gone_7.gif')
emperor_gone=[emperor_gone1,emperor_gone2,emperor_gone3,emperor_gone4,emperor_gone5,emperor_gone6,emperor_gone7]

frame1=Frame(app,width=500,height=60)
frame2=Frame(frame1,width=250,height=60)

frame3=Frame(frame1,width=250,height=60)

action=Label(app,text="", image=action_image,
           justify=LEFT,
           compound=CENTER,
            wraplength=500,height=23,
           font=("System", 14))

frame4=Frame(app,width=500,height=65, background="black")

frame5=Frame(frame4,width=15,background="black")

frame6=Frame(frame4,width=15,background="black")
def general_ina():
    global general_in_frame
    if general_in_frame!=16:
        
        background.configure(image=general_in[general_in_frame])
        general_in_frame=general_in_frame+1
        
        app.after(40,general_ina)
def base_animationa():
    global base_animation_frame
    if base_animation_frame!=11:
        
        background.configure(image=base_animation[base_animation_frame])
        base_animation_frame=base_animation_frame+1
        
        app.after(40,base_animationa)
def animationa():
    global animation_frame
    if animation_frame!=15:
        
        background.configure(image=animation[animation_frame])
        animation_frame=animation_frame+1
       
        app.after(40,animationa)
def teena():
    global teen_frame
    if teen_frame!=11:
        
        background.configure(image=teen[teen_frame])
        teen_frame=teen_frame+1
        
        app.after(40,teena)
def ashe_gonea():
    global ashe_gone_frame
    if ashe_gone_frame!=5:
        
        background.configure(image=ashe_gone[ashe_gone_frame])
        ashe_gone_frame=ashe_gone_frame+1
        
        app.after(40,ashe_gonea)
      
def ashe_trans_ina():
    global ashe_transin_frame
    if ashe_transin_frame!=7:
        
        background.configure(image=ashe_transin[ashe_transin_frame])
        ashe_transin_frame=ashe_transin_frame+1
        app.after(40,ashe_trans_ina)
        
def ashe_ina():
    global ashe_in_frame
    if ashe_in_frame!=5:
        
        background.configure(image=ashe_in[ashe_in_frame])
        ashe_in_frame=ashe_in_frame+1
       
        app.after(40,ashe_ina)
def ashe_outa():
    global ashe_out_frame
    global Fade
    if ashe_out_frame!=7:
        
        background.configure(image=ashe_out[ashe_out_frame])
        ashe_out_frame=ashe_out_frame+1
     
        app.after(40,ashe_outa)
    else:
        Fade=False
        win_fight()
def trancer_gonea():
    global trancer_gone_frame
    if trancer_gone_frame!=4:
        
        background.configure(image=trancer_gone[trancer_gone_frame])
        trancer_gone_frame=trancer_gone_frame+1
     
        app.after(40,trancer_gonea)
      
def trancer_trans_ina():
    global trancer_transin_frame
    if trancer_transin_frame!=7:
        
        background.configure(image=trancer_transin[trancer_transin_frame])
        trancer_transin_frame=trancer_transin_frame+1
        app.after(40,trancer_trans_ina)
        
def trancer_ina():
    global trancer_in_frame
    if trancer_in_frame!=4:
        
        background.configure(image=trancer_in[trancer_in_frame])
        trancer_in_frame=trancer_in_frame+1
        app.after(40,trancer_ina)

def trancer_outa():
    global trancer_out_frame
    global Fade
    if trancer_out_frame!=7:
        
        background.configure(image=trancer_out[trancer_out_frame])
        trancer_out_frame=trancer_out_frame+1
        app.after(40,trancer_outa)
    else:
        Fade=False
        win_fight()
def korino_gonea():
    global korino_gone_frame
    
    if korino_gone_frame!=5:
        
        background.configure(image=korino_gone[korino_gone_frame])
        korino_gone_frame=korino_gone_frame+1
        app.after(40,korino_gonea)
      
def korino_trans_ina():
    global korino_transin_frame
    if korino_transin_frame!=6:
        
        background.configure(image=korino_transin[korino_transin_frame])
        korino_transin_frame=korino_transin_frame+1
        
        app.after(40,korino_trans_ina)
        
def korino_ina():
    global korino_in_frame
    if korino_in_frame!=5:
        
        background.configure(image=korino_in[korino_in_frame])
        korino_in_frame=korino_in_frame+1
        app.after(40,korino_ina)
def korino_outa():
    global korino_out_frame
    global Fade
    if korino_out_frame!=21:
        
        background.configure(image=korino_out[korino_out_frame])
        korino_out_frame=korino_out_frame+1
        app.after(10,korino_outa)
    else:
        Fade=False
        win_fight()
def emperor_gonea():
    global emperor_gone_frame
    if emperor_gone_frame!=7:
        
        background.configure(image=emperor_gone[emperor_gone_frame])
        emperor_gone_frame=emperor_gone_frame+1
        app.after(40,emperor_gonea)
      
def emperor_trans_ina():
    global emperor_transin_frame
    if emperor_transin_frame!=9:
        
        background.configure(image=emperor_transin[emperor_transin_frame])
        emperor_transin_frame=emperor_transin_frame+1
        app.after(40,emperor_trans_ina)
        
def emperor_ina():
    global emperor_in_frame
    if emperor_in_frame!=10:
        
        background.configure(image=emperor_in[emperor_in_frame])
        emperor_in_frame=emperor_in_frame+1
        app.after(40,emperor_ina)
def emperor_outa():
    global emperor_out_frame
    global Fade
    if emperor_out_frame!=16:
        
        background.configure(image=emperor_out[emperor_out_frame])
        emperor_out_frame=emperor_out_frame+1
        app.after(40,emperor_outa)
    else:
        Fade=False
        win_fight()
def win_fight():
    global quote_sample
    global quote_num
    global Fade
    text1(quote_sample)
    
    if enemy=='Trancer':
        if Fade== True:
            
            trancer_outa()
        if Fade==False:
            boss_music.stop()
            general_cont.play()
            unpack_everything()
            repack()
            Fight=False
            namebox.configure(text='Leader')
            
            namebox.pack(side='bottom')
            trancer_gonea()
            Fade=True
    if enemy=='Ashe':
        if Fade== True:
            ashe_outa()
        if Fade==False:
            boss_music.stop()
            general_cont.play()
            unpack_everything()
            repack()
            Fight=False
            namebox.configure(text='Leader')
            
            namebox.pack(side='bottom')
        
            ashe_gonea()
            Fade=True
    
    if enemy=="Fake_Korino":
        boss_music.stop()
        namebox.pack(side='bottom')
        background.configure(image=korino_in5)
    if enemy=="Korino":
        if Fade== True:
            korino_outa()
        if Fade==False:
            boss_music.stop()
            general_cont.play()
            unpack_everything()
            repack()
            Fight=False
            namebox.pack(side='bottom')
            korino_gonea()
            Fade=True
    if enemy=='Emperor':
        emperor_death.play()
        if Fade== True:
            emperor_outa()
        if Fade==False:
            unpack_everything()
            repack()
            Fight=False
            namebox.pack_forget()
            emperor_gonea()
            Fade=True
            emperor_music.stop()
        win_game=True
        
def lose():
    unpack_everything()
    background.place_forget()
    death_background.place(x=0, y=0, relwidth=1, relheight=1)
    l1.configure(text="You have lost against " + enemy+".")
    l1.pack(side='bottom')
    b_loss.pack(side='bottom')
    boss_music.stop()
    emperor_music.stop()
    l_loss.configure(text="You have lost against " + enemy)
   
def pack_everything():
    
    global your_turn
    global Fight
    

    
    frame1.pack(side='bottom')
    frame2.pack(side='left')
    frame3.pack(side='right')

    frame4.pack(side='bottom',fill='x')
    frame5.pack(side='left')
    frame6.pack(side='right')
    action.pack(side='bottom')
    b1.pack(side='top')
    b2.pack(side='top')
    b3.pack(side='bottom')
    b4.pack(side='bottom')
    hp_image.pack(side='left')
    bhp_image.pack(side='right')
    your_turn=True
    Fight=True
def fake_pack_everything():
    global your_turn
    global Fight
    

    
    frame1.pack(side='bottom')
    frame2.pack(side='left')
    frame3.pack(side='right')

    frame4.pack(side='bottom',fill='x')
    frame5.pack(side='left')
    frame6.pack(side='right')
    action.pack(side='bottom')
    fakeb1.pack(side='top')
    fakeb2.pack(side='top')
    fakeb3.pack(side='bottom')
    fakeb4.pack(side='bottom')
    hp_image.pack(side='left')
    bhp_image.pack(side='right')
    your_turn=True
    Fight=True
def unpack_everything():
    global bcurrent
    action.pack_forget()
    b1.pack_forget()
    b2.pack_forget()
    b3.pack_forget()
    b4.pack_forget()
    hp_image.pack_forget()
    bhp_image.pack_forget()
    frame1.pack_forget()
    frame2.pack_forget()
    frame3.pack_forget()
    frame4.pack_forget()
    frame5.pack_forget()
    frame6.pack_forget()



bhp_image=Label(frame4,image=bhp_current,width=225,height=58)
hp_image=Label(frame4,image=hp_current,width=225,height=58)
def enemy_trancer():
    global bcurrent
    global current
    global enemy
    general_start.stop()
    boss_music.play()
    enemy="Trancer"
    action.configure(text="Trancer is ready to fight")
    bcurrent=10
    current=20
    hp_image.configure(image=hp[current])
    bhp_image.configure(image=bhp[bcurrent])
    
    trancer_trans_ina()
    unpack()                  
    
def enemy_ashe():
    global bcurrent
    global current
    global enemy
    global stun
    general_cont.stop()
    boss_music.play()
    stun=0
    enemy="Ashe"
    action.configure(text="Ashe is ready to fight")
    bcurrent=20
    current=20
    hp_image.configure(image=hp[current])
    bhp_image.configure(image=bhp[bcurrent])
    ashe_trans_ina()
    unpack()
def enemy_korino():
    global bcurrent
    global current
    global enemy
    global korino_transin_frame
    enemy="Korino"
    action.configure(text="Korino is ready to fight")
    bcurrent=30
    current=20
    boss_music.play()
    hp_image.configure(image=hp[current])
    bhp_image.configure(image=bhp[bcurrent])
    korino_transin_frame=0
    korino_trans_ina()
    unpack()
def fake_enemy_korino():
    global bcurrent
    global current
    global enemy
    general_cont.stop()
    boss_music.play()
    enemy="Fake_Korino"
    action.configure(text="Korino is ready to fight")
    bcurrent=30
    current=20
    hp_image.configure(image=hp[current])
    bhp_image.configure(image=bhp[bcurrent])
    korino_trans_ina()
    l1.pack_forget()
    
    namebox.pack_forget()
    fake_pack_everything()
def enemy_fuhrer():
    global bcurrent
    global current
    global enemy
    global revivecount
    revivecount=0
    enemy="Emperor"
    action.configure(text="You face the Emperor")
    bcurrent=40
    current=20
    hp_image.configure(image=hp[current])
    bhp_image.configure(image=bhp[bcurrent])
   
    emperor_trans_ina()
    unpack()
def punch_prep():
    global your_turn
    if your_turn==True:
        global dmg
        action.configure(text="Punch: Deal 3 damage")
        your_turn=False
        dmg=3
        punch()
        punch_sound.play()
def punch():
    global bcurrent
    global bhp_current
    global bhp
    global dmg
    global revivecount
    if dmg>0:
        
        dmg=dmg-1
        bcurrent=bcurrent-1
        bhp_image.configure(image=bhp[bcurrent])

        
        if bcurrent>0:
            app.after(40,punch)
        else:
            if enemy=="Emperor":
                
                if revivecount==0:
                    revivecount=revivecount+1
                    action.configure(text="Emperor: I AM UNDEFEATABLE!")
                    revive()
                elif revivecount==1:
                    revivecount=revivecount+1
                    action.configure(text="Emperor: YOU'LL NEVER KILL ME!")
                    revive()
                elif revivecount==2:
                    revivecount=revivecount+1
                    action.configure(text="Emperor: NO! I AM IMMORTAL! I AM A GOD!")
                    revive()
                else:
                    
                    
                    win_fight()
    
            else:
                
                win_fight()
    else:
        app.after(750,enemy_turn())

def heal_prep():
    global your_turn
    if your_turn==True:
        global dmg
        action.configure(text="Heal: Recover 6 health")
        your_turn=False
        dmg=6
        heal()
        heal_sound.play()
def heal():
    global current
    global hp_current
    global hp
    global dmg
    if current==20:
        app.after(1000,enemy_turn())
    else:
        if dmg>0:
            
            dmg=dmg-1
            current=current+1
            hp_image.configure(image=hp[current])
            
            app.after(40,heal)
            
        else:
            app.after(750,enemy_turn())
def kick_prep():
    global your_turn
    

    if your_turn==True:
        global dmg
        action.configure(text="Kick: Deal 5 damage")
        your_turn=False
        dmg=5
        kick()
        kick_sound.play()
def kick():
    global bcurrent
    global bhp_current
    global bhp
    global dmg
    global revivecount
    if dmg>0:
        
        dmg=dmg-1
        bcurrent=bcurrent-1
        bhp_image.configure(image=bhp[bcurrent])
        if bcurrent>0:
            app.after(40,kick)
        else:
            if enemy=="Emperor":
                
                if revivecount==0:
                    revivecount=revivecount+1
                    action.configure(text="Emperor: I AM UNDEFEATABLE!")
                    revive()
                elif revivecount==1:
                    revivecount=revivecount+1
                    action.configure(text="Emperor: YOU'LL NEVER KILL ME!")
                    revive()
                elif revivecount==2:
                    revivecount=revivecount+1
                    action.configure(text="Emperor: NO! I AM IMMORTAL! I AM A GOD!")
                    revive()
                else:
                   
                    win_fight()
    
            else:
              
                win_fight()
    else:
        app.after(750,enemy_turn())
def revive():
    global bcurrent
    if bcurrent !=40:
        bcurrent=bcurrent+1
        bhp_image.configure(image=bhp[bcurrent])
            
        app.after(40,revive)
    else:
        app.after(750,enemy_turn())
def run():
    action.configure(text="Running is for losers")
def trancer_attack_prep():
        global dmg
        action.configure(text="Trancer attacks for 2 dmg")
        
        dmg=2
        trancer_attack()
def trancer_attack():
    global current
    global hp_current
    global hp
    global dmg
    global your_turn
    if dmg>0:
        
        dmg=dmg-1
        current=current-1
        hp_image.configure(image=hp[current])
        if current==0:
            lose()
        else:
            app.after(40,trancer_attack)
        
    else:
        
        your_turn=True
def ashe_attack_prep():
        global dmg
        action.configure(text="Ashe attacks for 2 dmg")
        
        dmg=2
        ashe_attack()
def ashe_attack():
    global current
    global hp_current
    global hp
    global dmg
    global your_turn
    if dmg>0:
        
        dmg=dmg-1
        current=current-1
        hp_image.configure(image=hp[current])
        if current==0:
            lose()
        else:
            app.after(40,ashe_attack)
        
    else:
        your_turn=True
def ashe_stun_prep():
        global dmg
        action.configure(text="Ashe attacks for 2 dmg and stuns")
        
        dmg=2
        ashe_stun()
def ashe_stun():
    global current
    global hp_current
    global hp
    global dmg
    global your_turn
    if dmg>0:
        
        dmg=dmg-1
        current=current-1
        hp_image.configure(image=hp[current])
        if current==0:
            lose()
        else:
            app.after(40,ashe_stun)
        
    else:
        app.after(2500,enemy_turn())
def korino_attack_prep():
        global dmg
        action.configure(text="Korino attacks for 5 dmg")
        
        dmg=5
        korino_attack()
def korino_attack():
    global current
    global hp_current
    global hp
    global dmg
    global your_turn
    if dmg>0:
        
        dmg=dmg-1
        current=current-1
        hp_image.configure(image=hp[current])
        if current==0:
            lose()
        else:
            app.after(40,korino_attack)
        
    else:
        your_turn=True
def laser():
    emperor_laser.play()
def fuhrer_attack_prep():
        global dmg
        
        action.configure(text="Emperor attacks for 4 dmg")
        app.after(100,laser)
        dmg=4
        fuhrer_attack()
def fuhrer_attack():
    global current
    global hp_current
    global your_turn
    global hp
    global dmg
    if dmg>0:
        
        dmg=dmg-1
        current=current-1
        hp_image.configure(image=hp[current])
        if current==0:
            lose()
        else:
            app.after(40,fuhrer_attack)
        
    else:
        your_turn=True
def fake():
    fakeb1.pack_forget()
    fakeb2.pack_forget()
    fakeb3.pack_forget()
    fakeb4.pack_forget()
    unpack_everything()
    repack()
    Fight=False
    text1(quote_sample)
    
    win_fight()
def enemy_turn():
    global stun
    global dmg
    if enemy=='Trancer':
        trancer_attack_prep()
    if enemy=='Ashe':
        if stun==3:
            stun=0
            ashe_stun_prep()
        else:
            stun=stun+1
            ashe_attack_prep()
    if enemy=='Korino':
        korino_attack_prep()
    if enemy=='Emperor':
        fuhrer_attack_prep()
b1=Button(frame2,text='Punch',command=punch_prep,image=button,compound=CENTER,width=250,height=23)
b2=Button(frame3,text='Heal',command=heal_prep,image=button,compound=CENTER,width=250,height=23)
b3=Button(frame2,text='Kick',command=kick_prep,image=button,compound=CENTER,width=250,height=23)
b4=Button(frame3,text='Run',command=run,image=button,compound=CENTER,width=250,height=23)
fakeb1=Button(frame2,text='Punch',command=fake,image=button,compound=CENTER,width=240,height=23)
fakeb2=Button(frame3,text='Heal',command=fake,image=button,compound=CENTER,width=240,height=23)
fakeb3=Button(frame2,text='Kick',command=fake,image=button,compound=CENTER,width=240,height=23)
fakeb4=Button(frame3,text='Run',command=fake,image=button,compound=CENTER,width=240,height=23)
#------------------------------------------------------------------------------------------------

def unpack():
    

    l1.pack_forget()
    
    namebox.pack_forget()
    pack_everything()
def repack():
    global Fight
    background.place(x=0, y=0, relwidth=1, relheight=1)
  
    l1.pack(side='bottom')
    
    
    
    if quote_num in no_speakers:
        example=1
    else:
        namebox.pack(side='bottom')
    Fight=False
def text1(quote):
    global example
    global num
    global quote_num
    global quotes
    global quote_sample
    if example==1: #start playing text
        
        example=2
        fill(quote)
    elif example==2: #finish playing text
        
        example=3
        l1.configure(text=quote)
        num = len(quote)+1
        example=3
    elif example==3: #advance to next text
        quote_num=quote_num+1
        num=0
        example=1
        quote_sample=quotes[quote_num]
        text1(quote_sample)
def fill(text):
    global num
    global example
    if num== len(text)+1:
        example=3
    elif num < len(text)+1:
        
        word=text[0:num]
        num=num+1
        l1.configure(text=word)
        app.after(19,s1)
    
def s1():
    fill(quote_sample)

def keypress(event):
    global quote_sample
    global stop
    global Fight
    global quote_num
    global win_game
    global korino_transin_frame
    global general_in_frame
    global sample
    global sample2
    x = event.char
    if Fight==False:
        if stop==True:
            meh=1
        elif x == "z":
            if win_game==True:
                example=1
            if win_game==False:
                
                text1(quotes[quote_num])
               
                
                
                if quote_num==0:
                    background.configure(image = animation1)
                if quote_num==1:
                    if sample==1:
                        intro.play()
                        sample=2
                if quote_num==2:
                    teena()
                    
                if quote_num==5:
                    base_animationa()
                if quote_num==6:
                    intro.stop()
                    if sample2==1:
                        general_ina()
                        general_start.play()
                        sample2=2
                if quote_num==7:
                    namebox.pack(side='bottom')
                    namebox.configure(text='General')
                if quote_num==11:
                    trancer_ina()
                    
                    namebox.configure(text='Trancer')
                if quote_num==12:
                    namebox.pack_forget()
                    enemy_trancer()
                    
                if quote_num==13:
                    namebox.pack(side='bottom')
                    namebox.configure(text='Leader')
                if quote_num==15:
                    
                    namebox.configure(text='???')
                if quote_num==16:
                    namebox.configure(text='Ashe')
                    ashe_ina()
                if quote_num==17:
                    
                    namebox.pack_forget()
                    enemy_ashe()
                    
                if quote_num==18:
                    namebox.pack(side='bottom')
                    
                    namebox.configure(text='Leader')
                if quote_num==20:
                    
                    korino_ina()
                    namebox.configure(text='???')
                if quote_num==21:
                    
                    namebox.configure(text='Leader')
                if quote_num==22:
                    
                    namebox.configure(text='???')
                
                if quote_num==25:
                    
                    namebox.configure(text='Korino')
                if quote_num==26:
                    
                    namebox.pack_forget()
                    fake_enemy_korino()
                if quote_num==27:
                    
                    namebox.pack(side="bottom")
                if quote_num==31:
                    
                    namebox.pack_forget()
                    enemy_korino()
                    
                    
                if quote_num==33:
                    
                    namebox.configure(text='General')
                    namebox.pack(side="bottom")
                    
                    
               
                    
                if quote_num==34:
                    general_in_frame=0
                    general_ina()
                if quote_num==36:
                    
                    namebox.configure(text='???')
                if quote_num==37:
                    background.configure(image = stab)
                    general_cont.stop()
                    emperor_music.play()
                    stab_sound.play()
                    namebox.configure(text='Emperor')
                if quote_num==38:
                    emperor_ina()
                if quote_num==40:
                    
                    namebox.pack_forget()
                    enemy_fuhrer()
                if quote_num==42:
                    
                    win_game=True
                    win_music.play()
                
                
app.geometry('500x500')


textbox_image=PhotoImage(file="images/back.gif")
namebox_image=PhotoImage(file="images/back1.gif")
app.bind_all('<KeyRelease>', keypress)





def retry():
    global trancer_transin_frame
    global ashe_transin_frame
    global korino_transin_frame
    global emperor_transin_frame
    trancer_transin_frame=0
    ashe_transin_frame=0
    korino_transin_frame=0
    if enemy=="Trancer":
        enemy_trancer()
        boss_music.play()
        trancer_trans_ina()
    if enemy=="Ashe":
        enemy_ashe()
        boss_music.play()
        ashe_trans_ina()
    if enemy=="Korino":
        korino_transin_frame=0
        enemy_korino()
        boss_music.play()
        korino_trans_ina()
    if enemy=="Emperor":
        emperor_transin_frame=0
        enemy_fuhrer()
        emperor_music.play()
    death_background.place_forget()
    background.place(x=0, y=0, relwidth=1, relheight=1)
    l1.pack_forget()
    b_loss.pack_forget()
    
def replay():
    
    variables()
    replay_button.pack_forget()
    background.configure(image = animation1)
    l1.configure(text="Press 'z' to advance text")
l1 = Label(app,text="Press 'z' to advance text", image=textbox_image,
   height='145',width='500',
   justify=LEFT,
   compound=CENTER,wraplength=480,
   
   font=("System", 20))
l1.pack(side='bottom')



l_loss=Label(app,text="You have lost against" + enemy)
b_loss=Button(app,text="Try again?",command=retry,image=button,compound=CENTER,width=250,height=23)
namebox=Label(app,text='speaker',image=namebox_image,
   justify=LEFT,background='white',width='150',height='45',
   compound=CENTER,wraplength=480,
   
   font=("System", 17))
replay_button=Button(app,text="Replay?",command=replay,image=button,compound=CENTER,width=250,height=23)

f_loss=Frame(app,height=150)
l1.pack(side='bottom')
app.mainloop()
