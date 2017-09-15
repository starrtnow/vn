# You can place the script of your game in this file.

init:
    python:        
        
        def Char(name, _color=None):
            if _color: return Character(name, color=_color, kind=talk)
            else: return Character(name, kind=talk)
        
        def MoveInRight(time):
            return MoveTransition(time, enter_factory=MoveIn((1.0,1.0,0.0,1.0)))
        
        def MoveInLeft(time):
            return MoveTransition(time, enter_factory=MoveIn((0.0,1.0,1.0,1.0)))
            
        # Special dict object with attribute getters and setters
        class AttrDict(dict):
            def __init__(self, init={}):
                dict.__init__(self, init)

            def __getstate__(self):
                return self.__dict__.items()

            def __setstate__(self, items):
                for key, val in items:
                    self.__dict__[key] = val

            def __repr__(self):
                return "%s(%s)" % (self.__class__.__name__, dict.__repr__(self))

            def __setitem__(self, key, value):
                return super(AttrDict, self).__setitem__(key, value)

            def __getitem__(self, name):
                return super(AttrDict, self).__getitem__(name)

            def __delitem__(self, name):
                return super(AttrDict, self).__delitem__(name)

            __getattr__ = __getitem__
            __setattr__ = __setitem__

            def copy(self):
                ch = AttrDict(self)
                return ch
        
        def show_display_say_two_window(who, what, who_args = {}, what_args = {}, window_args = {}, image = False, two_window = True, **kwargs):
            if who == None:
                return renpy.show_display_say(who, what, who_args, what_args, window_args, image, two_window = False, **kwargs)
            else:
                return renpy.show_display_say(who, what, who_args, what_args, window_args, image, two_window = True, **kwargs)
        
        # Special characters for templates and whatnot.
        talk = Character(None, what_prefix='"', what_suffix='"', window_left_padding=20, window_right_padding=20, show_two_window=True, who_xalign = 0.5, show_function = show_display_say_two_window)
        regnar = Character(None, window_left_padding=20, window_right_padding=20)
        nvlnar = Character(None, kind=nvl, what_prefix='   ', window_left_padding=20, window_right_padding=20)
        narrator = regnar
        
        # Main characters        
        nvlchr = Character(None, what_prefix='  "', what_suffix='"', window_left_padding=20, window_right_padding=20, kind=nvl)
        pc = DynamicCharacter('pcname', kind=talk, color="#8080D0FF")
        pcnvl = Character(kind=nvlchr)
        pcname = None
        d = DynamicCharacter('dname', kind=talk, color ="#D09090FF")
        dnvl = Character(kind=nvlchr)
        dname = 'Dwinelle'
        e = DynamicCharacter('ename', kind=talk, color ="#90D090FF")
        envl = Character(kind=nvlchr)
        ename = 'Evans'
        p = DynamicCharacter('pname', kind=talk, color ="#D090D0FF")
        pnvl = Character(kind=nvlchr)
        pname = 'Pimentel'
        l = DynamicCharacter('lname', kind=talk, color = "#A0A0D0FF")
        lnvl = Character(kind=nvlchr)
        lname = 'Latimer'
        h = DynamicCharacter('hname', kind=talk)
        hnvl = Character(kind=nvlchr)
        hname = 'Haas'
        c = DynamicCharacter('cname', kind=talk, color = "#D0B0C5FF")
        hnvl = Character(kind=nvlchr)
        cname = 'Cheit'
        s = DynamicCharacter('sname', kind=talk, color = "#FFC040FF")
        snvl = Character(kind=nvlchr)
        sname = 'Sather'
        sg = DynamicCharacter('sgname', kind=talk, color = "#80C080FF")
        sgnvl = Character(kind=nvlchr)
        sgname = 'Sather\'s Sister'
        sp = DynamicCharacter('spname', kind=talk, color = "#6060E0FF")
        spnvl = Character(kind=nvlchr)
        spname = 'Sproul'
        ss = DynamicCharacter('ssname', kind=talk, color = "#6060E0FF")
        ssnvl = Character(kind=nvlchr)
        ssname = 'Sproul-sensei'
        g = DynamicCharacter('gname', kind=talk, color="#D05050FF")
        gnvl = Character(kind=nvlchr)
        gname = "Goldman-sensei"
        
        mom = Character('Mom', kind=talk)
        
        scenenames = AttrDict({})
        sn = scenenames
        sn.cr_001 = "The First Morning"
        sn.cr_002 = "Lost"
        sn.cr_003 = "Gold and Blue"
        sn.cr_004 = "Maid"
        sn.cr_005 = "Fast Friends"
        sn.cr_006 = "Return of the Apologetic Girl"
        sn.cr_007a = "To the Rescue"
        sn.cr_007b = "To the Infirmary"
        sn.cr_008 = "From On High"
        sn.cr_009 = "Love at First Sight"
        sn.cr_010 = "Walking Alone"
        sn.cr_011 = "The Transfer Student"
        sn.cr_012 = "The Tour"
        sn.cr_012a = "Chat with Cheit over Lunch"
        sn.cr_012b = "Chatting at the Pool"
        sn.cr_012c = "Visiting the Clubs"
        sn.cr_012d = "This Is BAD"
        sn.cr_012e = "It's Time for Science!"
        sn.cr_012f = "We're in Your Hands"
        sn.cr_013a = "Walking Alone Again"
        sn.cr_013b = "Job Offer"
        sn.cr_013c = "Too Good"
        sn.cr_013d = "The Vote, The Vote 2, and The Vote 3: Resurrection"
        sn.cr_014 = "Return of the Dwinelle"
        sn.cr_015 = "Dwinelle's Opinion"
        sn.cr_015a = "Overprotective Little Sister"
        sn.cr_015b = "Captured"
        sn.cr_015c = "I can't decide..."
        sn.cr_016 = "Lunch with Dwinelle"
        sn.cr_016a = "Summer Jobs"
        sn.cr_017 = "Still Alone"
        sn.cr_017a = "Walking with Dwinelle"
        sn.cr_018 = "Indecisive"
        sn.cr_018s = "Choosing the Play"
        sn.cr_018h = "Maid Cafe"
        sn.cr_018e = "Let's Have a Haunted House"
        sn.cr_018t = "The Science of Fortune"
        sn.cr_019 = "Back to Before"
        sn.cr_sproul1 = "Sproul-sensei: Indecisive"

        scenes = dict()
        scenes["cr_001"] = "The First Morning"
        scenes["cr_002"] = "Lost"
        scenes["cr_003"] = "Gold and Blue"
        scenes["cr_004"] = "Maid"
        scenes["cr_005"] = "Fast Friends"
        scenes["cr_006"] = "Return of the Apologetic Girl"
        scenes["cr_007a"] = "To the Rescue"
        scenes["cr_007b"] = "To the Infirmary"
        scenes["cr_008"] = "From On High"
        scenes["cr_009"] = "Love at First Sight"
        scenes["cr_010"] = "Walking Alone"
        scenes["cr_011"] = "The Transfer Student"
        scenes["cr_012"] = "The Tour"
        scenes["cr_012a"] = "Chat with Cheit over Lunch"
        scenes["cr_012b"] = "Chatting at the Pool"
        scenes["cr_012c"] = "Visiting the Clubs"
        scenes["cr_012d"] = "This Is BAD"
        scenes["cr_012e"] = "It's Time for Science!"
        scenes["cr_012f"] = "We're in Your Hands"
        scenes["cr_013a"] = "Walking Alone Again"
        scenes["cr_013b"] = "Job Offer"
        scenes["cr_013c"] = "Too Good"
        scenes["cr_013d"] = "The Vote, The Vote 2, and The Vote 3: Resurrection"
        scenes["cr_014"] = "Return of the Dwinelle"
        scenes["cr_015"] = "Dwinelle's Opinion"
        scenes["cr_015a"] = "Overprotective Little Sister"
        scenes["cr_015b"] = "Captured"
        scenes["cr_015c"] = "I can't decide..."
        scenes["cr_016"] = "Lunch with Dwinelle"
        scenes["cr_016a"] = "Summer Jobs"
        scenes["cr_017"] = "Still Alone"
        scenes["cr_017a"] = "Walking with Dwinelle"
        scenes["cr_018"] = "Indecisive"
        scenes["cr_018s"] = "Choosing the Play"
        scenes["cr_018h"] = "Maid Cafe"
        scenes["cr_018e"] = "Let's Have a Haunted House"
        scenes["cr_018t"] = "The Science of Fortune"
        scenes["cr_019"] = "Back to Before"
        scenes["cr_sproul1"] = "Sproul-sensei: Indecisive"

        scene_order = ["cr_001",
        "cr_002",
        "cr_003",
        "cr_004",
        "cr_005",
        "cr_006",
        "cr_007a", "cr_007b",
        "cr_008",
        "cr_009",
        "cr_010",
        "cr_011",
        "cr_012", "cr_012a", "cr_012b", "cr_012c", "cr_012d", "cr_012e", "cr_012f",
        "cr_013a", "cr_013b", "cr_013c", "cr_013d",
        "cr_014",
        "cr_015",
        "cr_015a", "cr_015b",  "cr_015c",
        "cr_016", "cr_016a",
        "cr_017", "cr_017a",
        "cr_018", "cr_018s",
        "cr_018h", "cr_018e", "cr_018t",
        "cr_019",
        "cr_sproul1"]
        
        quick = Dissolve(0.1)
        timeskip = Fade(0.5, 1.0, 0.5)
        
        far_right = Position(xpos = 2.0, xanchor=2.0, ypos=1.0, yanchor=1.0)
        far_left = Position(xpos = -1.0, xanchor=-1.0, ypos=1.0, yanchor=1.0)
        
        persistent.seen_scenes = Set()
        persistent.use_persistent = True
        persistent.skip_all = True
        
        def ChooseRoute(rel, flag):
            if rel.sather >= 2 and flag.first_bad:
                return "s"
            if rel.evans >= 2:
                return "e"
            if rel.twins >= 3:
                return "t"
            if rel.haas >= 2 and flag.took_flier:
                return "h"
            else:
                return None
        
        def JumpPrologue(label):
            renpy.show_display_say(None, "hello")
            _intra_jumps(label, None)
            
        def CanSkip(s):
            return (renpy.seen_label(s) and persistent.allow_skipping) or (getattr(persistent, s) and persistent.use_persistent) or (persistent.skip_all)
            
        def SkipMenu(s):
            return SkipMenuBool(s, CanSkip(s))
        
        def SkipMenuBool(s, bool):
            if bool:
                if not renpy.showing("bg skipscreen"):
                    _window = False
                    renpy.scene()
                    renpy.show("bg skipscreen")
                    renpy.with_statement(dissolve)
                if s in scenenames: 
                    Character(None, kind=regnar, interact=False)("You have already seen the scene \"%s\". Would you like to skip it?{fast}" % (sn[s]))
                else:
                    Character(None, kind=regnar, interact=False)("You have already seen this scene. Would you like to skip it?{fast}")
                ret = renpy.display_menu( [("Yes", True),  ("No", False)] )
                _window = True
                return ret
            _window = True
            return False
            
    
# The game starts here.
label start:
    $ renpy.music.stop(fadeout=1)
    jump cr_001
    
label splashscreen:
    $  right = Position(xpos = 1.0, xanchor =  0.8)
    scene bg black
    show haas summer sly 1 at right
    $ narrator = nvlnar
    Character(None, kind=nvl) "\nDear Player\n{fast}{nw}"
    "Thank you for trying out this game.{fast}{nw}"
    "Be warned, this is only a demo, and very unfinished at that. We haven't added much color, and CGs are absent.{fast}{nw}"
    "Regardless, we hope you enjoy what we {i}do{/i} have. Hopefully the incompleteness does not deter you from playing the game.{fast}{nw}"
    "If you have any questions or comments, please send an email to projectvnad@gmail.com or visit our blog at projectvnad.blogspot.com. We hope to finish the game someday, so critiques and encouragement are welcome.\n\n{fast}{nw}"
    Character(None, kind=nvl, what_xalign=1.0, what_first_indent = 500) "- Canal{fast}"
    nvl clear
    $ narrator = regnar
    return

label demo_end:
    scene bg classroom 1
    show sproul sensei happy 1
    with timeskip
    ss "Oh, looks like you've reached the end of the demo.{w} Hopefully you've enjoyed yourselves."
    ss "Since this is only a demo, you won't be able to see the real endings of the game."
    ss "If you want to see more of us, send an email to ProjectVNAD@gmail.com or visit their blog at ProjectVNAD.blogspot.com."
    show sproul sensei glad 1
    ss "We hope to see you again really soon!"
    scene bg black
    with fade
