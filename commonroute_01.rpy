label cr_001:
    python:
        # Common Route Relationship Variables
        crrel = AttrDict({})
        crrel.sather = 0
        crrel.evans = 0
        crrel.haas = 0
        crrel.twins = 0
        
        # Common Route Flags
        crflag = AttrDict({})
        crflag.first_bad = False
        crflag.helped_evans = False
        crflag.took_flier = False
        crflag.met_gate = False
        crflag.experiment_appointment = False
        crflag.chosen_route = None

        from pprint import pprint
        pprint(persistent.seen_scenes)

    if SkipMenu('cr_001'):
        $ dname = 'Dwinelle'
        $ narrator = regnar
        $ pcname = None
        jump cr_002
    play music "music/normal_theme.ogg"
    scene bg path 1 with Fade(1.0, 1.0, 1.0)
    $ narrator = nvlnar
    $ dname = 'Girl'
    "A confession."
    menu:
        "This is a test menu"
        "Choice 1":
            "You picked choice 1"
        "Choice 2":
            "You picked choice 2"
        "Choice 3":
            "You picked choice 3"
        "Choice 4":
            "You picked choice 4"

    "That's what it had to be."
    "Why else would I get a note asking me to wait for her at the back of the school?"
    "It's a dream.{w=1.0} It has to be a dream.{w=1.0} It can't not be a dream."
    "It's a dream. {w=1.0}Isn't it?"
    
    nvl clear
    
    "So I wait.{w=1.0} And wait.{w=2.0} And wait."
    "She's not going to show."
    "She's already five minutes late."
    "Why isn't she here yet?"
    
    nvl clear
    
    "I wait.{w=1.0} And wait.{w=2.0} And wait."
    "Cherry blossom petals fall around me.{w} It's spring, after all.{w=0.3} Isn't it?"
    
    nvl clear
    
    "I wait."
    
    nvl clear
    
    show dwinelle dream worried 1 with Dissolve(2.0)
    dnvl "Sorry."
    "A voice. I look around and find a girl nearby. But without my glasses I can barely make out her face."
    "Why aren't I wearing my glasses?{w} That wasn't smart of me, was it?"
    pcnvl "Uh..."
    "I struggle. I don't really know what to say."
    pcnvl "I-it's okay."
    dnvl "Still, I made you wait."
    
    nvl clear
    
    show dwinelle dream happy 1 with quick
    "She approaches, smiling brilliantly. Even without my glasses I can see the luminescence of her smile."
    "A pause."
    "We don't say anything for a few moments."
    "I must look as red as her hair."
    pcnvl "Really,{w=0.5} it's okay."
    "There's not much else I can say. What {i}can{/i} I say to this beautiful girl whom I've never met?"
    show dwinelle dream stern 1 with quick
    "Her smile falters for a moment."
    show dwinelle dream happy 1 with quick
    
    nvl clear
    
    "I clear my throat."
    pcnvl "So, uh..."
    "This isn't near anywhere as dramatic as it is in manga."
    "She gasps."
    dnvl "Oh, that's right!"
    "She moves and stands a good distance away."
    $ narrator = regnar
    nvl clear
    with Fade(1.0, 1.0, 1.0, color="#FFFFFF")
    stop music fadeout 1.0
    d "Can I call you Aniki?"
    $ pcname = "Aniki"
    pc "I... I like yo--"
    $ pcname = None
    "Wait.{p=1.0}What did she say?"
    "It clearly wasn't \"I like you.\""
    d "Aniki!"
    "Stop calling me that!"
    "But... Aniki? Why that?"
    d "Aniki! Wake up!"
    "I said stop--\"Wake up\"?"
    "So it is a dream?"
    "I'm dreaming?"
    $ dname = 'Dream Girl'
    scene bg bedroom 1
    show dwinelle winter stern 1:
        zoom 5.0 xanchor 0.5 yanchor 1.0 ypos 4.0 xpos 0.6
    with Pixellate(2.0, 20)
    d "ANIKI!"
    pc "GAH! Don't get so close!"
    show dwinelle winter stern 1:
        linear 0.5 zoom 1.0 xpos 0.5 ypos 1.0
    d "It's your own fault for not having woken up, isn't it?"
    "She's dressed in a uniform. A school uniform."
    "Ah! That's right! School!"
    hide dwinelle
    show dwinelle winter happy 1
    with quick
    d "Looks like you're awake now, though.{w} So, did you have a good dream?"
    d "'I... I like yo--'"
    d "What were you going to say, I wonder?"
    "I don't say anything. Instead, I pick her up and throw her out the door."
    show dwinelle winter stern 1 with quick
    show dwinelle winter stern 1:
        ease 0.3 xalign 0.8
        pause 0.2
        ease 0.3 xalign 2.4
    d "Wha-- HEY!"
    hide dwinelle
    "I slam the door shut."
    "I can't tell if I'm blushing, but my face feels like it's on fire."
    "But that will not break my resolve."
    "Shion Dwinelle will never know that I dreamed about meeting her, today."
    $ dname = 'Dwinelle'
    "I pull my new uniform out."
    "The blazer is dark blue, and my tie is red like all first years."
    "It's newly washed and newly pressed especially for my first day of high school."
    "It's hard to keep it from wrinkling."
    "I put it on, but before I can finish buttoning the coat, my door bursts open."
    show dwinelle winter stern 1:
        xalign 2.0 yalign 1.0
        ease 0.7 xalign 0.5
    d "Took too long."
    "She grabs my sleeve and with a speed that defies logic, we're out of the apartments and on the streets."
    $ _window = False
    scene bg house 1
    show dwinelle winter stern 1
    with wiperight
    
    scene bg street 1
    show dwinelle winter stern 1
    with wiperight
    
    pause 0.5
    $ _window = True
    pc "Hey, at least let me eat breakfast!"
    show dwinelle winter happy 1 with quick
    d "The early bird gets the worm."
    "I don't think the saying fits the situation."
    show dwinelle winter stern 1 with quick
    d "It's your own fault, isn't it? That you got up late?"
    d "If you got up in time you might have been able to eat something."
    "A tell-tale noise preempts my retort."
    
    pause 1.0
    show dwinelle winter worried 1 with quick
    pc "You're one to talk."
    pc "You probably got up, realized you were late, then woke me up so I couldn't have anything to eat, either."
    "The look on her face definitely said \"busted\"."
    pc "You haven't even tied your tie."
    show dwinelle winter happy 1 with quick
    d "Details.{w} Besides, that's not the point.{w} The point is that I still got up earlier than you did, Aniki."
    pc "Don't call me that."
    d "Okay, Ani-ue."
    $ pcname = "Ani-ue"
    pc "No. That's even worse."
    $ pcname = None
    "Looks like I'm Aniki, then.{w=0.8} How troublesome."
    
    $ narrator = nvlnar
    "Let me get this straight."
    "This noisy girl is Shion Dwinelle and despite what she calls me, we are not{w=0.3} not{w=0.7} NOT{w=1.0} related."
    "She's just a girl who lives in my neighborhood."
    
    nvl clear
    scene bg evans street 1
    show dwinelle winter happy 1
    with wiperight
    
    "Don't misunderstand."
    "We're not childhood friends, either."
    "She just happened to be in my class when I transferred in during my first year of middle school."
    "And she was in my class the year after that."
    "And the year after that, too."
    
    nvl clear
    
    "Don't ask me why she calls me Aniki. I'm still figuring that one out."
    "I suspect she's forgotten my name and doesn't want to be found out.{w=0.4} Again."
    "I also suspect her family is Yakuza.{w} You didn't hear that from me."
    
    nvl clear
    
    pause 0.3
    $ narrator = regnar
    show dwinelle winter happy 1 at left with move
    d "'How troublesome.'{w=1.0} ... is what you're thinking, isn't it?"
    "She guessed right."
    "We walk on."
    $ persistent.seen_scenes.add("cr_001")

label cr_002:
    $ ename = 'Apologetic Girl'
    if SkipMenu('cr_002'):
        jump cr_003
    if not renpy.showing("bg evans street 1"):
        scene bg evans street 1
        show dwinelle winter happy 1 at left
        with fade
    "We've been walking for a long time."
    "We should have reached the school by now."
    "We haven't."
    "Instead, we seem to be wandering down unfamiliar streets in an unfamiliar neighborhood."
    "Nothing I can see resembles the great gray building that we are looking for."
    "Then I realize what happened."
    "I made a mistake."
    "I followed Shion."
    
    $ narrator = nvlnar
    
    "Looks like it's time for another round of let's explore Dwinelle."
    "Shion possesses many things."
    "   - Beauty and charm."
    "   - A dry wit."
    "   - A level, if forgetful, head."
    "   - A habit for being late."
    "But a sense of direction she has not."
    
    nvl clear
    
    "If she could have a negative sense of direction...{w=1.0} Actually, I'm sure she has a negative sense of direction."
    "If anyone in the world has it, it's her."
    "She could get lost in a hallway if you leave her for long enough."
    "A hallway with only two exits."
    
    nvl clear
    
    "I've heard rumors that she's been found on the third floor of the middle school looking for a classroom on the second floor and thinking she's on the first floor."
    "She claims she never saw a flight of stairs."
    
    nvl clear
    
    $ narrator = regnar
    
    pc "Great. I don't know which way the school is from here."
    d "That's easy, it's..."
    
    show dwinelle winter worried 1 with quick
    d "It's..."
    "I'm on the edge of my seat here."
    "A few moments pass."
    pc "You don't know where we are either, do you."
    "Not that I'm surprised."
    "I begin to walk again."
    show evans winter worried 1 at right with MoveInRight(1.0)
    #    xalign 2.0
    #    linear 1.0 xalign 1.0
    "Unexpectedly, something is in my way."
    show evans winter surprised 1 with quick
    with vpunch
    e "Ow..."
    
    scene bg black
    # scene cg evans common 1 1
    #show evans winter worried 1
    with dissolve
    play music "music/normal_theme.ogg"
    "On the ground is a girl I've never seen before.{w} Funny, that wasn't there before."
    "I wait for her to regain her bearings before I apologize."
    e "I... I'm sorry. Are you all right?"
    "Wait. That's my line."
    "Why is the person who got knocked down saying things that the person standing should be?"
    pc "Uh, yeah. I'm fine."
    pc "Aren't you the one that needs help?"
    "I extend my hand towards her."
    #show evans winter surprised 1 with quick
    extend " She seems to shrink away from it."
    e "Ah, no. It's okay."
    "Well she doesn't look like she's injured."
    "I stand there awkwardly while she sits on the ground."
    "After a while, she finally stands up."
   
    scene bg evans street 1
    show evans winter worried 1 at right
    show dwinelle winter worried 1 at left
    with dissolve
        
    "Then, Shion notices something I don’t."
    
    show dwinelle winter happy 1:
        ease 0.5 xalign .5
    
    "True to form, she acts by ignoring all laws of personal space."
    d "Hey, do you know where Kunaguma High is from here?"
    "Normally, such a question would be innocent. Without out incident."
    "With Shion, it becomes a disaster."
    "Her face was barely an inch away from the girl's."
    
    show evans winter surprised 1 at right:
        linear 0.05 ypos .95
        linear 0.05 ypos 1.0
        
    e "Eee!{w} Ah. I... I..."
    "Aren't you a bit close, there, Shion?{w} Look at her. She doesn't look like she's enjoying having your face pressed up so close to hers."
    
    show evans winter surprised 1 at right:
        linear 0.3 xalign 1.05
        linear 0.3 xalign 1.0
        repeat
        
    e "K-k-k-k..."
    show evans winter surprised 1:
        linear 0.3 xalign 1.0
    "Look at how flustered that girl is. She can't even finish her sentences.{w} Why are you asking her, anyway?"
    "Then I notice she's wearing the same uniform as Shion's, albeit actually pressed and worn correctly."
    "And she's wearing a red ribbon.{w} So we're in the same year..."
    "Oh.{w=0.5} Right.{w=0.5} Time to intervene."
    pc "Hey, Shion, aren't you being a bit familiar with this girl you've never met?"
    
    show dwinelle winter happy 1:
        easein 0.3 xalign 0.0
        
    "I pull her by the collar so she's no longer invading private airspace."
    d "Oh, she doesn't mind."
    "Judging from her reaction, she clearly does."
    pc "At least look at how she's reacting to your assault."
    "Not one to really notice trepidation, Shion is confused."
    
    show dwinelle winter worried 1 with quick
    
    show dwinelle winter worried 1:
        ease 5.0 xalign -2.0
    
    show evans winter worried 1
    "While she's is busy puzzling that one over, I take the opportunity and turn towards the girl."
    pc "Ah, sorry about her.{w=1.0} She's just an idiot."
    
    show dwinelle winter mad 1:
        xalign -0.55 yalign 1.0
    with Dissolve(0.1)
    "Funny, I didn't know you were supposed to be able to feel people glaring at your back."
    "Maybe I've developed some form of superpower?"
    hide dwinelle with Dissolve(0.1)
    
    e "Ah.{w=0.5} It's all right."
    pc "It's just that she must've noticed that you're wearing the same school uniform as us.{w} You go to Kanaguma?"
    e "That's right."
    pc "Do you mind walking with us there, then? We're kind of lost."
    
    show evans winter surprised 1 at right:
        linear 0.3 xalign 1.05
        linear 0.3 xalign 1.0
        repeat
        
    e "Eh?{w=0.5} Ah!"
    
    show evans winter surprised 1:
        ease 0.3 xalign 1.0
    
    "I can't really say her reaction is surprising. But it wasn't what I expected either."
    
    show evans winter surprised 1:
        ease 0.3 xalign 1.1
        
    e "Nononononono! "
    
    show evans winter surprised 1:
        ease 0.3 xalign 0.9
    
    extend "I can't walk with you at all!"
    
    show evans winter surprised 1:
        ease 0.3 xalign 1.1
    
    e "That is,{w=0.5} I'd like to.{w=1.0} But I can't walk with you."
    
    show evans winter surprised 1:
        ease 0.3 xalign 0.9
    
    e "And the school's not really very far at all."
    
    show evans winter surprised 1:
        ease 0.3 xalign 1.0 
    
    e "It's just down that street. Then take a left. Then a right. And then another left."
    
    show evans winter surprised 1:
        linear 0.3 xalign 1.05
        linear 0.3 xalign 1.0
        repeat
    
    "She says all this very fast, and flailing her arms about in a chaotic mess."
    e "And then you just keep going. And you'll be there."
        
    show evans winter surprised 1:
        linear 0.1 xalign 1.0
        
    pc "Wait, uh..."
    e "I'm sorry to have been a bother to you!"
    
    show evans winter surprised 1:
        linear 0.3 xalign 1.1
        pause 0.5
        ease 0.1 xalign 1.15
        ease 0.5 xalign 2.0
        
    e "Maybe we'll meet again, Sempai!"
    
    hide evans test
    
    $ pcname = "Sempai"
    pc "But I'm not--"
    $ pcname = None
    "Too late. She's already gone,{w=1.0} running off in completely the opposite direction she told me to go."
    "We're in the same year, right? I'll probably see her again."
    
    show dwinelle winter happy 1:
        xalign -2.0 yalign 1.0
        linear 1.0 xalign 0.5
        
    d "Ohohoho.{w} What was that, just now?"
    "A terrible voice looms behind me.{p}In all the commotion, I completely forgot Shion was here, too."
    d "To be so brazenly hitting on girls while your poor{w=0.5}, lonely{w=0.5}, childhood friend watches silently."
    "Hey, we're not childhood friends."
    show dwinelle winter stern 1 with quick
    d "You cad."
    pc "Weren't you the one who started asking her for directions?"
    d "Didn't you purposely run into her to start an encounter?"
    "Well, I won't say she's entirely wrong, but it's not as if I look for girls to purposely bump into."
    pc "You need to stop playing those kinds of games."
    d "I won't have any of your excuses!"
    with vpunch
    "The kick comes from nowhere.{w} It knocks me flat on my back, but Shion has forever engraved yet another moment in my mind."
    "As her kick flew up, I mused.{w} Shion Dwinelle is a very forgetful girl."
    "Just today, she's forgotten to get up early{w=0.1}, tie her tie{w=0.1}, eat breakfast{w=0.1}, button her shirt{w=0.1}, brush her hair."
    
    "I pinch my nose. Blood is leaking out."
    
    d "You saw didn't you?"
    "I saw something.{w} But not what you think I saw."
    d "I can see it in your eyes. You did!"
    d "I'll never forgive you!"
    with vpunch
    scene bg black with quick
    "As my beating came--as I blacked out--I thought to myself..."
    "\"What will happen to me when Shion finds out she forgot her underwear today?\""
    $ persistent.seen_scenes.add("cr_002")
    stop music fadeout 1.0

label cr_003:
    if SkipMenu('cr_003'):
        jump cr_004
    scene bg path 1
    show dwinelle winter worried 1
    with fade
    "Despite our efforts. We still arrive late to the opening ceremony."
    "A teacher is there to berate us for our faux pas, but otherwise she lets us off scot free."
    "Shion and I quickly find our places in line to stand."
    hide dwinelle with dissolve
    "I try my best to listen, but I can't seem to pay attention.{w} There is a powerful, nagging feeling in the back of my mind."
    "It looks like my superpower is acting up again."
    "I glance to my right."
    
    # scene cg sather common 01 with fade
    scene bg black with fade 
    "A tall girl is there with a sour expression on her face.{w} Aimed at me."
    "Her lips are pursed, but she remains silent{w=0.5}, glaring at me with accusing eyes.{w} Eyes that say, \"If I get in trouble because of you, you will be in for a world of horrible pain.\""
    "I can't help but notice that one of her eyes is bright gold."
    "I try to look away."
    "It doesn't help.{w} I can still feel her powerful glare piercing my soft flesh."
    pc "Ah..."
    "I don't really know what to say.{w} What {i}can{/i} I say?"
    "So I stay silent and try to listen to the speaker."
    
    scene bg path 1
    show sather winter annoyed 1 at right
    with fade
    "...{p}...{p}......................"
    "She's not looking away."
    "The ceremony is almost over now."
    "She's still not looking away."
    Char('Principal') "...and we can all enjoy our next year at Kanaguma high."
    "It's finally over."
    
    hide sather with Dissolve(1)
    "With a final look at me, the girl disappears in the crowd."
    
    show dwinelle winter glad 1 with dissolve
    d "Oi, Aniki!"
    "Gah! Don't call me that in public. You'll give people ideas."
    "Shion rushes to my side."
    d "Come on, let's get to homeroom!"
    "I don't even have a chance to reply. She's grabbed my sleeve and dragged me away."
    $ persistent.seen_scenes.add("cr_003")
    
label cr_004:
    if SkipMenu('cr_004'):
        jump cr_005
    scene bg hall 1
    show dwinelle winter happy 1 at right
    with fade
    pc "You do realize we aren't in the same class, don't you?"
    d "Ah... "
    
    show dwinelle winter dejected 1 with quick
    extend "You're right."
    "She seems a bit sad, really.{w} I can't help but feel a bit sorry for her, even if I don't understand why she hangs around me so much."
    pc "Don't worry.{w=0.5} It's not like we'll never see each other again.{w} We still live next to each other after all."
    d "I guess you're right..."
    
    show dwinelle winter glad 1 with quick
    d "Ah!{w} Look at that!"
    "I glance around to where she's pointing."
    show cheit maid sly 1:
        yalign 1.0 xalign 0.3
    show haas casual sly 1:
        yalign 1.0 xalign -0.3
    with Dissolve(0.5)
    
    pc "What the?!"
    "Honestly, I'm a little surprised too.{w} It's not everyday you see an honest-to-goodness maid, never mind at school."
    "She's a foreigner{w=0.3} and not a cosplayer, either.{w} The girl next to her smells of money."
    "The girl, herself, is dwarfed by her much taller companion, but she holds herself with an amazing sort of pride.{w} The priveleged{w=0.3}, responsible pride of old money."
    
    show cheit maid serious 1 with quick
    "I must have been staring.{w} The maid gives me an almost emotionless stare, but a dark feeling washes itself over me."
    show cheit maid sly 1 with quick
    "As quickly as the feeling came, it subsides."
    show dwinelle winter stern 1 with quick
    d "Come on, Aniki!"
    "Stop calling me that."
    d "We're gonna be late!{w=1.0} Again!"
    
    scene bg black
    with fade
    # scene cg haas common 01 with fade
    "As I follow her speeding form, I can't help but look back at the girl and her maid as they pass us."
    "It's odd.{w} Shion's lost interest much faster than normal."
    "Is this a product of her attention span?{w=2.0} Or did she feel the same darkness that I did...?"
    $ persistent.seen_scenes.add("cr_004")
    
label cr_005:
    if SkipMenu('cr_005'):
        jump cr_006
    scene bg classroom 1
    show sather winter annoyed 1
    with fade
    pc "Oh, no."
    $ sname = 'Tall Girl'
    s "What was that?"
    "Dammit.{w} Did I say that out loud?"
    "I can't help but think some kami is playing a trick on me.{w} What are the chances that {i}this{/i} girl would end up in my class?{w} And in the seat right in front of me no less."
    s "You're late.{w} Again."
    "Dammit again."
    "Wait a second."
    pc "Why do you care anyway?"

    s "Why do I care?!"
    "You don't have to shout."
    s "It's men like you who cause problems for the rest of us!"
    "You're making a scene. And what's with this \"men like me\"?"
    show sather winter annoyed 1:
        linear 0.3 zoom 1.5 ypos 1.5
    "She leans over my desk towards me."
    s "You undermine the efforts of everyone who tries hard with your disruptive behavior!"
    pc "Now wait just one minute.{w} What sort of person are you to accuse some whom you've {i}never{/i} met of being some sort of lowlife scum?"
    pc "It says a lot about your person when you can make such baseless accusations just from someone being late twice."
    s "A lot about {i}my{/i} person?{w} Tardiness is the easiest way to spot a delinquent!{w} Once is forgiveable{w=0.3}, but twice?"
    pc "At least wait for our own teacher to arrive before calling me tardy!"
    "I can already see the ending."
    "A few moments of silence pass between us.{w} My argument has thrown her off guard."
    "I'm the first to notice that we're nose-to-nose, now.{w} Our shouting match had brought our faces closer and closer together."
    pc "So..."
    "Her ears perk up.{w=0.5} My voice is a lot quieter than it had been."
    "I hesitate, but only for a moment."
    pc "Is this the part where we kiss?"
    
    show sather winter surprised 1 with quick:
        linear 0.3 zoom 1.0 ypos 1.0
    s "Wha-{w=0.3} wha?"
    "Understandably, she's a bit shocked.{w} She doesn't seem the type to have had those kinds of experiences with men."
    show sather winter embarrassed 1 with quick
    s "Why would I wanna go an' kiss a guy like you?{w} What a horrible thought!"
    show sather winter happy 1 with quick
    s "You moron."
    show sather winter surprised 1 with quick
    s "Ah. Sorry."
    "Osakan, huh.{w=0.5} Don't get many of them around here.{w} I wonder why she hides it."
    pc "What's there to be sorry about?"
    "Other than the horrible screaming match, I guess."
    show sather winter happy 1 with quick
    s "You seem like a pretty nice guy.{w=0.5} When you're not being late, anyway."
    s "I could get to like someone like you.{w=0.5} As friends.{w=0.5} You aren't getting any kisses from me any time soon."
    "I could get to like a girl who can take a joke like this so well."
    s "What's your name by the way?{w} I'm Sather.{w=0.5} Touru Sather."
    $ sname = 'Sather'
    pc "I'm--"
    $ gname = 'Sensei'
    show sather winter surprised 1:
        linear 0.3 xalign 0.0
    show goldman business glad 1:
        xalign 1.5 yalign 1.0
        linear 0.3 xalign 1.0
    pause 0.3
    g "Yoooo~!"
    "A new challenger has appeared."
    g "Sorry 'bout being, late everyone."
    "Another Osakan? Maybe they're not as uncommon here as I thought."
    g "Call me Goldman.{w=0.5} Or sensei.{w=0.5} Or Goldman-sensei.{w=0.5} Whatever you prefer.{w} And I'll be you're homeroom teacher for this year."
    $ gname = 'Goldman-sensei'
    Char('Class') "Good morning, Goldman-sensei."
    g "Well, now that I've introduced myself,{w=0.3} you should all do introductions, too."
    $ persistent.seen_scenes.add("cr_005")
    
label cr_006:
    if SkipMenu('cr_006'):
        jump cr_006choice
    scene bg classroom 1
    with fade
    "There isn't much incident until after math."
    "During the short break between classes, a familiar face walks into the room."
    show evans winter worried 1 at right with moveinright
    "She's about two or so hours late.{w=0.5} What amazing adventures she must have had after our encounter on the street."
    show sather winter annoyed 1 at left with moveinleft
    "But what's this?{w} A Sather approaches her,{w=0.3} sneaking up on her hapless prey as the latter turns her sad eyes towards me."
    show sather winter annoyed 1 at center with move
    show evans winter happy 1 with quick
    e "Senp--!"
    show evans winter surprised 1 with quick
    "Her jaw snaps shut.{w} That's bit of a relief, really, considering.{w} I don't need anymore nicknames."
    "It's amazing, actually. It's as though she could feel the glare. Maybe she has superpowers, too?{w} Am I no longer alone in this world?"
    s "And what do you think you're doing?"
    "Delinquent speech in 3{w=1.0}, 2{w=1.0}, 1{w=1.0}, now."
    s "You're late."
    e "I'm sorry, I..."
    s "Tardiness is the easiest way to spot a delinquent."
    "Somehow, that sounds oddly familiar."
    s "You're not a delinquent, are you?"
    "Subtle threat there, Sather.{w} I almost {i}couldn't{/i} feel the intense venom."
    e "..."
    $ persistent.seen_scenes.add("cr_006")
    
label cr_006choice:
    menu:
        "The girl opens her mouth, but no words escape.{w} I don't blame her, exactly, especially considering..."
        
        "Looks like I should help out":
            $ crflag.helped_evans = True
            jump cr_007a
            
        "It's not really my business":
            jump cr_007b
            
label cr_007a:
    $ crrel.sather = crrel.sather + 1
    $ crrel.evans = crrel.evans + 1
    if SkipMenu('cr_007a'):
        jump cr_008
    if not renpy.showing("bg classroom 1"):
        scene bg classroom 1
        show evans winter surprised 1 at right
        show sather winter annoyed 1
        with fade
    "Enough is enough.{w} Sather's being way too forceful with a girl who definitely cannot take that stress."
    pc "Sather-san.{w=0.5} Calm down."
    "I try to keep my voice soft but firm.{w} It feels a lot like commanding a dog, really."
    s "What?"
    "Despite the obvious heat in her voice, I keep my cool."
    pc "Look at her face.{w=0.5} Does that look like the face of a delinquent to you?"
    "Sather looks at the girl for a second."
    show sather winter confused 1 with quick
    s "Yes."
    "Oh, my god, this girl is unreasonable."
    pc "Really look.{w=0.5} Can't you see how she's shaking?{w} She looks like she's been through a lot today."
    pc "How would you feel if on your first day of high school something like this happened?"
    "A pause.{w} Please please PLEASE let my words pierce her skull."
    show sather winter surprised 1 with quick
    s "...{w} You're right."
    "SUCCESS!"
    show sather winter happy 1 with quick
    "That impressed look is on her face again.{w} I almost expect her to lapse into Osaka-ben again."
    "Instead, Sather turns toward the girl and starts speaking in shockingly formal tones."
    s "My sincerest apologies, miss.{w} I'm afraid I have a habit of jumping to conclusions when it comes to lateness."
    s "I, Touru Sather, will avoid distracting you from your studies from now on."
    "The girl looks confused."
    show evans winter surprised 1 with quick
    e "Ah, it's all right. {size=-8}I think.{/size}"
    hide sather with dissolve
    "And so Sather marches off, once more on the prowl for delinquents. {w}That girl needs to loosen up."
    show evans winter happy 1 with quick
    e "Sempai,{w=0.3} thank you for helping me out there."
    "No, no. Sempai isn't what you should be calling me."
    e "I don't know what I would've done if you hadn't..."
    pc "Don't worry about it.{w=0.5} It wasn't anything at all."
    show evans winter glad 1 with quick
    e "I appreciate it all the same."
    "She has an amazing smile when she's not looking horribly depressed."
    e "My name is Kazu Evans."
    $ ename = "Evans"
    e "Please take care of me, Sempai."
    $ persistent.seen_scenes.add("cr_007a")
    jump cr_008
    
label cr_007b:
    if SkipMenu('cr_007b'):
        jump cr_008
    scene bg classroom 1
    with fade
    "It's not really any of my business now, is it?"
    "I barely know Sather and I only talked with the other girl for maybe a few minutes."
    "Heck, I don't even know her name."
    ".{w=0.2}.{w=0.2}."
    s "WAH!"
    e "No don't!"
    with vpunch
    "A loud crash follows the frantic shouts."
    e "I'msorryI'msorryI'msorryI'msorryI'msorryI'msorry!"
    show evans winter embarrassed 1 at right with dissolve
    "Sather is on the ground, apparently unconscious."
    e "I didn't mean to do it!"
    "The girl is frantically waving her arms in denial."
    "Fine. It's time for proactive me to proact."
    pc "Come on.{w=0.5} Let's take her to the nurse's office."
    show evans winter surprised 1 with quick
    "I take Sather in my arms and start to walk.{w} She's amazingly light."
    scene bg hall 1
    show evans winter worried 1 at right
    with dissolve
    "Evans follows behind me, but she keeps a distance away.{w} A dejected, defeated look is on her face."
    pc "What happened?"
    show evans winter embarrassed 1 with quick
    e "I didn't do anything!"
    pc "I don't believe you did.{w} Still,{w=0.3} that doesn't explain how she ended up on the floor, unconscious."
    show evans winter worried 1 with quick
    "Thankfully, she calms down a bit{w=0.3}, but her face sinks into an even deeper depression."
    e "Bad things happen to people around me."
    "What?"
    e "Whenever I'm around, people have accidents and get hurt.{w} You shouldn't really stay close to me."
    "I don't know what to say to that.{w} This girl looks so harmless."
    pc "I...{w} What's your name?"
    "This is getting awkward."
    e "Oh, uh, I'm Evans."
    $ ename = 'Evans'    
    "She doesn't ask for my name.{w} She still seems to be stuck on the subject."
    pc "I'm--"
    show evans winter determined 1 with quick
    e "Sempai."
    "She suddenly says something intensely."
    "Uh, wait. Stop calling me Sempai."
    e "It's dangerous to be around me."
    "How depressing."
    show evans winter worried 1 with quick
    "We walk in silence for a while."
    pc "Uh, by the way..."
    pc "Which way is the nurse's office?"
    $ persistent.seen_scenes.add("cr_007b")
    
label cr_008:
    $ ename = 'Evans'
    if SkipMenu('cr_008'):
        jump cr_009
    scene bg classroom 1
    with timeskip
    play music "music/normal_theme.ogg"
    "Finally, it's lunchtime."
    "Amazingly, the day has been extremely quiet, considering the morning I've had."
    if crflag.helped_evans:
        Char('Boy A') "That was pretty cool."
        "What?"
        Char('Boy B') "Yeah.{w} How did you manage to calm down Sather like that?"
        Char('Boy A') "Twice no less!"
        Char('Girl A') "She was in my middle school class last year.{w} She can be so overbearing and bossy, you know?"
        Char('Boy B') "It was really annoying sometimes.{w} She really hated guys, too."
        Char('Girl B') "I don't really know her, but I've heard of her.{w=0.5} She's got a reputation."
        "They say all this in hushed tones, but Sather's already gone to get lunch."
        pc "It really wasn't anything, though."
        "Someone get me out of this situation quick."
    else:
        Char('Girl A') "I wonder if that girl's all right."
        Char('Girl B') "I can't help but feel she deserved it, though."
        Char('Girl C') "Yeah.{w} She's so annoying."
        Char('Girl B') "She was in my class last year.{w} She was so bossy."
        "Sounds like they're talking about Sather."
        Char('Girl B') "You're the one that took her to the infirmary aren't you?"
        "Huh? Are you talking to me?"
        pc "Uh, yeah."
        Char('Boy A') "You were the one that had that had that huge argument with her, too."
        Char('Girl C') "You're right!"
        "Ugh. Publicity."
        "Kami, save me from my plight."
    d "{size=+10}KIYAAAAAAAAAAAAAAAAAAAAAAAAAAIIIIII!{/size}"
    with vpunch
    "A flying kick arrives from nowhere, knocking me to the floor."
    show dwinelle winter stern 1 with quick
    d "That's for not telling me, Aniki."
    "Not telling her wha-- Oh. Right."
    d "You have no idea how embarrassing that was."
    pc "Wasn't it your fault to begin with? And don't call me that."
    "People are starting to stare again.{w=0.5} Well, the ones who weren't already staring from earlier."
    show dwinelle winter annoyed 1 with quick
    d "{size=-8}And I know that you saw.{/size}"
    pc "What was that?"
    show dwinelle winter happy 1 with quick
    d "Nevermind!"
    "She grabs me by the sleeve again.{w} That thing's going to get ripped off some day."
    pc "Where are you taking me?"
    d "Lunch, of course!"
    "Oh right. Lunch.{w} The sudden reminder that I haven't eaten anything all day causes my stomach to rumble."
    "With my greatest interests at stake, I allow her to pull me by my sleeve toward the cafeteria."
    scene bg path 1
    show dwinelle winter happy 1
    with dissolve
    "Oh, right.{w} This is Shion."
    "Somehow, she's managed to take us along the outside of the school."
    "What the hell. The cafeteria is nowhere near here."
    d "Whoops!"
    "I just glare at her."
    $ lname = 'Voice from above'
    l "{size=+10}Geronimooooooo!{/size}"
    "Something falls from the sky at high speeds in front of me"
    pc "What the hell?"
    stop music fadeout 1.0
    
    # scene cg latimer common 01
    scene bg black with fade
    with vpunch
    "The power of surprise knocks me to the floor."
    extend " From there, I stare up at a girl in a lab coat as a heavy cloth sheet drapes down behind her."
    $ lname = 'Girl Who Fell from the Sky'
    l "Experiment 626 Iteration 17b: Awaiting results."
    "I just gape at her.{w=0.5} An experiment?{w} Why is she experimenting during lunchtime?"
    $ pname = 'Voice from Nowhere'
    p "Geez, Mikoto.{w} Don't just suddenly jump from a building like that."
    "The girl begins to talk into her wrist."
    l "Never mind that, Rika-nee.{w=0.5} Did you get the data?"
    "A communicator?"
    p "What?{w} You think I could've gotten something written down so quickly?{w} Warn me before jumping down next time."
    l "*Sigh* Experiment 626 Iteration 17b: Inconclusive."
    l "For a famous scientist, you sure aren't on the ball about experimenting, Rika-nee."
    pc "No, no, I think you've got the experiment part wrong."
    p "I think you've got the experiment part wrong."
    "Uh, wait.{w} Did I say something out loud?"
    "The girl turns toward me, her unseen companion forgotten."
    pc "Uh... I mean..."
    l "Are you my servant?"
    pc "I... What?"
    "Did she just say what I think she said?"
    l "You have experience with experiments."
    "It wasn't a question."
    pc "Not real--"
    l "I ask you again, are you my servant?"
    "I really don't understand the question."
    l "Then it's a deal."
    "Wait, what?{w=0.5} I didn't say anything yet!"
    
    # scene bg school exterior
    scene bg path 1
    show latimer lab happy 1
    with fade
    "The serious expression melts from her face and a joy of glee forms on her face."
    l "I am soon-to-be world famous scientist, Mikoto Latimer.{w=0.3} Don't forget it!"
    $ lname = 'Latimer'
    l "From now on, you are Test Subject Alpha!"
    $ pcname = 'Test Subject Alpha'
    pc "Test Subject Alpha?"
    $ pcname = None
    "Another nickname?"
    l "You are my servant and I am your master!"
    "A wide grin appears on her face."
    l "Rest at ease, Test Subject Alpha.{w} With your help, your master will be able to follow in Rika-nee's footsteps."
    "I don't even know who that is."
    "The girl strolls away confidently, her goggles glinting in the sunlight.{w=0.5} It's amazing she doesn't trip on the lab coat that looks several sizes to large for her."
    hide latimer with dissolve
    pause 0.5
    show dwinelle winter happy 1 with dissolve
    d "You sure know how to meet girls, Test Subject Alpha."
    "Hey, don't you start."
    pc "Don't call me that."
    "Why am I just so {i}lucky{/i}?"
    pc "Come on.{w=0.5} Let's go get lunch."
    $ persistent.seen_scenes.add("cr_008")
    
label cr_009:
    if SkipMenu('cr_009'):
        $ pname = 'Pimentel'
        jump cr_010
    scene bg classroom 1
    show dwinelle winter glad 1 at left
    with fade
    stop music fadeout 1.0
    "I'm back in my class room again.{w} Shion is here, too, tearing into her bread.{w} And mine, too, for that matter."
    pc "Hey! That's mine!"
    d "I don't see your name on it."
    pc "I bought it!"
    d "Why can't you share, Aniki!"
    pc "Don't call me that!"
    s "Well you're just a regular playboy, aren't you."
    "Huh?{w} Oh, it's Sather."
    show sather winter happy 1 at right with dissolve
    "She's carrying an amazing stack of bread in her arms.{w} Melon bread, soba bread..."
    "Does she plan to finish all that?"
    d "Whoa..."
    if not crflag.helped_evans:
        pc "Are you all right now, Sather-san?"
        s "I'm fine.{w} Just tripped over my own feet, I think."
        s "By the way..."
    else:
        pc "Ah... Sather-san."
    s "You can drop the 'san' part. 'Sather' is just fine."
    pc "Okay then, Sather."
    "She moves her desk next to mine and dumps her pile of bread on top."
    s "You look hungry."
    "I'm not the one carrying a mountain of bread, though."
    pc "Ah, yeah.{w} I didn't have time to eat breakfast this morning."
    show sather winter annoyed 1 with quick
    "A sour expression crosses her face."
    s "That's right. You were late this morning."
    show sather winter happy 1 with quick
    d "Who is this, Aniki?{w=0.5}{size=-8} And why are you so close to her all of a sudden.{/size}"
    "Oh yeah. Shion is here, too."
    pc "Shion, I'd like you to meet Sather.{w} Sather, this nuisance is Shion.{w=0.3} Ow."
    "Shion removes her elbow from side."
    show dwinelle winter annoyed 1 with quick
    d "Pleased to meet you. I'm Shion Dwinelle."
    show sather winter annoyed 1 with quick
    s "Touru. Touru Sather. Pleased to meet you, too."
    "The atmosphere is getting tense.{w} It's almost like they really aren't pleased."
    show dwinelle winter happy 1 with quick
    d "What pleasant whether we're having. Ohohoho."
    show sather winter happy 1 with quick
    s "Yes. Quite. Ahahaha."
    "The barometer's still rising."
    "Things are getting worse."
    l "Test Subject A!"
    "Now what?"
    l "Rika-nee! That's Test Subject A!{w} I didn't know he was in our class."
    scene bg classroom 1
    show pimentel winter stern 1 at right
    show latimer winter happy 1 at left
    with fade
    "In the entryway is the parachute girl.{w} And beside her is the parachute girl again.{w} Does she have a clone?"
    $ pname = 'Rika-nee'
    p "Mikoto, it's rude to call someone something like 'Test Subje..ct...'"
    "Latimer No. 2 trails off."
    "A few tense moments pass."
    show pimentel winter lovestruck 1 with quick
    p "My darling!"
    $ pcname = 'My Darling'
    pc "Wha--?"
    $ pcname = None
    
    # scene cg pimentel common 01
    scene bg black
    with fade
    "I could almost see her eyes explode into hearts as she leaps and bounds toward me."
    p "Will you marry me, my darling?"
    "I think I'm a bit too young for that sort of thing."
    "Her face draws toward mine."
    pc "Wha wha wha?"
    "I shoot up from my seat and try to get her off me, but her iron grip refuses to be dislodged.{w} Instead I stumble over a desk and fall to the ground."
    p "Oh, no! My darling, are you all right?"
    p "Don't worry, my darling. I, your love, Rika Pimentel, will kiss it and make it feel better!"
    $ pname = 'Pimentel'
    "What is it with all these crazy women?!"
    "I scramble to stand up."
    pc "Nononono! I'm fine! I'm fine!"
    p "Are you sure?"
    pc "Yes yes yes!"
    "She pouts."
    p "All right."
    
    # scene bg school classroom
    scene bg classroom 1
    show latimer winter stern 1 at left
    show pimentel winter lovestruck 1:
        xalign 0.4 yalign 1.0
    with fade
    l "Geez, Rika-nee, I saw him first.{w} He can't be your test subject, too."
    "I'm not anyone's test subject, though."
    show dwinelle winter stern 1:
        xalign 0.8 yalign 1.0
    with dissolve
    d "Who is this hussy hanging all over you, Aniki?"
    show pimentel winter stern 1 with quick
    p "Who are you calling a hussy?"
    show sather winter annoyed 1:
        xalign 1.2 yalign 1.0
    with dissolve
    s "Someone who so blatantly shows their feelings like you must be a delinquent."
    p "What?"
    "The atmosphere's getting even worse now."
    "Suddenly, the bell rings."
    pc "Ahahahahaha! Dwinelle looks like it's time for you get back to your class!"
    d "Wha-- hey!"
    hide dwinelle with moveoutright
    pc "Everyone else ought to get back in their seats!"
    hide pimentel with moveoutleft
    hide latimer with moveoutleft
    hide sather with moveoutright
    "Reluctantly, everyone does what I say.{w} I'm amazed the situation could be dispelled so easily."
    "...{w}\n...{w}\n..........................."
    "Goldman-sensei isn't back yet."
    "..."
    "Lunch is over, isn't it?"
    "..."
    "Hurry up, sensei before the situation explodes again."
    show goldman business glad 1 with dissolve
    g "Sorry I'm late!"
    "Thank goodness!"
    show goldman business serious 1 with quick
    g "Hmm? Was there a fight in here?"
    "No, but it could've quickly evolved into one."
    show goldman business glad 1 with quick
    g "Eh, I guess it doesn't matter.{w} Who's up for some history?"
    $ persistent.seen_scenes.add("cr_009")
    
label cr_010:
    if SkipMenu('cr_010'):
        jump cr_011
    scene bg street 1 sunset
    with fade
    "Shion isn't there to walk home with me."
    "It's odd...{w} Even though she's a nuisance,{w=0.3} I feel lonely when she's not around."
    "Walking home is slow and uneventful."
    
    scene bg house 1 night
    with fade
    pc "I'm home."
    mom "Welcome back."
    "My mother's quiet voice drifts lazily from the back of the house."
    "She must be tired, as usual."
    pc "Have you started cooking dinner yet?"
    mom "...no. I haven't had the chance."
    pc "All right. I'll cook tonight."
    
    scene bg bedroom 1 night
    with fade
    "What a long day."
    "It feels like it's been forever since I last slept."
    "Is this feeling high school?"
    "The events of the day are still heavy in my mind, but soon I drift off into sleep."
    $ persistent.seen_scenes.add("cr_010")
    
label cr_011:
    if SkipMenu('cr_011'):
        jump cr_012
    scene bg classroom 1
    with timeskip
    play music "music/normal_theme.ogg"
    "It's June."
    "Things are a bit different now.{w} I've gotten used to walking home without Shion.{w}  Latimer drags me to assist her in science experiments."
    show sather summer annoyed 1 at right with dissolve
    s "Isn't there something you should be doing, {i}class rep{/i}?"
    "Did I mention I somehow became the class representative?"
    "Apparently, because of my successful handling of Sather, people decide I was the best candidate for the job."
    "Sather has been extremely cold to me since that day.{w} It's not that she doesn't talk to me, but she actively avoids interacting with me."
    s "Hurry up."
    "Usually."
    pc "Ah, right."
    hide sather with dissolve
    show goldman business glad 1 at left with dissolve
    pc "Stand!{w=0.5} Bow!{w=0.5} Sit!"
    g "Good mornin', class!"
    "Goldman-sensei is as lively as ever."
    g "Good news today, ladies and gentlemen!{w} We're getting a new student in our class today.{w} A transfer student from--"
    "Suddenly, the door slides open."
    show goldman business serious 1 with quick
    g "Oh, looks like she's here."
    show cheit maid sly 1 at right
    show haas summer sly 1 at right
    with dissolve
    "Into the door strides a confident-looking girl with light hair and tanned skin.{w} Her clothes are so clean and pressed, they look almost newer than new."
    e "Is that a maid?"
    l "That's a maid, isn't it?"
    p "That's definitely a maid."
    "Beside her is a tall, foreign-looking woman in a maid uniform that matches our uniform in color."
    "Come to think of it, this is an oddly familiar scene."
    pc "Ah!{w} It was that time!"
    "I said that out loud, didn't I?"
    g "You got something to say, Seat 10?"
    $ pcname = 'Seat No. 10'
    pc "Ah, it's nothing."
    $ pcname = None
    "I remember now.{w} This is the girl and the maid from the first day."
    "I suddenly recall the feeling of darkness.{w} The memory is so intense that the feeling is still overwhelming."
    "As suddenly as the feeling came, it goes away.{w} Wait was that even a memory at all?"
    show goldman business glad 1 with quick
    g "Please introduce yourself, Haas-san."
    hide goldman with dissolve
    show haas summer sly 1 at left
    show cheit maid sly 1 at center
    with move
    stop music fadeout 1.0
    "Both the girl and the maid move to the front of the class as though they are one being."
    "The girl stands in front of her audience with such a casual air that I can't help but think that she talks in front of many people often."
    "She doesn't say anything for a few moments.{w} The class is anxious for her to start."
    $ cname = 'Not Haas'
    c "'Good morning.'"
    "The girl's lips never moved.{w} The voice that speaks is deeper than what I'd expected."
    "Beside her, the maid speaks as though she was speaking for someone else.{w} She speaks fluently despite her foreign appearance."
    $ cname = 'Maid'
    c "'I'm Mitsuki Haas. My father is the CEO of the Haas Corporation,' is what Mitsuki-sama wishes to say."
    "Haas made no movement or gesture to communicate with the maid."
    "Suddenly, the maid bows."
    c "I'm Cheit, Mitsuki-sama's maid."
    $ cname = 'Cheit'
    "Cheit's voice seems to be barely restrained, as though she wants to say something else."
    c "Please treat us well."
    show goldman business serious 1 at right with dissolve
    g "Huh?{w} Oh, uh... There's an empty seat behind Number 10 over there."
    "Goldman-sensei points to me."
    "Wait a minute. Don't call me Number 10."
    show goldman business happy 1 with quick
    g "By the way, Number 10...{w=0.5}Show Haas-san around the school later. You're the rep, right?"
    "Well I am, but not because I want to be."
    hide cheit
    hide haas
    with dissolve
    "Haas takes the seat behind me."
    "Hey, Cheit, aren't you going to sit down?"
    show goldman business serious 1 with quick
    g "Oh, Cheit-san.{w=0.3} I'm afraid we don't have a seat for you right now. If you want I'll--"
    c "There is no need.{w} I will stand."
    g "Uh... If you're sure..."
    $ persistent.seen_scenes.add("cr_011")
    
label cr_012:
    if SkipMenu('cr_012'):
        jump cr_012choice
    scene bg classroom 1
    with fade
    "Class goes on."
    "I can't concentrate.{w} Cheit is still standing.{w} She's been standing since the moment she moved there."
    "It makes me uncomfortable."
    "The class feels like it's taking forever."
    "Is she staring at me?"
    "I think she's staring at me."
    "The darkness.{w=0.5} It's coming."
    "It's drowning me."
    "The bell rings."
    "I try to get out as quickly as possible."
    c "Wait a moment."
    "A deep voice stops me in my tracks.{w} I turn around.{w} Cheit is still standing there, the same neutral expression on her face."
    show cheit maid sly 1
    show haas summer sly 1 at left
    with dissolve
    c "Aren't you forgetting something?"
    "Forgetting... what...?"
    "Haas sits quietly, staring intently at me."
    pc "Oh!"
    "That's right. I need to show Haas around."
    pc "Haas-san, would you like to have a tour of the school?"
    "Haas doesn't say anything.{w} Her smile doesn't change at all."
    c "Mitsuki-sama accepts."
    "Uh... right."
    pc "We should go before lunch ends, then."
    "Haas stands deliberately and with the same confidence strides to stand beside me.{w} Cheit follows behind her with a maid's ease."
    "She waits expectantly.{w=1.0} Silently."
    pc "Then let's go."
    
    show bg hall 1 with dissolve
    "We leave the room."
    "I start walking down the hall with Cheit and Haas following close behind me."
    "We walk silently."
    c "Mitsuki-sama would like to know where we are headed, Class Representative-san."
    "Actually, to tell you the truth, I wouldn't really know.{w} Unfortunately, that's not an answer I think I can give Cheit."
    $ persistent.seen_scenes.add("cr_012")
    
label cr_012choice:
    menu:
        pc "Well..."
         
        "The cafeteria sounds good":
            jump cr_012a
             
        "What would Haas like?":
            jump cr_012b
            
label cr_012a:
    $ crrel.evans += 1
    if SkipMenu('cr_012a'):
        jump cr_013a
    if not renpy.showing("bg hall 1"):
        scene bg hall 1
        show cheit maid sly 1
        show haas summer sly 1 at left
        with fade
    pc "I was thinking we could go to the cafeteria. It is lunchtime after all."
    "Cheit's expression changed as though she were stopping herself from saying something."
    "Haas' smile never left her face."
    
    # scene cafeteria
    "The cafeteria is full of students clamoring for meals.{w} It's a bit noisy. I'm beginning to wonder if this was the best place to bring the daughter of the Haas corporation."
    "I look at my charges."
    "The same strained expression is still on Cheit's face, but Haas' seems quite pleased.{w} Then again, I'm not sure I can properly discern Haas' expression."
    c "I don't think..."
    "She pauses."
    c "Mitsuki-sama would like to--"
    show evans summer happy 1 at right with dissolve
    e "Oh, it's Sempai! {size=-10}Ah!{/size}"
    "The welcome interruption, courtesy of Evans, caused Haas and Cheit to turn towards the source of the sound."
    show evans summer embarrassed 1 with quick
    "Evans, true to form, began fidgeting uncomfortably."
    pc "Ah! Evans-san!{w} Pleasure meeting you here!"
    pause 1.0
    hide evans with dissolve
    "She hesitates a bit before hastily leaving."
    "Sorry, Evans.{w} Looks like you might miss lunch today because of me."
    c "Mitsuki-sama would like to know who that was."
    show cheit maid serious 1 with quick
    show haas summer annoyed 1 with quick
    "Cheit looks almost confused.{w} Haas' expression, on the other hand, is almost neutral."
    pc "Oh, that was Evans-san. She's in our class."
    c "She would also like to know why Evans-dono called you \"Sempai\"."
    "Well, I can't really say."
    pc "That I don't know."
    show cheit maid sly 1 with quick
    show haas summer sly 1 with quick
    "The atmosphere lights up. Haas' smile is back."
    c "Then if all the interruptions are done, Mitsuki-sama would like to have her meal."
    c "Do you have any suggestions?"
    "What sort of food do rich people eat?{w} I don't think this school can afford caviar."
    pc "What would you prefer, Haas-san?{w} Usually I have bread, but some ramen would be fine today."
    c "Mitsuki-sama would like to have bread."
    "Haas seems pretty inviting.{w} If only Cheit wasn't around."
    "We start to move toward the bread line, but suddenly Haas raises her arm as if to stop us."
    "Cheit and I stop immediately."
    c "It... Mitsuki-sama would like to know what bread you would prefer."
    pc "Huh? You're offering?"
    "Haas nods."
    pc "Um..."
    "I don't know how rich people act.{w} Will she make me pay her back for this?{w} With interest?"
    "Stinginess wins out."
    pc "Uh, croquet bread please."
    hide haas with dissolve
    "Haas heads into the line alone."
    "Wait.{w} I've never heard Haas speak.{w} Is this my chance to hear her voice?"
    show cheit maid serious 1 with quick
    c "Don't you start getting any ideas, brat."
    "I freeze."
    "The darkness has returned.{w} It's heavy.{w=0.3} So heavy."
    "Cheit's words are so different from her usual and so contrary to her appearance."
    $ pcname = "Brat"
    pc "Don't... D-Don't call me br-brat."
    $ pcname = None
    "My voice keeps catching in my throat.{w} I can't even deny a nickname without stuttering."
    "Cheit pointedly ignore my outburst."
    c "You are scum, brat.{w} You're not worth the dirt on Mitsuki's shoes.{w} Don't get any ideas."
    pc "I think you're jumping to conclusions.{w} I'm not interested in--"
    show haas summer sly 1 at left with dissolve
    show cheit maid sly 1 with quick
    c "Welcome back, Mitsuki-sama."
    "Haas is back with a bag of bread in her arms.{w} She looks back and forth between Cheit and me."
    c "I trust you didn't have any trouble?"
    "Haas shakes her head.{w} She turns to me and offers me bread."
    pc "Ah, thank you."
    $ persistent.seen_scenes.add("cr_012a")
    jump cr_013
    
label cr_012b:
    $ crrel.haas += 1
    if SkipMenu('cr_012b'):
        jump cr_012bchoice
    if not renpy.showing("bg hall 1"):
        scene bg hall 1
        show cheit maid sly 1
        show haas summer sly 1 at left
        with fade
                
    pc "What do you do for fun, Haas-san?"
    "Cheit hesitates."
    c "Mitsuki-sama enjoys many things, especially sports and business.{w} She is really very competitive."
    pc "Sports, huh?"
    "Well, there's no one playing anything during lunch, but..."
    pc "How about the pool, then?{w} Since it's summer, the pool will be filled with water, so we can go see it."
    "Haas' smile becomes a tiny bit wider."
    c "It... It seems Mitsuki-sama accepts your proposal."
    "With that, we head off."
    show bg path 1 with dissolve
    "Kanaguma High's pool is really quite large, probably due to the large number students per class."
    "It's really a pain to clean, too.{w} Luckily, I've had to do {i}that{/i} only once."
    hide haas with dissolve
    "Haas walks to the side of the pool and splashes the water around with her fingers."
    show cheit maid serious 1 with quick
    c "I sense good intentions, within you, brat.{w} But don't go thinking you can just gallivant around with Mitsuki.{w} You.{w=0.2} Are.{w=0.2} Not.{w=0.2} Worth her."
    "Cheit suddenly says something unexpected.{w} Haas is still at the poolside.{w} Nothing's going to save me now."
    $ pcname = 'Brat'
    pc "D-don't call me b-brat."
    $ pcname = None
    "My voice breaks and I stutter.{w} I can't help it, even if she gives me an unwanted nickname.{w} The darkness, it comes!"
    pc "A-and aren't you j-jumping to c-c-conlclusions?"
    "Cheit's gaze becomes extremely hard."
    c "You will not get any closer to Mitsuki."
    pc "But I--"
    c "You.{w=0.3} Will.{w=0.3} Not."
    show cheit maid sly 1 with quick
    show haas summer sly 1 at left with dissolve
    c "Mitsuki-sama."
    "Haas has stopped playing with the water. Cheit moves back to her side."
    c "Is it to your liking?"
    "Haas nods."
    "It looks like Cheit is back to her normal self.{w=0.5} Does Haas know about her other side?"
    c "Then, Class Representative-san, what will you show us next?{nw}"
    $ persistent.seen_scenes.add("cr_012b")
    
label cr_012bchoice:
    menu:
        c "Then, Class Representative-san, what will you show us next?{fast}"
        
        "How about the club rooms?":
            jump cr_012c
            
        "Explore the main building":
            jump cr_012d
            
        "Let's eat something":
            if SkipMenu('cr_012bex'):
                jump cr_013a
            if not renpy.showing("bg path 1"):
                scene bg path 1
                show cheit maid sly 1
                show haas summer sly 1 at left
                with fade
            "Lunchtime is almost over. I wonder if they're hungry."
            pc "Let's get something to eat before lunch is over."
            "Cheit looks at Haas."
            c "Mitsuki-sama thinks that's a fine decision."
            $ persistent.seen_scenes.add("cr_012bex")
            jump cr_013
            
label cr_012c:
    $ crflag.experiment_appointment = True
    if SkipMenu('cr_012c'):
        jump cr_012cchoice
    if not renpy.showing("bg path 1"):
        scene bg path 1
        show cheit maid sly 1
        show haas summer sly 1 at left
        with fade
    play music "music/normal_theme.ogg"
    pc "How about we take a look at what sort of clubs are here?"
    "Cheit looks at Haas, who nods."
    c "Mitsuki-sama wishes to go."
    show bg club building 1 with dissolve
    "The club rooms are in a building off to the side of the school."
    "I don't really make it a habit to come here though.{w} It's not that I enjoy being in the Go-Home club, but..."
    p "My darling!"
    show pimentel summer lovestruck 1:
        xalign 1.03 yalign 1.0
    with dissolve
    "But that.{w} Why are you even in the club building during lunchtime?"
    pc "How many times do I have to tell you not to call me that!?"
    show pimentel summer dramatic 1 with quick
    p "You haven't come and visited at all!{w} How dare you forget to visit your lover!"
    "Why do people insist on shouting things that could cause misunderstandings?{w} This is not a shoujo manga!"
    pc "I'm not your lover, either."
    p "Boohoohoohoo!{w} Spurned by my husband-to-be."
    "Stop that."
    show cheit maid serious 1 with quick
    c "Mitsuki-sama would like to reprimand you for failing to please your fiancee."
    "Cheit's face looks horribly neutral, and Haas' smile is twitching."
    c "She wishes to say that you are poor husband material."
    p "*Gasp* You're on my side?"
    show cheit maid sly 1 with quick
    c "MItsuki-sama is always glad to help a woman in need."
    "I think you're enjoying this situation a little too much."
    l "Rika-nee, where did you go? We need to start the experiment."
    "Oh! Looks like the sequel to Trouble, Trouble II is coming out today."
    show latimer lab happy 1:
        xalign 0.7 yalign 1.0
    with dissolve
    "Latimer walks out of the club room dressed in her usual lab coat."
    l "Uwah! Test Subject Alpha! You got my message then?"
    stop music fadeout 1.0
    "Message?"
    pc "I'm not your test subject.{w=0.3} And aside from that, what message?"
    "She pulls a sheet of paper from behind her."
    
    $ nvl_variant = "paper"
    $ narrator = Character(None, kind=nvlnar, what_prefix='', what_color="#000044FF") 
    nvl clear
    "{font=FREESCPT.ttf}{size=+10}Test Subject Alpha:\n\n
    Come over to the club during lunch today. We are running important experiments today.\n\n
    Bring a few other test subjects as well. We'll be needing more than one. Preferably two.\n\n
    Your master,\nMikoto\n\n
    P.S. Don't have anything to eat for lunch.{/size}{/font}{fast}"
    
    nvl clear
    
    $ narrator = regnar
    "What is this."
    $ nvl_variant = None
    pc "This looks like you wrote it just now."
    "She smiles innocently."
    "Don't play cute when you do something so sinister."
    show pimentel summer stern 1 with quick
    p "What is this?"
    "Why do I always forget that I have audiences?"
    p "My husband-to-be continues to cuckold me, with my own cousin no less!"
    p "O, cruel fate! O, unkind heart!"
    "Haas and Cheit applaud her performance while she bows."
    "What an amazing actr--wait a minute."
    pc "Oy, this isn't time for drama."
    l "That's right! It's time for science!{nw}"
    $ persistent.seen_scenes.add("cr_012c")
    
label cr_012cchoice:
    menu:
        l "That's right! It's time for science!{fast}"
        "Yeah, it's time for science!":
            if SkipMenu('cr_012cex'):
                jump cr_013a
            if not renpy.showing("bg club building 1"):
                scene bg club building 1
                show cheit maid sly 1
                show haas summer sly 1 at left
                show pimentel summer dramatic 1:
                    xalign 1.03 yalign 1.0
                show latimer lab happy 1:
                    xalign 0.7 yalign 1.0
                with fade
            pc "Yeah, it's time for sci--No, it's not."
            show latimer lab annoyed 1 with quick
            "Latimer bites her lip."
            l "B-but--"
            pc "No buts.{w} Goldman-sensei wants me to tour these girls around the school."
            "I look at my watch."
            pc "And it looks like lunch is about over anyway. Sorry, but I can't do it.{w} Maybe some other time."
            l "Fine."
            pc "C'mon, Haas-san, Cheit-san.{w} We should get something to eat before lunch ends."
            "I start to walk toward the cafeteria with Haas and Cheit following behind."
            p "Come visit me again, my darling!"
            hide pimentel with dissolve
            l "Alpha! Tomorrow! Right as lunch starts!{w} You'd better be here then!"
            hide latimer with dissolve
            $ persistent.seen_scenes.add("cr_012cex")
            jump cr_013
            
        "I'll just ignore her":
            jump cr_012e
    

label cr_012d:
    $ crrel.sather += 1
    $ crflag.first_bad = True
    #if crrel.sather >= 1 or CanSkip('cr_012dex'):
    #    if SkipMenu('cr_012d'):
    #        if crrel.sather >= 1:
    #            jump cr_012f
    #        jump cr_013
    
    if SkipMenu('cr_012d'):
        jump cr_013a
    if not renpy.showing("bg path 1"):
        scene bg path 1
        show cheit maid sly 1
        show haas summer sly 1 at left
        with fade
    pc "We should take a look at the main building. It's where we'll be most of the day, after all."
    "I take the lead."
    "First year classrooms are on the third floor, but there isn't much incentive to go up there right now."
    scene bg hall 1
    show haas summer annoyed 1:
        xalign 0.2 yalign 1.0
    show cheit maid serious 1 at left
    with fade
    "So we explore the first floor, the third year classrooms."
    c "Mitsuki-sama wishes to know why you are showing us the first floor."
    pc "It's a bit of a hassle to go all the way back up to the third floor.{w} It's okay, though. All the floors have pretty identical plans so if you know one floor you know the others."
    "Unless you're Shion, of course."
    show dwinelle summer worried 1 at right with dissolve
    "Speak of the devil."
    pc "Shion, what are you doing here? Did you get lost again?"
    d "Aniki!"
    extend " It really sucks.{w} Somebody wrecked this classroom.{w=0.5} {size=-5}By the way what's with the maid?{/size}"
    
    scene bg classroom 1 beatup with dissolve
    "She's right. The room's a mess.{w} Desks are thrown everywhere, some are even broken."
    d "It's really unfortunate. This is the third time this month!"
    "Third time? This is the first I've heard of it."
    scene bg hall 1
    show haas summer annoyed 1:
        xalign 0.2 yalign 1.0
    show cheit maid serious 1 at left
    show dwinelle summer worried 1 at right
    with dissolve
    d "If the culprit keeps doing this, I don't know if our budget can cover the damages. The school's budget is tight as it is."
    show cheit maid sly 1
    c "Mitsuki-sama would like to offer to pay the cost of the damaged desks."
    d "What, really?{w} Wait, who are you anyway?"
    pc "This is--"
    c "I am Cheit. This is Mitsuki-sama, daughter of the Haas Corporation."
    d "The Haas Corporation!? Aren't they that really big, really rich company?"
    d "I'd really like to take the offer, but I'm afraid."
    $ spname = 'Pretty Girl'
    sp "Well if it isn't Katanashi-kun."
    show cheit maid serious 1:
        linear 0.2 xalign -1.0
    show haas summer annoyed 1:
        linear 0.2 xalign -1.5
    show dwinelle summer worried 1:
        linear 0.2 xalign 0.0
    show sproul summer happy 1:
        xalign 2.0 yalign 1.0
        linear 0.2 xalign 0.9
    $ pcname = 'Katanashi'
    pc "It's Takanashi--{w=0.2}{nw}"
    $ pcname = 'Takanashi'
    extend "{w=0.2}No, it isn't that either."
    $ pcname = None
    d "Hey there, prez."
    pc "Even you're here, Sproul-sempai?"
    $ spname = 'Sproul'
    show sproul summer worried 1 with quick
    sp "It's a big problem for us in the student council.{w} Unfortunately, we don't have any clue at all who's behind it at all."
    sp "They left this behind, though."
    
    $ nvl_variant = "paper"
    $ narrator = Character(None, kind=nvlnar, what_prefix='', what_color="#000000FF") 
    nvl clear
    "{font=courbd.ttf}{size=+5}\n\n\n\n\n\n\nThis is BAD.{/size}{/font}{fast}"
    
    nvl clear
    
    $ narrator = regnar
    "The note was typed.{w} This \"Bad\" wants to be known, but..."
    $ nvl_variant = None
    sp "I don't know what to do."
    "Sproul-sempai looks so hopeless."
    pc "Don't worry.{w=0.2} Things'll turn out fine."
    pause 0.3
    show sproul summer happy 1 with quick
    sp "You sure know how to cheer a girl up, Arararagi-kun."
    $ persistent.seen_scenes.add("cr_12d")
    jump cr_012f
    
    sp "If you'll excuse us, then.{w} We have Student Council business to attend to."
    hide sproul
    hide dwinelle
    with moveoutright
    
    "I turn back to Haas and Cheit."
    
    show haas summer annoyed 1 at center
    show cheit maid serious 1 at right
    with dissolve
    
    pc "Sorry.{w=0.3} Looks like we don't have much time to tour around."
    hide haas with moveoutright
    c "Mitsuki-sama accepts your apology. However, she would like to offer her services to the school student council."
    hide cheit with moveoutright
    pc "Ah, okay, then."
    "They walk off following Sproul-sempai and Shion leaving me alone in the hallway."
    $ persistent.seen_scenes.add("cr_012dex")
    jump cr_013a
    
label cr_012e:
    $ crrel.twins += 2
    if SkipMenu('cr_012e'):
        jump cr_013a
    if not renpy.showing("bg club building 1"):
        scene bg club building 1
        show cheit maid sly 1
        show haas summer sly 1 at left
        show pimentel summer dramatic 1:
            xalign 1.03 yalign 1.0
        show latimer lab happy 1:
            xalign 0.7 yalign 1.0
            
    "I'll pretend she never said that."
    play music "music/lab_theme.ogg"
    l "See! Alpha even agrees with me."
    "I did no such thing!"
    l "Then let's go! Experiment 720: Electromagnetism START!"
    "She has a surprisingly strong grip for such a small girl."
    "I{w=0.2} can't{w=0.2} escape!"
    show pimentel summer happy 1 with quick
    p "Ohohohohohohohoho!"
    l "Waahahahahahahaha!"
    pc "Cheit-san! Haas-san! Help me! Please!"
    "There they are, frozen in horror (I hope).{w} They don't move to help me. I don't blame them.{w} Danger lurks nearby."
    "It's too much! I can't hold on."
    scene bg classroom 1
    with Fade(2.0, 2.0, 1.0, color="#FFFFFFFF")
    stop music fadeout 1.0
    "Wha?"
    "I'm in class again."
    "Was it all a dream?"
    "I look at the board. It's... history? Lunch just ended?"
    "Behind me are Haas and Cheit.{w} That part wasn't a dream."
    "No one seems to think anything weird has happened."
    show latimer summer happy 1 at right with dissolve
    "I catch sight of Latimer and she notices."
    "Then she whispers something horrible."
    l "Experiment success!"
    hide latimer with dissolve
    "It wasn't a dream."
    "What experiment?"
    "What horrible things did she do to my unconscious body?"
    "The world may never know."
    $ persistent.seen_scenes.add("cr_012e")
    jump cr_013a
    
label cr_012f:
    #if SkipMenu('cr_012f'):
    #    jump cr_013a
    if not renpy.showing("bg hall 1"):
        scene bg hall 1
        show sproul summer happy 1:
            xalign 0.9 yalign 1.0
        show dwinelle summer worried 1 at left
        with fade
    s "What's everyone doing here?"
    show dwinelle summer worried 1 at center with move
    show sather summer happy 1 at left with moveinleft
    "Sather walks down the hall toward us."    
    "Then she notices the broken class."
    show sather summer surprised 1 with quick
    s "WHAAAAT?!{w} Who did this?!"
    "I show her the note."
    pc "Somebody calling themselves 'Bad'."
    s "This is..."
    show sather summer annoyed 1 with quick
    "Sather is glaring again."
    "Maybe I should get out now."
    s "Class Rep."
    "Too late."
    s "Find the culprit."
    "Don't grab me like that!"
    pc "Why me?!"
    s "You're Class Rep! It's your duty!"
    pc "This is the student council's job! Right, Sproul-sempai?"
    "Help me out here!"
    "Sproul-sempai looks thoughtful for a moment."
    show sproul summer coy 1
    show dwinelle summer happy 1
    with dissolve
    sp "We're in your hands now, Otonashi-kun."
    hide dwinelle with moveoutright
    hide sproul with moveoutright
    "I stare as she and Shion walk off, leaving me alone with Sather."
    s "Tomorrow."
    hide sather with moveoutleft
    "Tomorrow what?"
    "Too late.{w} She's already gone."
    $ persistent.seen_scenes.add("cr_012f")

label cr_013:
    scene bg street 1 sunset
    with fade
    "School is over for the day."
    "Lunch--and the rest of the day, for that matter--went by uneventfully."
    "There wasn't much time to show Cheit and Haas anything else, but Cheit said that Haas didn't mind."
    "Then again, I'm not sure I can trust anything Cheit says."
    $ persistent.seen_scenes.add("cr_013")

label cr_013a:
    if SkipMenu('cr_013a'):
        jump cr_013achoice
    if not renpy.showing("bg street 1 sunset"):
        scene bg street 1 sunset
        with fade
    "I'm walking home alone again, but I've grown accustomed to it now. It still feels lonely."
    "Two months.{w} Has it really been that long?"
    "There's not much to do, other than walk."
    "No annoying girls.{w} No getting lost.{w} No one to talk to."
    "But I'm used to it now."
    "Out of the corner of my eye, I see a flier on a pole.{w} A job offer for the summer."
    "Room and board. Amazing pay. Reputable owner. In a great part of town."
    $ persistent.seen_scenes.add("cr_013a")
    
label cr_013achoice:
    menu:
        "We {i}are{/i} running a bit tight on money..."
        "Look into it":
            $ crrel.haas += 1
            $ crflag.took_flier = True
            jump cr_013b
        "Sounds too good to be true":
            jump cr_013c

label cr_013b:
    if SkipMenu('cr_013b'):
        jump cr_013d
    if not renpy.showing("bg street 1 sunset"):
        scene bg street 1 sunset
        with fade
    "This sounds like a good deal.{w} And I won't say no to a little pocket money, either."
    "The work doesn't look too hard either.{w} Something like an attendant or a babysitter?"
    "I take the flier from the pole."
    "Hopefully no one manages to apply before I do."
    Char("Voice") "{size=-10}Success.{/size}"
    "What was that?"
    pc "Anyone there?"
    "No reply."
    pc "I must be hearing things."
    "And I'm talking to myself, now, too."
    $ persistent.seen_scenes.add("cr_013b")
    jump cr_013d
    
label cr_013c:
    if SkipMenu('cr_013c'):
        jump cr_013d
    if not renpy.showing("bg street 1 sunset"):
        scene bg street 1 sunset
        with fade
    "It's too good to be true."
    "It's a bit shady, too.{w} Who would offer that much money for that kind of work?"
    "No, just forget about it."
    Char("Voice") "{size=-10}Damn.{w=0.2} Missed.{/size}"
    "Huh? Did someone say something?"
    pc "Anyone there?"
    "Looks like no one's here."
    "I better hurry home.{w} If I'm starting to hear things, who know what's wrong with me."
    $ persistent.seen_scenes.add("cr_013c")
    
label cr_013d:
    if SkipMenu('cr_013d'):
        jump cr_014
    scene bg classroom 1
    show goldman business glad 1
    with timeskip
    "Wait."
    pc "What did you say?"
    g "I said we need to start planning for our cultural festival activities.{w} I'm not gonna get showed up by Cloyne again this year."
    "That's not really a reasonable excuse, is it?"
    
    show goldman business happy 1 with quick
    g "So,{w=0.2} anyone got any suggestions?"
    "Who would have suggestions right here and now?"
    "As expected nobody speaks up."
    
    show goldman business serious 1 with quick
    g "Come on. Somebody's gotta have an idea."
    "Still no replies."
    
    show goldman business surprised 1 with quick
    g "Really?{w} Nobody has any replies?{w} Aw, man.{w=0.2} Cloyne's gonna rubbing it in my face for sure!"
    "I'm not sure I even know who this Cloyne is anyway."
    e "Sensei!"
    
    show goldman business serious 1 with quick
    show goldman business serious 1:
        linear 0.5 xalign 0.0
    show evans summer embarrassed 1:
        xalign 2.0 yalign 1.0
        linear 0.5 xalign 1.0
    pause 0.5
    "The most unexpected voice speaks out."
    g "Oh, Seat 4."
    e "How about...{w} How about..."
    "She's having so much trouble just trying to spit the words out."
    show evans summer determined 1 with quick
    e "How about a haunted house!"
    "The silence is deafening."
    show evans summer embarrassed 1 with dissolve
    show evans summer embarrassed 1:
        linear 0.1 xalign 1.01
    show evans summer embarrassed 1:
        linear 0.2 xalign 0.99
        linear 0.2 xalign 1.01
        repeat
    "Evans starts to fidget."
    Char("Boy A") "That sound good."
    Char("Girl A") "I don't know...{w} Seems a bit overplayed?"
    show evans summer embarrassed 1:
        linear 0.5 xalign 2.0
    show goldman business serious 1:
        linear 0.5 xalign 1.0

    show latimer summer happy 1:
        xalign -1.0 yalign 1.0
        linear 0.5 xalign 0.3
    pause 0.5
    p "Oooh!{w} I know, I know!"
    hide evans
    p "We've developed this great machine that could be used to tell the future!"
    "That sounds a bit far-fetched."
    p "Let's use it to make a fortune-telling booth!"
    image pimentel summer happy 1 flip = im.Flip(ImageReference("pimentel summer happy 1"), horizontal = True)
    show pimentel summer happy 1 flip:
        xalign -1.0 yalign 1.0
        linear 0.5 xalign 0.0
    pause 0.5
    l "I have been meaning to test it out.{w}{nw}"
    image pimentel summer lovestruck 1 flip = im.Flip(ImageReference("pimentel summer lovestruck 1"), horizontal = True)
    show pimentel summer lovestruck 1 flip with quick
    extend " Think of all the tests we could run!"
    Char("Girl A") "Now {i}that{/i} is different."
    Char("Girl B") "But if it's scientific, is it really fortune telling?"
    show pimentel summer lovestruck 1 flip:
        linear 0.5 xalign -1.0
    show latimer summer happy 1:
        linear 0.5 xalign -1.0
    show goldman business serious 1:
        linear 0.5 xalign 0.0
    show haas summer sly 1:
        xalign 3.0 yalign 1.0
        linear 0.5 xalign 0.9
    show cheit maid sly 1:
        xalign 2.0 yalign 1.0
        linear 0.5 xalign 1.0
    pause 0.5
    c "Mitsuki-sama would like to propose a maid cafe.{w} Mitsuki-sama believes there is nothing wrong with
        trying to earn a little extra money every now and then{nw}"
    hide pimentel
    hide latimer
    if crflag.first_bad:
        extend ", especially after recent events{nw}"
    extend "."
    Char ("Boy B") "Whoa! That means there will be even more maids!"
    Char ("Girl C") "Ew! I don't want to wear a maid outfit!"
    Char ("Girl D") "I don't know... Maybe it'll look really cute?"
    
    s "Um..."
    "Amidst the noise is a quiet voice."
    show haas summer sly 1:
        linear 0.5 xalign 3.0
    show cheit maid sly 1:
        linear 0.5 xalign 2.0
    show goldman business serious 1:
        linear 0.5 xalign 1.0
    show sather summer embarrassed 1:
        xalign -1.0 yalign 1.0
        linear 0.5 xalign 0.0
    pause 0.5
    s "How about a play?"
    hide haas
    hide cheit
    Char("Boy A") "A play?"
    Char("Boy C") "Tower's actually suggesting something?"
    show sather summer annoyed 1 with quick
    Char("Boy A") "Don't call her that while she's listening!"
    show sather summer happy 1 with quick
    Char("Girl A") "What kind of play?{w} You can't just suggest doing a play with suggesting what play."
    s "I have one in mind."
    show sather summer embarrassed 1 with quick
    extend " It's a mystery romance."
    Char("Girl B") "Oooh! A romance!"
    Char("Boy B") "Awesome! A mystery!{w} Sounds cool!"
    show sather summer embarrassed 1:
        linear 0.5 xalign -1.0
    show goldman business serious 1:
        linear 0.5 xalign 0.5
    pause 0.5
    hide sather
    show goldman business glad 1 with quick
    g "Now that's more like it!"
    show goldman business serious 1 with quick
    g "Seat 10, get up here and take the votes."
    "Why me?"
    g "'Cause you're the representative, right?"
    "Ugh, fine."
    hide goldman with dissolve
    "I write the choices on the board:{w} Haunted house.{w} Fortune teller's booth.{w} Maid cafe.{w} Play."
    pc "All right, then."
    pc "Write your vote on a slip of paper and bring it up here. I'll tally up the votes."
    "The voting proceeds and I count the votes up."
    pc "Eight...{w} Eight...{w} Eight...{w} Eight..."
    "Amazing. A 4-way tie.{w} Everyone stares in awe."
    pc "Uh... Let's try that again.{w} Try not to vote for the same thing, I guess?"
    "We vote again."
    pc "Eight.{w} Eight.{w} Eight.{w} And eight.{w} Another tie."
    pc "All right. One last time!"
    "...{w} Same results."
    pc "What the hell."
    Char("Girl A") "Uh... rep.{w} Did you vote?"
    "Did I vote?{w} No, I didn't."
    pc "Whoops."
    show goldman business glad 1 with dissolve
    g "Looks like this'll be easy, then."
    "How so?"
    g "Since Seat 10 over here is the only one who hasn't voted, and you guys can't decide among yourselves, he gets to decide."
    pc "What me?"
    g "It's only fair, right?"
    show goldman business serious 1 with quick
    extend " Don't worry. You don't have to pick now.{w} Just have your choice ready by tomorrow."
    show goldman business glad 1 with quick
    g "I'm gonna beat Cloyne this year for sure!"
    "This isn't for the athletic festival, you know."
    g "We're leaving it up to you."
    "The bell rings."
    g "Oh. Gotta go! See ya'll later!"
    hide goldman with easeoutright 
    "With Goldman gone, I'm assaulted by classmates."
    show latimer summer serious 1 at left
    show pimentel summer happy 1
    with dissolve
    l "You make sure you choose the fortune teller booth, Alpha.{w} Your master wills it!"
    show pimentel summer lovestruck 1 with quick
    p "Don't worry.{w} Darling will surely vote for his brides' suggestion."
    show latimer summer annoyed 1 with quick
    l "Your suggestion?! I suggested it remember?"
    pc "Uh..."
    "I feel a tug on my shirt."
    show evans summer determined 1:
        xalign -1.0 yalign 1.0
        ease 0.2 xalign 0.0
    show pimentel summer lovestruck 1:
        ease 0.2 xalign 1.0
    show latimer summer annoyed 1:
        ease 0.2 xalign 0.5
    pause 0.2
    e "Sempai.{w} Please choose the haunted house."
    "She looks incredibly serious about what she's saying."
    pc "I can't say I will but..."
    show evans summer determined 1:
        ease 0.2 xalign 1.0
    show pimentel summer lovestruck 1:
        ease 0.2 xalign 3.0
    show latimer summer annoyed 1:
        ease 0.2 xalign 2.5
    show haas summer sly 1:
        xalign -2.0 yalign 1.0
        ease 0.2 xalign 0.0
    show cheit maid sly 1:
        xalign -1.5 yalign 1.0
        ease 0.2 xalign 0.5
    pause 0.2
    c "I'm afraid Mitsuki-sama believes you're all mistaken.{w} A maid cafe is clearly the best choice for everyone."
    hide latimer
    hide pimentel
    show evans summer surprised 1 with quick
    e "What?"
    "I agree with Evans.{w} Please explain your logic."
    c "Working in the service industry will give you a better appreciation for your studies, isn't that right?"
    show evans summer surprised 1:
        ease 0.2 xalign 3.0
    show cheit maid sly 1:
        ease 0.2 xalign 2.5
    show haas summer sly 1:
        ease 0.2 xalign 2.2
    show sather summer happy 1:
        xalign -1.0 yalign 1.0
        ease 0.2 xalign 0.5
    pause 0.5
    show sather summer surprised 1
    pause 1.0
    show sather summer embarrassed 1 with quick
    s "What?"
    hide cheit
    hide haas
    hide evans
    pc "Uh, I thought you wanted to say something, too."
    show sather summer happy 1 with quick
    s "No.{w} Just pick what you like."
    "Maybe she warming back up to me again."
    if crflag.first_bad:
        show sather summer annoyed 1 with quick
        s "Besides, we have more important things we should worry about."
    pause 1.0
    show sather summer embarrassed 1 with quick
    s "Why are you still staring at me?"
    pc "Uh.{w=0.3} Sorry."
    hide sather with dissolve
    "I guess that's that, then.{w} I have the rest of the day to decide what we do for the cultural festival."
    "They all sound pretty promising, though."
    "Which is the best choice?"    
    $ persistent.seen_scenes.add("cr_013d")
    
label cr_014:
    if SkipMenu("cr_014"):
        jump cr_014choice
    scene bg classroom 1
    with timeskip
    "It's almost lunchtime.{w} Half the day is gone and I still don't know what I should choose."
    "It's not a hard decision, really.{w} I could just pick one and be done with it
    but...{w} I can't help but feel I don't want to let any of the girls down."
    "I can't even really pay attention to class at all."
    "I try to concentrate on the teacher but all I hear is gibberish."
    "Why can't I stop thinking about it?"
    "Who do I choose?"
    "Evans and her haunted house?{w} The twins and their fortune-telling machine?{w} Haas' maid cafe?{w} Sather's play?"
    d "Aniki!"
    show dwinelle summer glad 1 with dissolve
    pc "Huh, Dwinelle?{w} What are you doing here?"
    show dwinelle summer stern 1 with quick    
    d "What, I can't eat lunch with you anymore?"
    show dwinelle summer happy 1 with quick
    d "I just haven't had lunch with you for a while, you know?"
    pc "Yeah.{w} You've been busy."
    "It's been kind of lonely without you."
    if crflag.first_bad:
        pc "Any news on Bad yet?"
        show dwinelle summer dejected 1 with quick
        d "Unfortunately, no."
        pc "That's too bad."
        show dwinelle summer happy 1 with quick
    d "So how've you been?"
    pc "Okay, I guess."
    "A silence."
    show dwinelle summer worried 1 with quick
    "It's awkward."
    $ persistent.seen_scenes.add("cr_014")
    
label cr_014choice:
    menu:
        "What should I do?"
        "Ask what she would choose":
            jump cr_015
        "Go for lunch":
            jump cr_016
            
label cr_015:
    if SkipMenu("cr_015"):
        if crflag.first_bad:
            jump cr_015a
        if crflag.experiment_appointment:
            jump cr_015b
        jump cr_015c
    if not renpy.showing("bg classroom 1"):
        scene bg classroom 1
        show dwinelle summer worried 1
        with fade
    pc "Uh..."
    "How do I put this?{w} Might as well just spit it all out."
    pc "If you had to choose between a haunted house, a maid cafe, fortune-telling, and a play, which would you choose?"
    show dwinelle summer happy 1 with quick
    d "What?"
    pc "Haunted house, maid caf--"
    d "No. I mean why."
    "I wonder, too."
    pc "Goldman-sensei told me to decide the activity for the cultural festival."
    d "Now?"
    "I nod."
    "It {i}is{/i} kind of odd."
    $ persistent.seen_scenes.add("cr_015")
    
    if crflag.first_bad:
        jump cr_015a
    if crflag.experiment_appointment:
        jump cr_015b
    jump cr_015c
    
label cr_015a:
    $ crrel.sather += 1
    $ crflag.met_gate = True
    if SkipMenu("cr_015a"):
        $ sgname = "Sather's Sister"
        jump cr_017
    if not renpy.showing("bg classroom 1"):
        scene bg classroom 1
        show dwinelle summer happy 1
        with fade
    d "Well..."
    "Shion puts on a thoughtful face for a moment."
    d "If it were me, I'd choose the play.{w} It's a mystery, right?"
    pc "Huh, yeah.{w} How did you know?"
    show dwinelle summer glad 1 with quick
    "Shion just smiles like she always does when she knows something I don't."
    d "By the way..."
    pc "Hmm?"
    show dwinelle summer happy 1 with quick
    d "Have you noticed that girl out there?"
    "Shion points out the window."
    "Outside is a girl wearing a sailor uniform.{w} It looks like the uniform for the nearby girl's middle school."
    show dwinelle summer worried 1 with quick
    d "She looks kind of lost."
    "Funny that {i}you{/i} should point something like that out, Shion."
    d "Hey.{w} Let's go help her!"
    pc "Help her what?"
    d "I don't know. Help her!"
    pc "Fine, fine."
    "We head outside."
    
    scene bg gate 1
    show gate summer shocked 1
    with fade
    
    "The girl looks incredibly flustered."
    show dwinelle summer happy 1:
        xalign -1.0 yalign 1.0
        linear 0.5 xalign 0.0
    show gate summer shocked 1:
        linear 0.5 xalign 1.0
    d "What's the matter?"
    $ sgname = "Girl at the Gate"
    sg "Wh-what?"
    d "You look kind of lost.{w} Anything we can do to help?"
    show gate summer embarrassed 1 with quick
    sg "I... I'm not lost!"
    "Whoa. She's got a bit of a temper."
    pc "Well, then.{w} What's a middle schooler like you doing at the high school during lunchtime then."
    sg "W-Who are you!?"
    "Dwinelle whispers to me."
    d "Let me take care of it."
    d "You're looking for someone, right?"
    show gate summer mad 1 with quick
    "The girl nods."
    d "Well, what does he--or she--look like?"
    sg "It's my sister's...{w} Someone my sister knows."
    d "Your sister goes to this school?"
    "The girl nods."
    "Wait a minute.{w} This girl's starting to look very familiar."
    pc "Your sister wouldn't happen to be Touru Sather, would it?"
    sg "Wha... How did--?"
    show gate summer tearing 1 with quick
    $ sgname = "Sather's Sister"
    sg "It's your fault!"
    "What, my fault?"
    "The sudden outburst almost knocks me off balance."
    sg "You broke my sister's heart and smashed it into a million pieces!"
    "I did {i}what{/i} now?"
    show dwinelle summer stern 1 with quick
    d "What?!"
    pc "I don't know what she's talking about!"
    sg "Y-you p-playboy!"
    sg "First you break Sis's heart, then you pick her up again, and now you're dumping her again?{w} What kind of scum are you?!"
    pc "What are you talking about?!"
    sg "You're all she ever talks about now!{w} Did you know she came home crying when you broke up with her?"
    "Came home...{w} Wait a second. That must have been the day I became class rep."
    pc "I think you're misunde--"
    sg "How dare you pick her up again, you- you jerk!"
    d "I think you have a serious problem, Aniki."
    "Don't you side with her on this!"
    sg "Just you wait! I'll never forgive you!"
    hide gate with moveoutright
    show dwinelle summer worried 1 with quick
    d "Will she be all right."
    "I'm sure she'll be fine."
    $ persistent.seen_scenes.add("cr_015a")
    jump cr_017

label cr_015b:
    $ crrel.twins += 1
    if SkipMenu("cr_015b"):
        jump cr_017
    if not renpy.showing("bg classroom 1"):
        scene bg classroom 1
        show dwinelle summer worried 1
        with fade
    show dwinelle summer happy 1 with quick
    d "I would think..."
    show dwinelle summer glad 1 with quick
    d "A fortune-telling machine sounds awesome!"
    show dwinelle summer stern 1 with quick
    d "I've always been interested in things like mystery and occult."
    "You have?"
    show dwinelle summer happy 1 with quick
    "I'll be sure to visit your class for sure!"
    show latimer lab annoyed 1 at right with dissolve
    l "There you are, Alpha!{w} Did you forget? We've got a very important experiment to run today!"
    "I don't--"
    show dwinelle summer worried 1 with quick
    d "Well, I wanted to have lunch with you, but I looks like you have prior arrangements."
    hide dwinelle with dissolve
    "No! Don't go!"
    l "Come on."
    "I resist, but I know what's coming.{w} I feel a prick on my arm."
    scene bg black with irisout    
    scene bg classroom 1
    with fade
    "I wake up."
    "Why does this happen to me so often?"
    "Lunch is done and I'm sitting in the middle of class."
    "What did she do?"
    l "Success!"
    "I don't think I'll ever find out."
    $ persistent.seen_scenes.add("cr_015b")
    jump cr_017
    
label cr_015c:
    if SkipMenu("cr_015c"):
        jump cr_016
    if not renpy.showing("bg classroom 1"):
        scene bg classroom 1
        show dwinelle summer worried 1
        with fade
    d "That's not really a decision I can make easily."
    "I thought not."
    "I sigh."
    pc "Ah, well.{w} I guess I'll have to make the decision myself."
    d "That's how it should be, right?"
    pc "Uh, yeah."
    "She's right about that."
    "We sit awkwardly for a moment."
    d "So, wanna have lunch?"
    $ persistent.seen_scenes.add("cr_015c")
    jump cr_016
    
label cr_016:
    if crflag.took_flier:
        jump cr_016a
    $ crrel.evans += 1
    if SkipMenu("cr_016"):
        jump cr_017
    scene bg hall 1
    show dwinelle summer happy 1 at left
    with fade
    "The cafeteria is crowded."
    "Everyone is trying to get their lunches as quickly as possible.{w} Ironically, that means that waiting in line will take a lot longer."
    e "Sempai!"
    show evans summer happy 1 at right with dissolve
    "Evans appears out of nowhere."
    show dwinelle summer glad 1 with quick
    d "Oh! It's fall-down girl!"
    pc "Don't call her that."
    e "Have you made your decision yet, Sempai?"
    pc "Ah, not yet."
    show evans summer determined 1 with quick
    e "Please pick the haunted house!"
    show evans summer embarrassed 1 with quick
    e "Ah!"
    pc "Well, I can't tell you how the decision will turn out, but I'll keep your determination in mind."
    show evans summer glad 1 with quick
    e "Thanks!"
    hide evans with dissolve
    d "What was that all about?"
    pc "Uh, don't mind."
    show dwinelle summer stern 1 with quick
    d "Right."
    show dwinelle summer dejected 1 with quick
    "Well that was a mood-killer.{w} Even though we grab lunch together and eat at the same table,
    we don't really talk much at all."
    "We finish quickly."
    show dwinelle summer happy 1 with quick
    d "See ya!"
    hide dwinelle with dissolve
    "With that Shion and I part ways again.{w} Who knows how long until I'm with her again?"
    $ persistent.seen_scenes.add("cr_016")
    jump cr_017
    
label cr_016a:
    $ crrel.haas += 1
    if SkipMenu("cr_016a"):
        jump cr_017
    scene bg hall 1
    show dwinelle summer happy 1 at left
    with timeskip
    "The cafeteria is crowded."
    "Everyone is trying to get their lunches as quickly as possible.{w} Ironically, that means that waiting in line will take a lot longer."
    d "Hmm?{w} What's that?"
    pc "What's what?"
    "She points at my pocket.{w} The flier from yesterday is still in it."
    pc "It's a flier for a summer job."
    d "A summer job?"
    show dwinelle summer glad 1 with quick
    extend " Don't you remember what happened the last time you did that?"
    pc "Don't remind me."
    "Never answer a want ad for a restaurant without knowing for sure what they're for.{w} You might end up in a mascot
    costume on the hottest summer ever."
    d "Lemme see that."
    "She takes the flier from my hand before I can react."
    show dwinelle summer happy 1 with quick
    d "It looks like an ad for a live-in maid."
    "I grab the flier from her."
    pc "It's not for a maid."
    show dwinelle summer glad 1 with quick
    d "I'm just joking.{w} Sounds like a good deal."
    pc "Hopefully they take me, right?"
    "I buy myself some bread."
    d "Thank you."
    "Shion plucks one of the packages from my arms and tears it open."
    pc "Wha-- hey!"
    "I protest but it's an almost welcome feeling of nostalgia."
    "I almost wish that things had never changed."
    $ persistent.seen_scenes.add("cr_016a")
    jump cr_017
    
label cr_017:
    $ crflag.chosen_route = ChooseRoute(crrel, crflag)
    if crflag.chosen_route:
        jump cr_017a
    if SkipMenu("cr_017"):
        jump cr_018
    scene bg street 1 sunset
    with fade
    "School's over for the day now, and I'm walking alone again."
    "I'm really missing walking back with Shion now."
    "I just feel so hopeless.{w} I don't even have anything close to a decision in my mind, yet."
    pc "Argh! Why is this bothering me so much?!"
    Char("Little Girl") "Why is that man shouting?"
    Char("Mother") "Hush! Don't look at the crazy man."
    "Sorry, folks. Don't mind me."
    
    scene bg house 1 night
    with fade
    pc "I'm home."
    mom "Are you okay?"
    pc "Yeah, mom."
    mom "You sound tired."
    pc "I'll be fine."
    "I brush of my mother's prying and head right to my room."
    scene bg bedroom 1 night
    with fade
    "I don't even bother turning on the light.{w} I just lay on my bed worrying about tomorrow."
    $ persistent.seen_scenes.add("cr_017")
    jump cr_018
    
label cr_017a:
    if SkipMenu('cr_017a'):
        jump cr_018
    scene bg street 1 sunset
    with fade
    "I think after my talk with Shion, I came to realize what I wanted to choose."
    "I should thank her."
    pc "Thanks, Shion."
    "I say it out loud for no real reason."
    d "You're welcome."
    pc "Wha?!"
    show dwinelle summer glad 1 with dissolve
    pc "Shion?!"
    show dwinelle summer happy 1 with quick
    d "You're welcome, I said.{w} Though I don't know what you're thanking me for."
    pc "Ah.{w=0.2} It's nothing.{w} Don't you have student council duties?"
    "It's nice having you here, though."
    d "I realized that I haven't walked home with you in a while, so I told C-kun to do my work for me."
    "I get the feeling you're not telling me everything about that, Shion."
    "We walk in silence.{w} It's the silence between two friends who don't know how to talk to each other anymore."
    d "Hey, Aniki."
    pc "Yeah, Shion?"
    show dwinelle summer worried 1 with quick
    d "If I did something bad, you'd still be my Aniki, right?"
    "Did something bad...?{w} What would Shion consider bad?"
    pc "Well, I suppose it would depend on what you did."
    show dwinelle summer dejected 1 with quick
    extend " But I think I could forgive you for it anyway."
    # show dwinelle summer surprised 1 with quick
    # pause 0.5
    show dwinelle summer happy 1 with quick
    d "Thanks, Aniki."
    "Even if we see each other rarely, I get the feeling we still understand each other."
    "I hope."
    
    $ persistent.seen_scenes.add("cr_017a")
    jump cr_018
    
label cr_018:
    if crflag.chosen_route:
        $ renpy.jump('cr_018' + crflag.chosen_route)
    if SkipMenu("cr_018"):
        jump cr_bad1
    scene bg classroom 1
    show goldman business serious 1
    if not renpy.showing("bg black"):
        with timeskip
    else:
        with dissolve
    g "So, Seat 10.{w} Have you come to a decision?"
    "What do I say?"
    pc "Uh... sorry."
    g "What?"
    show goldman business stern 1 with quick
    g "I expected better of you."
    "He looks mad.{w} Why was it so hard to make the decision?"
    "Why did it have to turn out like this?"
    g "Sorry, class.{w} Looks like we'll have to this out ourselves."
    "I somehow get the feeling that I've been exclude from that statement."
    scene bg black with dissolve
    $ narrator = nvlnar
    "My story ends here."
    "The rest of the year, I felt like I was class representative in name only.{w} No one talked to me.{w} Everyday
    I just went through the motions."
    "I would take my tests and do my work, but everything just felt so empty."
    "I hope that, maybe someday, I won't regret this anymore."
    nvl clear
    $ persistent.seen_scenes.add("cr_018")
    jump cr_bad1
    
label cr_018s:
    if SkipMenu("cr_018s"):
        jump cr_019
    scene bg classroom 1
    show goldman business happy 1
    with fade
    g "So you've made your decision?"
    pc "Yeah."
    pause 1.0
    show goldman business serious 1 with quick
    g "Well then let's hear it!"
    hide goldman with dissolve
    "I take a deep breath.{w} I stand in front of the class and tell them all."
    pc "We, Class 1-C, will be doing a play for the cultural festival this year."
    s "Wha-- really?!"
    "You don't have to sound so surprised Sather."
    l "Aw, man! Subject Alpha didn't chose ours."
    p "Don't worry.{w} Maybe darling will change his mind...?"
    c "How unfortunate."
    e "...I wanted to have a haunted house."
    "Amidst the din, Sather walks up to me."
    show sather summer annoyed 1 with dissolve
    s "You didn't meet with me yesterday."
    "Oh, right. \"Tomorrow.\""
    pc "Sorry, with everything that was happening I forgot."
    if crflag.met_gate:
        "I wonder if she knows..."
        pc "I met your sister yesterday."
        show sather summer surprised 1 with quick
        s "Eh? Toko?"
        "Is that her name?"
        s "She didn't say anything weird, did she?"
        "I don't think she said anything that wasn't weird."
        pc "Don't worry."
    show sather summer happy 1 with quick
    "Looks like she's calmed down."
    s "I jumped the gun a bit there.{w} Yesterday was too soon."
    pc "What do you mean?"
    s "Now that we know about Bad, why would he attack during school hours--or while school is even in session at all?"
    "I don't think I understand what you're trying to say."
    s "That's why, you'll meet with me over the summer and we'll make sure it doesn't happen again."
    pc "But can we even--"
    Char("Girl A") "So Sather-san, what is this play we're doing, anyway?"
    show sather summer embarrassed 1 with quick
    s "It's called {i}Budget Cuts{/i}."
    s "I-I'll give everyone the copies of the scripts soon."
    hide sather with dissolve
    "With that, Sather disappears into the class."
    "I don't suppose I'll ever find out how we're going to get into the school during summer, will I?"
    show goldman business glad 1 with dissolve
    g "Then that's that!"
    g "We need to get to work right away.{w} Get these scripts out to us as quickly as possible!"
    s "Y-yes, sir!"
    g "I'll get the best of Cloyne yet!"
    $ persistent.seen_scenes.add("cr_018s")
    jump cr_019

label cr_018h:
    if SkipMenu("cr_018h"):
        jump cr_019
    scene bg classroom 1
    show goldman business serious 1
    with fade
    g "So, Seat 10.{w} What's the verdict?"
    pc "I've decided that we ought to do the maid cafe."
    g "The maid cafe?"
    s "What a pervert."
    Char("Girl C") "He just wants to see us dressed as maids!"
    p "How could you, my darling?"
    l "B-but Alpha!"
    e "... So no haunted house?"
    "I think I'm starting to regret choosing the maid cafe now."
    g "Whoa, calm down!"
    hide goldman with dissolve
    "Goldman-sensei rushes to try to keep the commotion low."
    show haas summer sly 1 at right
    show cheit maid sly 1 with dissolve
    c "Mitsuki-sama wishes to congratulate you on making the right decision."
    "\"Right decision\"?"
    c "But one does not simply walk into the business world.{w} You would do 
    well to gather experience before attempting to run a cafe."
    "Who says I'm running the cafe?"
    hide cheit 
    hide haas
    with dissolve
    "They're gone before I can say anything."
    "It does sound like a good idea though."
    "Maybe I'll end up taking this summer job.{w} It {i}does{/i} sound similar to 
    what a maid does. It might be good experience."
    $ persistent.seen_scenes.add("cr_018h")
    jump cr_019

label cr_018e:
    if SkipMenu("cr_018e"):
        jump cr_019
    scene bg classroom 1
    show goldman business serious 1
    with fade
    g "So, Seat 10. Have any idea what we're gonna do?"
    pc "I think we should go with the Haunted house idea."
    e "YES!"
    "What the?"
    hide goldman
    show evans summer surprised 1 at left with dissolve
    e "A-Ah!"
    pc "You seem really pleased about it."
    e "Well, ah..."
    pause 1.0
    show evans summer determined 1 with quick
    e "I really, really like horror!"
    "That... is completely unexpected from someone like you."
    show goldman business glad 1 at right with dissolve
    g "Looks like we're having a haunted house, then.{w} Let's get as much as we can
    done over the summer!"
    l "Can we at least have horror fortune-telling?"
    p "I think I have a few machines we can use for special effects."
    show evans summer glad 1
    e "Ah, thanks everyone!"
    "Evans' smile is amazingly bright."
    pc "I look forward to working with you."
    e "Me, too."
    $ persistent.seen_scenes.add("cr_018e")
    jump cr_019

label cr_018t:
    if SkipMenu("cr_018t"):
        jump cr_019
    scene bg classroom 1
    show goldman business serious 1
    with fade
    g "Time's up, Seat 10.{w} What have you got for us?"
    pc "I'm afraid I could come to no decision."
    show goldman business stern 1 with quick
    g "What really?"
    pc "I could come to no decision{w=0.5} except for the fortune-telling machine."
    show goldman business glad 1 with quick
    g "Hoo. You almost gave me a heart attack there."
    show pimentel summer lovestruck 1 at left with dissolve
    p "Oooh, I knew my darling would choose me in the end!"
    show latimer summer stern 1 at right with dissolve
    l "Test Subject Alpha."
    show latimer summer happy 1 with quick
    extend " Good job!"
    Char("Girl C") "Are we going to have to wear costumes?"
    Char("Girl B") "Of course, we are! What kind of fortune-telling doesn't have costumes?"
    show goldman business serious 1 with quick
    g "You guys already have the machine, right?"
    show pimentel summer happy 1 with dissolve
    p "Of course."
    l "We just need to work the kinks out."
    "Kinks?"
    pc "What kinks?"
    l "It kind of overheats.{w} A lot."
    p "Don't worry, darling! I'll fix it!"
    "It doesn't sound especially safe, now that I think about it."
    show goldman business glad 1 with quick
    g "Well, summer's coming up.{w} Looks like you'll have time to work on it."
    p "Did you hear that, darling?"
    l "Looks like you'll be around to do experiments all summer long, Alpha!"
    "Oh, no."
    p "Ohohohohoho!"
    l "Wahahahaha!"
    $ persistent.seen_scenes.add("cr_018t")
    jump cr_019
    
label cr_019:
    if SkipMenu('cr_019'):
        $ renpy.jump(crflag.chosen_route + "r_001")
    scene bg street 1 sunset
    with fade
    "Summer, huh?"
    "Come to think of it, I haven't really made any new friends since the beginning of the year."
    "Maybe this will be a chance for me to get to know new people."
    d "Aniki!"
    show dwinelle summer glad 1 with dissolve
    pc "Wha-- Shion?!"
    d "What's up?"
    pc "Aren't you supposed to have student council duties or something?"
    d "Don't worry, C-kun's doing my work again."
    pc "Again?"
    d "He doesn't mind."
    "I get the feeling he actually does."
    d "You looked deep in thought.{w} What's on your mind?"
    "I smile at her."
    pc "I'm just thinking about how this summer might be one of the best ones I've had for the longest time."
    show dwinelle summer worried 1 with quick
    d "That's good..."
    show dwinelle summer embarrassed 1 with quick
    "A spark."
    show dwinelle summer stern 1 with quick
    d "Wait, no it isn't!{w} It's only been two summers since I've met you!"
    "I start to run."
    hide dwinelle with quick
    extend " Shion is a bit slow on the uptake."
    d "Hey, Aniki!{w} Come back here!"
    d "Don't just say something like that and start running!{w} Do you want to get punished?!"
    pc "Nope!"
    "While Shion chases me back home, I can't help but think:"
    "Maybe--just maybe--my first year of high school will change my life."
    $ _window = False
    scene bg black with dissolve
    pause 1.0
    $ persistent.seen_scenes.add("cr_019")
    $ renpy.jump(crflag.chosen_route + "r_001")

label cr_bad1:
    $ narrator = regnar
    scene bg badend with Fade(0.2, 1.0, 1.0)
    pause 5.0
    scene bg black with dissolve
    menu:
        Character(None, window_style = 'sproul_opening') "Would you like to ask Sproul-sensei for help?"
        "Yes":
            jump cr_sproul1
        "No":
            pass
    return
    
label cr_sproul1:
    $ narrator = regnar
    if SkipMenu("cr_sproul1"):
        return
    scene bg classroom 1
    show sproul sensei worried 1
    with fade
    ss "Oh, my."
    ss "It looks like you've hit the very first dead end of this game."
    ss "Since this is a romance game, this means that you didn't focus enough on
    capturing one of the girls."
    show sproul sensei happy 1 with quick
    ss "Don't worry, though.{w} With Sproul-sensei here, we can figure it out together!"
    ss "I've heard Haas-chan can be a bit selfish, but she really appreciates people who 
    are willing to work."
    ss "You might want to help out Evans-chan as often as you can, too.{w} I've heard 
    she eats at the cafeteria during lunch."
    ss "Pimentel-chan and Latimer-chan can be kind of pushy.{w} Maybe you could try 
    to use reverse psychology when it comes to them?"
    ss "Sather-chan can be difficult to be nice to, but she appreciates people who can
    stand up for themselves and others.{w} She eats lunch in the classroom. Maybe you
    could find her there?"
    pause 0.5
    ss "Oh. Looks like time's up!"
    show sproul sensei glad 1 with quick
    ss "Start again and try to make the right decisions this time."
    ss "I hope I don't have to see you again, Ric-kun."
    $ persistent.seen_scenes.add("cr_sproul1") 
    return
