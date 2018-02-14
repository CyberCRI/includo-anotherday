
label act4:
    $act_4_completed = False

    $talk_bapat_act4 = False
    $talk_priyanka_act4 = False
    $talk_donatello_act4 = False
    $talk_manali_act4 = False
    $talk_gopinath_act4 = False

    $talk_bapat_act4_2 = False
    $talk_priyanka_act4_2 = False
    $talk_donatello_act4_2 = False
    $talk_manali_act4_2 = False
    $talk_rajkumar_act4_2 = False
    $talk_gopinath_act4_2 = False

    $act_4_ending_10 = False
    $act_4_ending_25 = False
    $act_4_ending_26 = False
    $act_4_ending_28 = False

    window hide

    stop music fadeout 1.0

    stop background fadeout 1.0

    scene bg none

    $renpy.pause(3.0)

    play music "music/Kevin_MacLeod_Eastminster.ogg" fadein 3.0 fadeout 3.0

    thinking "The issues have been piling up lately, forcing me to take difficult decisions."

    thinking "It's maybe for the best, as all these decisions are slowly shaping a new work environment for everyone."

    thinking "An environment that I've chosen."

    thinking "Of course, I've pushed the employees one way or another, and the atmosphere is now tenser than before."

    thinking "Which is why I thought it would be a good idea to copy our competitor BUNGALOO and invite a Brahmin to bless the office."

    thinking "Nothing like a joyful, and beautiful ceremony to rekindle the bonding."

    window hide

    show bg office with Dissolve(3.0)

    narration "Just as you’re imagining the ceremony, smiling to yourself, you notice Giti waiting for you by your office’s door with a grim expression."

    show giti dark at not_talking, center
    with dissolve

    thinking "What now?"

    narration "You let her in, and she starts talking straight away."

    show giti at talking

    giti "Abhay Sir, this is because of the ceremony."

    show giti dark at not_talking

    abhay "Oh yes, Giti! {w=0.25}It's going to be great!"

    show giti sad at talking

    stop music fadeout 3.0

    giti "Abhay Sir, maybe you forgot, I am Muslim."

    show giti sad dark at not_talking

    thinking "{b}Of course{/b}, how could I have forgotten?"

    abhay "My goodness, that's true!{w=0.5} Let's-"

    show giti at talking

    giti "I cannot participate, Abhay Sir, these are not my beliefs."

    show giti dark at not_talking

    show narration_background

    menu:
        thinking "What should I tell her?"
        "\"I know exactly what to do, what about this...\"":
            jump .scene2
        "\"Give me today to think about it, and talk with the others\"":
            jump .scene3

label .scene2:
    menu:
        thinking "So she doesn't want to participate... {w=0.25}well, {w=0.25}I know exactly what to do."
        "Tell her you'll fire her if she doesn't come.":
            jump .scene9
        "Offer her to take a sick leave tomorrow.":
            jump .scene11
        "Tell her she can skip the ceremony, and come to work later.":
            jump .scene12

label .scene3:

    window hide

    scene bg meeting_room with dissolve

    narration "To find the true feelings of your employees on such a delicate matter, you don't think that calling people to your office is the best idea."

    narration "You decide to use the meeting room as a more neutral place for informal discussions."

    narration "You move to the meeting room with a pen, and a piece of paper, you want this to be as informal as possible, but you need to hear what they think about the situation."

    play music "music/Kevin_MacLeod_Eastminster.ogg" fadein 3.0 fadeout 3.0

label .employees:
    menu:
        thinking "This is a delicate matter, who will I hear out?"
        "Bapat." if not talk_bapat_act4:
            jump .scene4
        "Priyanka." if not talk_priyanka_act4:
            jump .scene5
        "Donatello." if not talk_donatello_act4:
            jump .scene6
        "Manali." if not talk_manali_act4:
            jump .scene7
        "Write to Mr. Gopinath instead." if not talk_gopinath_act4:
            jump .scene8
        "I've talked to enough people." if talk_bapat_act4 or talk_priyanka_act4 or talk_donatello_act4 or talk_manali_act4 or talk_gopinath_act4:
            jump .advices

label .advices:
    
    menu:
        thinking "Now know what my next move will be."
        "Tell Giti you'll fire her if she doesn't come." if talk_bapat_act4 or talk_priyanka_act4 or talk_donatello_act4:
            jump .scene9
        "Offer Giti to take a sick leave tomorrow." if talk_donatello_act4:
            jump .scene11
        "Tell Giti she can skip the ceremony, and come later." if talk_manali_act4:
            jump .scene12
        "Talk to the other employees." if not talk_bapat_act4 or not talk_priyanka_act4 or not talk_donatello_act4 or not talk_manali_act4 or not talk_gopinath_act4:
            jump .employees

label .scene4:

    show bapat at talking, center
    with dissolve

    bapat "Abhay, it will ruin the ceremony if she doesn’t come!"

    bapat "It's either all of us, or none of us."

    show bapat dark at not_talking
    with dissolve

    abhay "But Bapat, she's not Hindu."

    show bapat at talking

    bapat "Hindu, or not, Abhay, it's not the point, it's being together for the company."

    show bapat angry
    with dissolve

    bapat angry "How can she exclude herself, and still pretend she's working with us?"

    show bapat dark at not_talking

    abhay "Well, technically, Bapat, we also exclude her by having a Hindu ceremony."

    show bapat at talking

    bapat "No, no, Abhay, you don't get it, it's not about religion, it's about the team spirit."

    bapat "You know how much it matters to me."

    show bapat dark at not_talking

    abhay "Indeed."

    abhay "You have proven it {i}quite a lot{/i} these last few days... {w=0.5}*sigh*"

    show bapat smug at talking

    bapat "Yes, Abhay, you know me well."

    show bapat smug dark at not_talking

    

    thinking "Seems like he didn't take the hint."

    thinking "Well, it doesn't matter."

    abhay "So what would you advise me?"

    show bapat at talking

    bapat "Tell her that she's fired if she doesn't come, it's the only way, Abhay."

    show bapat at not_talking

    thinking "Should I listen to his advice?"

    $talk_bapat_act4 = True

    hide bapat
    with dissolve

    jump .advices

label .scene5:
    
    show priyanka at talking, center
    with dissolve

    priyanka "We can't have this, Abhay."

    show priyanka dark at not_talking

    abhay "And why not?"

    abhay "Why not respect her religion?"

    show priyanka angry at talking

    priyanka "This is India, Abhay, the Motherland, this is a Hindu country."

    priyanka "Everyone has to accept, or to leave, Abhay."

    priyanka "This is as much a part of being Indian as knowing the language, or the National Anthem."

    show priyanka dark at not_talking

    abhay "How-{w=0.25}{nw}"

    show priyanka at talking

    priyanka "She can have her religion of course, but this is a public function, that she has to attend."

    show priyanka dark at not_talking

    abhay "You know that India is a secular country, don't you?"

    show priyanka at talking

    priyanka "This has nothing to do with that, Abhay, this is official business."

    show priyanka dark at not_talking

    abhay "I've heard you, Priyanka."

    abhay "*sigh*{w=1} Let me consider it."

    hide priyanka
    with dissolve    

    thinking "Should I listen to her advice?"

    $talk_priyanka_act4 = True

    jump .advices

label .scene6:

    show donatello determined at center, talking
    with dissolve

    donatello "This is tricky, Abhay."

    donatello "The others won't understand if she won't come, but if you force her, she will snap."

    show donatello determined dark at not_talking

    abhay "Exactly."

    show donatello determined at talking

    donatello "Still, if you want this to be an opportunity to unite the employees, it needs to happen."

    show donatello
    with dissolve

    donatello "So I really don't know what to advise you."

    show donatello at not_talking

    abhay "What would you do yourself in my position?"

    show donatello at talking

    donatello "I don't know. She can't just skip it openly."

    show donatello determined
    with dissolve

    donatello determined "Either you force her, and see what happens,{w=0.25} or you let her call in sick, maybe?"

    show donatello thoughtful
    with dissolve

    donatello "She could take a sick leave, and you would tell she's got a flu, or something?"

    show donatello thoughtful dark at not_talking

    

    thinking "Should I listen to his advice?"

    hide donatello with dissolve

    $talk_donatello_act4 = True

    jump .advices

label .scene7:
    show manali at center, talking
    with dissolve

    play music "music/Kai_Engel_Ode_To_The_World.ogg" fadein 2.0 fadeout 2.0

    manali "Oh why bother, respected Sir?"

    manali "One India, many religions."

    show manali dark at not_talking

    thinking "I-I didn't expect this. She's surprising me this time."

    thinking "So this is where she takes a stand?"

    show manali at talking

    manali "Why not let Giti be, she can always come later, why the intolerance?"

    show manali dark at not_talking

    abhay "It's just that the others won't like this, Manali."

    show manali at talking

    manali "Abhay Sir, let them talk."

    manali "Why is it that we always hurt the feelings of someone in this company?"

    show manali dark at not_talking

    abhay "I wish this could be as simple as that, Manali."

    show manali smiling at talking

    manali smiling "Of course, this would be more simple if we were all Hindus, Abhay Sir, but this isn’t our reality."

    manali smiling "This is why we have national holidays for all religions."

    show manali smiling dark at not_talking

    abhay "You may have a point here. I need to think about it."

    hide manali with dissolve

    play music "music/Kevin_MacLeod_Eastminster.ogg" fadein 3.0 fadeout 3.0

    $talk_manali_act4 = True

    jump .advices

label .scene8:

    narration "You decide to write to Mr. Gopinath about it, and explain the situation. You receive an automatic out-of-the-office answer minutes later, and never hear about it again."

    window hide
    show mail_icon_blink

    pause

    hide mail_icon_blink
    show mail_icon_open

    $mail_gopinath(("I am currently on leave, visiting the jungles of Angkor Wat. I will answer you as soon as I reach my office back.\n"
        "If you have any urgent matter, kindly write to Mr. Chandrakant at the following email: {color=#0000FF}{u}abhay.chandrakant@cryptaloo.in{/u}{/color}.\n"
        "\nBest regards,\nMr. Gopinath\n"
        "{font=fonts/Oswald-Regular.ttf}{size=14}{k=-1}{color=#009fff}Adnan Gopinath, Administrative Director{/color}{/k}{/size}\n"
        "{size=12}{k=-1}Pearls Omaxe Building, Off # 1005, 10th Floor, First Tower{/k}{/size}\n"
        "{size=12}{k=-1}Netaji Subhash Place Complex, Pitampura, Delhi 110034, INDIA{/k}{/size}{/font}"))

    hide mail_icon_open

    pause 3.0

    window show

    jump .advices

label .scene9:

    window hide

    stop music fadeout 3.0

    show bg office with dissolve

    show giti dark at not_talking, center
    with dissolve

    abhay "It's not possible, Giti.{w=0.25} We are like one family here."

    abhay "Surely you can't go away when your family has a function, can you?"

    show giti at talking

    giti "..."

    show giti stern
    with dissolve

    giti "My family would respect my religion, Abhay Sir."

    show giti stern dark at not_talking

    abhay "As we all do, as we all do,{w=0.25} but it's not only about religion."

    abhay "It's about being together, and participating."

    abhay "This is why I can't have you running away at an important time for the company, I'm sure you understand."

    show giti stern at talking

    giti "Not really, Abhay Sir, I-"

    show giti stern dark at not_talking

    abhay "Now come on."

    abhay "I'm sure you want to reassure everybody that you belong here."

    show giti compassionate at talking

    giti "I thought I was belonging already, Abhay Sir."

    show giti sad dark at not_talking

    abhay "Indeed, indeed, all the more reason why you should come then."

    show giti stern at talking

    giti "I will not, Sir."

    show giti stern dark at not_talking

    abhay "..."

    thinking "She's stubborn, but I will leave her no choice, this is too important."

    play music "music/Kai_Engel_Anxiety.ogg" fadein 1.0 fadeout 1.0

    abhay "You will, or you will no longer be part of this company."

    abhay "See you tomorrow."

    narration "You leave the office."

    hide giti
    with dissolve

    menu:
        thinking "That went well."
        "Let's see how well.":
            jump .scene10

label .scene10:

    window hide 

    scene bg none with dissolve

    narration "You left her no choice."

    narration "The next day, Giti doesn’t show up at work.{p}
                You decide to let it slip, and to welcome her when she finally comes back, but she doesn’t—ever."

    narration "Since she was handling just about everything while Mr. Gopinath’s away, and left without a notice, or a word, her sudden departure threatens your core business, and no one is ready to replace her."

    narration "You start looking for a new Chief Secretary, but whoever comes next will need at least six months before he or she can handle Giti’s work efficiently. Let’s hope you can paper over the problems until the new CEO arrives, you want to make a good impression."

    $act_4_ending_10 = True
    jump .end

label .scene11:
    window hide

    stop music fadeout 3.0

    scene bg office with fade

    show giti dark at center, not_talking
    with dissolve

    abhay "I think I have found a solution, Giti."

    show giti at talking

    giti "Yes, Abhay Sir?"

    show giti at not_talking

    abhay "I understand that you don’t want to participate in the ceremony..."

    abhay "...But from what I’ve gathered, it’s not so easy for everyone to accept that."

    show giti at talking

    giti "What's so difficult to accept, Abhay Sir?"

    show giti dark at not_talking

    abhay "Oh you know very well, Giti, please, let me help you with this."

    show giti stern at talking

    giti "I am listening, Abhay Sir."

    show giti dark at not_talking

    play music "music/Kevin_MacLeod_Eastminster.ogg" fadein 3.0 fadeout 3.0

    abhay "Let’s just say you caught a flu{w=0.25}, or something, you know,{w=0.25} call in sick, and take a leave tomorrow so that you can skip the blessing."

    show giti compassionate at talking

    giti "But, Sir, everybody will know that I have no flu, and that I just want to avoid the blessing."

    show giti compassionate dark at not_talking

    abhay "Yes, but you can always pretend that you were sick to save face."

    show giti compassionate at talking

    giti "But this wouldn’t be the truth, and…"

    show giti
    with dissolve

    giti ".{w=0.25}.{w=0.25}."

    show giti stern
    with dissolve

    giti "I understand, Abhay Sir, I will stay home tomorrow."

    hide giti
    with dissolve

    menu:
        "The aftermath.":
            jump .scene13

label .scene12:

    stop music fadeout 3.0

    scene bg office with fade

    show giti compassionate dark at not_talking, center
    with dissolve

    abhay "You can have the religion you like, Giti, and I respect that."

    narration "She nods."

    show giti dark
    with dissolve

    play music "music/Kai_Engel_Ode_To_The_World.ogg" fadein 3.0

    abhay "When the Brahmin will come, just go drink a chair downstairs, or whatever, okay?"

    abhay "Let’s not make a big issue of this, there’s nothing to worry about."

    show giti at talking

    giti "I appreciate it, Abhay Sir."

    show giti at not_talking

    abhay "It’s not just me, it’s the Law, Giti, we must abide with the freedom of conscience, and religion."

    abhay "I don’t even see how that could be a problem for anyone, we’re not an ashram here."

    show giti smiling at talking

    giti "*laughs*"

    show giti stern dark at not_talking

    giti ".{w=0.25}.{w=0.25}."

    abhay "What's the matter, Giti?"

    show giti at talking

    giti "Nothing, it’s nothing Abhay Sir, thank you."

    show giti dark at not_talking

    hide giti
    with dissolve

    narration "And with that, she salutes you with her hands joined, and leaves your office."

    menu:
        "The aftermath.":
            jump .scene13

label .scene13:

    window hide

    show bg none with Dissolve (3.0)

    play music "music/Kevin_MacLeod_Eastminster.ogg" fadein 3.0 fadeout 3.0

    narration "As planned, Giti doesn’t show up on the next day."

    narration "With everyone busy watching the Brahmin, or singing mantras, and prayers, her absence didn’t seem to be noticed. If it was, everyone was tactful enough to avoid mentioning it, at the very least. {/i}Problem solved!{i} You congratulate yourself."

    narration "The morning following the ceremony, however, as you fetch your tea and whistle {/i}You are my Soniya{i} on your way, you find Giti waiting for you in front of your office."    

    thinking "{/i}Again?{i}"

    narration "You let her in."

    show bg office with Dissolve (3.0)

    show giti dark at center, not_talking
    with dissolve

    abhay "What can I do for you, Giti Madam?"

    show giti at talking

    giti "Abhay Sir, I was thinking."

    show giti dark at not_talking

    abhay "Good, I approve this, we should be thinking more!"

    show giti stern at talking

    giti "Yes, Abhay Sir."

    show giti stern dark at not_talking

    abhay "I was kidding, Giti, please tell me."

    show giti stern at talking

    giti "You know, Sir, since we were talking about it the other day, I thought I needed to tell you everything."

    show giti stern dark at not_talking 

    abhay "About what?"

    show giti at talking

    giti "About religion{w=0.25}, you see{w=0.25}, Abhay Sir{w=0.25}, I do my prayers during the day."

    giti "And since there's no space to pray, I have to do my prayers in the toilet."

    giti "And now the ladies' toilets are clogged too so that I have to do in the general toilet."

    show giti dark at not_talking

    

    thinking "I know what she means."

    thinking "The men's loo could use some refresh{w=0.25}, or a flamethrower maybe."

    abhay "So what do you want, Giti?"

    show giti determined at talking

    giti "I want a room I can use for my prayers, Abhay Sir."

    show giti sad
    with dissolve

    giti "It's not good to pray in the dirt like this."

    

    menu:
        thinking "What should I do?"
        "Take a decision straight away.":
            jump .scene14
        "Have lunch first":
            hide giti with dissolve
            jump .scene15

label .scene14:
    
    thinking "There can be no compromise on serious issues like religion."

    hide giti with dissolve

    menu:
        thinking "I've taken my decision the minute she's started to talk."
        "Reject her request.":
            jump .scene23
        "Accept immediately.":
            jump .scene24

label .scene15:
    window hide

    show bg lunch_room with dissolve

    play music "music/Kai_Engel_Holyday_Gift.ogg" fadein 3.0 fadeout 3.0

    play background "music/crowd.ogg" fadein 3.0 fadeout 3.0

    thinking "First things first, a man needs his food three times a day."

    narration "You open your lunch box, and find delicious paneer fingers inside, with a side of steamed okras."

    abhay "Why did it have to be okras...?"

    show giti smiling at center_left, talking
    with dissolve

    giti smiling "You have fried paneer, don't you complain." (show_namepos="left")

    show giti smiling dark at not_talking with None
    show priyanka smiling at center_center_right, talking
    with dissolve

    priyanka "This won't happen if you cook it yourself, Abhay Sir!" (show_namepos="center_right")

    show priyanka smiling dark at not_talking with None
    show bapat angry at center_center_left, talking
    with dissolve

    bapat angry "This is not a man's job!" (show_namepos="center_left")

    show bapat dark at not_talking with None

    abhay "I'm afraid I don't cook so well."

    show manali smiling at center_right, talking
    with dissolve

    manali smiling "Then you learn! Hihi!" (show_namepos="center_right")

    show manali smiling dark at not_talking

    abhay "I will try.{w=0.25} Why not?"

    show manali smiling at talking

    manali "See, Bapat, Abhay Sir is ready for new experiences at least." (show_namepos="center_right")

    show manali smiling dark at not_talking
    show bapat smug at talking

    bapat smug "As is Donatello." (show_namepos="center_left")

    show bapat smug dark at not_talking with None
    show donatello determined at talking, center with dissolve

    donatello "You're really looking for trouble, aren't you?"

    show donatello determined dark at not_talking behind bapat
    show bapat at talking

    bapat "Just kidding this time, just kidding, trust me." (show_namepos="center_left")

    show bapat dark at not_talking

    thinking "Well, give peace a chance."

    thinking "It's been only two days, and here they are, talking, and laughing again."

    narration "You smile, then remember you have a pressing matter to solve, and shuffle back to your office."

    hide bapat
    hide donatello
    hide giti
    hide manali
    hide priyanka
    with dissolve

    window hide

    show bg office with dissolve

    stop background fadeout 3.0

    menu:
        thinking "So, what should I do now?"
        "Talk to the employees.":
            jump .scene16

label .scene16:
    thinking "Let's not change a winning strategy."

    play music "music/Kai_Engel_Machinery.ogg" fadein 3.0 fadeout 3.0

label .employees2:
    menu:
        thinking "Which one should I talk to?"
        "Bapat." if not talk_bapat_act4_2:
            jump .scene17
        "Priyanka." if not talk_priyanka_act4_2:
            jump .scene18
        "Donatello." if not talk_donatello_act4_2:
            jump .scene19
        "Manali." if not talk_manali_act4_2:
            jump .scene20
        "Mr. Rajkumar, the company's lawyer." if not talk_rajkumar_act4_2:
            jump .scene21
        "Mr. Gopinath." if not talk_gopinath_act4_2:
            jump .scene22
        "I've talked to enough people." if talk_bapat_act4_2 or talk_priyanka_act4_2 or talk_donatello_act4_2 or talk_manali_act4_2 or talk_rajkumar_act4_2:
            jump .advices2

label .advices2:

    menu:
        thinking "What should I do now?"
        "Tell Giti she won't have a room." if talk_bapat_act4_2 or talk_priyanka_act4_2 or talk_donatello_act4_2 or talk_rajkumar_act4_2:
            jump .scene23
        "Give Giti a room for her prayers." if talk_manali_act4_2:
            jump .scene24
        "Email the Brahmin" if talk_manali_act4_2 or talk_rajkumar_act4_2:
            jump .scene27
        "Talk to someone else." if not talk_bapat_act4_2 or not talk_priyanka_act4_2 or not talk_donatello_act4_2 or not talk_manali_act4_2 or not talk_rajkumar_act4_2 or not talk_gopinath_act4_2:
            jump .employees2

label .scene17:
    window hide

    show bg meeting_room with dissolve

    show bapat angry at center, talking 
    with dissolve

    bapat "The nerve of this woman!"

    show bapat dark at not_talking

    abhay "Well, Bapat, all that she wants is to be able to pray."

    show bapat angry at talking

    bapat angry "She can pray to her God, who am I to say she can't pray?"

    show bapat angry dark at not_talking

    abhay "You know very well that praying in the toilets isn’t very nice, Bapat, she does that!"

    abhay "It's been three years!"

    show bapat 

    bapat "Oh so she uses our toilets for this as well?"

    show bapat smug
    with dissolve

    bapat smug "No wonder they’re dirty."

    show bapat smug dark at not_talking

    abhay "What can she do, she has no other spaces in the company for praying!"

    show bapat angry at talking

    bapat angry "She can go to the mosque!"

    bapat angry "When I pray, I go to the temple myself, why can’t she do the same, why special rights, and service all the time?"

    bapat angry "Do I ask for special rights?"

    show bapat dark at not_talking

    abhay "You aren’t exactly a member of a minority in need, Bapat."

    show bapat angry at talking

    bapat angry "This is our country, Abhay, don’t fall prey to their stratagems!"

    show bapat smug
    with dissolve

    bapat smug "Already they should be grateful that we play {i}Khwaja Mere Khwaja{/i} during company functions like we always do, so that they’re happy"

    show bapat angry
    with dissolve

    bapat angry "That’s it, don’t overdo it!"

    show bapat angry dark at not_talking

    hide bapat
    with dissolve

    $talk_bapat_act4_2 = True

    jump .advices2

label .scene18:

    window hide

    show bg meeting_room with dissolve

    show priyanka at talking, center
    with dissolve

    priyanka "I knew this would happen."

    priyanka "The minute you decide to give them special treatment, they ask for more, and more, and-"

    show priyanka annoyed dark at not_talking

    abhay "I get it, Priyanka."

    show priyanka angry at talking

    priyanka "You can’t turn this office into a mosque, Abhay!"

    show priyanka angry dark at not_talking

    abhay "We’re talking one room, here, small one, for less than an hour a day in total."

    show priyanka angry at talking

    priyanka angry "And then what?{w=0.5} What will it be next?{w=0.5} More holidays?{w=0.5} A salary raise?"

    show priyanka angry dark at not_talking

    abhay "She never asked for any of this, it’s only decent, Priyanka, she’s been kneeling in the toilets for three years!"

    show priyanka angry at talking

    priyanka angry "It makes us all very uncomfortable, Abhay!"

    show priyanka angry dark at not_talking

    abhay "Who's \"us\", tell me?"

    show priyanka angry at talking

    priyanka "{i}All of us!{/i}"

    show priyanka dark angry at not_talking

    hide priyanka
    with dissolve

    $talk_priyanka_act4_2 = True

    jump .advices2

label .scene19:
    window hide

    show bg meeting_room with dissolve

    show donatello at talking, center
    with dissolve

    donatello "This is too much, Abhay"

    show donatello dark at not_talking

    abhay "Why?"

    show donatello thoughtful at talking

    donatello "Not forcing her to go to Hindu ceremonies is one thing, but this prayer space idea is going too far."

    donatello "It’s not Emirate Airlines here."

    show donatello thoughtful at not_talking

    abhay "You do realize she’s praying in the {i}toilet{/i}, Donald?"

    show donatello determined at talking

    donatello "And what of us all?"

    donatello "We don’t have a room either, this is unfair."

    show donatello determined dark at not_talking

    abhay "This is a different religion, that’s why."

    abhay "We allow sikhs with turbans, and even kukris, don’t we?"

    show donatello nervous at talking

    donatello "It’s not the same thing,{w=0.25} we didn’t build a mandir in here, did we?"

    show donatello nervous dark at not_talking

    abhay "But we have a mandir, just over there."

    narration "You point in the general direction of the shrine in the office."

    show donatello angry at talking

    donatello angry "Not a mandir room, Abhay, she wants a whole room just for herself!"

    show donatello thoughtful
    with dissolve

    donatello "How can you accept this?"

    show donatello angry
    with dissolve

    donatello angry "How come they have all the benefits, and nothing for us, this is {i}our{/i} country!"

    show donatello determined dark at not_talking

    abhay "You don’t accept her religion, Donald."

    show donatello at talking

    donatello "Of course I do."

    show donatello thoughtful
    with dissolve

    donatello "Don’t be naive, Abhay, you can’t give them what even we don’t have!"

    hide donatello
    with dissolve

    $talk_donatello_act4_2 = True

    jump .advices2

label .scene20:

    window hide

    show bg meeting_room with dissolve

    show manali at center, talking
    with dissolve

    play music "music/Kai_Engel_Ode_To_The_World.ogg" fadein 3.0 fadeout 3.0

    manali "So she's been praying in the toilet for three years?"

    show manali dark at not_talking

    narration "You nod. She whistle."

    show manali at talking

    manali "Maybe it's about time we do something to change that?"

    show manali dark at not_talking

    abhay "Yes, Manali, but don’t you think that this would be unfair for Hindus since we have no prayer room either?"

    show manali at talking 

    manali "..."

    show manali smiling
    with dissolve

    manali "You know, Abhay, if I imagine myself in her place..."

    show manali nervous
    with dissolve

    manali "I must say that the whole office is a bit of a prayer room."

    show manali
    with dissolve

    manali "There’s the Ganapati up there, and the incense, and flower offerings we do in the morning."

    manali "We even invite brahmins to bless the office!"

    show manali dark at not_talking

    abhay "Fair enough."

    abhay "So you think I should agree?"

    show manali at talking

    manali "I don’t know.{w=0.25} I don’t know how the others will react."

    show manali dark at not_talking

    abhay "*sigh*"

    show manali at talking

    manali "Maybe you could ask the brahmin who came yesterday?"

    show manali smiling
    with dissolve

    manali "He seemed a good man."

    hide manali
    with dissolve

    $talk_manali_act4_2 = True

    play music "music/Kai_Engel_Machinery.ogg" fadein 3.0 fadeout 3.0

    jump .advices2

label .scene21:

    narration "You write to Mr. Rajkumar, the company’s Lawyer, and explain him the situation so that he can give you his advice. He answers a few hours later"
    window hide
    show mail_icon_blink

    pause

    hide mail_icon_blink
    show mail_icon_open

    $mail_lawyer_act4(("Dear Mr. Chandrakant,\n\n"
        "The company cannot be held responsible {i}ceteris paribus{/i} of the freedom of religion of its employees. As such, and notwithstanding, you are in no legal obligation to provide for a prayer locus, except in such situations where a prayer locus has been created within the company precincts for other confessions, in which case your employee could claim an unequal treatment, and ask for the corresponding damages.\n"
        "Since the matter entails subjects of philosophical, as well as  spiritual importance, I kindly urge you to ask to the spiritual authorities of your convenience for the rule of the Law falters in front of such highness.\n\n"
        "Also, having the toilets cleaned won’t probably hurt your case.\n\n"
        "With my very best regards,\n"
        "Mr. Rajkumar"))

    hide mail_icon_open

    pause 3.0

    window show

    $talk_rajkumar_act4_2 = True

    jump .advices2

label .scene22:

    narration "You write to Mr. Gopinath, and ask for his advice. You receive an automatic out-of-the-office answer minutes later, and never hear about it again."

    window hide
    show mail_icon_blink

    pause

    hide mail_icon_blink
    show mail_icon_open

    $mail_gopinath(("I am currently on leave as I participate in a sledge competition in Finland. I will answer you as soon as I am back in office.\n"
        "If you have any urgent matter, kindly write to Mr. Chandrakant at the following email: {color=#0000FF}{u}abhay.chandrakant@cryptaloo.in{/u}{/color}.\n"
        "\nBest regards,\nMr. Gopinath\n"
        "{font=fonts/Oswald-Regular.ttf}{size=14}{k=-1}{color=#009fff}Adnan Gopinath, Administrative Director{/color}{/k}{/size}\n"
        "{size=12}{k=-1}Pearls Omaxe Building, Off # 1005, 10th Floor, First Tower{/k}{/size}\n"
        "{size=12}{k=-1}Netaji Subhash Place Complex, Pitampura, Delhi 110034, INDIA{/k}{/size}{/font}"))

    hide mail_icon_open

    pause 3.0

    window show

    $talk_gopinath_act4_2 = True

    jump .advices2

label .scene23:
    window hide

    show bg meeting_room with dissolve

    show giti dark at center, not_talking
    with dissolve

    play music "music/Kai_Engel_Anxiety.ogg" fadein 3.0 fadeout 3.0

    abhay "I can't do this, Giti."

    thinking "Better get straight to the point."

    show giti at talking

    giti "Why not, Abhay Sir?"

    show giti dark at not_talking

    abhay "Because the others won’t understand why Muslims would get a special place, when we don't have any such spaces for Hindus."

    abhay "They think it’s unfair."

    show giti stern at talking

    giti "Yet they have a shrine in the office itself, and blessing ceremonies."

    show giti stern dark at not_talking

    abhay "It’s true, Giti, but that’s how it is, there’s nothing I can do. I am sorry."

    show giti compassionate at talking

    giti "We can’t have everything, can we?"

    show giti compassionate at not_talking

    narration "You nod, and smile, happy that she understands."

    show giti stern at talking

    giti stern "We can't even have tolerance these days, this is too much to ask for in this world."

    show giti stern dark at not_talking

    narration "You stop smiling."

    abhay "Giti, please, don't talk it like this..."

    show giti smiling at talking

    giti smiling "It’s fine, Abhay Sir."

    giti smiling "I’ve been praying in the toilets for three years."

    giti smiling "I can do it some more."

    play music "music/Kai_Engel_Moonlight_Reprise.ogg" fadein 3.0 fadeout 3.0

    hide giti with dissolve

    menu:
        thinking "What now?"
        "What now?":
            jump .scene25

label .scene24:
    window hide

    show bg meeting_room with dissolve

    show giti dark at not_talking, center
    with dissolve

    play music "music/Kai_Engel_Ode_To_The_World.ogg" fadein 3.0 fadeout 3.0

    abhay "Of course, you'll have it, Giti."

    show giti at talking

    giti "..."

    show giti smiling
    with dissolve

    giti smiling "Sir, Abhay Sir, this is very good of you."

    show giti smiling dark at not_talking

    abhay "Don’t mention it, Giti, it’s nothing."

    abhay "We never use the fifth floor storage room anyway so, why not get it cleaned, and prepared for your prayers?"

    show giti smiling at talking

    giti smiling "I will never forget, Abhay Sir, and I will pray for you!"

    show giti smiling dark at not_talking

    abhay "You can.{w=0.25} You have the room for this now after all!"

    hide giti with dissolve

    thinking "What now?"

    menu:
        "What now?":
            jump .scene26

label .scene25:

    window hide

    show bg none with fade

    narration "You can’t make a single person happy at the expense of all the others..."

    narration "The following weeks, Giti’s a little bit less active during the meetings, and eats more on her own at lunch, you hope she will understand your decision, and come back to her kind, efficient self before the new CEO steps in."

    $act_4_ending_25 = True
    jump .end

label .scene26:

    window hide

    scene bg none with fade

    narration "Of course, Giti is delighted. All the other employees except Manali resent your decision, though, you can feel it in the way they talk, and look at you."

    narration " Well, you’re the Human Resources Manager, not their best friend forever, and you hope that once the dust settles, everybody will get back to their former, friendly selves."

    $act_4_ending_26 = True
    jump .end
    

label .scene27:
    play music "music/Kevin_MacLeod_Eastminster.ogg" fadein 3.0 fadeout 3.0

    narration "You decide to write to the Brahmin who came to bless the office, and to explain him the situation with Giti. After all, you’re dealing with a religious issue, and he’s a religious person. On the other hand, he’s a representative of the Hindus, and you assume that his answer will not help Giti much, but who knows?{p}
                He answers a few hours later."

    window hide
    show mail_icon_blink

    pause

    hide mail_icon_blink
    show mail_icon_open

    $mail_brahmin(("Abhay,\n"
        "If we want respect from others, we should give them our respect first.\nWe live in peace now in India because of this respect.\nI have seen prayer rooms in international airports, they are open to all, I have sung prayers in one such room in the past next to a Jewish Rabbi.\nMaybe you could use airports as an inspiration?\n\n\n"
        "Be blessed,\n"
        "Swami Ram Ram"))

    hide mail_icon_open

    pause 3.0

    window show

    menu:
        thinking "I think I know what to do now."
        "Create a neutral prayer space for all.":
            jump .scene28

label .scene28:
    window hide
    scene bg none with fade
    narration "Following Swami Ram Ram’s advice, you create a neutral space open to the prayers, yoga, and meditation of all religions. There is still some resistance from some of the employees, but at the end, even Bapat uses it for his yoga, and peace has returned to the office. Congratulations."
    
    $act_4_ending_28 = True
    jump .end

label .end:
    $act_4_completed = True

    $renpy.hide("narration_background")
    
    show bg end_act_4 with Dissolve(3.0)

    pause

    show bg none with Dissolve(3.0)

    $renpy.call_screen("act_menu")

    return
