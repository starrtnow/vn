#Day 1
label hr_001:
    play music "music/normal_theme.ogg"
    $ hrel = 0
    scene bg outside 1 with fade
    "The summer has started. I should go check out that job."

label hr_005:
    scene bg haas mansion 1 with fade
    "WOW! That is one giant mansion!"

label hr_006:
    scene bg haas entrance 1 with fade
    show cheit maid happy 1 with dissolve
    c "Welcome to the Haas mansion."

label hr_007:
    "I SHOULD'VE KNOWN!!"
    pc "I'm here to apply for the butler position that runs for a week."

label hr_008:
    # show happy Cheit at left
    c "Please report back here at 7:00 AM tomorrow." 
    c "You'll be staying here at the mansion for next week." 
    c "Please don't be late. We'll see you tomorrow."
    scene bg black with fade

#Day 2

label hr_009:
    scene bg haas entrance 1 with fade
    show cheit maid happy 1 with dissolve
    menu:
        c "Welcome to your first day at the job. Your choice of the first chore of the day is one of the following."
        
        "Iron Haas's clothes":
            $ hrel = hrel + 3
        "Make breakfast":
            $ hrel = hrel + 2
        "Take out the trash":
            $ hrel = hrel + 1
            
label hr_011:
    with timeskip
    "Well, that was a lot of work, let's see what I have to do next."

label hr_012:
    show cheit maid happy 1 at left with move
    c "Our Mitsuki-sama will be down here to meet you in a second."
    "Finally..."

label hr_013:
    show haas casual sly 1 at right with dissolve
    pc "Is there anything I can do for you?"
    h "..."

label hr_014:
    hide haas with moveoutright
    show cheit maid happy 1 at center with move
    c "Our Mitsuki-sama is very happy to see you."

label hr_015:
    show cheit maid happy 1 at right with move
    c "We would like you to start prepare dinner."
    c "Please remember that Mitsuki-sama does not like to eat anything spicy or too salty."
    scene bg black with fade

    #Chiet and Haas exit

label hr_016:
    scene bg haas dining 1 with fade
    menu:
        "What should I cook?"
        "Mapo Tofu":
            $ hrel = hrel - 1
        "Chicken Curry":
            $ hrel = hrel + 1
        "Parmesan Chicken":
            $ hrel = hrel + 3

#After dinner
label hr_017:
    with timeskip
    show cheit maid happy 1 at right with dissolve
    c "Mitsuki-sama thanked you for your work for the day."
    c "Your work for the day is finished."
    c "You are welcome to go back to your room and rest for the day,"
    #Chiet exits
    scene bg black with timeskip

label hr_018:
    "Well, that was a tiring day."

label hr_019:
    # "AHHHHH" comes from Haas's room
    scene bg haas library 1 with fade
    Char('Voice') "AHHHHHHH!!!!!"
    "Wow! What was that?!"

label hr_020:
    menu:
        "Ignore":
            $ hrel = hrel + 0
            jump hr_021
        "Call for help":
            $ hrel = hrel + 1
            jump hr_022
        "Burst in":
            $ hrel = hrel + 2
            jump hr_023

# If choosing 1
label hr_021:
    "Guess I'll just go to sleep."
    scene bg black with timeskip
    jump hr_027

# If choosing 2
label hr_022:
    show cheit maid serious 1 with dissolve
    pc "Chiet! Is everything okay?!"
    c "Everything is fine. Please rest assure."
    scene bg black with timeskip
    jump hr_027

#If choosing 3
label hr_023:
    scene bg haas room 1 with fade
    pc "Is everything okay?!"

label hr_024:
    "Err... I see...."
    "Haas fell while changing..."
    
label hr_025:
    show haas casual annoyed 1 at right
    show cheit maid serious 1 at left
    with dissolve
    c "HOW DARE YOU!"
    "!!!"
    with hpunch
    "Ouch that slap hurt!"
    # Protagonist got slapped
    scene bg black with fade
    #exit Haas and Cheit
    
label hr_026:
    "Guess that's what I get for not knocking before entering..."
    scene bg black with timeskip
    #end of Choice 3

#Day 3
label hr_027:
    scene bg haas entrance 1 with fade
    "Ah, man. Have to get to work."
    menu:
        "What's this? List of chores...?"
        "Wash the bath tub":
            $ hrel = hrel + 1
        "Clean out all of the rain gutters":
            $ hrel = hrel + 2
        "Dust all the chandeliers":
            $ hrel = hrel + 3

label hr_028:
    with timeskip
    show cheit maid happy 1 at left with dissolve
    c "Thank you for your work,"
    c "Mitsuki-sama would like to accompany you today."
    hide cheit

label hr_029:
    menu:
        "And do what?"
        "Walk the dog with her":
            $ hrel = hrel + 3
        "Play a piano piece with her":
            $ hrel = hrel + 2
        "Arrange flowers with her":
            $ hrel = hrel + 1

    with timeskip
    show haas casual sly 1 at left with dissolve
    pc "Is there anything else you need me to do?"
    show cheit maid happy 1 at right with dissolve
    h "..."
    c "Thank you for all your hard work for today."
    scene bg black with timeskip

#Day 4
label hr_030:
    scene bg haas entrance 1 with fade
    menu:
        "Ugh. More work today."
        "Wash the dog":
            $ hrel = hrel + 2
        "Carve the hedge into the head of Haas":
            $ hrel = hrel + 3
        "Clean the kitchen":
            $ hrel = hrel + 1

label hr_031:
    with timeskip
    scene bg haas room 2 with fade
    show cheit maid happy 1 with dissolve
    c "Mitsuki-sama will have a party this coming Friday night."
    c "Everyone there will most definitely be of the elite class."
    c "We must all be on our best behavior."

label hr_032:
    pc "What do you want me to do?"

label hr_033:
    c "Mitsuki-sama would like you to help her choose out the dress she will wear to the party."
    c "This is a very important party."

label hr_034:
    menu:
        "I'm not really a fashion expert, but..."
        "That princess-looking dress looks nice":
            $ hrel = hrel + 1
        "You know what they say about little black dresses":
            $ hrel = hrel + 2
        "I think I like that pink one":
            $ hrel = hrel - 1

label hr_035:
    show cheit maid sly 1 with dissolve
    c "Thank you for helping out and choosing her dress."
    c "Please make invitations for all the guests on this list."
    c "And after that, you can rest for the day."
    scene bg black with timeskip

#Day 5
label hr_036:
    scene bg haas entrance 1 with fade
    menu:
        "I think I'm getting used to this."
        "Water the garden":
            $ hrel = hrel + 1
        "Relax":
            $ hrel = hrel - 1
        "Carve an ice sculpture of Haas' dog":
            $ hrel = hrel + 3

label hr_037:
    show cheit maid happy 1 at left with dissolve
    c "Mitsuki-sama would like you to prepare the party for her."

label hr_038:
    pc "Is there anything she needs me to do?"

label hr_039:
    c "Please escort all the guests into the house please."

label hr_040:
    "That sounds easy... "
    scene bg black with timeskip

#Night
label hr_041:
    scene bg haas party 1 with fade
    "Wow, a lot of people showed up..."
    "Let's see how Haas is doing."

label hr_042:
    # show pretty Haas at left
    show haas summer sly 1 with dissolve

label hr_043:
    menu:
        "Wow, she looks beautiful in that dress."
        "Dance with her":
            $ hrel = hrel + 3
        "Watch her":
            $ hrel = hrel
        "Praise her":
            $ hrel = hrel + 1

    show haas summer sly 1 at left
    show cheit maid sly 1 at right
    with move
    c "Thank you for all your work for the week."
    c "It was a very successful party. Mitsuki-sama is very satisfied."

#Cheit exist
label hr_044:
    scene bg haas entrance 1 with timeskip
    "Well, that was a busy day."
    "But finally, I'll get paid tomorrow."
    scene bg black with timeskip

#Day 6
label hr_045:
    scene bg haas entrance 1 with fade
    menu:
        "I wonder if this is all worth it?"
        "Wash the dishes":
            $ hrel = hrel + 1
        "Bake Haas a cake":
            $ hrel = hrel + 2
        "Ask Haas to pose for a painting":
            $ hrel = hrel + 3

    # show happy Cheit at left
    with timeskip
    show cheit maid happy 1 at left with dissolve
    c "Thank you for all your hard work for the past week."
    c "Here is your payment."

label hr_046:
    pc "Thank you so much."
    scene bg black with timeskip
    
    if hrel < 8:
        jump hr_047
    elif hrel >= 8 and hrel < 15:
        jump hr_049
    else:
        jump hr_053

label hr_047:
    scene bg haas dining 1 with fade
    show cheit maid serious 1 with dissolve
    c "We do appreciate all your work."
    c "But as a butler, I do not personally feel like you cater to Mitsuki-sama's taste."
    c "Please do not appear in front of Mitsuki-sama anymore."
    c "I wish you have a good day."

label hr_048:
    pc "Whatever..."
    scene bg black with timeskip
    jump hr_057

label hr_049:
    scene bg haas dining 1 with fade
    show cheit maid happy 1 at left with dissolve
    c "We appreciate all your hard work."
    c "Mitsuki-sama would like you to have this as a token of appreciation."

label hr_050:
    pc "A coupon?"

label hr_051:
    c "It's a 50\% coupon for all Haas Corporation owned stores."

label hr_052:
    "It's still going to be thousands dollars..."
    pc "Thank you very much."
    c "Well, hope you have a great summer. We'll see you in school."
    scene bg black with timeskip
    jump hr_057

#Good End
label hr_053:
    scene bg haas dining 1 with fade
    show cheit maid sly 1 at left with dissolve
    c "We appreciate all your hard work."
    c "Mitsuki-sama would like to thank you personally."

label hr_054:
    "She's finally gonna speak to me?!"

label hr_055:
    show haas casual sly 1 at right with dissolve
    h "...."
    pc "???"

label hr_056:
    show haas casual sly 1:
        xalign 1.0 xanchor 1.0
        easein 1.0 zoom 5.0 xanchor 1.0 xpos 2.0 ypos 3.8
    "!!!"
    scene bg black with timeskip

#Day 7
label hr_057:
    scene bg street 1 with fade
    "Well, one week passes pretty fast."
    "Now I need to look for another job."

    # scene Haas & Cheit peeking Protagonist
    pc "Let's see... more jobs..."
    
    jump demo_end
