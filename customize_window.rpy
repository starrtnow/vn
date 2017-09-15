init -100 python:
    style.say_who_window.yalign = 1.0 
    style.say_who_window.yoffset = 6
    style.say_who_window.background = Frame("effects/frame2.png", 4, 4)
    style.say_who_window.xpadding= 20
    style.say_who_window.ypadding= 4
    style.say_who_window.xminimum = 50
    style.say_who_window.left_margin = 10
    
    style.say_window.yalign = 1.0
    style.say_window.background= Frame("effects/frame2.png", 4, 4)
    style.say_window.xpadding=15
    style.say_window.ypadding= 6
    style.say_window.bottom_margin = 10
    style.say_window.xalign = 0.5
    style.say_window.xmargin = 20
    
    style.create("sproul_opening", 'say_window')
    style.sproul_opening.background = None
