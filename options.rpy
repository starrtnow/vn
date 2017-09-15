## This file contains some of the options that can be changed to customize
## your Ren'Py game. It only contains the most common options... there
## is quite a bit more customization you can do.
##
## Lines beginning with two '#' marks are comments, and you shouldn't
## uncomment them. Lines beginning with a single '#' mark are
## commented-out code, and you may want to uncomment them when
## appropriate.

init -1 python hide:

    ## Should we enable the use of developer tools? This should be
    ## set to False before the game is released, so the user can't
    ## cheat using developer tools.

    config.developer = True

    ## These control the width and height of the screen.

    config.screen_width = 800
    config.screen_height = 600

    ## This controls the title of the window, when Ren'Py is
    ## running in a window.

    config.window_title = u"Building Relationships"

    #########################################
    # Layouts
    
    ## This enables the use of an in-game menu that is made out of
    ## buttons.

    layout.button_menu()
    layout.scrolling_load_save()
    layout.two_column_preferences()

    #########################################
    # Themes
    
    ## We then want to call a theme function. themes.roundrect is
    ## a theme that features the use of rounded rectangles. It's
    ## the only theme we currently support.
    ##
    ## The theme function takes a number of parameters that can
    ## customize the color scheme.

    theme.roundrect(
        # Color scheme: Colorblind
                                    
        ## The color of an idle widget face.
        widget = "#DEBF80",

        ## The color of a focused widget face.
        widget_hover = "#F0E0A0",

        ## The color of the text in a widget.
        widget_text = "#603018",

        ## The color of the text in a selected widget. (For
        ## example, the current value of a preference.)
        widget_selected = "#FFFFFF",

        ## The color of a disabled widget face. 
        disabled = "#B07040",

        ## The color of disabled widget text.
        disabled_text = "#C08050",

        ## The color of informational labels.
        label = "#F2D2A0",

        ## The color of a frame containing widgets.
        frame = "#985028",

        ## The background of the main menu. This can be a color
        ## beginning with '#', or an image filename. The latter
        ## should take up the full height and width of the screen.
        mm_root = "bg/mm.jpg",

        ## The background of the game menu. This can be a color
        ## beginning with '#', or an image filename. The latter
        ## should take up the full height and width of the screen.
        gm_root ="bg/skipscreen.jpg",

        ## If this is True, the in-game window is rounded. If False,
        ## the in-game window is square.
        rounded_window = True,

        ## And we're done with the theme. The theme will customize
        ## various styles, so if we want to change them, we should
        ## do so below.            
        )


    #########################################
    ## These settings let you customize the window containing the
    ## dialogue and narration, by replacing it with an image.

    ## The background of the window. In a Frame, the two numbers
    ## are the size of the left/right and top/bottom borders,
    ## respectively.

    #style.window.background = Frame("bg/frame.jpg", 12, 12)

    ## Margin is space surrounding the window, where the background
    ## is not drawn.

    #style.window.left_margin = 6
    #style.window.right_margin = 6
    #style.window.top_margin = 6
    #style.window.bottom_margin = 6

    ## Padding is space inside the window, where the background is
    ## drawn.

    #style.window.left_padding = 6
    #style.window.right_padding = 6
    #style.window.top_padding = 6
    #style.window.bottom_padding = 6

    ## This is the minimum height of the window, including the margins
    ## and padding.

    # style.window.yminimum = 250


    #########################################
    ## This lets you change the placement of the main menu.

    ## The way placement works is that we find an anchor point
    ## inside a displayable, and a position (pos) point on the
    ## screen. We then place the displayable so the two points are
    ## at the same place.

    ## An anchor/pos can be given as an integer or a floating point
    ## number. If an integer, the number is interpreted as a number
    ## of pixels from the upper-left corner. If a floating point,
    ## the number is interpreted as a fraction of the size of the
    ## displayable or screen.

    # style.mm_menu_frame.xpos = 0.5
    # style.mm_menu_frame.xanchor = 0.5
    # style.mm_menu_frame.ypos = 0.75
    # style.mm_menu_frame.yanchor = 0.5


    #########################################
    ## These let you customize the default font used for text in Ren'Py.

    ## The file containing the default font.

#    style.default.font = "segoeui.ttf"
    style.default.font = "Asap-Regular.ttf"

    ## The default size of text.

    style.default.size = 20
    style.menu_choice_chosen_button.background = "#f00"
    style.say_dialogue["rollback"].color = "#FF0000"

    ## Note that these only change the size of some of the text. Other
    ## buttons have their own styles.


    #########################################
    ## These settings let you change some of the sounds that are used by
    ## Ren'Py.

    ## Set this to False if the game does not have any sound effects.

    config.has_sound = True

    ## Set this to False if the game does not have any music.

    config.has_music = True

    ## Set this to False if the game does not have voicing.

    config.has_voice = False

    ## Sounds that are used when button and imagemaps are clicked.

    # style.button.activate_sound = "click.wav"
    # style.imagemap.activate_sound = "click.wav"

    ## Sounds that are used when entering and exiting the game menu.

    # config.enter_sound = "click.wav"
    # config.exit_sound = "click.wav"

    ## A sample sound that can be played to check the sound volume.

    # config.sample_sound = "click.wav"

    ## Music that is played while the user is at the main menu.

    config.main_menu_music = "music/menu_theme.ogg"
    
    config.main_menu = [
        (u"New Game", "start", "True"),
        (u"Load", _intra_jumps("load_screen", "main_game_transition"), "True"),
        (u"Options", _intra_jumps("preferences_screen", "main_game_transition"), "True"),
        #(u"Prologue", "prologue", "persistent.finished_prologue"),
        (u"Scene Gallery", "scene_gallery", "True"),
        (u"Quit", ui.jumps("_quit"), "True")
        ]

    config.game_menu = [
        ( None, u"Return", ui.jumps("_return"), 'True'),
        ( "preferences", u"Preferences", _intra_jumps("preferences_screen", "intra_transition"), 'True' ),
        ( "save", u"Save Game", _intra_jumps("save_screen", "intra_transition"), 'True', 'not main_menu' ),
        ( "load", u"Load Game", _intra_jumps("load_screen", "intra_transition"), 'True'),
        ( None, u"Main Menu", ui.callsinnewcontext("_main_menu_prompt"), 'True', 'not main_menu' ),
        ( None, u"Quit", ui.callsinnewcontext("_quit_prompt"), 'True' ),
        ]


    #########################################
    ## Help.

    ## This lets you configure the help option on the Ren'Py menus.
    ## It may be:
    ## - A label in the script, in which case that label is called to
    ##   show help to the user.
    ## - A file name relative to the base directory, which is opened in a
    ##   web browser.
    ## - None, to disable help.   
    config.help = "README.txt"


    #########################################
    ## Transitions.
    
    quick = Dissolve(0.1)

    ## Used when entering the game menu from the game.
    config.enter_transition  = dissolve

    ## Used when exiting the game menu to the game.
    config.exit_transition = dissolve

    ## Used between screens of the game menu.
    config.intra_transition = quick

    ## Used when entering the game menu from the main menu.
    config.main_game_transition = dissolve

    ## Used when returning to the main menu from the game.
    config.game_main_transition = dissolve

    ## Used when entering the main menu from the splashscreen.
    config.end_splash_transition = fade

    ## Used when entering the main menu after the game has ended.
    config.end_game_transition = fade

    ## Used when a game is loaded.
    config.after_load_transition = Fade(0.5, 1.0, 1.0)

    ## Used when the window is shown.
    config.window_show_transition = quick

    ## Used when the window is hidden.
    config.window_hide_transition = quick


    #########################################
    ## This is the name of the directory where the game's data is
    ## stored. (It needs to be set early, before any other init code
    ## is run, so the persisten information can be found by the init code.)
python early:
    config.save_directory = "VNAD-1285790046"

init -1 python hide:
    #########################################
    ## Default values of Preferences.

    ## Note: These options are only evaluated the first time a
    ## game is run. To have them run a second time, delete
    ## game/saves/persistent

    ## Should we start in fullscreen mode?

    config.default_fullscreen = False

    ## The default text speed in characters per second. 0 is infinite.

    config.default_text_cps = 60

    #########################################
    ## More customizations can go here.
    
  #  config.nvl_paged_rollback = True
   # style.nvl_vbox.box_spacing = 0
  #  style.nvl_window.xpadding = 60
   # style.nvl_window.ypadding = 70
   # config.adv_nvl_transition = dissolve
   # config.nvl_adv_transition = dissolve
    
  #  style.vbox.box_spacing = 0
   # style.nvl_window.background = im.Alpha("bg/nvlwindow.png", 0.60)
    
  #  style.nvl_window['paper'].background = "bg/nvlpaper.png"
   # style.nvl_window['paper'].xpadding = 120
