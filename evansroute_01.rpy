label er_001:
    
    $progress = 0
    $relationship = 0
    
    #Generic Background: Classroom
    scene bg classroom 1 with fade
    play music "music/normal_theme.ogg"    
    "The school day is over."
    "I really want to go home, but..."
    show evans summer happy 1 with dissolve
    "I really should get started on our cultural festival project."
    "I mean, I am the class rep after all."
    e "e equals 2.7182818284590452..."
    pc "Hey, Evans?"
    show evans summer surprised 1 with dissolve
    e "H-huh!? Sempai!?"
    pc "That was a good idea, you know."
    show evans summer embarrassed 1 with dissolve
    e "Oh...I mean, it's...nothing...."
    "This could be difficult..."
    pc "Um, Evans?"
    show evans summer surprised 1 with dissolve
    e "Y-yes!?"
    pc "I was just wondering...could you help me with researching what we could do for the haunted house?"
    e "Eh-Ehh..!?"
    pc "I mean, it was your idea, and you're good at math and stuff, right? I was thinking you could be a big help."
    e "Oh...I...a-alright..."
    show evans summer glad 1 with dissolve
    "She's pretty when she smiles."
    e "So...where do you want to do research?"
    pc "Hmmm...."
    hide evans
    menu:
        "Go to the library together":
            jump er_004
        "Go to the computer lab by yourself":
            jump er_003
        "Go home and research on your own":
            jump er_002

label er_002: #Go home and research on your own
    pc "I think I'll go home first and do some research on my own."
    show evans summer worried 1 with dissolve
    e "Oh...OK..."
    "So, I went home to do research."
    hide evans with dissolve
    scene bg workstation 1 with fade
    pc "Oh, this looks interesting..."
    pc "Wow, I had no idea..."
    pc "Haha, that is so true..."
    scene bg black with dissolve
    "In the end, I became addicted to tvtropes and dropped out of school."
    "I wonder what happened to Evans and everyone else..."
    jump er_ridiculous_end

label er_003: #Go to the computer lab individually
    pc "I think I'll go down to the computer lab myself and do some research there."
    show evans summer worried 1 with dissolve
    e "Oh...OK..."
    #(Computer Lab)
    scene bg black with dissolve
    "I went down to the computer lab and spent the afternoon doing research."
    $progress += 1
    jump er_005

label er_004: #Go to the library together
    pc "Let's go to the library together."
    show evans summer embarrassed 1 with dissolve
    e "Oh, O-eeehhhh!?"
    pc "You...you're not filling me with lots of confidence here."
    e "B-but...there are PEOPLE at the library..."
    pc "Ummm....yeah? There are people at the library. So what?"
    e "B-but if something were to happen..."
    pc "Don't worry, we'll be alright. I'll be there for you."
    e "O-oh, OK..."
    scene bg library 1 with fade
    "We went to the school library and checked out several books on magic tricks and props."
    scene bg library 2 with fade
    "We also got some books on real haunted houses and a couple on basic home improvement."
    "I also had several books fall on me."
    scene bg black with timeskip
    $progress += 1
    $relationship +=1
    jump er_005

label er_005:
    #Background: Supply closet, or something.
    scene bg classroom 1 with fade
    show evans summer happy 1 with dissolve
    "Today, Evans and I are going through the supply room at school to look for stuff we can use."
    pc "Hey, this looks good."
    "I hold up a battered-looking orange cell phone with a cracked and bloodstained display."
    e "That belongs to the Occult Club, so you shouldn't touch it without permission."
    "She had a point. The prop was in an area marked off for the Occult Club."
    "Their president, a third year named Kumashiro, has a bit of a reputation for being easily angered."
    pc "Alright...hey, what's this?"
    "I see what looks like a rope hanging from the ceiling."
    show evans summer surprised 1 with dissolve
    e "No! Don't-"
    "Her words come too late."
    "As I pulled on the rope, I realized that it was connected to something on the top shelf."
    hide evans
    "Then it hits me."
    "Literally."
    "WHAM" #and probably sound effect of WHAM!
    "A rather large canoe falls on my head."
    "It's colored dark blue, with \"Nice Boat\" written on the side in yellow letters."
    show evans summer worried 1 with dissolve
    e "Kyaa! Are you alright!?"
    "I nod and stand with some difficulty."
    pc "Ow..."
    e "Awawaw....Pi equals 3.141592653589..."
    pc "Maybe you ARE a curse..."
    show evans summer embarrassed 1 with dissolve
    e "N-no, I'm not..."
    "It seems she's taking this a bit hard."
    pc "Hey, don't worry. I'm fine. See?"
    "I do a couple of jumping jacks to demonstrate."
    pc "See? Don't worry."
    hide evans
    #DING DONG DING DONG
    "We head back to class when the bell rings."
    scene bg black with dissolve

label er_006:
    "Kiii"
    scene bg sky 1 with fade
    "Kiii"
    "Summer."
    "Cicadas..."
    "Popsicles..."
    "Girls in swimsuits..."
    "Heat..."
    "FREAKING MOUNTAINS OF HOMEWORK."
    scene bg bedroom 1 with fade
    "This is just great..."
    "We Japanese students only get 40 days of summer vacation to begin with..."
    "...and that number is further whittled away by mountains of homework!"
    "RIIING" #RIIIIINNNNGGGGGGGG
    "My cell phone rings."
    "I pick it up and look irritably at the caller."
    "It's Evans."
    "Evans."
    "...Evans?"
    p "\[Hello?\]"
    "I answer reluctantly."
    e "\[Ah, Sempai?\]"
    "Her voice is somewhat difficult to make out, but it's there."
    e "\[I was just wondering...\]"
    e "\[Would you like to come over to my house to do homework?\]"
    "I'm not sure what to say."
    "Going over to her house to do homework would be good, but..."
    "It's so freaking hot outside..."
    menu:
        "Go":
            jump er_007
        "Don't go":
            jump er_008

label er_007: #Go
    pc "\[Alright. I'll be there in a few minutes.\]"
    e "\[Ok, I'll be waiting!\]"
    "CLICK" #CLICK cellphone button!
    "..."
    "I reluctantly get up and get my school things together."
    scene bg street 1 with fade
    pause 2
    scene bg evans house 1 with fade
    show evans summer surprised 1 with dissolve
    e "Oh!"
    show evans summer glad 1 with dissolve
    e "You're here!"
    e "Come on in!"
    scene bg evans wall 1 with fade
    "It was nice to get out of the sun."
    "We spent that day doing homework."
    scene bg black with dissolve
    $relationship += 1
    jump er_009

label er_008: #Don't go
    pc "\[Uguu...not today....\]"
    e "\[Oh, alright...\]"
    "She sounded disappointed."
    e "\[Maybe tomorrow then?\]"
    pc "\[Yeah, maybe...\]"
    e "\[Okay! See you tomorrow!\]"
    "CLICK" #CLICK cellphone click
    "..."
    "Maybe that wasn't such a good idea..."
    scene bg black with dissolve
    jump er_009
    
label er_009:
    #Classroom
    scene bg classroom 1 with fade
    "Preparations for the School Festival are really picking up."
    "Evans helped pick out materials, and now everyone is working to finish the project."
    show evans summer determined 1 with dissolve
    "Evans is working on something too."
    "I mean, the haunted house was her idea and all, but..."
    "It's nice to see that she's actually getting along with everyone else."
    e "Huh? This can't be right..."
    "It looks like she's run into trouble."
    pc "Need a hand?"
    show evans summer surprised 1 with dissolve
    e "Oh!"
    e "I-I suppose I could use a hand..."
    "I looked down at what Evans was working on."
    "It was a chainsaw with the teeth removed."
    "Normally, they'd be pretty expensive, but we were lucky to find one cheap at a junk dealer's."
    "The only problem was,"
    "It was old."
    "And broken."
    "Which was why we got it cheap."
    "Evans was sitting there with an instruction manual in one hand, trying to figure out how to fix it."
    show evans summer determined 1 with dissolve
    e "That's funny."
    e "It should be perfectly alright now, but..."
    pc "Hmmm..."
    "This wasn't good."
    "She had been working on this for the past few hours now..."
    "What should I do?"
    hide evans
    menu:
        "Suggest that she work on something else.":
            jump er_010
        "Help her.":
            jump er_011
        "Call it quits for the night.":
            jump er_012

label er_010: #Suggest that she work on something else.
    pc "You know, maybe you should work on something else."
    e "E-eh?"
    pc "I mean, you've been working on that for a while, right?"
    pc "It might be more productive to do something else right now."
    pc "You know, a change of perspective?"
    e "Oh...OK."
    "Evans set aside the chainsaw and began helping Dwinelle with some ghost costumes."
    scene bg black with dissolve
    $progress += 1
    jump er_013

label er_011: #Help her.
    pc "Here, let me give you a hand."
    e "A-are you sure...I mean...I've been working on this for a while now..."
    pc "Don't worry. We can do this."
    show evans summer glad 1 with dissolve
    e "A-alright..."
    "We got to work immediately."
    scene bg classroom 1 with timeskip
    "It took us a few more hours, but we finally got it to work."
    "Although by that time, everyone else had gone home, and we wound up sleeping at school, in our uniforms."
    "But, I suppose that that in and of itself would make a nice memory..."
    scene bg black with fade
    $progress += 1
    $relationship += 1
    jump er_013

label er_012: #Call it quits for the night.
    pc "Well, I think I'll call it quits for the night."
    e "O-oh, okay...."
    "I left the classroom and went back home to sleep for the night."
    scene bg black with fade
    jump er_013
    
label er_013:
    pause 1
    scene bg classroom 1 with fade
    show sproul sensei happy 1 at right with dissolve
    ss "Thanks for playing this demo version!"
    show evans summer surprised 1 at left with dissolve
    e "Sp-Sproul Sempai!?"
    ss "No! In this section, call me Sproul-Sensei!"
    e "Oh, okay..."
    ss "Right! Now, Protagonist!"
    ss "You've made it this far, which means you're done with the demo!"
    ss "Was it fun?"
    e "Y-yes..."
    ss "Well, if the demo's fun, the final game's gonna be even better!"
    ss "So make sure to buy it when it comes out, got it!?"
    e "Y-yes! Sproul-Sensei!"
    ss "Well then, see you in the other routes! And buy the full version!"
    scene bg black with fade
    #Demo-exclusive end
    jump er_end

label er_ridiculous_end:
    #title, I think: Teach me, Sproul Sensei!
    "Ding Dong Ding Dong....it's time for \"Teach me, Sproul-Sensei!\""
    pc "That didn't work so well."
    scene bg classroom 2 with fade
    show evans summer annoyed 1 at left with dissolve
    e "Not at all."
    show sproul sensei worried 1 at right with dissolve
    ss "Well, let's look at where you went wrong."
    pc "Don't remind me..."
    show sproul sensei happy 1 at right with dissolve
    ss "Basically, to get the best ending, you have to choose options that will allow you to make progress on the haunted house as well as build up your relationship with Evans."
    pc "Hmmm..."
    show evans summer glad 1 at left with dissolve
    e "That would have increased both Progress and Relationship, right?"
    ss "Exactly. On the other hand, with the computer lab option..."
    e "Since it's at school, he would have at least been able to stay on task."
    show sproul sensei worried 1 at right with dissolve
    ss "Somehow I doubt that, but..."
    pc "Hey..."
    show sproul sensei happy 1 at right with dissolve
    ss "Anyhow, to get the best ending, you need to make progress as well as build up your relationship. Got it?"
    pc "Right!"
    e "Right!"
    hide evans
    hide sproul
    #Evans Silly End 1 "TVtropes will ruin your life"
    jump er_end

label er_end:
    jump demo_end
