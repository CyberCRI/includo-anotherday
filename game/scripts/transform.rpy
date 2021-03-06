# All the transforms go into this file

transform from_right(easein_time=3.0, pause_time=3, xdestination=0.5):
    from_horizontal(1, xdestination, easein_time, pause_time)

transform from_left(easein_time=3.0, pause_time=0, xdestination=0.5):
    from_horizontal(0, xdestination, easein_time, pause_time)

transform from_horizontal(xorigin, xdestination, easein_time=3.0, pause_time=0):
    subpixel True
    alpha 0.0 xalign xorigin xanchor 0.0
    time pause_time
    xalign xorigin
    parallel:
        easein easein_time alpha 1.0
    parallel:
        easein easein_time xalign xdestination
    on hide:
        alpha 1 zoom 1 xanchor xdestination
        block:
            linear 0.1 zoom 1.1
            linear 0.5 zoom 0


transform from_top(easein_time=3.0, pause_time=0, ydestination=0.5):
    subpixel True
    alpha 0.0 yalign 0.0 yanchor 0.0
    pause_time
    parallel:
        easein easein_time alpha 1.0
    parallel:
        easein easein_time yalign ydestination
    on hide:
        alpha 1 zoom 1 yanchor ydestination
        block:
            linear 0.1 zoom 1.1
            linear 0.5 zoom 0

transform elastic_splash(zoom_value=1.0, time_value=0.0):
    alpha 0.0
    zoom 5.0
    time time_value
    subpixel True
    alpha 1.0
    linear 0.2 zoom zoom_value

transform elastic_splash_rotate(zoom_value=1.0, time_value=0.0, rotate_value=-3.0):
    alpha 0.0
    zoom 5.0
    time time_value
    subpixel True
    alpha 1.0
    linear 0.2 zoom zoom_value
    function play_effect
    pause 2
    easein_elastic 1.5 rotate rotate_value

transform bloom(easein_time=1.0, time_value=0.0, zoom_value=1.0):
    alpha 0.0 zoom zoom_value
    time time_value
    subpixel True
    easein easein_time alpha 1.0

transform fade_in(easein_time=1.0):
    alpha 0.0
    easein easein_time alpha 1.0

transform zoom_on_hover(idle_value, hover_value):
    on hover:
        easein 0.25 zoom hover_value
    on idle:
        easein 0.25 zoom idle_value
transform zoom(zoom_value):
    zoom zoom_value

transform rotate(value):
    rotate_pad True
    rotate value

transform center:
    yalign -0.05 xalign 0.5

transform center_left:
    yalign -0.05 xalign 0.1

transform center_right:
    yalign -0.05 xalign 1.0

transform center_center_left:
    yalign -0.05 xalign 0.33

transform center_center_right:
    yalign -0.05 xalign 0.66

transform talking:
    easein 0.25 zoom 1.025

transform not_talking:
    easein 0.25 zoom 1.0

transform move_right:
    easein 2.0 xalign 1.0

transform move_left:
    easein 2.0 xalign 0.1

transform move_center_from_right:
    xalign 1.0
    easein 2.0 xalign 0.5

transform change_transform(old, new):
    contains:
        old
        yalign 1.0
        xpos 1.0 xanchor 1.0
        parallel:
            easein 0.5 xanchor 0.0
        parallel:
            easein 0.5 alpha 0.0
    contains:
        new
        yalign 1.0
        xpos 2.0 xanchor 1.0
        parallel:
            easein 0.5 xpos 1.0
        parallel:
            easein 0.5 alpha 1.0

transform flip:
    xzoom -1
#define config.side_image_change_transform = change_transform