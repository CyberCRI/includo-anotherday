
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

    narration "Just as you’re imagining the ceremony, smiling to yourself, you notice Giti waiting for you by your office’s door with a grim expression."

    show giti with dissolve

    thinking "What now?"

    narration "You let her in, and she starts talking straight away."

    giti "Abhay Sir, this is because of the ceremony."

    abhay "Oh yes, Giti! {w=0.25}It's going to be great!"

    show giti sad

    giti sad "Abhay Sir, maybe you forgot, I am Muslim."

    thinking "{b}Of course{/b}, how could I have forgotten?"

    abhay "My goodness, that's true!{w=0.5} Let's-"

    giti sad "I cannot participate, Abhay Sir, these are not my beliefs."

    menu:
        thinking "..."
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

    scene bg meeting_room with dissolve 

    narration "To find the true feelings of your employees on such a delicate matter, you don't think that calling people to your office is the best idea."

    narration "You decide to use the meeting room as a more neutral place for informal discussions."

    narration "You move to the meeting room with a pen, and a piece of paper, you want this to be as informal as possible, but you need to hear what they think about the situation."

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
        "Write to M. Gopinath instead." if not talk_gopinath_act4:
            jump .scene8
        "I've talked to enough people." if talk_bapat_act4 or talk_priyanka_act4 or talk_donatello_act4 or talk_manali_act4 or talk_gopinath_act4:
            jump .advices

label .advices:
    menu:
        "Tell Giti you'll fire her if she doesn't come." if talk_bapat_act4 or talk_priyanka_act4 or talk_donatello_act4:
            jump .scene9
        "Offer Giti to take a sick leave tomorrow." if talk_donatello_act4:
            jump .scene11
        "Tell Giti she can skip the ceremony, and come later." if talk_manali_act4:
            jump .scene12
        "Talk to the other employees." if not talk_bapat_act4 or not talk_priyanka_act4 or not talk_donatello_act4 or not talk_manali_act4 or not talk_gopinath_act4:
            jump .employees

label .scene4:

    show bapat with dissolve

    bapat "Abhay, it will ruin the ceremony if she doesn’t come!"

    bapat "It's either all of us, or none of us."

    abhay "But Bapat, she's not Hindu."

    bapat "Hindu, or not, Abhay, it's not the point, it's being together for the company."

    show bapat angry

    bapat angry "How can she exclude herself, and still pretend she's working with us?"

    abhay "Well, technically, Bapat, we also exclude her by having a Hindu ceremony."

    show bapat

    bapat "No, no, Abhay, you don't get it, it's not about religion, it's about the team spirit."

    bapat "You know how much it matters to me."

    abhay "Indeed."

    abhay "You have proven it {i}quite a lot{/i} these last few days... {w=0.5}*sigh*"

    show bapat smug

    bapat smug "Yes, Abhay, you know me well."

    thinking "Seems like he didn't take the hint."

    thinking "Well, it doesn't matter."

    abhay "So what would you advise me?"

    show bapat

    bapat "Tell her that she's fired if she doesn't come, it's the only way, Abhay."

    thinking "Should I listen to his advice?"

    $talk_bapat_act4 = True

    hide bapat with dissolve

    jump .advices

label .scene5:
    
    show priyanka with dissolve

    priyanka "We can't have this, Abhay."

    abhay "And why not?"

    abhay "Why not respect her religion?"

    show priyanka angry

    priyanka angry "This is India, Abhay, the Motherland, this is a Hindu country."

    priyanka angry "Everyone has to accept, or to leave, Abhay."

    priyanka angry "This is as much a part of being Indian as knowing the language, or the National Anthem."

    abhay "How-{w=0.25}{nw}"

    priyanka angry "She can have her religion of course, but this is a public function, that she has to attend."

    abhay "You know that India is a secular country, don't you?"

    show priyanka

    priyanka "This has nothing to do with that, Abhay, this is official business."

    abhay "I've heard you, Priyanka."

    abhay "*sigh*{w=1} Let me consider it."

    hide priyanka with dissolve

    thinking "Should I listen to her advice?"

    $talk_priyanka_act4 = True

    jump .advices

label .scene6:

    show donatello determined with dissolve

    donatello determined "This is tricky, Abhay."

    donatello determined "The others won't understand if she won't come, but if you force her, she will snap."

    abhay "Exactly."

    donatello determined "Still, if you want this to be an opportunity to unite the employees, it needs to happen."

    show donatello

    donatello "So I really don't know what to advise you."

    abhay "What would you do yourself in my position?"

    donatello "I don't know. She can't just skip it openly."

    show donatello determined

    donatello determined "Either you force her, and see what happens,{w=0.25} or you let her call in sick, maybe?"

    show donatello

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

    abhay "It's just that the others won't like this, Manali."

    manali "Abhay Sir, let them talk."

    manali "why is it that we always hurt the feelings of someone in this company?"

    abhay "I wish this could be as simple as that, Manali."

    show manali smiling

    manali smiling "Of course, this would be more simple if we were all Hindus, Abhay Sir, but this isn’t our reality."

    manali smiling "This is why we have national holidays for all religions."

    abhay "You may have a point here. I need to think about it."

    hide manali with dissolve

    $talk_manali_act4 = True

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

    abhay "It's not possible, Giti.{w=0.25} We are like one family here."

    abhay "Surely you can't go away when your family has a function, can you?"

    show giti eager

    giti eager "...!"

    giti eager "My family would respect my religion, Abhay Sir."

    abhay "As we all do, as we all do,{w=0.25} but it's not only about religion."

    abhay "It's about being together, and participating."

    abhay "This is why I can't have you running away at an important time for the company, I'm sure you understand."

    giti eager "Not really, Abhay Sir, I-"

    abhay "Now come on."

    abhay "I'm sure you want to reassure everybody that you belong here."

    show giti sad

    giti sad "I thought I was belonging already, Abhay Sir."

    abhay "Indeed, indeed, all the more reason why you should come then."

    show giti eager

    giti eager "I will not, Sir."

    abhay "..."

    thinking "She's stubborn, but I will leave her no choice, this is too important."

    abhay "You will, or you will no longer be part of this company."

    abhay "See you tomorrow."

    narration "You leave the office."

    hide giti with dissolve

    menu:
        thinking "That went well."
        "Let's see how well.":
            jump .scene10

label .scene10:

    scene bg none with dissolve

    narration "You left her no choice."

    narration "The next day, Giti doesn’t show up at work.{p}
                You decide to let it slip, and to welcome her when she finally comes back, but she doesn’t—ever."

    narration "Since she was handling just about everything while M. Gopinath’s away, and left without a notice, or a word, her sudden departure threatens your core business, and no one is ready to replace her."

    narration "You start looking for a new Chief Secretary, but whoever comes next will need at least six months before he or she can handle Giti’s work efficiently. Let’s hope you can paper over the problems until the new CEO arrives, you want to make a good impression."

    $act_4_ending_10 = True
    jump .end

label .scene11:

    scene bg office with dissolve

    show giti with dissolve

    abhay "I think I have found a solution, Giti."

    giti "Yes, Abhay Sir?"

    abhay "I understand that you don’t want to participate in the ceremony..."

    abhay "...But from what I’ve gathered, it’s not so easy for everyone to accept that."

    giti "What's so difficult to accept, Abhay Sir?"

    abhay "Oh you know very well, Giti, please, let me help you with this."

    show giti determined

    giti determined "I am listening, Abhay Sir."

    abhay "Let’s just say you caught a flu{w=0.25}, or something, you know,{w=0.25} call in sick, and take a leave tomorrow so that you can skip the blessing."

    show giti sad

    giti sad "But, Sir, everybody will know that I have no flu, and that I just want to avoid the blessing."

    abhay "Yes, but you can always pretend that you were sick to save face."

    giti sad "But this wouldn’t be the truth, and…"

    show giti 

    giti ".{w=0.25}.{w=0.25}."

    show giti determined

    giti determined "I understand, Abhay Sir, I will stay home tomorrow."

    menu:
        "The aftermath.":
            hide giti with dissolve
            jump .scene13

label .scene12:

    show giti with dissolve

    abhay "You can have the religion you like, Giti, and I respect that."

    narration "She nods."

    abhay "When the Brahmin will come, just go drink a chai downstairs, or whatever, okay?"

    abhay "Let’s not make a big issue of this, there’s nothing to worry about."

    giti "I appreciate it, Abhay Sir."

    abhay "It’s not just me, it’s the Law, Giti, we must abide with the freedom of conscience, and religion."

    abhay "I don’t even see how that could be a problem for anyone, we’re not an ashram here."

    show giti smiling

    giti "*laughs*"

    show giti determined

    giti determined ".{w=0.25}.{w=0.25}."

    abhay "What's the matter, Giti?"

    show giti

    giti "Nothing, it’s nothing Abhay Sir, thank you."

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

    abhay "What can I do for you, Giti Madam?"

    giti "Abhay Sir, I was thinking."

    abhay "Good, I approve this, we should be thinking more!"

    giti "Yes, Abhay Sir."

    abhay "I was kidding, Giti, please tell me."

    show giti determined

    giti determined "You know, Sir, since we were talking about it the other day, I thought I needed to tell you everything."

    abhay "About what?"

    show giti

    giti "About religion{w=0.25}, you see{w=0.25}, Abhay Sir{w=0.25}, I do my prayers during the day."

    giti "And since there's no space to pray, I have to do my prayers in the toilet."

    giti "And now the ladies' toilets are clogged too so that I have to do in the general toilet."

    thinking "I know what she means."

    thinking "The men's loo could use some refresh{w=0.25}, or a flamethrower maybe."

    abhay "So what do you want, Giti?"

    show giti determined 

    giti determined "I want a room I can use for my prayers, Abhay Sir."

    show giti sad

    giti sad "It's not good to pray in the dirt like this."

    menu:
        thinking "What should I do?"
        "Take a decision straight away.":
            jump .scene14
        "Have lunch first":
            jump .scene15

label .scene14:
    thinking "There can be no compromise on serious issues like religion."

    menu:
        thinking "I've taken my decision the minute she's started to talk."
        "Reject her request.":
            jump .scene23
        "Accept immediately.":
            jump .scene24

label .scene15:
    scene bg lunch_room with dissolve

    thinking "First things first, a man needs his food three times a day."

    narration "You open your lunch box, and find delicious paneer fingers inside, with a side of steamed okras."

    abhay "Why did it have to be okras...?"

    giti smiling "You have fried paneer, don't you complain."

    priyanka smiling "This won't happen if you cook it yourself, Abhay Sir!"

    bapat angry "This is not a man's job!"

    abhay "I'm afraid I don't cook so well."

    manali smiling "Then you learn! Hihi!"

    abhay "I will try.{w=0.25} Why not?"

    manali smiling "See, Bapat, Abhay Sir is ready for new experiences at least."

    bapat smug "As is Donatello."

    donatello determined "You're really looking for trouble, aren't you?"

    bapat "Just kidding this time, just kidding, trust me."

    thinking "Well, give peace a chance."

    thinking "It's been only two days, and here they are, talking, and laughing again."

    narration "You smile, then remember you have a pressing matter to solve, and shuffle back to your office."

    scene bg office with dissolve

    menu:
        thinking "So, what should I do now?"
        "Talk to the employees.":
            jump .scene16

label .scene16:

    thinking "Let's not change a winning strategy."

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
        "M. Rajkumar, the company's lawyer." if not talk_rajkumar_act4_2:
            jump .scene21
        "M. Gopinath." if not talk_gopinath_act4_2:
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
    scene bg meeting_room with dissolve

    show bapat angry with dissolve

    bapat angry "The nerve of this woman!"

    abhay "Well, Bapat, all that she wants is to be able to pray."

    bapat angry "She can pray to her God, who am I to say she can't pray?"

    abhay "You know very well that praying in the toilets isn’t very nice, Bapat, she does that!"

    abhay "It's been three years!"

    show bapat 

    bapat "Oh so she uses our toilets for this as well?"

    show bapat smug 

    bapat smug "No wonder they’re dirty."

    abhay "What can she do, she has no other spaces in the company for praying!"

    show bapat angry

    bapat angry "She can go to the mosque!"

    bapat angry "When I pray, I go to the temple myself, why can’t she do the same, why special rights, and service all the time?"

    bapat angry "Do I ask for special rights?"

    abhay "You aren’t exactly a member of a minority in need, Bapat."

    show bapat angry

    bapat angry "This is our country, Abhay, don’t fall prey to their stratagems!"

    show bapat smug

    bapat smug "Already they should be grateful that we play {i}Khwaja Mere Khwaja{/i} during company functions like we always do, so that they’re happy"

    show bapat angry

    bapat angry "That’s it, don’t overdo it!"

    hide bapat

    $talk_bapat_act4_2 = True

    jump .advices2

label .scene18:

    scene bg meeting_room with dissolve

    show priyanka with dissolve

    priyanka "I knew this would happen."

    priyanka "The minute you decide to give them special treatment, they ask for more, and more, and-"

    abhay "I get it, Priyanka."

    show priyanka angry

    priyanka angry "You can’t turn this office into a mosque, Abhay!"

    abhay "We’re talking one room, here, small one, for less than an hour a day in total."

    priyanka angry "And then what?{w=0.5} What will it be next?{w=0.5} More holidays?{w=0.5} A salary raise?"

    abhay "She never asked for any of this, it’s only decent, Priyanka, she’s been kneeling in the toilets for three years!"

    priyanka angry "It makes us all very uncomfortable, Abhay!"

    abhay "Who's \"us\", tell me?"

    priyanka angry"{i}All of us!{/i}"

    hide priyanka

    $talk_priyanka_act4_2 = True

    jump .advices2

label .scene19:

    scene bg meeting_room with dissolve

    show donatello with dissolve

    donatello "This is too much, Abhay"

    abhay "Why?"

    donatello "Not forcing her to go to Hindu ceremonies is one thing, but this prayer space idea is going too far."

    donatello "It’s not Emirate Airlines here."

    abhay "You do realize she’s praying in the {i}toilet{/i}, Donald?"

    show donatello determined

    donatello determined "And what of us all?"

    donatello determined "We don’t have a room either, this is unfair."

    abhay "This is a different religion, that’s why."

    abhay "We allow sikhs with turbans, and even kukris, don’t we?"

    show donatello

    donatello "It’s not the same thing,{w=0.25} we didn’t build a mandir in here, did we?"

    abhay "But we have a mandir, just over there."

    narration "You point in the general direction of the shrine in the office."

    show donatello angry

    donatello angry "Not a mandir room, Abhay, she wants a whole room just for herself!"

    show donatello

    donatello "How can you accept this?"

    show donatello angry

    donatello angry "How come they have all the benefits, and nothing for us, this is {i}our{/i} country!"

    abhay "You don’t accept her religion, Donald."

    show donatello determined

    donatello determined "Of course I do."

    show donatello

    donatello "Don’t be naive, Abhay, you can’t give them what even we don’t have!"

    $talk_donatello_act4_2 = True

    jump .advices2

label .scene20:

    scene bg office with dissolve

    show manali with dissolve

    manali "So she's been praying in the toilet for three years?"

    narration "You nod. She whistle."

    manali "Maybe it's about time we do something to change that?"

    abhay "Yes, Manali, but don’t you think that this would be unfair for Hindus since we have no prayer room either?"

    manali "..."

    manali "You know, Abhay, if I imagine myself in her place..."

    manali "I must say that the whole office is a bit of a prayer room."

    manali "There’s the Ganapati up there, and the incense, and flower offerings we do in the morning."

    manali "We even invite brahmins to bless the office!"

    abhay "Fair enough."

    abhay "So you think I should agree?"

    manali "I don’t know.{w=0.25} I don’t know how the others will react."

    abhay "*sigh*"

    manali "Maybe you could ask the brahmin who came yesterday?"

    manali "He seemed a good man."

    $talk_manali_act4_2 = True

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

    abhay "I can't do this, Giti."

    thinking "Better get straight to the point."

    giti "Why not, Abhay Sir?"

    abhay "Because the others won’t understand why Muslims would get a special place, when we don't have any such spaces for Hindus, they think it’s unfair."

    giti "Yet they have a shrine in the office itself, and blessing ceremonies."

    abhay "It’s true, Giti, but that’s how it is, there’s nothing I can do. I am sorry."

    show giti compassionate

    giti compassionate "We can’t have everything, can we?"

    narration "You nod, and smile, happy that she understands."

    show giti angry

    giti angry "We can't even have tolerance these days, this is too much to ask for in this world."

    narration "You stop smiling."

    abhay "Giti, please, don't talk it like this..."

    show giti smiling

    giti smiling "It’s fine, Abhay Sir, I’ve been praying in the toilets for three years."

    hide giti with dissolve

    giti smiling "I can do it some more."

    menu:
        thinking "What now?"
        "What now?":
            jump .scene25

label .scene24:
    scene bg meeting_room with dissolve

    show giti with dissolve

    abhay "Of course, you'll have it, Giti."

    giti "...!"

    show giti smiling

    giti smiling "Sir, Abhay Sir, this is very good of you."

    abhay "Don’t mention it, Giti, it’s nothing."

    abhay "We never use the fifth floor storage room anyway so, why not get it cleaned, and prepared for your prayers?"

    show giti smiling

    giti smiling "I will never forget, Abhay Sir, and I will pray for you!"

    abhay "You can.{w=0.25} You have the room for this now after all!"

    hide giti with dissolve

    thinking "What now?"

    menu:
        "What now?":
            jump .scene26

label .scene25:

    narration "You can’t make a single person happy at the expense of all the others..."

    narration "The following weeks, Giti’s a little bit less active during the meetings, and eats more on her own at lunch, you hope she will understand your decision, and come back to her kind, efficient self before the new CEO steps in."

    $act_4_ending_25 = True
    jump .end

label .scene26:
    narration "Of course, Giti is delighted. All the other employees except Manali resent your decision, though, you can feel it in the way they talk, and look at you."

    narration " Well, you’re the Human Resources Manager, not their best friend forever, and you hope that once the dust settles, everybody will get back to their former, friendly selves."

    $act_4_ending_26 = True
    jump .end

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
    jump .end

label .end:
    narration "Act 4 End."
    $act_4_completed = True
    $renpy.call_screen("act_menu")

    return
