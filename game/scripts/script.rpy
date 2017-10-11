init 9999 python:
    narration = Character(None, kind=centered, what_color="#CCFFFF", what_prefix="{i}", what_suffix="{/i}")


image side placeholder:
    "images/characters/side/placeholder.png"

    on replace:
        alpha 0.0
        linear .5 alpha 1.0
    on replaced:
        linear .5 alpha 0.0

define employee = Character(None, image="placeholder")
define priyanka = Character("Priyanka", kind=employee, who_color="#FFFFFF", image="placeholder")
define bapat = Character("Bapat", kind=employee, who_color="#FFFFFF")
define donatello = Character("Donatello", kind=employee, who_color="#FFFFFF")
define giti = Character("Giti", kind=employee, who_color="#FFFFFF")
define manali = Character("Manali", kind=employee, who_color="#FFFFFF")
define ashwini = Character("Ashwini", kind=employee, who_color="#FFFFFF")
define abhay = Character("Abhay", who_color="#FFFFFF")
define thinking = Character("Abhay", what_color="#85B3D9", what_prefix="{i}(", what_suffix="){/i}")

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