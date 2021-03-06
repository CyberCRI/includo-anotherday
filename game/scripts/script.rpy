init python:
    renpy.music.register_channel("background", mixer="sfx", loop=True)

    def play_effect(trans, st, at):
        renpy.play("sound/paperdrop.wav", "sound")

    def show_narration_background(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show":
            renpy.show("narration_background")

        if event == "show_done":
            renpy.sound.play("sound/typewriter.wav")

        if event == "slow_done":
            renpy.sound.stop()

        if event == "end":
            renpy.sound.play("sound/typewriter_linebreak.wav")

    def thinking_callback(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show":
            renpy.show("narration_background")

        if event == "end":
            renpy.sound.play("sound/say.wav")

    def hide_narration_background(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show":
            renpy.hide("narration_background")

        if event == "end":
            renpy.sound.play("sound/say.wav")


init 9999 python:
    narration = Character(None, kind=centered, layout="subtitle", what_color="#CCFFFF", what_prefix="{i}", what_suffix="{/i}", window_left_padding=30, window_right_padding=30, what_size=30, callback=show_narration_background)

image narration_background:
    "images/narration_background.png"

    on show:
        alpha 0.0
        easein 1.0 alpha 1.0

    on hide:
        alpha 1.0
        easein 1.0 alpha 0.0

image ctc_blink:
    "gui/ctc.png"
    linear 0.5 alpha 1.0
    linear 0.5 alpha 0.0
    repeat

image mail_icon_blink:
    xalign 0.1
    yalign 0.1
    "images/mail_icon1.png"
    pause 0.5
    "images/mail_icon2.png"
    pause 0.5
    repeat

image mail_icon_open:
    xalign 0.1
    yalign 0.1
    "images/mail_icon_open.png"

image side placeholder:
    "images/characters/side/placeholder.png"

    on replace:
        alpha 0.0
        linear 0.5 alpha 1.0
    on replaced:
        linear 0.5 alpha 0.0

default show_quick_menu = True
        
define employee = Character(None, who_color="#032837", ctc="ctc_blink", ctc_position="nestled", screen="say", callback=hide_narration_background)
define priyanka = Character("PRIYANKA", image="priyanka", kind=employee, show_job="{i}Marketing Assistant{/i}")
define bapat = Character("BAPAT", image="bapat", kind=employee, show_job="{i}Marketing Executive{/i}")
define donatello = Character("DONATELLO", image="donatello", kind=employee, show_job="{i}Senior Commercial Assistant{/i}")
define giti = Character("GITI", image="giti", kind=employee, show_job="{i}Chief Secretary{/i}")
define manali = Character("MANALI", image="manali", kind=employee, show_job="{i}Secretary{/i}")
define ashwini = Character("ASHWINI", image="ashwini", kind=employee, show_job="{i}CEO of CRYPTALOO{/i}", show_namepos="left")

define abhay = Character("ABHAY", who_color="#032837", ctc="ctc_blink", ctc_position="nestled",screen="say", show_job="{i}Human Resources Manager{/i}", show_side_image=False, callback=hide_narration_background, show_namepos="left", show_main_character=True)
define thinking = Character("ABHAY", who_color="#032837", what_color="#85B3D9", what_prefix="{i}(", what_suffix="){/i}", ctc="ctc_blink", ctc_position="nestled", show_job="{i}Human Resources Manager{/i}", show_side_image=False, show_namepos="left", callback=thinking_callback, show_main_character=True)


define mail = Character("mail", what_color="#000000", what_size=22, what_font="fonts/Mizo Arial.ttf", what_prefix="{k=-1}", what_suffix="{/k}", ctc="ctc_blink", ctc_position="nestled", screen="mail_say", callback=show_narration_background)

define mail_gopinath = Character(kind=mail,
                        show_mail_subject="{k=-1}Out of the Office{/k}",
                        show_mail_from="{size=12}{k=-1}{b}Adnan Gopinath{/b} <adnan.gopinath@cryptaloo.com>{/k}{/size}",
                        show_mail_to="{size=12}{k=-1}to abhay.chandrakant@cryptaloo.in{/k}{/size}",
                        show_mail_image=False)

define mail_brahmin = Character(kind=mail,
                        show_mail_subject="{k=-1}Re: Giti Madam{/k}",
                        show_mail_from="{size=12}{k=-1}{b}Swami Ram Ram{/b} <swamiramram@jio.in>{/k}{/size}",
                        show_mail_to="{size=12}{k=-1}to abhay.chandrakant@cryptaloo.in{/k}{/size}",
                        show_mail_image=False)

define mail_lawyer = Character(kind=mail, what_size=22,
                        show_mail_from="{size=12}{k=-1}{b}Mr. Rajkumar{/b} <rajkumarrajkumarltd@gmail.com>{/k}{/size}",
                        show_mail_to="{size=12}{k=-1}to abhay.chandrakant@cryptaloo.in{/k}{/size}",
                        show_mail_image=False)

define mail_lawyer_act1 = Character(kind=mail_lawyer, show_mail_subject="{k=-1}Re: Decency and dress code at work{/k}")
define mail_lawyer_act2_1 = Character(kind=mail_lawyer, show_mail_subject="{k=-1}Re: Promotion and Discrimination{/k}")
define mail_lawyer_act2_2 = Character(kind=mail_lawyer, show_mail_subject="{k=-1}Re: Subpoena/Giti Shaikh{/k}")
define mail_lawyer_act3_1 = Character(kind=mail_lawyer, show_mail_subject="{k=-1}Re: Homosexuality and Discrimination{/k}")
define mail_lawyer_act3_2 = Character(kind=mail_lawyer, show_mail_subject="{k=-1}Re: Inclusive Policy{/k}")
define mail_lawyer_act3_3 = Character(kind=mail_lawyer, show_mail_subject="{k=-1}Re: Re: Re: Inclusive Policy{/k}")
define mail_lawyer_act4 = Character(kind=mail_lawyer, show_mail_subject="{k=-1}Re: Prayer room{/k}")

label start:
    $act_1_completed = False
    $act_2_completed = False
    $act_3_completed = False
    $act_4_completed = False

    $act_1_ending_14 = False
    $act_1_ending_31 = False
    $act_1_ending_32 = False
    $act_1_ending_33 = False
    $act_1_ending_34 = False

    $act_2_ending_18 = False
    $act_2_ending_23 = False

    $act_3_ending_10 = False
    $act_3_ending_13 = False
    $act_3_ending_28 = False

    $act_4_ending_10 = False
    $act_4_ending_25 = False
    $act_4_ending_26 = False
    $act_4_ending_28 = False

    $show_quick_menu = False
    call screen act_menu
    return