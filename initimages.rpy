init:
    python:
        def DreamPortrait(name, outfit, emotion, pose, w, h, x):
            return im.Recolor(MakePortrait(name, outfit, emotion, pose, w, h, x), rmul = 10, gmul = 10, bmul = 10)
            
        def MakePortrait(name, outfit, emotion, pose, w, h, x):
            f = "portraits/" + name + "/" + outfit + "_" + emotion + "_" + str(pose) + ".png"
            r, g, b = 255, 255, 255
            #if name == "sather":
            #    r, g, b = 255, 200, 0
            #elif name == "dwinelle":
            #    r, g, b = 255, 150, 150
            #elif name == "gate":
            #    r, g, b = 150, 255, 150
            return im.Recolor(im.FactorScale(im.Crop(im.Image(f, xanchor=x), 0, 0, w, h), 0.667), rmul = r, gmul = g, bmul = b)
            
        def MakeBG(name, num):
           return im.Image("bg/" + name + "_" + str(num) + ".jpg")

    image bg black = Solid("#000000")
    image bg blue = Solid("#202030")
    image bg skipscreen = im.Recolor("bg/skipscreen.jpg", rmul = 100, gmul = 90, bmul = 80)
    image bg badend = "bg/badend.jpg"
    
    ########################################################################
    
    # DWINELLE
    $ w, h, x = 651, 830, 266
    
    # Summer Uniform
    image dwinelle summer annoyed 1 = MakePortrait("dwinelle", "summer", "annoyed", 1, w, h, x)
    image dwinelle summer dejected 1 = MakePortrait("dwinelle", "summer", "dejected", 1, w, h, x)
    image dwinelle summer embarrassed 1 = MakePortrait("dwinelle", "summer", "embarrassed", 1, w, h, x)
    image dwinelle summer glad 1 = MakePortrait("dwinelle", "summer", "glad", 1, w, h, x)
    image dwinelle summer happy 1 = MakePortrait("dwinelle", "summer", "happy", 1, w, h, x)
    image dwinelle summer mad 1 = MakePortrait("dwinelle", "summer", "mad", 1, w, h, x)
    image dwinelle summer worried 1 = MakePortrait("dwinelle", "summer", "worried", 1, w, h, x)
    image dwinelle summer stern 1 = MakePortrait("dwinelle", "summer", "stern", 1, w, h, x)
    
    # Winter Uniform
    image dwinelle winter annoyed 1 = MakePortrait("dwinelle", "winter", "annoyed", 1, w, h, x)
    image dwinelle winter dejected 1 = MakePortrait("dwinelle", "winter", "dejected", 1, w, h, x)
    image dwinelle winter embarrassed 1 = MakePortrait("dwinelle", "winter", "embarrassed", 1, w, h, x)
    image dwinelle winter glad 1 = MakePortrait("dwinelle", "winter", "glad", 1, w, h, x)
    image dwinelle winter happy 1 = MakePortrait("dwinelle", "winter", "happy", 1, w, h, x)
    image dwinelle winter mad 1 = MakePortrait("dwinelle", "winter", "mad", 1, w, h, x)
    image dwinelle winter worried 1 = MakePortrait("dwinelle", "winter", "worried", 1, w, h, x)
    image dwinelle winter stern 1 = MakePortrait("dwinelle", "winter", "stern", 1, w, h, x)
    
    # Dream Dwinelle
    image dwinelle dream annoyed 1 = DreamPortrait("dwinelle", "winter", "annoyed", 1, w, h, x)
    image dwinelle dream dejected 1 = DreamPortrait("dwinelle", "winter", "dejected", 1, w, h, x)
    image dwinelle dream embarrassed 1 = DreamPortrait("dwinelle", "winter", "embarrassed", 1, w, h, x)
    image dwinelle dream glad 1 = DreamPortrait("dwinelle", "winter", "glad", 1, w, h, x)
    image dwinelle dream happy 1 = DreamPortrait("dwinelle", "winter", "happy", 1, w, h, x)
    image dwinelle dream mad 1 = DreamPortrait("dwinelle", "winter", "mad", 1, w, h, x)
    image dwinelle dream worried 1 = DreamPortrait("dwinelle", "winter", "worried", 1, w, h, x)
    image dwinelle dream stern 1 = DreamPortrait("dwinelle", "winter", "stern", 1, w, h, x)
    
    # EVANS
    $ w, h, x = 466, 760, 201
    
    # Summer Uniform
    image evans summer annoyed 1 = MakePortrait("evans", "summer", "annoyed", 1, w, h, x)
    image evans summer glad 1 = MakePortrait("evans", "summer", "glad", 1, w, h, x)
    image evans summer happy 1 = MakePortrait("evans", "summer", "happy", 1, w, h, x)
    image evans summer surprised 1 = MakePortrait("evans", "summer", "surprised", 1, w, h, x)
    image evans summer worried 1 = MakePortrait("evans", "summer", "worried", 1, w, h, x)
    image evans summer embarrassed 1 = MakePortrait("evans", "summer", "embarrassed", 1, w, h, x)
    image evans summer determined 1 = MakePortrait("evans", "summer", "determined", 1, w, h, x)
    
    # Winter Uniform
    image evans winter annoyed 1 = MakePortrait("evans", "winter", "annoyed", 1, w, h, x)
    image evans winter glad 1 = MakePortrait("evans", "winter", "glad", 1, w, h, x)
    image evans winter happy 1 = MakePortrait("evans", "winter", "happy", 1, w, h, x)
    image evans winter surprised 1 = MakePortrait("evans", "winter", "surprised", 1, w, h, x)
    image evans winter worried 1 = MakePortrait("evans", "winter", "worried", 1, w, h, x)
    image evans winter embarrassed 1 = MakePortrait("evans", "winter", "embarrassed", 1, w, h, x)
    image evans winter determined 1 = MakePortrait("evans", "winter", "determined", 1, w, h, x)
    
    # SATHER
    $ w, h, x = 482, 1000, 216
    
    # Summer Uniform
    image sather summer annoyed 1 = MakePortrait("sather", "summer", "annoyed", 1, w, h, x)
    image sather summer confused 1 = MakePortrait("sather", "summer", "confused", 1, w, h, x)
    image sather summer embarrassed 1 = MakePortrait("sather", "summer", "embarrassed", 1, w, h, x)
    image sather summer happy 1 = MakePortrait("sather", "summer", "happy", 1, w, h, x)
    image sather summer surprised 1 = MakePortrait("sather", "summer", "surprised", 1, w, h, x)
    
    # Winter Uniform
    image sather winter annoyed 1 = MakePortrait("sather", "winter", "annoyed", 1, w, h, x)
    image sather winter confused 1 = MakePortrait("sather", "winter", "confused", 1, w, h, x)
    image sather winter embarrassed 1 = MakePortrait("sather", "winter", "embarrassed", 1, w, h, x)
    image sather winter happy 1 = MakePortrait("sather", "winter", "happy", 1, w, h, x)
    image sather winter surprised 1 = MakePortrait("sather", "winter", "surprised", 1, w, h, x)
    
    # HAAS
    $ w, h, x = 680, 740, 322
    
    # Casual Dress
    image haas casual annoyed 1 = MakePortrait("haas", "casual", "annoyed", 1, w, h, x)
    image haas casual sly 1 = MakePortrait("haas", "casual", "sly", 1, w, h, x)
    
    # Summer Uniform
    image haas summer annoyed 1 = MakePortrait("haas", "summer", "annoyed", 1, w, h, x)
    image haas summer sly 1 = MakePortrait("haas", "summer", "sly", 1, w, h, x)
    
    # CHEIT
    $ w, h, x = 377, 900, 176
    
    # Maid Uniform
    image cheit maid happy 1 = MakePortrait("cheit", "maid1", "happy", 1, w, h, x)
    image cheit maid serious 1 = MakePortrait("cheit", "maid1", "serious", 1, w, h, x)
    image cheit maid sly 1 = MakePortrait("cheit", "maid1", "sly", 1, w, h, x)
    
    # GOLDMAN
    $ w, h, x = 509, 930, 187
    
    # Business Dress
    image goldman business glad 1 = MakePortrait("goldman", "business", "glad", 1, w, h, x)
    image goldman business happy 1 = MakePortrait("goldman", "business", "happy", 1, w, h, x)
    image goldman business serious 1 = MakePortrait("goldman", "business", "serious", 1, w, h, x)
    image goldman business stern 1 = MakePortrait("goldman", "business", "stern", 1, w, h, x)
    image goldman business surprised 1 = MakePortrait("goldman", "business", "surprised", 1, w, h, x)
    
    # LATIMER
    $ w, h, x = 354, 750, 168
    
    # Labcoat
    image latimer lab annoyed 1 = MakePortrait("latimer", "lab", "annoyed", 1, w, h, x)
    image latimer lab glad 1 = MakePortrait("latimer", "lab", "glad", 1, w, h, x)
    image latimer lab happy 1 = MakePortrait("latimer", "lab", "happy", 1, w, h, x)
    image latimer lab serious 1 = MakePortrait("latimer", "lab", "serious", 1, w, h, x)
    image latimer lab stern 1 = MakePortrait("latimer", "lab", "stern", 1, w, h, x)
    
    # Summer Uniform
    image latimer summer annoyed 1 = MakePortrait("latimer", "summer", "annoyed", 1, w, h, x)
    image latimer summer glad 1 = MakePortrait("latimer", "summer", "glad", 1, w, h, x)
    image latimer summer happy 1 = MakePortrait("latimer", "summer", "happy", 1, w, h, x)
    image latimer summer serious 1 = MakePortrait("latimer", "summer", "serious", 1, w, h, x)
    image latimer summer stern 1 = MakePortrait("latimer", "summer", "stern", 1, w, h, x)
    
    # Winter Uniform
    image latimer winter annoyed 1 = MakePortrait("latimer", "winter", "annoyed", 1, w, h, x)
    image latimer winter glad 1 = MakePortrait("latimer", "winter", "glad", 1, w, h, x)
    image latimer winter happy 1 = MakePortrait("latimer", "winter", "happy", 1, w, h, x)
    image latimer winter serious 1 = MakePortrait("latimer", "winter", "serious", 1, w, h, x)
    image latimer winter stern 1 = MakePortrait("latimer", "winter", "stern", 1, w, h, x)
    
    # PIMENTEL
    $ w, h, x = 390, 755, 156
    
    # Summer Uniform
    image pimentel summer dramatic 1 = MakePortrait("pimentel", "summer", "dramatic", 1, w, h, x)
    image pimentel summer happy 1 = MakePortrait("pimentel", "summer", "happy", 1, w, h, x)
    image pimentel summer lovestruck 1 = MakePortrait("pimentel", "summer", "lovestruck", 1, w, h, x)
    image pimentel summer stern 1 = MakePortrait("pimentel", "summer", "stern", 1, w, h, x)
    image pimentel summer worried 1 = MakePortrait("pimentel", "summer", "worried", 1, w, h, x)
    
    # Winter Uniform
    image pimentel winter dramatic 1 = MakePortrait("pimentel", "winter", "dramatic", 1, w, h, x)
    image pimentel winter happy 1 = MakePortrait("pimentel", "winter", "happy", 1, w, h, x)
    image pimentel winter lovestruck 1 = MakePortrait("pimentel", "winter", "lovestruck", 1, w, h, x)
    image pimentel winter stern 1 = MakePortrait("pimentel", "winter", "stern", 1, w, h, x)
    image pimentel winter worried 1 = MakePortrait("pimentel", "winter", "worried", 1, w, h, x)
    
    # SPROUL
    $ w, h, x = 393, 790, 180
    
    # Summer Uniform
    image sproul summer coy 1 = MakePortrait("sproul", "summer", "coy", 1, w, h, x)
    image sproul summer glad 1 = MakePortrait("sproul", "summer", "glad", 1, w, h, x)
    image sproul summer happy 1 = MakePortrait("sproul", "summer", "happy", 1, w, h, x)
    image sproul summer worried 1 = MakePortrait("sproul", "summer", "worried", 1, w, h, x)
    
    # SPROUL-SENSEI    
    $ w, h, x = 372, 790, 174
    
    image sproul sensei coy 1 = MakePortrait("sproul", "sensei", "coy", 1, w, h, x)
    image sproul sensei glad 1 = MakePortrait("sproul", "sensei", "glad", 1, w, h, x)
    image sproul sensei happy 1 = MakePortrait("sproul", "sensei", "happy", 1, w, h, x)
    image sproul sensei worried 1 = MakePortrait("sproul", "sensei", "worried", 1, w, h, x)
    
    # GATE
    $ w, h, x = 592, 770, 275
    
    # Summer Uniform
    image gate summer embarrassed 1 = MakePortrait("gate", "summer", "embarrassed", 1, w, h, x)
    image gate summer happy 1 = MakePortrait("gate", "summer", "happy", 1, w, h, x)
    image gate summer mad 1 = MakePortrait("gate", "summer", "mad", 1, w, h, x)
    image gate summer shocked 1 = MakePortrait("gate", "summer", "shocked", 1, w, h, x)
    image gate summer tearing 1 = MakePortrait("gate", "summer", "tearing", 1, w, h, x)
    
    
    ########################################################################
    # BACKGROUNDS
    
    image bg classroom 1 = MakeBG("classroom", 1)
    image bg classroom 2 = MakeBG("classroom", 2)
    
    image bg classroom 1 beatup = im.Recolor(MakeBG("classroom", 1),gmul = 0, bmul = 0)
    image bg classroom 1 faded = im.Recolor(MakeBG("classroom", 1), rmul = 40, gmul = 20, bmul = 20)
        
    image bg hall 1 = MakeBG("hall", 1)
    image bg hall 1 sunset = im.Recolor(MakeBG("hall", 1), gmul = 120, bmul = 50)
    
    image bg outside 1 = MakeBG("outside", 1)
    
    image bg workstation 1 = MakeBG("workstation", 1)
    
    image bg haas mansion 1 = MakeBG("haas_mansion", 1)
    image bg haas entrance 1 = MakeBG("haas_entrance", 1)
    image bg haas dining 1 = MakeBG("haas_dining", 1)
    image bg haas library 1 = MakeBG("haas_library", 1)
    image bg haas room 1 = MakeBG("haas_room", 1)
    image bg haas room 2 = MakeBG("haas_room", 2)
    image bg haas party 1 = MakeBG("haas_party", 1)
    
    image bg library 1 = MakeBG("library", 1)
    image bg library 2 = MakeBG("library", 2)
    
    image bg sky 1 = MakeBG("sky", 1)
    
    image bg house 1 = MakeBG("house", 1)
    image bg house 1 night = im.Recolor(MakeBG("house", 1), rmul = 10, gmul = 10, bmul = 120)
    image bg bedroom 1 = MakeBG("bedroom", 1)
    image bg bedroom 1 night = im.Recolor(MakeBG("bedroom", 1), rmul = 10, gmul = 10, bmul = 100)
    
    image bg street 1 = MakeBG("street", 1)
    image bg street 1 sunset = im.Recolor(MakeBG("street", 1), gmul = 80, bmul = 20)
    
    image bg evans house 1 = MakeBG("evans_house", 1)
    image bg evans wall 1 = MakeBG("evans_wall", 1)
    image bg evans street 1 = MakeBG("evans_street", 1)
    
    image bg gate 1 = MakeBG("gate", 1)
    
    image bg path 1 = MakeBG("path", 1)
    
    image bg school stairs 1 = MakeBG("school_stairs", 1)
    
    image bg club building 1 = MakeBG("club_building", 1)
