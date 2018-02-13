# The script of the game goes in this file.
# The game starts here.

label act3:
    $act_3_completed = False

    $talk_bapat_act3 = False
    $talk_manali_act3 = False
    $talk_priyanka_act3 = False
    $talk_giti_act3 = False

    $talk_bapat_act3_2 = False
    $talk_manali_act3_2 = False
    $talk_priyanka_act3_2 = False
    $talk_giti_act3_2 = False

    $act_3_ending_10 = False
    $act_3_ending_13 = False

    window hide

    stop music fadeout 1.0

    stop background fadeout 1.0

    scene bg none

    $renpy.pause(3.0)

    play background "music/crowd.ogg" fadein 3.0 

    narration "Everybody’s at lunch, gathered together in the small canteen."

    scene bg lunch_room
    with Dissolve(3.0)

    play music "music/Kai_Engel_Ode_To_The_World.mp3" fadein 3.0 fadeout 3.0

    narration "You unpack your lunchbox, and share around the delicious parathas you find inside before starting to eat.{p}
            The last events have taken their toll, and the atmosphere is rather uneasy."


    thinking "People don't like change."

    narration "Priyanka and Manali’s jokes are most welcome today, lifting up the mood a bit."

    show priyanka smiling at center, talking with dissolve

    priyanka smiling "...And then, he turned around and said, “Are you sure these are your trousers?”"

    narration "Manali bursts into laughter, almost tipping her glass over."

    hide priyanka
    show manali at center, talking
    with dissolve

    manali smiling "So he's not the one, I guess, Priyanka?"

    hide manali
    show priyanka smiling at center, talking
    with dissolve

    priyanka smiling "Definitely not the one."

    hide priyanka
    show manali smiling at center, talking
    with dissolve

    manali "Well, he sounds funny at least. Is your husband funny, Giti?"

    narration "They both laugh."

    hide manali
    show giti smiling at center, talking
    with dissolve

    giti smiling "Shoo, you girls, what a racket you're making today!"

    hide giti
    show priyanka smiling at center, talking
    with dissolve

    priyanka smiling "Come one, Giti, everybody’s married except us, we are entitled to our fun!"

    hide priyanka
    show bapat at center, talking
    with dissolve

    bapat "Not everyone!"

    hide bapat
    show priyanka at center, talking
    with dissolve

    priyanka "..."

    hide priyanka
    show bapat smug at center, talking
    with dissolve

    bapat smug "Donatello is a bachelor as well!"

    stop music fadeout 3.0

    hide bapat
    show donatello nervous at center, talking
    with dissolve

    donatello "..."

    hide donatello
    show manali at center, talking
    with dissolve

    manali "Is it true, Donald?"

    hide manali
    show donatello at center, talking
    with dissolve

    donatello "..."

    stop music fadeout 3.0

    narration "Donatello wipes his mouth with a napkin, and stares into the void a little too long before answering."

    show donatello at talking

    donatello "I am a bachelor, yes."

    show donatello dark at not_talking, move_right

    show priyanka smiling at center, talking
    with dissolve

    show priyanka at move_left

    play music "music/Kai_Engel_Machinery.mp3"

    priyanka "How come?!" (show_namepos="left")

    priyanka "You have a good job and all, why aren't you married?" (show_namepos="left")

    hide priyanka
    show bapat smug at center_left, talking
    with dissolve

    bapat "Yes, {i}why{/i}?" (show_namepos="left")

    show bapat smug dark at not_talking
    show donatello nervous at talking

    donatello "..." (show_namepos="right")

    hide bapat
    show manali smiling at center_left, talking
    with dissolve

    manali "Maybe he hasn't found the one true love?" (show_namepos="left")

    hide manali
    show bapat smug at center_left, talking
    with dissolve

    bapat "Or maybe he can't tell..." (show_namepos="left")

    hide bapat
    show priyanka angry at center_left, talking
    with dissolve

    priyanka "We were joking, Bapat, don't be your usual downer!" (show_namepos="left")

    hide priyanka
    show bapat smug at center_left, talking
    with dissolve

    bapat "I am joking too!{w=0.5} {i}Hahaha!{/i}" (show_namepos="left")

    show bapat smug dark at not_talking

    show donatello at talking

    donatello "..." (show_namepos="right")

    show donatello dark at not_talking

    narration "Donatello leaves the table, heading to the sink with his plate, shortly followed by Bapat."

    hide donatello with dissolve
    hide bapat with dissolve

    thinking "Here comes trouble..."

    menu:
        "You follow them as well.":
            jump .scene2

label .scene2:

    window hide

    show bg none with fade

    stop background fadeout 3.0

    narration "You see Bapat and Donatello whispering furiously to each other inside the meeting room. From the sound of it, their conversation doesn't seem especially friendly."    

    menu:
        thinking "I'm being too curious there. Maybe I should just let them be..."
        "Get closer to hear what they say.":
            jump .scene3
        "Slip away, and let them be.":
            jump .scene4

label .scene3:

    scene bg meeting_room
    with Dissolve(3.0)

    show bapat angry dark at center_left, not_talking
    show donatello dark at center_right, not_talking with dissolve

    show bapat angry at center_left, talking

    bapat "I was going to pay, yes." (show_namepos="left")

    bapat "But no longer." (show_namepos="left")

    show bapat smug dark at not_talking
    show donatello angry at talking

    donatello "What are you talking about?" (show_namepos="right")

    donatello "Of course you will give me the money back, Bapat, or I will-" (show_namepos="right")

    show donatello dark at not_talking
    show bapat angry at talking

    bapat "You will nothing." (show_namepos="left")

    show bapat smug dark at not_talking
    show donatello nervous dark with dissolve

    narration "Bapat takes his cell phone out of his pocket."

    show donatello nervous at talking

    donatello "And why is that?" (show_namepos="right")

    show donatello nervous dark at not_talking

    show bapat smug dark with dissolve

    show bapat smug at talking

    bapat "You just look at this." (show_namepos="left")

    show bapat smug dark at not_talking

    narration "Bapat shows his phone to Donatello."

    show donatello nervous at talking

    donatello "..." (show_namepos="right")

    show donatello angry
    with dissolve

    donatello "Where did you get this?!" (show_namepos="right")

    show donatello nervous dark at not_talking

    show bapat smug at talking

    bapat "Ah, ah, interested now?" (show_namepos="left")

    show bapat
    with dissolve

    bapat "I've taken a picture of your computer, you've left your email open, Donald." (show_namepos="left")

    show bapat smug
    with dissolve

    bapat "or should I say...{w=0.5} {i}Daisy{/i}?" (show_namepos="left")

    show bapat smug dark at not_talking

    show donatello angry at talking 

    donatello "Are you threatening me for real?" (show_namepos="right")

    show donatello determined dark at not_talking 

    show bapat at talking

    bapat "Oh I am,{w=0.5} yes I am, either you support my decisions, or I tell everyone." (show_namepos="left")

    show bapat with dissolve

    bapat "How would you like it,{w=0.25} the whole office knowing?" (show_namepos="left")

    bapat "I can almost hear them already." (show_namepos="left")

    show bapat smug dark at not_talking

    abhay "{i}Ahem.{/i}"

    stop music fadeout 3.0

    show bapat at talking

    bapat "..." (show_namepos="left")

    show bapat dark at not_talking

    show donatello nervous at talking

    donatello "..." (show_namepos="right")

    show donatello dark at not_talking

    abhay "Knowing {i}what{/i}?"

    show bapat nervous at talking
    with dissolve

    bapat "Nothing, Abhay, it's nothing." (show_namepos="left")

    show bapat
    with dissolve

    bapat "Professional stuff, corporate stuff, high-level." (show_namepos="left")

    show bapat dark at not_talking

    abhay "Indeed."

    abhay "Is there anything you'd like to report to me, Donatello?"

    show donatello dark
    show bapat nervous at talking

    bapat "..." (show_namepos="left")

    show bapat nervous dark at not_talking

    show donatello at talking

    donatello "No, Abhay, no, it's nothing." (show_namepos="right")

    show donatello dark at not_talking

    abhay "We'll see about that."

    hide donatello
    with dissolve

    narration "You leave the room."

    hide bapat
    with dissolve

    menu:
        thinking "Bapat's behaviour is suspicious to say the least."
        "Give a warning to Bapat straight away.":
            jump .scene5
        "Let them cope by themselves.":
            jump .scene6

label .scene4:
    narration "You’re not supposed to be spying on the employees, so you walk away, and let them sort out whatever it is they need to sort out among themselves.{p}
                The rest of the day is uneventful though you can’t dismiss the feeling that you’ve missed something important no matter how hard you try to shrug it off."

    window hide

    show bg office with dissolve

    play music "music/Kai_Engel_Anxiety.mp3" fadein 3.0 fadeout 3.0

    narration "The next day, just before lunch break, Donatello asks to see you."

    narration "Since you remember the last team lunch vividly enough, you let him come into your office, and talk."

    show donatello nervous at center, talking with dissolve

    donatello nervous "I need to tell it to everyone, Abhay."

    donatello nervous "I don't see why I should hide, and let people like Bapat try to take advantage of me."

    show donatello nervous dark at not_talking

    abhay "Wait, say what?{w=0.5} What did Bapat do?"

    show donatello at talking

    donatello "Doesn't matter, Abhay."

    show donatello nervouswith dissolve

    donatello nervous "What matters is that I need to say it, I really need."

    donatello nervous "And be able to live my life as myself, not the image I give all the time."

    show donatello nervous dark at not_talking

    stop music fadeout 3.0

    abhay "What on Earth are you talking about?"

    show donatello determined at talking

label .gay:

    play music "music/Kevin_MacLeod_I_Knew_A_Guy.mp3" fadein 3.0 fadeout 3.0

    donatello "I am gay, Abhay, that's why I'm not married."

    show donatello determined dark at not_talking

    abhay "W-What?"

    abhay "But it was only yesterday that you groped Priyanka!{w=0.5} Are you insane?"

    show donatello determined at talking

    donatello "That was a mask, Abhay. I was overdoing it on purpose."

    show donatello determined dark at not_talking

    thinking "Just wow."

    abhay "Did you even think about how she felt?"

    abhay "You should have tried to tell her, maybe she would have helped!"

    show donatello thoughtful at talking

    donatello "You don't know Priyanka so well, Abhay, no offense but-"

    show donatello dark at not_talking

    abhay "Right. But why the hurry?"

    abhay "Why do you need to shout it to the whole office, Donald?"

    abhay "You're not married with these people, you don't owe them any kind of explanation."

    show donatello determined at talking

    donatello determined "It's not that."

    donatello determined "I feel like I'm lying to them- all the time, and to myself!"

    donatello determined "Plus they already know, Abhay, it's too late for hiding."

    show donatello nervous
    with dissolve

    donatello nervous "Bapat tried to use it against me, they all will, and it will be worse, better say it now!"

    show donatello nervous dark at not_talking

    thinking "He's awfully nervous, even out of his mind."

    thinking "Is this because what he's doing right now takes a lot of courage..."

    thinking "Or is he going mad somewhat, and just making this all up?"

    abhay "You should think before going ahead like that, Donald."

    abhay "There will be consequences, and you won't be able to take it back, and-"

    play music "music/Kai_Engel_Anxiety.mp3" fadein 3.0 fadeout 3.0

    show donatello angry at talking

    donatello angry "You, of all people, I thought you would understand, Abhay!"

    show donatello angry dark at not_talking

    hide donatello with dissolve

    narration "Donatello strides away in a whirlwind."

    thinking "Wait, no!"

    menu:
        "Follow him":
            jump .scene7


label .scene5:
    window hide 

    scene bg office with dissolve

    show bapat dark at center_left, not_talking with dissolve

    show donatello dark at center_right, not_talking with dissolve

    play music "music/Kai_Engel_Anxiety.mp3" fadein 3.0 fadeout 3.0

    narration "You call Bapat and Donatello together into your office just before the lunch break on the next morning.
                Neither of them sit down. {w=0.5}Instead they both stand in front of you like naughty college students waiting for their scolding."

    abhay "I heard you threatening Donatello yesterday, Bapat"

    show bapat nervous at talking

    bapat nervous "Oh, Abhay, it's not like that-" (show_namepos="left")

    show bapat nervous dark at not_talking

    abhay "I've heard it!{w=0.5} Kindly don't insult my intelligence."

    narration "You give him {b}the look{/b}, forehead lowered, eyes looking up straight at him like a bull."

    abhay "I don’t want to know what you’ve threatened him with, Bapat, I just-"

    show donatello determined at talking

    donatello "But you will." (show_namepos="right")

    show donatello determined dark at not_talking with None

    show bapat at talking

    bapat "..." (show_namepos="left")

    show bapat dark at not_talking

    abhay "I beg your pardon?"

    show donatello determined at talking

    donatello "You will know because I've had enough." (show_namepos="right")

    donatello  "I need to tell it to everyone, Abhay" (show_namepos="right")

    donatello "I don’t see why I should hide, and let people like Bapat try to take advantage of me." (show_namepos="right")

    show donatello determined dark at not_talking

    stop music fadeout 3.0

    abhay "Wait, say what?"

    hide bapat with dissolve

    show donatello determined at center_right, move_center_from_right, talking
    with None

    jump .gay

label .scene6:

    thinking "Something's not right, I can feel it in my bones."

    thinking "After all those years as a HR Manager, I've developed some kind of special sense when it comes to trouble, and trouble there is."

    thinking "Yet, I can't really accuse Bapat without more proof than something I've overheard at the canteen."

    thinking "Plus, I'm not supposed to listen in on private conversations."

    thinking "It's better to let it slip."

    window hide

    scene bg office with Dissolve(3.0)

    pause 3.0

    play music "music/Kai_Engel_Anxiety.mp3" fadein 3.0 fadeout 3.0

    narration "The next day, just before lunch break, Donatello asks to see you."

    narration "Since you remember the last team lunch vividly enough, you let him come into your office, and talk."

    show donatello nervous at talking
    with dissolve

    donatello "I need to tell it to everyone, Abhay."

    show donatello determined
    with dissolve

    donatello "I don't see why I should hide, and let people like Bapat try to take advantage of me."

    show donatello determined dark at not_talking

    abhay "Wait, say what?{w=0.5} What did Bapat do?"

    show donatello determined at talking

    donatello "Doesn't matter, Abhay."

    show donatello nervous
    with dissolve

    donatello "What matters is that I need to say it, I really need."

    donatello "And be able to live my life as myself, not the image I give all the time."

    show donatello nervous dark at not_talking

    stop music fadeout 3.0

    abhay "What on Earth are you talking about?"

    show donatello determined at move_center_from_right, talking

    jump .gay

label .scene7:

    narration "You lean back into your chair, surprised by the turn the events have taken."

    narration "A few minutes later, you start wondering where Donatello might have gone after storming out of your office, and you head to the canteen."

    window hide

    scene bg lunch_room with dissolve

    play background "music/crowd.ogg"

    narration "When you reach it, you hear Donatello’s shaky voice echoing in a dead silence before you open the door."

    show donatello determined at center_left, talking
    with dissolve

    donatello "... So no, I'm not married, and never will be, {w=0.5}or not to a woman." (show_namepos="left")

    show donatello nervous dark at not_talking

    thinking "So he did it."

    thinking "There's no way to predict how people will react to this."

    thinking "And I can't help feeling afraid of the consequences..."

    thinking "He must be feeling the same way."

    show bapat angry at center_right, talking
    with dissolve

    bapat "You should move to the US if you want to marry a man, there will none of it here!" (show_namepos="right")

    show bapat angry dark at not_talking with None

    show donatello at talking

    donatello "..." (show_namepos="left")

    show donatello dark at not_talking

    narration "You hear a couple of people clapping, cheering, and whistling."

    show bapat angry at talking

    bapat angry "How can I work with you now that I know?" (show_namepos="right")

    show bapat smug
    with dissolve

    bapat smug "I'm not going to be your girlfriend, you need to move to another office!" (show_namepos="right")

    show donatello nervous dark at not_talking
    show bapat smug dark at not_talking

    thinking "Just look at him, excited by his own success."

    thinking "Everyone has fifteen minutes of glory in life, or so I've heard, maybe this is Bapat's moment of fame."

    show bapat angry at talking

    bapat angry "Are we supposed to accept this indecency?!" (show_namepos="right")

    hide bapat
    show donatello determined dark at not_talking
    show giti at center_right, talking
    with dissolve

    giti "..." (show_namepos="right")

    show giti dark at not_talking

    thinking "Ok, time to step in."

    narration "You push the door, and see Bapat standing, his face contorted with anger.
            Priyanka, and Manali are laughing nervously. Only Giti remains silent, still listening to Donatello, who seems to be holding his own."

    hide giti
    show bapat smug dark at center_right, not_talking
    with dissolve

    abhay "Did he say he wants you for a boyfriend, Bapat?{w=0.5} {i}Who would?{/i}"

    show bapat angry at talking

    bapat angry "He should offer his services elsewhere, Abhay, we can't work like this!" (show_namepos="right")

    hide bapat
    show donatello nervous dark at not_talking
    show giti stern at center_right, talking
    with dissolve

    stop music fadeout 3.0

    giti "That's enough." (show_namepos="right")

    hide giti
    show bapat angry at center_right, talking
    with dissolve

    bapat "..." (show_namepos="right")

    show bapat angry dark at not_talking

    show donatello determined at talking

    donatello "..." (show_namepos="left")

    stop background fadeout 3.0

    show donatello determined dark at not_talking

    hide bapat with dissolve
    hide donatello with dissolve

    narration "Giti stands up, and takes Donatello’s hands in hers, and for a magic moment, everybody stops, and just watches."

    show giti compassionate at center, talking

    giti compassionate "He is who he is, Bapat Sir, why can’t we just accept it?"

    hide giti

    narration "Bapat sits back into his chair, and the laughter stops."

    show donatello at center, talking

    donatello "Thank you for understanding, Giti"

    hide donatello

    narration "He releases her hands as he leaves the room."
    
    menu:
        thinking "Do I need to do something?{w=0.5} And if yes, what?"
        "Think about it":
            jump .scene8

label .scene8:

    scene bg none with Dissolve(3.0)

    pause 3.0

    narration "Giti’s magic moment didn’t last long."

    narration "During the next days, you hear a lot of homophobic “jokes”, and notice that there has been no meeting of the Sales & Marketing Department where Bapat and Donatello are supposed to work together.{p}
            Every time you’ve walked past his office, or his seat at lunch, Donatello was alone, and staring off into the distance."

    scene bg office with Dissolve(3.0)

    play music "music/Kevin_MacLeod_Impact_Prelude.mp3" fadein 3.0

    menu:
        thinking "The situation festers. Should I do something about it?"
        "Give a collective warning to everyone but Giti":
            jump .scene9
        "Ask for the lawyer's advice.":
            jump .scene11
        "Leave it be, the situation will resolve itself.":
            jump .scene12
        "Talk to the other employees.":
            jump .scene14

label .scene9:

    scene bg none
    with dissolve

    narration "It’s your duty to preserve a safe and welcoming workspace for all your employees."

    narration "You need to keep the team together, and to make sure they can work without harassment because of their orientation, gender, religion, caste, or origin."

    narration "Now that Donatello has come out in the open, it is your responsibility to protect him from the rampant homophobia you’ve seen for a few days."

    narration "Since everyone but Giti has been contributing to his lynching, you decide to give them all a warning."

    menu:
        "Give them a warning.":
            jump .scene10

label .scene10:
    narration "You assumed that giving them a warning would make them reconsider their actions and attitudes, and eventually stop harassing him, but instead the opposite happened."

    narration "You’ve just made it worse for Donatello since everyone now resents him for the warning they’ve got as well."

    narration "In the next few days, the harassment reaches a whole new level as people stop talking to him altogether, and leave the room when he comes in."

    narration "There’s nothing you can do now, except to wait for the new CEO to step in, hoping that they can resolve the situation, and maybe even help Donatello."

    $act_3_ending_10 = True
    jump .end

label .scene11:
    narration "You write to Mr. Rajkumar, You write to Mr. Rajkumar, the company’s Lawyer, and explain the situation to him so that he can give you his advice.{p}
                He answers a few hours later."

    window hide

    show mail_icon_blink

    pause

    hide mail_icon_blink
    show mail_icon_open

    $mail_lawyer_act3_1(("Respected Mr. Chandrakant,\n\n"
        "It will be very difficult to protect your employee since homosexual intercourse is still considered a criminal offence under the Indian Law, section 377 of the Indian Penal Code. Hence and hereby, he cannot be protected against discrimination where the fact discriminated {i}hitherto{/i}"
        "would fall under penal Law, and {i}Nemo auditur propriam turpitudinem allegans{/i} would apply so that his arguing on the basis of his homosexuality would {i}ipso facto{/i} disqualify him from the protections the Law normally applies for discrimination.\n\n"
        "With my very best regards,\n\n"
        "Mr. Rajkumar"))

    hide mail_icon_open

    pause 3.0

    narration "After you’ve googled the sentences in Latin to decode this legal talk, you lay back into your chair."

    narration "{b}Ipso facto{/b} indeed."

    narration "{b}Ipso facto{/b} there's nothing you can do."

    narration "{b}Ipso facto{/b}, Donatello is harassed, and you can do nothing but watch."

    thinking "So much for the work atmosphere."

    menu:
        "A few days later.":
            jump .scene19

label .scene12:
    thinking "I can't spend my whole work day roaming in the office like a traffic cop, handing out warnings to everyone making jokes."

    thinking "Furthermore, doing so will only just turn them all against Donatello."

    thinking "After all, {i}he{/i}'s the one who's decided to come out of the closed, why did he need to do that?"

    thinking "I could have scolded Bapat, and that would have been the end of it!"

    thinking "Wasn't Donatello the first to harass Priyanka a few days ago?"

    thinking "Wasn't he discriminating against Giti himself?"

    thinking "Why is everyone wanting some special status in this company?"

    thinking "Is this because there's no CEO yet?{w=0.5} Well, they sure will sing a different kind of song when the CEO will come!"

    menu:
        "The next days.":
            jump .scene13

label .scene13:
    window hide

    scene bg none with dissolve

    narration "Since you did nothing, the situation escalates quickly. Every day, you receive a new formal complaint from an employee, or another, telling you how Donatello leaned too close to them, or was looking at them suggestively."

    narration "Every day, you hear new cruel jokes made at his expense."

    narration "Eventually, he stops to speak to anyone, and stays on his own."

    thinking "If only he could leave before the new CEO comes in..."

    thinking "Chances are he wont."

    thinking "No matter, I'll explain everything, and all will be well."

    $act_3_ending_13 = True
    jump .end
    

label .scene14:

    thinking "The situation has gone beyond what lawyers and warnings could help with."

    thinking "What am I going to write in the warning?"

    thinking "\"Don't be yourself\"?"

    thinking "\"Stop making bad jokes, it's cruel, and useless?\""

    thinking "It doesn't work like this, I should talk to the other employees instead."

    thinking "But which one first?"

label .employees:
    menu:
        thinking "Who should I talk to ?"
        "Bapat" if not talk_bapat_act3:
            jump .scene15
        "Manali" if not talk_manali_act3:
            jump .scene16
        "Priyanka" if not talk_priyanka_act3:
            jump .scene17
        "Giti" if not talk_giti_act3:
            jump .scene18
        "You talked to enough people." if talk_giti_act3:
            jump .scene19

label .scene15:
    window hide

    scene bg office with fade

    show bapat angry at talking, center
    with dissolve

    bapat angry "Have you heard that, Abhay?"

    show bapat smug
    with dissolve

    bapat "The guy has the nerve to tell everyone!"

    show bapat angry
    with dissolve

    bapat "Now, he must leave, there's nothing else we can do!"

    show bapat dark at not_talking

    abhay "I see. {w=0.5}You would try to hide it if it were you, isn't it, Bapat?"

    show bapat angry at talking

    bapat "No need, I'm not gay!"

    show bapat angry dark at not_talking

    abhay "But since that's how you would react yourself, you thought that his orientation would be a good tool to threaten him with."

    show bapat nervous at talking

    bapat "No, no, Abhay, it's not that at all!"

    show bapat smug
    with dissolve

    bapat "I was just telling him that I could remain silent about it, the best thing for everybody, honest, and that he should be more grateful to me."

    show bapat dark at not_talking

    abhay "Graceful for {i}what?{/i}{w=0.5} For disrespecting him?"

    show bapat angry at talking

    bapat "Abhay, Abhay, stop getting on your high horses again!"

    show bapat smug
    with dissolve

    bapat "I'm {i}protecting this company{/i}, it's against the Law, do you know that?"

    show bapat angry
    with dissolve

    bapat "And what if we become gay too?!"

    show bapat smug dark at not_talking

    narration "You suppress a rising laugh."

    abhay "I must admit that I didn't think about that."

    show bapat smug at talking

    bapat "Ah! Ah!"

    show bapat smug dark at not_talking

    abhay "Oh {i}come on{/i}, Bapat, I was joking.{w=0.5} It's not a disease, you can't catch it!"

    show bapat at talking

    bapat "Who knows, Abhay!"

    bapat "And now he's spreading propaganda too!"

    show bapat dark at not_talking

    abhay "He {i}expressed{/i} himself, Bapat, just you would if you ever had anything interesting to say."

    show bapat at talking

    bapat "..."

    show bapat dark at not_talking

    narration "You sigh and dismiss him."

    hide bapat with dissolve

    thinking "It's worthless. Nothing I can say will change his mind."

    $talk_bapat_act3 = True

    menu:
        "Talk to someone else.":
            jump .employees

label .scene16:
    window hide

    scene bg office with fade

    show manali dark at not_talking, center
    with dissolve

    play music "music/Kai_Engel_Ode_To_The_World.mp3" fadein 3.0 fadeout 3.0

    abhay "Do you have a boyfriend, Manali?"

    show manali nervous dark
    with dissolve

    narration "She blushes."

    abhay "Maybe there was someone you liked in high school, or college, isn't it?"

    show manali at talking

    manali "..."

    show manali dark at not_talking

    abhay "You know in high school when somebody laughs at you because you like someone special, for instance?"

    show manali at talking

    manali "..."

    show manali dark at not_talking

    abhay "Well that's a little bit the same thing you're doing to Donatello right this moment, {w=0.25}only worse."

    show manali at talking

    manali "..."

    show manali dark at not_talking

    manali "Oh."

    abhay "This is not a very mature behaviour, Manali."

    abhay "We are all in this together, trying to make this company successful, as well as a nice place to work."

    abhay "Do you think this is a nice place to work for Donatello now?"

    show manali at talking

    manali "No, Sir."

    show manali dark at not_talking

    abhay "And why not?"

    show manali nervous at talking

    manali nervous "But why did he have to say it, Sir?"

    manali nervous "He could just say he's not married, that's all, there was no need to talk about this...{w=0.5}thing."

    show manali
    with dissolve

    manali "That's {i}his{/i} fault."

    show manali dark at not_talking

    abhay "Being gay?"

    show manali nervous dark
    with dissolve  

    narration "She blushes again."

    show manali nervous at talking

    manali nervous "No, Sir, not that!{w=0.5} Maybe.{w=0.5}I don't know."

    show manali
    with dissolve

    manali "But telling us, that's his fault."

    show manali dark at not_talking

    abhay "So you prefer lies, or else you mock people?"

    show manali at talking

    manali "No, Sir."

    show manali dark at not_talking

    abhay "This needs to stop, Manali, is this clear?"

    show manali at talking

    manali "Yes, Abhay Sir, I will stop."

    show manali dark at not_talking

    abhay "And work with him, in peace and respect."

    show manali at talking

    manali "I will do my best, Sir."

    show manali dark at not_talking

    thinking "She'll do it, I'm confident about it."

    stop music fadeout 3.0

    hide manali with dissolve

    thinking "But things won't ever be the same with Donatello..."

    $talk_manali_act3 = True

    play music "music/Kevin_MacLeod_Impact_Prelude.mp3" fadein 3.0

    menu:
        "Talk to someone else":
            jump .employees

label .scene17:
    window hide

    scene bg office with fade

    show priyanka at talking, center
    with dissolve

    priyanka "I don't care much, Abhay"

    show priyanka dark at not_talking

    abhay "Then why?{w=0.5} Why you hurt someone if you don't care?"

    priyanka ".{w=0.3}.{w=0.3}."

    priyanka ".{w=0.3}.{w=0.3}."

    show priyanka at talking

    priyanka "He's betrayed us, Abhay,{w=0.25} that's why."

    show priyanka dark at not_talking

    abhay "You mean you thought he was an abusive man, and now that you find out that he's not what you thought..."

    abhay "You take this opportunity to bite him back?"

    show priyanka angry at talking

    priyanka angry "No, please, it's not that!"

    priyanka angry "Of course he's been an idiot for a long time, that doesn't change the fact, but we thought he was like us, {w=0.25}normal."

    show priyanka dark at not_talking

    abhay "My goodness, Priyanka, he {b}is{/b} normal, or maybe nobody is."

    show priyanka at talking

    priyanka "This is difficult to accept, Abhay, what will I say to my family?{w=0.5} They will want me to move."

    show priyanka dark at not_talking

    abhay "So they were happy to let you stay when you stay when you were shamed for the way you dress."

    abhay "But they will want you to move is someone being honest with you in the company?"

    show priyanka at talking

    priyanka "Maybe, I don't need to tell them."

    show priyanka dark at not_talking

    abhay "Maybe yes, Priyanka, and you need to accept him as he is, the way he is."

    show priyanka at talking

    priyanka "...I will try my best, Abhay."

    hide priyanka with dissolve

    $talk_priyanka_act3 = True

    menu:
        "Talk to someone else.":
            jump .employees

label .scene18:
    window hide

    stop music fadeout 3.0

    scene bg office with fade

    show giti dark at not_talking, center
    with dissolve

    abhay "I must admit I was surprised by what you've done, Giti"

    show giti at talking

    giti "No need for surprise, Abhay Sir."

    play music "music/Kai_Engel_Street_As_Friends.mp3" fadein 3.0 fadeout 3.0

    show giti dark at not_talking

    abhay "I mean, Donatello isn't exactly a nice person, he-"

    show giti stern at talking

    giti "He's not."

    giti "But if we are never nice to mean people,{w=0.25} that doesn't leave many people to be nice to."

    show giti dark at not_talking

    abhay "*laughs*"

    abhay "True, very true."

    show giti compassionate at talking

    giti compassionate "I am not a learned person, Abhay Sir, but I know we are all the same, and all equal."

    giti compassionate "White,{w=0.25} black,{w=0.25} gay,{w=0.25} not gay,{w=0.25} it is not different, Sir."

    show giti compassionate dark at not_talking

    abhay "..."

    show giti at talking

    giti "..."

    show giti at not_talking

    abhay "What should I do, Giti?"

    show giti at talking

    giti "Last year I had the same problem with the Transportation Department, Abhay Sir."

    show giti dark at not_talking

    abhay "And what did you do?"

    show giti

    giti "I talked to them, {w=0.25}I said{w=0.25} \"We need to respect each other\",{w=0.25} they stopped after that."

    show giti dark not talking

    abhay "If only that worked here."

    show giti stern at talking

    stop music fadeout 3.0

    giti "It can't, Abhay Sir, here it's too serious, and there's no policy to protect Donatello."

    giti "In the office, people won't do anything without a policy, it's not like in the Transportation Department."

    show giti stern dark at not_talking

    abhay "Would he {i}want{/i} that?"

    show giti at talking

    giti "I will check, Abhay Sir."

    hide giti with dissolve

    $talk_giti_act3 = True

    play music "music/Kevin_MacLeod_Impact_Prelude.mp3" fadein 3.0

    menu:
        thinking "I wonder if Donatello would be interested in this policy..."
        "Find out.":
            jump .scene19
        "Talk to someone else.":
            jump .employees

label .scene19:
    window hide

    scene bg office with fade

    stop music fadeout 3.0

    narration "The sound of the printer is relaxing sometimes, you think. You hear the sheets shuffle back and forth, as if the machine were purring. It smells of fresh ink, and of warm paper, lulling you to sleep."

    narration "You fight it to keep up with the day, drinking yet another cup of tea, surveilling the corridor through your open door."

    narration "Seeing Donatello walk straight to your office wakes you up instantly."

    show donatello nervous dark at not_talking, center
    with dissolve
    
    play music "music/Kai_Engel_Anxiety.mp3"

    thinking "Up to something again."

    thinking "I hope it's good..."

    show donatello angry at talking

    donatello angry "It doesn't work, Abhay!"

    show donatello nervous dark at not_talking

    abhay "What doesn't work?"

    show donatello nervous at talking

    donatello "Nothing does, warnings, talking to the people, nothing."

    show donatello angry
    with dissolve

    donatello angry "They simply won’t accept me, and won’t work with me anymore. This is all falling apart!"

    show donatello nervous dark at not_talking

    abhay "And what's your solution, then?"

    show donatello thoughtful at talking

    donatello "You are the HR Manager, Abhay, this is your responsibility!"

    show donatello smug
    with dissolve

    donatello "But fortunately I spoke with Giti, and she gave me an idea."

    show donatello nervous dark at not_talking

    abhay "Tell me."

    show donatello determined at talking

    donatello "We need a policy, an inclusive policy."

    donatello "A policy which recognizes the rights of homosexual employees when they face discrimination."

    donatello "And gives them equal opportunities."

    show donatello smug
    with dissolve

    donatello smug "If this becomes part of our policy, they will change, Abhay."

    show donatello smug dark at not_talking

    abhay "I'm not sure I can, Donald, because-"

    show donatello angry at talking

    donatello "Because {i}what{/i}?!"

    show donatello determined
    with dissolve

    donatello determined "I will request it officially to the company headquarters."

    show donatello determined dark at not_talking

    thinking "Would that be a solution?"

    thinking "How will the others react to that?"

    thinking "Is that even legally possible?"

    menu:
        thinking "Mr. Rajkumar could help me with legal matters."
        "Ask Mr. Rajkumar, the company's lawyer":
            jump .scene20
        "Ask the others.":
            jump .scene21

label .scene20:
    window hide

    scene bg office with fade

    narration "You write to Mr. Rajkumar, the company’s Lawyer, and explain him the situation so that he can give you his advice. He answers a few hours later."

    window hide
    show mail_icon_blink

    pause

    hide mail_icon_blink
    show mail_icon_open

    $mail_lawyer_act3_2(("Dear Mr. Chandrakant,\n\n"
        "Since homosexuality is criminal in India, it is not possible to implement a policy protecting it at the office, {i}cadit quaestio{/i}, and {i}casus belli{/i} henceforthwith.\n\n"
        "With my very best regards,\n\n"
        "Mr. Rajkumar"))

    hide mail_icon_open

    pause 3.0

    menu:
        thinking "So a policy isn't an option. Alright."
        "Reject Donatello's request.":
            jump .scene13
        "Ask the others.":
            jump .scene21


label .scene21:
    window hide

    scene bg office with fade

    menu:
        thinking "Who do I want to talk to?"
        "Bapat." if not talk_bapat_act3_2:
            jump .scene22
        "Manali." if not talk_manali_act3_2:
            jump .scene23
        "Priyanka." if not talk_priyanka_act3_2:
            jump .scene24
        "Giti." if not talk_giti_act3_2:
            jump .scene25

label .choices:

    menu:
        thinking "What's my next move?"
        "Talk to someone else." if not talk_giti_act3_2 or not talk_manali_act3_2 or not talk_priyanka_act3_2 or not talk_bapat_act3_2:
            jump .scene21
        "Ask Mr. Rajkumar." if talk_giti_act3_2:
            jump .scene26
        "Check the international policy." if talk_giti_act3_2:
            jump .scene27

label .scene22:
    window hide 
    scene bg office with fade
    show bapat angry at talking, center
    with dissolve

    bapat "A policy?"

    bapat "A {i}policy{/i}?!{w=0.5} And why not a bonus!"

    show bapat dark at not_talking

    abhay "It's just to protect him, Bapat"

    show bapat smug at talking

    bapat smug "Oh yes?{w=0.5} Special rights now. A schedule, why not!"

    show bapat smug dark at not_talking

    abhay "You work here, Bapat, right?"

    show bapat at talking

    bapat "I do, Abhay brother."

    show bapat smug dark at not_talking

    abhay "So if a policy is implemented, and approved at the highest level, you will have no choice, will you?"

    show bapat at talking

    bapat "No I won’t, but it won’t happen."

    show bapat smug
    with dissolve

    bapat "You just wait until the new CEO comes!"

    show bapat smug dark at not_talking

    abhay "So you'll stay?"

    show bapat smug at talking

    bapat "Yes of course, why would I leave?{w=0.5} He wants my job now, this Donaldino?"

    show bapat smug dark at not_talking

    abhay "See, the way you talk convinces me even more to draft it."

    show bapat angry at talking

    bapat angry "Do whatever you want, Abhay, it won’t pass."

    show bapat smug dark at not_talking

    hide bapat with dissolve

    $talk_bapat_act3_2 = True

    jump .choices

label .scene23:
    window hide
    scene bg office with fade
    show manali at talking, center
    with dissolve

    play music "music/Kai_Engel_Ode_To_The_World.mp3" fadein 3.0 fadeout 3.0

    if talk_manali_act3:
        manali "I thought about what you've said to me the other day, Abhay Sir."
    else:
        manali "I thought a lot about all the situation with Donatello, Abhay Sir."

    show manali dark at not_talking

    abhay "Oh yes?"

    show manali at talking

    manali "Yes, and I think I want to change now, I have not been very nice."

    show manali dark at not_talking

    abhay "Yes, Manali, and thank you for this."

    abhay "You would be OK with a policy protecting our employees from this kind of discrimination, then?"

    show manali smiling at talking

    manali "Yes, I would, Sir, since I'm doing it already."

    show manali smiling dark at not_talking

    hide manali
    with dissolve

    play music "music/Kai_Engel_Anxiety.mp3" fadein 3.0 fadeout 3.0

    $talk_manali_act3_2 = True

    jump .choices

label .scene24:
    window hide
    scene bg office with dissolve
    show priyanka dark at not_talking, center
    with dissolve

    abhay "So here’s what I’m thinking, Priyanka."

    abhay "I could add an inclusivity clause to our policy to see that everyone is putting their best efforts into accepting each other, as they are."

    show priyanka at talking

    priyanka "But we already do, Abhay, as long as they’re not too-"

    show priyanka dark at not_talking

    abhay "No you don’t, Priyanka, think about Donatello."

    show priyanka angry at talking

    priyanka "But he’s mean anyway, why protect him?"

    show priyanka annoyed dark at not_talking

    abhay "Because it’s not about him."

    show priyanka annoyed at talking

    priyanka "..."

    show priyanka annoyed dark at not_talking

    abhay "It’s about everybody, people we don’t know yet, who will come in the future, and that the likes of Bapat will harass, and it’s about the image of our company."

    show priyanka annoyed at talking

    priyanka "But precisely, Abhay, the company’s image will suffer."

    show priyanka annoyed dark at not_talking

    abhay "From {i}whom{/i}?"

    show priyanka
    with dissolve

    abhay "We sell to the younger generations, don’t you think this can convey a positive message, I don’t know, like we’re Apple or something?"

    show priyanka annoyed at talking

    priyanka "Apple works with China, Abhay, and I am representative of the young generation."

    show priyanka annoyed dark at not_talking

    abhay "All harassment is connected, Priyanka, you don’t get it."

    abhay "Gay-shaming,{w=0.25} slut-shaming,{w=0.25} it’s the same!"

    abhay "You, of all people, are a victim of this frame of mind already, don’t you see it?"

    show priyanka dark
    with dissolve

    priyanka ".{w=0.25}.{w=0.25}."

    show priyanka at talking

    priyanka "I will think about it, Abhay."

    show priyanka at not_talking

    hide priyanka with dissolve

    $talk_priyanka_act3_2 = True

    jump .choices

label .scene25:
    window hide
    scene bg office with fade

    show giti stern at center, talking
    with dissolve

    play music "music/Kai_Engel_Street_As_Friends.mp3" fadein 3.0 fadeout 3.0

    giti "I have done my research, Abhay."

    show giti stern dark at not_talking

    abhay "What research, tell me?"

    show giti stern at talking

    giti "The Penal Code says that homosexual sexual intercourse is illegal, not that being homosexual is criminal."

    show giti stern dark at not_talking

    abhay "But-"

    show giti stern at talking

    giti "Wait, Abhay, wait."

    giti "Also I have seen that nowhere since 2013 this has been applied."

    giti "A policy is possible."

    show giti
    with dissolve

    giti "In fact, our own company CRYPTALOO, already has this policy in the USA, and for Europe too."

    show giti smiling
    with dissolve

    giti smiling "Such a policy isn’t illegal, after all. You can make one, Abhay."

    show giti smiling dark at not_talking

    abhay "And if I decide to make  it, maybe I can just copy the international policy, and-"

    show giti smiling at talking

    giti smiling "Yes, Abhay, that’s a good idea."

    show giti smiling dark at not_talking

    stop music fadeout 3.0

    thinking "Still, this is Giti talking, and she could be wrong in her interpretation of the law."

    thinking "Should I check CRYPTALOO's international policy, or ask Mr. Rajkumar for his advice?"

    hide giti with dissolve

    $talk_giti_act3_2 = True

    jump .choices

label .scene26:

    narration "You write to Mr. Rajkumar, the company’s Lawyer, and tell him what Giti’s just told you, asking for his advice."

    window hide
    show mail_icon_blink

    pause

    hide mail_icon_blink
    show mail_icon_open

    $mail_lawyer_act3_3(("Dear Mr. Chandrakant,\n\n"
        "Technically, your colleague is right, the Indian Penal Code only forbids the sexual intercourse {i}de jure{/i}, not the fact of declaring oneself homosexual, which would be {i}doli incapax{/i}, but we all know that there cannot be one without the other.\n"
        "Further, it is not because a Law hasn’t been applied that it is invalid, a vote must first happen to change, or cancel the Law accordingly so that you would always take a risk for the future of the company by drafting, and implementing this policy, which I don’t recommend.\n\n"
        "With my very best regards,\n\n"
        "Mr. Rajkumar"))

    hide mail_icon_open

    pause 3.0

    menu:
        thinking "What should I do?"
        "Check the international policy nevertheless":
            jump .scene27
        "Follow the lawyer's advice.":
            jump .scene13

label .scene27:
    window hide
    scene bg office with fade

    narration "You can’t believe what you find  when you finally receive the international inclusivity policy from CRYPTALOO’s headquarters.{p}
                Not only is discrimination on the basis of sexual orientation forbidden, but it is severely punished as well, a rightful cause of the work contract’s termination, as is the protection of the person’s privacy."

    narration "There’s a lot more in this document, but you prefer to take one step at a time. You copy the international policy into the branch’s policy, and send it off to the whole comapny by email. Later, you forward this email to the new CEO."

    menu:
        "The aftermath.":
            jump .scene28

label .scene28:
    window hide
    scene bg none with fade

    narration "Now that a policy has been passed, effective immediately, nobody dares harass Donatello anymore.{p}
                Some employees have sent emails to complain about you, and threatened to leave.{p}
                They’ve even found the new CEO’s email, and forwarded their complaints there. Let’s hope this move will be appreciated. Else you’re in big, big trouble."

    $act_3_ending_28 = True
    jump .end

label .end:
    $act_3_completed = True
    show bg end_act_3 with Dissolve(3.0)

    pause

    show bg none with Dissolve(3.0)
    window hide
    $renpy.call_screen("act_menu")

    return