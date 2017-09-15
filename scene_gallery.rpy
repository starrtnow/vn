label scene_gallery:
    python:
        for label in ["cr_001", "cr_002", "cr_003"]:
            persistent.seen_scenes.add(label)
        ui.add("bg/skipscreen.jpg")
        ui.window(left_margin=100,
                  right_margin=100,
                  top_margin=50,
                  bottom_margin=50)
        ui.side(['c', 'r', 'b'], spacing=10)
        vp = ui.viewport(mousewheel=True)
        ui.vbox()
        for scene_label in scene_order:
            if scene_label in persistent.seen_scenes:
                ui.textbutton(scenes[scene_label], clicked=ui.jumps(scene_label))
            else:
                ui.textbutton("Locked")
        ui.close()
        ui.bar(adjustment=vp.yadjustment, style="vscrollbar")
        
        ui.textbutton("Return to Menu", clicked=ui.returns(True))
        ui.close()
        ui.interact(suppress_underlay=True, suppress_overlay=True)