init 9999 python:
    narration = Character(None, kind=centered, layout="subtitle", what_color="#CCFFFF", what_prefix="{i}", what_suffix="{/i}", window_left_padding=30, window_right_padding=30, what_size=30)

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
        linear .5 alpha 1.0
    on replaced:
        linear .5 alpha 0.0

define employee = Character(None, image="placeholder", who_color="#CAE7FE", ctc="ctc_blink", ctc_position="nestled", screen="say")
define priyanka = Character("PRIYANKA", kind=employee, image="placeholder", show_job="{i}Marketing Assistant{/i}")
define bapat = Character("BAPAT", kind=employee, show_job="{i}Marketing Executive{/i}")
define donatello = Character("DONATELLO", kind=employee, show_job="{i}Senior Commercial Assistant{/i}")
define giti = Character("GITI", kind=employee, show_job="{i}Chief Secretary{/i}")
define manali = Character("MANALI", kind=employee, show_job="{i}Secretary{/i}")
define ashwini = Character("ASHWINI", kind=employee, show_job="{i}CEO of CRYPTALOO{/i}")
define abhay = Character("ABHAY", who_color="#CAE7FE", ctc="ctc_blink", ctc_position="nestled",screen="say", show_job="{i}Human Resources Manager{/i}", show_side_image=False)
define thinking = Character("ABHAY", who_color="#CAE7FE", what_color="#85B3D9", what_prefix="{i}(", what_suffix="){/i}", ctc="ctc_blink", ctc_position="nestled", show_job="{i}Human Resources Manager{/i}", show_side_image=False)
define mail = Character("mail", what_color="#000000", what_size=20, what_font="fonts/Mizo Arial.ttf", what_prefix="{k=-1}", what_suffix="{/k}", ctc="ctc_blink", ctc_position="nestled", screen="mail_say",
                        show_mail_subject="{k=-1}Out of the Office{/k}",
                        show_mail_from="{size=12}{k=-1}{b}Adnan Gopinath{/b} <adnan.gopinath@cryptaloo.com>{/k}{/size}",
                        show_mail_to="{size=12}{k=-1}to abhay.chandrakant@cryptaloo.in{/k}{/size}")

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

    call screen act_menu
    return