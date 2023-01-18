from turtle import*
score_1 = 0
score_2 = 0

penup()

goto(-300,300)
write("ответы первого игрока", font = ("arial", 14, "normal") )
goto(-300,200)
write("ответы второго игрока", font = ("arial", 14, "normal") )
ans_1 = textinput("задание 1", "зимой и летом одним цветом")
if ans_1 == "1":
    res = "+"
    score_1 += 1
    goto(-300,280)
    write(res,font=("Arial",14, "normal") ) 
else:
    res = "x"
    goto(-300,280)
    write(res, font=("Arial",14, "normal") ) 

ans_2 = textinput("задание 2", "зимой и летом одним цветом")
if ans_2 == "1":
    res = "+"
    score_2 += 1
    goto(-300,180)
    write(res,font=("Arial",14, "normal") ) 
else:
    res = "x"
    goto(-300,180)
    write(res, font=("Arial",14, "normal") ) 


ans_1 = textinput("задание 2", "кто такой кОт")
if ans_1 == "1":
    res = "+"
    score_1 += 1
    goto(-300,280)
    write(res,font=("Arial",14, "normal") ) 
else:
    res = "x"
    goto(-300,280)
    write(res, font=("Arial",14, "normal") ) 

ans_2 = textinput("задание 1", "кто такой кОт")
if ans_2 == "1":
    res = "+"
    score_2 += 1
    goto(-300,180)
    write(res,font=("Arial",14, "normal") ) 
else:
    res = "x"
    goto(-300,180)
    write(res, font=("Arial",14, "normal") )



ans_1 = textinput("задание 3", "Сколько стволов было у Данте")
if ans_1 == "1":
    res = "+"
    score_1 += 1
    goto(-300,280)
    write(res,font=("Arial",14, "normal") ) 
else:
    res = "x"
    goto(-300,280)
    write(res, font=("Arial",14, "normal") ) 

ans_2 = textinput("задание 3", "Сколько стволов было у Данте")
if ans_2 == "1":
    res = "+"
    score_2 += 1
    goto(-300,180)
    write(res,font=("Arial",14, "normal") ) 
else:
    res = "x"
    goto(-300,180)
    write(res, font=("Arial",14, "normal") )



ans_1 = textinput("задание 4", "ты Слава Мэрлоу")
if ans_1 == "1":
    res = "+"
    score_1 += 1
    goto(-300,280)
    write(res,font=("Arial",14, "normal") ) 
else:
    res = "x"
    goto(-300,280)
    write(res, font=("Arial",14, "normal") ) 

ans_2 = textinput("задание 4", "зимой и летом одним цветом")
if ans_2 == "1":
    res = "+"
    score_2 += 1
    goto(-300,180)
    write(res,font=("Arial",14, "normal") ) 
else:
    res = "x"
    goto(-300,180)
    write(res, font=("Arial",14, "normal") )


ans_1 = textinput("задание 1", "зимой и летом одним цветом")
if ans_1 == "1":
    res = "+"
    score_1 += 1
    goto(-300,280)
    write(res,font=("Arial",14, "normal") ) 
else:
    res = "x"
    goto(-300,280)
    write(res, font=("Arial",14, "normal") ) 

ans_2 = textinput("задание 1", "зимой и летом одним цветом")
if ans_2 == "1":
    res = "+"
    score_2 += 1
    goto(-300,180)
    write(res,font=("Arial",14, "normal") ) 
else:
    res = "x"
    goto(-300,180)
    write(res, font=("Arial",14, "normal") )


    
if score_1 > score_2:
    goto(0,0)
    write("выиграл первый игрок",font=("Arial",14, "normal"))

elif score_1 == score_2:
    goto(0,0)
    write("ничья",font=("Arial",14, "normal"))
else:
    goto(0,0)
    write("выиграл второй игрок",font=("Arial",14, "normal"))


exitonclick()
