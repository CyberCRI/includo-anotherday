
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

    scene bg office with dissolve

    thinking "The issues have been piling up lately, forcing me to take difficult decisions."

    thinking "It's maybe for the best, as all these decisions are slowly shaping a new work environment for everyone."

    thinking "An environment that I've chosen."

    thinking "Of course, I've pushed the employees one way or another, and the atmosphere is now tenser than before."

    thinking "Which is why I thought it would be a good idea to copy our competitor BUNGALOO and invite a Brahmin to bless the office."

    thinking "Nothing like a joyful, and beautiful ceremony to rekindle the bonding."

    narration " Just as you’re imagining the ceremony, smiling to yourself, you notice Giti waiting for you by your office’s door with a grim expression."

    show giti with dissolve

    thinking "What now?"

    narration "You let her in, and she starts talking straight away."

    giti "Abhay Sir, this is because of the ceremony."

    "Oh yes, Giti! {w=0.25}It's going to be great!"

    giti "Abhay Sir, maybe you forgot, I am Muslim."

    thinking "{b}Of course{/b}, how could I have forgotten?"

    "My goodness, that's true!{w=0.5} Let's-"

    giti "I cannot participate, Abhay Sir, these are not my beliefs."

    menu:
        "\"I know exactly what to do, what about this...\"":
            jump .scene2
        "\"Give me today to think about it, and talk with the others.\"":
            jump .scene3

label .scene2:

    thinking "So she doesn't want to participate... {w=0.25}well, {w=0.25}I know exactly what to do."

    menu:
        "Tell her you'll fire her if she doesn't come.":
            jump .scene9
        "Offer her to take a sick leave tomorrow.":
            jump .scene11
        "Tell her she can skip the ceremony, and come to work later.":
            jump .scene12

label .scene3:

    scene bg meeting_room with dissolve 

    narration "To find the true feelings of your employees on such a delicate matter, you don't think that calling people to your office is the best idea."

    narration "You decide to use the meeting room as a more neutral place for informal discussions."

    narration "You move to the meeting room with a pen, and a piece of paper, you want this to be as informal as possible, but you need to hear what they think about the situation."

label .employees:

    thinking "This is a delicate matter, who will I hear out?"

    menu:
        "Bapat." if talk_bapat_act4 == False:
            jump .scene4
        "Priyanka." if talk_priyanka_act4 == False:
            jump .scene5
        "Donatello." if talk_donatello_act4 == False:
            jump .scene6
        "Manali." if talk_manali_act4 == False:
            jump .scene7
        "Write to M. Gopinath instead." if talk_gopinath_act4 == False:
            jump .scene8
        "I've talked to enough people." if if talk_bapat_act4 == True or talk_priyanka_act4 == True or talk_donatello_act4 == True or talk_manali_act4 == True or talk_gopinath_act4 == True:
            jump .advices

label .advices:
    menu:
        "Tell Giti you'll fire her if she doesn't come." if talk_bapat_act4 == True or talk_priyanka_act4 == True or talk_donatello_act4 == True:
            jump .scene9
        "Offer Giti to take a sick leave tomorrow." if talk_donatello_act4 == True:
            jump .scene11
        "Tell Giti she can skip the ceremony, and come later." if talk_manali_act4 == True:
            jump .scene12
        "Talk to the other employees." if talk_bapat_act4 == False or talk_priyanka_act4 == False or talk_donatello_act4 == False or talk_manali_act4 == False or talk_gopinath_act4 == False:
            jump .employees

label .scene4:

    show bapat with dissolve

    bapat "Abhay, it will ruin the ceremony if she doesn’t come!"

    bapat "It's either all of us, or none of us."

    "But Bapat, she's not Hindu."

    bapat "Hindu, or not, Abhay, it's not the point, it's being together for the company."

    bapat "How can she exclude herself, and still pretend she's working with us?"

    "Well, technically, Bapat, we also exclude her by having a Hindu ceremony."

    bapat "No, no, Abhay, you don't get it, it's not about religion, it's about the team spirit."

    bapat "You know how much it matters to me."

    "Indeed."

    "You have proven it {i}quite a lot{/i} these last few days..."

    bapat "Yes, Abhay, you know me well."

    "So what would you advise me?"

    bapat "Tell her that she's fired if she doesn't come, it's the only way, Abhay."

    thinking "Should I listen to his advice?"

    $talk_bapat_act4 = True

    hide bapat with dissolve

    jump .advices

label .scene5:
    
    show priyanka with dissolve

    priyanka "We can't have this, Abhay."

    "And why not?"

    "Why not respect her religion?"

    priyanka "This is India, Abhay, the Motherland, this is a Hindu country."

    priyanka "Everyone has to accept, or to leave, Abhay, this is as much a part of being Indian as knowing the language, or the National Anthem."

    "You-{w=0.25}{nw}"

    priyanka "She can have her religion of course, but this is a public function, that she has to attend."

    "You know that India is a secular country, don't you?"

    priyanka "This has nothing to do with that, Abhay, this is official business."

    "I've heard you, Priyanka."

    "*sigh* Let me consider it."

    hide priyanka with dissolve

    thinking "Should I listen to her advice?"

    $talk_priyanka_act4 = True

    jump .advices

label .scene6:

    show donatello with dissolve

    donatello "This is tricky, Abhay."

    donatello "The others won't understand if she won't come, but if you force her, she will snap."

    "Exactly."

    donatello "Still, if you want this to be an opportunity to unite the employees, it needs to happen."

    donatello "So I really don't know what to advise you."

    "What would you do yourself in my position?"

    donatello "I don't know. She can't just skip it openly."

    donatello "Either you force her, and see what happens,{w=0.25} or you let her call in sick, maybe?"

    donatello "She could take a sick leave, and you would tell she's got a flu, or something?"

    thinking "Should I listen to his advice?"

    hide donatello with dissolve

    $talk_donatello_act4 = True

    jump .advices

label .scene7:
    show manali with dissolve

    manali "Oh why bother, respected Sir?"

    manali "One India, many religions."

    thinking "I-I didn't expect this. She's surprising me this time."

    thinking "So this is where she takes a stand?"

    manali "Why not let Giti be, she can always come later, why the intolerance?"

    "It's just that the others won't like this, Manali."

    manali "Abhay Sir, let them talk."

    manali "why is it that we always hurt the feelings of someone in this company?"

    "I wish this could be as simple as that, Manali."

    manali "Of course, this would be more simple if we were all Hindus, Abhay Sir, but this isn’t our reality."

    manali "This is why we have national holidays for all religions."

    "You may have a point here. I need to think about it."

    jump .advices

label .scene8:

    narration "You decide to write to M. Gopinath about it, and explain the situation. You receive an automatic out-of-the-office answer minutes later, and never hear about it again."

    mail "adnan.gopinath@cryptaloo.com 
            To: abhay.chandrakant@cryptaloo.in
            Out of the Office
            I am currently on leave, visiting the jungles of Angkor Wat. I will answer you as soon as I reach my office back. If you have any urgent matter, kindly write to M. Chandrakant at the following email: abhay.chandrakant@cryptaloo.in.
            Best regards,
            M. Gopinath"

    jump .advices

label .scene9:

    scene bg office with dissolve

    show giti with dissolve

    "It's not possible, Giti.{w=0.25} We are like one family here."

    "Surely you can't go away when your family has a function, can you?"

    narration "Giti looks at you with anger."

    giti "My family would respect my religion, Abhay Sir."

    "As we all do, as we all do,{w=0.25} but it's not only about religion."

    "It's about being together, and participating."

    "This is why I can't have you running away at an important time for the company, I'm sure you understand."

    giti "Not really, Abhay Sir, I-"

    "Now come on."

    "I'm sure you want to reassure everybody that you belong here."

    giti "I thought I was belonging already, Abhay Sir."

    "Indeed, indeed, all the more reason why you should come then."

    giti "I will not, Sir."

    "..."

    thinking "She's stubborn, but I will leave her no choice, this is too important."

    "You will, or you will no longer be part of this company."

    "See you tomorrow."

    narration "You leave the office."

    hide giti with dissolve

    thinking "That went well."

    menu:
        "Let's see how well.":
            jump .scene10

label .scene10:

    scene bg none with dissolve

    narration "You left her no choice."

    narration "The next day, Giti doesn’t show up at work.{p}
                You decide to let it slip, and to welcome her when she finally comes back, but she doesn’t—ever."

    narration "Since she was handling just about everything while M. Gopinath’s away, and left without a notice, or a word, her sudden departure threatens your core business, and no one is ready to replace her."

    narration " You start looking for a new Chief Secretary, but whoever comes next will need at least six months before he or she can handle Giti’s work efficiently. Let’s hope you can paper over the problems until the new CEO arrives, you want to make a good impression."

    $act_4_ending_10 = True
    $act_4_completed = True

    return

label .scene11:

    scene bg office with dissolve

    show giti with dissolve

    "I think I have found a solution, Giti."

    giti "Yes, Abhay Sir?"

    "I understand that you don’t want to participate in the ceremony, but from what I’ve gathered, it’s not so easy for everyone to accept that."

    giti "What's so difficult to accept, Abhay Sir?"

    "Oh you know very well, Giti, please, let me help you with this."

    giti "I am listening, Abhay Sir."

    "Let’s just say you caught a flu{w=0.25}, or something, you know,{w=0.25} call in sick, and take a leave tomorrow so that you can skip the blessing."

    giti "But, Sir, everybody will know that I have no flu, and that I just want to avoid the blessing."

    "Yes, but you can always pretend that you were sick to save face."

    giti "But this wouldn’t be the truth, and…"

    giti "…"

    giti "I understand, Abhay Sir, I will stay home tomorrow."

    menu:
        "The aftermath.":
            jump .scene13

label .scene12:

    show giti with dissolve

    "You can have the religion you like, Giti, and I respect that."

    narration "She nods."

    "When the Brahmin will come, just go drink a chai downstairs, or whatever, okay?"

    "Let’s not make a big issue of this, there’s nothing to worry about."

    giti "I appreciate it, Abhay Sir."

    "It’s not just me, it’s the Law, Giti, we must abide with the freedom of conscience, and religion."

    "I don’t even see how that could be a problem for anyone, we’re not an ashram here."

    narration "She laughs, then seems to ponder something."

    "What's the matter, Giti?"

    "Nothing, it’s nothing Abhay Sir, thank you."

    narration "And with that, she salutes you with her hands joined, and leaves your office."

    menu:
        "The aftermath.":
            jump .scene13

label .scene13:
    narration "As planned, Giti doesn’t show up on the next day."

    narration "With everyone busy watching the Brahmin, or singing mantras, and prayers, her absence didn’t seem to be noticed. If it was, everyone was tactful enough to avoid mentioning it, at the very least. {/i}Problem solved!{i} You congratulate yourself."

    narration "The morning following the ceremony, however, as you fetch your tea and whistle {/i}You are my Soniya{i} on your way, you find Giti waiting for you in front of your office."

    thinking "{/i}Again?{i}"

    narration "You let her in."

    show giti with dissolve

    "What can I do for you, Giti Madam?"

    giti "Abhay Sir, I was thinking."

    "Good, I approve this, we should be thinking more!"

    giti "Yes, Abhay Sir."

    "I was kidding, Giti, please tell me."

    giti "You know, Sir, since we were talking about it the other day, I thought I needed to tell you everything."

    "About what?"

    giti "About religion{w=0.25}, you see{w=0.25}, Abhay Sir{w=0.25}, I do my prayers during the day."

    giti "And since there's no space to pray, I have to do my prayers in the toilet, and now the ladies' toilets are clogged too so that I have to do in the general toilet."

    thinking "I know what she means."

    thinking "The men's loo could use some refresh{w=0.25}, or a flamethrower maybe."

    "So what do you want, Giti?"

    giti "‘I want a room I can use for my prayers, Abhay Sir."

    giti "It's not good to pray in the dirt like this."

    thinking "What should I do?"

    menu:
        "Take a decision straight away.":
            jump .scene14
        "Have lunch first":
            jump .scene15

label .scene14:
    thinking "There can be no compromise on serious issues like religion."

    thinking "I've taken my decision the minute she's started to talk."

    menu:
        "Reject her request.":
            jump .scene23
        "Accept immediately.":
            jump .scene24

label .scene15:
    scene bg lunch_room with dissolve

    thinking "First things first, a man needs his food three times a day."

    narration "You open your lunch box, and find delicious paneer fingers inside, with a side of steamed okras."

    "Why did it have to be okras...?"

    giti "You have fried paneer, don't you complain."

    priyanka "This won't happen if you cook it yourself, Abhay Sir!"

    bapat "This is not a man's job!"

    "I'm afraid I don't cook so well."

    manali "Then you learn! Hihi!"

    "I will try.{w=0.25} Why not?"

    manali "See, Bapat, Abhay Sir is ready for new experiences at least."

    bapat "As is Donatello."

    donatello "You're really looking for trouble, aren't you?"

    bapat "Just kidding this time, just kidding, trust me."

    thinking "Well, give peace a chance."

    thinking "It's been only two days, and here they are, talking, and laughing again."

    narration "You smile, then remember you have a pressing matter to solve, and shuffle back to your office."

    scene bg office with dissolve

    thinking "So, what should I do now?"

    menu:
        "Talk to the employees.":
            jump .scene16

label .scene16:

    thinking "Let's not change a winning strategy."

    thinking "Which one should I talk to first?"

label .employees2:

    menu:
        "Bapat." if talk_bapat_act4_2 == True:
            jump .scene17
        "Priyanka." if talk_priyanka_act4_2 == True:
            jump .scene18
        "Donatello." if talk_donatello_act4_2 == True:
            jump .scene19
        "Manali." if talk_manali_act4_2 == True:
            jump .scene20
        "M. Rajkumar, the company's lawyer." if talk_rajkumar_act4_2 == True:
            jump .scene21
        "M. Gopinath." if talk_gopinath_act4_2 == True:
            jump .scene22
        "I've talked to enough people." if talk_bapat_act4_2 == True or talk_priyanka_act4_2 == True or talk_donatello_act4_2 == True or talk_manali_act4_2 == True or talk_rajkumar_act4_2 == True:
            jump .advices2

label .advices2:

    menu:
        "Tell Giti she won't have a room." if talk_bapat_act4_2 == True or talk_priyanka_act4_2 == True or talk_donatello_act4_2 == True or talk_rajkumar_act4_2 == True:
            jump .scene23
        "Give Giti a room for her prayers." if talk_manali_act4_2 == True:
            jump .scene24
        "Email the Brahmin" if talk_manali_act4_2 == True or talk_rajkumar_act4_2 == True:
            jump .scene27
        "Talk to someone else." if talk_bapat_act4_2 == False or talk_priyanka_act4_2 == False or talk_donatello_act4_2 == False or talk_manali_act4_2 == False or talk_rajkumar_act4_2 == False or talk_gopinath_act4_2 == False:
            jump .employees2

label .scene17:
    scene bg meeting_room with dissolve

    show bapat with dissolve

    bapat "The nerve of this woman!"

    "Well, Bapat, all that she wants is to be able to pray."

    bapat "She can pray to her God, who am I to say she can't pray?"

    "You know very well that praying in the toilets isn’t very nice, Bapat, she does that!"

    "It's been three years!"

    bapat "Oh so she uses our toilets for this as well?{w=0.5} No wonder they’re dirty."

    "What can she do, she has no other spaces in the company for praying!"

    bapat "She can go to the mosque!"

    bapat "When I pray, I go to the temple myself, why can’t she do the same, why special rights, and service all the time?"

    bapat "Do I ask for special rights?"

    "You aren’t exactly a member of a minority in need, Bapat."

    bapat "This is our country, Abhay, don’t fall prey to their stratagems!"

    bapat "Already they should be grateful that we play {i}Khwaja Mere Khwaja{/i} during company functions like we always do, so that they’re happy, that’s it, don’t overdo it!"

    thinking "What should I do now?"

    $talk_bapat_act4_2 = True

    jump .advices2

label .scene18:

    scene bg meeting_room with dissolve

    show priyanka with dissolve

    priyanka "I knew this would happen."

    priyanka "The minute you decide to give them special treatment, they ask for more, and more, and-"

    "I get it, Priyanka."

    priyanka "You can’t turn this office into a mosque, Abhay!"

    "We’re talking one room, here, small one, for less than an hour a day in total."

    priyanka "And then what?{w=0.5} What will it be next?{w=0.5} More holidays?{w=0.5} A salary raise?"

    "She never asked for any of this, it’s only decent, Priyanka, she’s been kneeling in the toilets for three years!"

    priyanka "It makes us all very uncomfortable, Abhay!"

    "Who's \"us\", tell me?"

    priyanka "{i}All of us!{/i}"

    $talk_priyanka_act4_2 = True

    thinking "What should I do now?"

    jump .advices2

label .scene19:

    scene bg meeting_room with dissolve

    show donatello with dissolve

    donatello "This is too much, Abhay"

    "Why?"

    donatello "Not forcing her to go to Hindu ceremonies is one thing, but this prayer space idea is going too far, it’s not Emirate Airlines here."

    "You do realize she’s praying in the {i}toilet{/i}, Donald?"

    donatello "And what of us all?"

    donatello "We don’t have a room either, this is unfair."

    "This is a different religion, that’s why."

    "We allow sikhs with turbans, and even kukris, don’t we?"

    donatello "It’s not the same thing,{w=0.25} we didn’t build a mandir in here, did we?"

    "But we have a mandir, just over there."

    narration "You point in the general direction of the shrine in the office."

    donatello "Not a mandir room, Abhay, she wants a whole room just for herself!"

    donatello "How can you accept this?"

    donatello "How come they have all the benefits, and nothing for us, this is {i}our{/i} country!"

    "You don’t accept her religion, Donald."

    donatello "Of course I do."

    donatello "Don’t be naive, Abhay, you can’t give them what even we don’t have!"

    $talk_donatello_act4_2 = True

    thinking "What should I do now?"

    jump .advices2

label .scene20:

    scene bg office with dissolve

    show manali with dissolve

    manali "So she's been praying in the toilet for three years?"

    narration "You nod. She whistle."

    manali "Maybe it's about time we do something to change that?"

    "Yes, Manali, but don’t you think that this would be unfair for Hindus since we have no prayer room either?"

    manali "..."

    manali "You know, Abhay, if I imagine myself in her place..."

    manali "I must say that the whole office is a bit of a prayer room."

    manali "There’s the Ganapati up there, and the incense, and flower offerings we do in the morning."

    manali "We even invite brahmins to bless the office!"

    "Fair enough."

    "So you think I should agree?"

    manali "I don’t know.{w=0.25} I don’t know how the others will react."

    "*sigh*"

    manali "Maybe you could ask the brahmin who came yesterday?"

    manali "He seemed a good man."

    $talk_manali_act4_2 = True

    thinking "What should I do now?"

    jump .advices2

label .scene21:

    narration "You write to M. Rajkumar, the company’s Lawyer, and explain him the situation so that he can give you his advice. He answers a few hours later"

    mail "rajkumarrajkumarltd@gmail.com 
        To: abhay.chandrakant@cryptaloo.in
        Re: Prayer room
        Dear M. Chandrakant,
        The company cannot be held responsible ceteris paribus of the freedom of religion of its employees. As such, and notwithstanding, you are in no legal obligation to provide for a prayer locus, except in such situations where a prayer locus has been created within the company precincts for other confessions, in which case your employee could claim an unequal treatment, and ask for the corresponding damages. Since the matter entails subjects of philosophical, as well as  spiritual importance, I kindly urge you to ask to the spiritual authorities of your convenience for the rule of the Law falters in front of such highness. Also, having the toilets cleaned won’t probably hurt your case.
        With my very best regards,
        M. Rajkumar"

    $talk_rajkumar_act4_2 = True

    thinking "What should I do now?"

    jump .advices2

label .scene22:

    narration "You write to M. Gopinath, and ask for his advice. You receive an automatic out-of-the-office answer minutes later, and never hear about it again."

    mail "adnan.gopinath@cryptaloo.com 
            To: abhay.chandrakant@cryptaloo.in
            Out of the Office
            I am currently on leave as I participate in a sledge competition in Finland. I will answer you as soon as I am back in office. If you have any urgent matter, kindly write to M. Chandrakant at the following email: abhay.chandrakant@cryptaloo.in.
            Best regards,
            M. Gopinath"

    $talk_gopinath_act4_2 = True

    jump .advices2

label .scene23:
    scene bg meeting_room with dissolve

    show giti with dissolve

    "I can't do this, Giti."

    thinking "Better get straight to the point."

    giti "Why not, Abhay Sir?"

    "Because the others won’t understand why Muslims would get a special place, when we don't have any such spaces for Hindus, they think it’s unfair."

    giti "Yet they have a shrine in the office itself, and blessing ceremonies."

    "It’s true, Giti, but that’s how it is, there’s nothing I can do. I am sorry."

    giti "We can’t have everything, can we?"

    narration "You nod, and smile, happy that she understands."

    giti "We can't even have tolerance these days, this is too much to ask for in this world."

    narration "You stop smiling."

    "Giti, please, don't talk it like this..."

    giti "It’s fine, Abhay Sir, I’ve been praying in the toilets for three years."

    hide giti with dissolve

    giti "I can do it some more."

    thinking "What now?"

    menu:
        "What now?":
            jump .scene25

label .scene24:
    scene bg meeting_room with dissolve

    show giti with dissolve

    "Of course, you'll have it, Giti."

    giti "...!"

    giti "Sir, Abhay Sir, this is very good of you."

    "Don’t mention it, Giti, it’s nothing."

    "We never use the fifth floor storage room anyway so, why not get it cleaned, and prepared for your prayers?"

    giti "I will never forget, Abhay Sir, and I will pray for you!"

    "You can.{w=0.25} You have the room for this now after all!"

    hide giti with dissolve

    thinking "What now?"

    menu:
        "What now?":
            jump .scene26

label .scene25:

    narration "You can’t make a single person happy at the expense of all the others..."

    narration "The following weeks, Giti’s a little bit less active during the meetings, and eats more on her own at lunch, you hope she will understand your decision, and come back to her kind, efficient self before the new CEO steps in."

    $act_4_ending_25 = True
    $act_4_completed = True
    return

label .scene26:
    narration "Of course, Giti is delighted. All the other employees except Manali resent your decision, though, you can feel it in the way they talk, and look at you."

    narration " Well, you’re the Human Resources Manager, not their best friend forever, and you hope that once the dust settles, everybody will get back to their former, friendly selves."

    $act_4_ending_26 = True
    $act_4_completed = True

    return

label .scene27:
    narration "You decide to write to the Brahmin who came to bless the office, and to explain him the situation with Giti. After all, you’re dealing with a religious issue, and he’s a religious person. On the other hand, he’s a representative of the Hindus, and you assume that his answer will not help Giti much, but who knows?{p}
                He answers a few hours later."

    mail "swamiramram@jio.in 
        To: abhay.chandrakant@cryptaloo.in
        Re: Giti Madam
        Abhay,
        If we want respect from others, we should give them our respect first. We live in peace now in India because of this respect. I have seen prayer rooms in international airports, they are open to all, I have sung prayers in one such room in the past next to a Jewish Rabbi. Maybe you could use airports as an inspiration?
        Be blessed,
        Swami Ram Ram"

    menu:
        "Create a neutral prayer space for all.":
            jump .scene28

label .scene28:
    narration "Following Swami Ram Ram’s advice, you create a neutral space open to the prayers, yoga, and meditation of all religions. There is still some resistance from some of the employees, but at the end, even Bapat uses it for his yoga, and peace has returned to the office. Congratulations."
    
    $act_4_ending_28 = True
    $act_4_completed = True
    return

label .end:
    narration "Act 4 End."
    $act_4_completed = True
    $renpy.call_screen("act_menu")

    return
