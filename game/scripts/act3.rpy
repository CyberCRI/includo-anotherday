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

    scene bg lunch_room with dissolve

    narration "Everybody’s at lunch, gathered together in the small canteen."

    narration "You unpack your lunchbox, and share around the delicious parathas you find inside before starting to eat.{p}
            The last events have taken their toll, and the atmosphere is rather uneasy."

    thinking "People don't like change."

    narration "Priyanka and Manali’s jokes are most welcome today, lifting up the mood a bit."

    priyanka "...And then, he turned around and said, “Are you sure these are your trousers?”"

    narration "Manali bursts into laughter, almost tipping her glass over."

    manali "So he's not the one, I gues, Priyanka?"

    priyanka "Definitely not the one."

    manali "Well, he sounds funny at least. Is your husband funny, Giti?"

    narration "They both laugh."

    giti "Shoo, you girls, what a racket you're making today!"

    priyanka "Come one, Giti, everybody’s married except us, we are entitled to our fun!"

    bapat "Not everyone!"

    priyanka "!"

    giti "!"

    manali "!"

    bapat "Donatello is a bachelor as well!"

    donatello "...!"

    manali "Is it true, Donald?"

    donatello "..."

    narration "Donatello wipes his mouth with a napkin, and stares into the void a little too long before answering."

    donatello "I am a bachelor, yes."

    priyanka "How come?!"

    priyanka "You have a good job and all, why aren't you married?"

    bapat "Yes, {i}why{/i}?"

    #bapat sly

    donatello "..."

    #donatello red

    manali "Maybe he hasn't found the one true love?"

    #manali joking

    bapat "Or maybe he can't tell..."

    #bapat sly

    priyanka "We were joking, Bapat, don't be your usual downer!"

    #priyanka annoyed

    bapat "I am joking too! {i}Hahaha!{/i}"

    #bapat forced laugher

    donatello "..."

    narration "Donatello leaves the table, heading to the sink with his plate, shortly followed by Bapat."

    thinking "Here comes trouble..."

    menu:
        "You follow them as well.":
            jump .scene2

label .scene2:
    narration "You see Bapat and Donatello whispering furiously to each other near the sink. From the sound of it, their conversation doesn't seem especially friendly."

    thinking "Maybe I should let them be..."

    menu:
        "Get closer to hear what they say.":
            jump .scene3
        "Slip away, and let them be.":
            jump .scene4

label .scene3:
    show bapat with dissolve

    bapat "I was going to pay, yes."

    bapat "But no longer."

    #bapat menacing

    show donatello with dissolve

    donatello "What are you talking about?"

    donatello "Of course you will give me the money back, Bapat, or I will-"

    show bapat with dissolve

    bapat "You will nothing."

    narration "Bapat takes his cell phone out of his pocket."

    show donatello with dissolve

    donatello "And why is that?"

    show bapat with dissolve

    bapat "You just look at this."

    narration "Bapat shows his phone to Donatello."

    show donatello with dissolve

    donatello "...{b}!{/b}"

    #donatello surprised

    donatello "Where did you get this?!"

    #donatello scared

    show bapat with dissolve

    #bapat evil

    bapat "Ah, ah, interested now?"

    bapat "I've taken a picture of your computer, you've left your email open, Donald."

    bapat "or should I say... {i}Daisy{/}?"

    show donatello with dissolve

    donatello "Are you threatening me for real?"

    #donatello angry

    show bapat with dissolve

    bapat "Oh I am{w=0.5}, yes I am, either you support my decisions, or I tell everyone."

    bapat "How would you like it, the whole office knowing?"

    #bapat evil

    bapat "I can almost hear them already."

    "{i}Ahem.{/i}"

    bapat "!"

    show donatello with dissolve

    donatello "!"

    "Knowing {i}what{/i}?"

    show bapat with dissolve

    bapat "Nothing, Abhay, it's nothing."

    bapat "Professional stuff, corporate stuff, high-level."

    "Indeed."

    "Is there anything you'd like to report to me, Donatello?"

    show donatello with dissolve

    donatello "No, Abhay, no, it's nothing."

    "We'll see about that."

    hide donatello with dissolve

    narration "You leave the room."

    thinking "This is definitely suspicious to say the least."

    menu:
        "Give a warning to Bapat straight away.":
            jump .scene5
        "Let them cope by themselves.":
            jump .scene6

label .scene4:
    narration "You’re not supposed to be spying on the employees, so you walk away, and let them sort out whatever it is they need to sort out among themselves.{p}
                The rest of the day is uneventful though you can’t dismiss the feeling that you’ve missed something important no matter how hard you try to shrug it off."

    scene bg office with dissolve

    narration "The next day, just before lunch break, Donatello asks to see you."

    narration "Since you remember the last team lunch vividly enough, you let him come into your office, and talk."

    show donatello with dissolve

    donatello "I need to tell it to everyone, Abhay."

    donatello "I don't see why I should hide, and let people like Bapat try to take advantage of me."

    "Wait, say what? What did Bapat do?"

    donatello "Doesn't matter, Abhay."

    donatello "What matters is that I need to say it, I really need."

    donatello "And be able to live my life as myself, not the image I give all the time."

    "What on Earth are you talking about?"

label .gay:

    donatello "I am gay, Abhay, that's why I'm not married."

    "W-What?"

    "But it was only yesterday that you groped Priyanka! Are you insane?"

    donatello "That was a mask, Abhay. I was overdoing it on purpose."

    thinking "Just wow."

    "Did you even think about how she felt?"

    "You should have tried to tell her, maybe she would have helped!"

    donatello "You don't know Priyanka so well, Abhay, no offense but-"

    "Right. But why the hurry?"

    "Why do you need to shout it to the whole office, Donald?"

    "You're not married with these people, you don't owe them any kind of explanation."

    donatello "It's not that."

    donatello "I feel like I'm lying to them- all the time, and to myself!"

    donatello "Plus they already know, Abhay, it's too late for hiding."

    donatello "Bapat tried to use it against me, they all will, and it will be worse, better say it now!"

    #donatello nervous

    thinking "He's awfully nervous, even out of his mind."

    thinking "Is this because what he's doing right now takes a lot of courage..."

    thinking "Or is he going mad somewhat, and just making this all up?"

    "You should think before going ahead like that, Donald."

    "There will be consequences, and you won't be able to take it back, and-"

    donatello "You, of all people, I thought you would understand, Abhay!"

    #donatello angry

    hide donatello with dissolve

    narration "Donatello strides away in a whirlwind."

    thinking "Wait, no!"

    menu:
        "Follow him":
            jump .scene7


label .scene5:
    scene bg office with dissolve

    show bapat at left with dissolve

    show donatello at right with dissolve


    narration "You call Bapat and Donatello together into your office just before the lunch break on the next morning.
                Neither of them sit down. {w=0.5}Instead they both stand in front of you like naughty college students waiting for their scolding."

    "I heard you threatening Donatello yesterday, Bapat"

    bapat "Oh, Abhay, it's not like that-"

    #bapat surprised

    "I've heard it! {w=0.5}Kindly don't insult my intelligence."

    narration "You give him {b}the look{/b}, forehead lowered, eyes looking up straight at him like a bull."

    "I don’t want to know what you’ve threatened him with, Bapat, I just-"

    hide bapat with dissolve

    show donatello with dissolve

    donatello "But you will."

    bapat "...!"

    "I beg your pardon?"

    donatello "You will know because I've had enough."

    donatello " I need to tell it to everyone, Abhay, I don’t see why I should hide, and let people like Bapat try to take advantage of me."

    "Wait, say what?"

    jump .gay

label .scene6:

    thinking "Something's not right, I can feel it in my bones."

    thinking "After all those years as a HR Manager, I've developed some kind of special sense when it comes to trouble, and trouble there is."

    thinking "Yet, I can't really accuse Bapat without more proof than something I've overheard at the canteen."

    thinking "Plus, I'm not supposed to listen in on private conversations."

    thinking "It's better to let it slip."

    scene bg office with dissolve

    pause 1.0

    narration "The next day, just before lunch break, Donatello asks to see you."

    narration "Since you remember the last team lunch vividly enough, you let him come into your office, and talk."

    show donatello with dissolve

    donatello "I need to tell it to everyone, Abhay."

    donatello "I don't see why I should hide, and let people like Bapat try to take advantage of me."

    "Wait, say what? What did Bapat do?"

    donatello "Doesn't matter, Abhay."

    donatello "What matters is that I need to say it, I really need."

    donatello "And be able to live my life as myself, not the image I give all the time."

    "What on Earth are you talking about?"

    jump .gay

label .scene7:

    narration "You lean back into your chair, surprised by the turn the events have taken."

    narration "A few minutes later, you start wondering where Donatello might have gone after storming out of your office, and you head to the canteen."

    scene bg lunch_room with dissolve

    narration "When you reach it, you hear Donatello’s shaky voice echoing in a dead silence before you open the door."

    donatello "... So no, I'm not married, and never will be, {w=0.5}or not to a woman."

    thinking "So he did it."

    thinking "There's no way to predict how people will react to this."

    thinking "And I can't help feeling afraid of the consequences..."

    thinking "He must be feeling the same way."

    bapat "You should move to the US if you want to marry a man, there will none of it here!"

    donatello "..."

    narration "You hear a couple of people clapping, cheering, and whistling."

    bapat "How can I work with you now that I know?"

    bapat "I'm not going to be your girlfriend, you need to move to another office!"

    #bapat sly

    thinking "Just look at him, excited by his own success."

    thinking "Everyone has fifteen minutes of glory in life, or so I've heard, maybe this is Bapat's moment of fame."

    bapat "Are we supposed to accept this indecency ?!"

    giti "..."

    #bapat angry

    thinking "Ok, time to step in."

    narration "You push the door, and see Bapat standing, his face contorted with anger.
            Priyanka, and Manali are laughing nervously. Only Giti remains silent, still listening to Donatello, who seems to be holding his own."

    "Did he say he wants you for a boyfriend, Bapat? {i}Who would?{/i}"

    show bapat with dissolve

    bapat "He should offer his services elsewhere, Abhay, we can't sork like this!"

    show giti with dissolve

    giti "That's enough."

    #giti determined

    bapat "...!"

    donatello "...!"

    hide giti with dissolve

    narration "Giti stands up, and takes Donatello’s hands in hers, and for a magic moment, everybody stops, and just watches."

    show giti with dissolve

    giti "He is who he is, Bapat Sir, why can’t we just accept it?"

    narration "Bapat sits back into his chair, and the laughter stops."

    donatello "Thank you for understanding, Giti"

    narration "He releases her hands as he leaves the room."

    thinking "Do I need to do something? And if yes, what?"

    menu:
        "Think about it":
            jump .scene8

label .scene8:

    scene bg office with dissolve

    narration "Giti’s magic moment didn’t last long."

    narration "During the next days, you hear a lot of homophobic “jokes”, and notice that there has been no meeting of the Sales & Marketing Department where Bapat and Donatello are supposed to work together.{p}
            Every time you’ve walked past his office, or his seat at lunch, Donatello was alone, and staring off into the distance."

    thinking "The situation festers."

    menu:
        "Give a collective warning to everyone but Giti":
            jump .scene9
        "Ask for the lawyer's advice.":
            jump .scene11
        "Leave it be, the situation will resolve itself.":
            jump .scene12
        "Talk to the other employees.":
            jump .scene14

label .scene9:
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
    $act_3_completed = True
    return

label .scene11:
    narration "You write to M. Rajkumar, You write to M. Rajkumar, the company’s Lawyer, and explain the situation to him so that he can give you his advice.{p}
                He answers a few hours later."

    mail "rajkumarrajkumarltd@gmail.com 
            To: abhay.chandrakant@cryptaloo.in
            Re: Homosexuality and Discrimination
            Respected M. Chandrakant,
            It will be very difficult to protect your employee since homosexual intercourse is still considered a criminal offence under the Indian Law, section 377 of the Indian Penal Code. Hence and hereby, he cannot be protected against discrimination where the fact discriminated hitherto would fall under penal Law, and Nemo auditur propriam turpitudinem allegans would apply so that his arguing on the basis of his homosexuality would ipso facto disqualify him from the protections the Law normally applies for discrimination.
            With my very best regards,
            M. Rajkumar"

    narration "After you’ve googled the sentences in Latin to decode this legal talk, you lay back into your chair."

    thinking "{b}Ipso facto{/b} indeed."

    thinking "{b}Ipso facto{/b} there's nothing I can do."

    thinking "{b}Ipso facto{/b}, Donatello is harassed, and you I do nothing but watch."

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

    thinking "Is this because there's no CEO yet? Well, they sure will sing a different kind of song when the CEO will come!"

    menu:
        "The next weeks.":
            jump .scene13

label .scene13:
    scene none with dissolve

    narration "Since you did nothing, the situation escalates quickly. Every day, you receive a new formal complaint from an employee, or another, telling you how Donatello leaned too close to them, or was looking at them suggestively."

    narration "Every day, you hear new cruel jokes made at his expense."

    narration "Eventually, he stops to speak to anyone, and stays on his own."

    thinking "If only he could leave before the new CEO comes in..."

    thinking "Chances are he wont."

    thinking "No matter, I'll explain everything, and all will be well."

    $act_3_ending_13 = True
    $act_3_completed = True
    return

label .scene14:

    thinking "The situation has gone beyond what lawyers and warnings could help with."

    thinking "What am I going to write in the warning ?"

    thinking "\"Don't be yourself\"?"

    thinking "\"Stop making bad jokes, it's cruel, and useless?\""

    thinking "It doesn't work like this, I should talk to the other employees instead."

    thinking "But which one first?"

label .employees:
    menu:
        "Bapat" if talk_bapat_act3 == False:
            jump .scene15
        "Manali" if talk_manali_act3 == False:
            jump .scene16
        "Priyanka" if talk_priyanka_act3 == False:
            jump .scene17
        "Giti" if talk_giti_act3 == False:
            jump .scene18
        "You talked to enough people." if talk_giti_act3 == True:
            jump .scene19

label .scene15:
    scene bg office with dissolve

    show bapat with dissolve

    bapat "Have you heard that, Abhay?"

    bapat "The guy has the nerve to tell everyone!"

    bapat "Now, he must leave, there's nothing else we can do!"

    "I see. {w=0.5}You would try to hide it if it were you, isn't it, Bapat?"

    bapat "No need, I'm not gay!"

    #bapat angry

    "But since that's how you would react yourself, you thought that his orientation would be a good tool to threaten him with."

    bapat "No, no, Abhay, it's not that at all!"

    bapat "I was just telling him that I could remain silent about it, the best thing for everybody, honest, and that he should be more grateful to me."

    "Graceful for {i}what{/i}? For disrespecting him?"

    bapat "Abhay, Abhay, stop getting on your high horses again!"

    bapat "I'm {i}protecting this company{/i}, it's against the Law, do you know that?"

    bapat "And what if we become gay too?!"

    narration "You suppress a rising laugh."

    "I must admit that I didn't think about that."

    bapat "Ah! Ah!"

    "Oh {i}come on{/i}, Bapat, I was joking.{w=0.5} It's not a disease, you can't catch it!"

    bapat "Who knows, Abhay!"

    bapat "And now he's spreading propaganda too!"

    "He {i}expressed{/i} himself, Bapat, just you would if you ever had anything interesting to say."

    bapat "...!"

    narration "You sigh and dismiss him."

    hide bapat with dissolve

    thinking "It's worthless. Nothing I can say will change his mind."

    $talk_bapat_act3 = True

    menu:
        "Talk to someone else.":
            jump .employees

label .scene16:
    scene bg office with dissolve

    show manali with dissolve

    "Do you have a boyfriend, Manali?"

    #manali blushing

    narration "She blushes."

    "Maybe there was someone you liked in high school, or college, isn't it?"

    manali "...!"

    #manali shocked

    "You know in high school when somebody laughs at you because you like someone special, for instance?"

    manali "..."

    narration "She nods."

    "Well that's a little bit the same thing you're doing to Donatello right this moment, {w=0.25}only worse."

    manali "!"

    manali "Oh."

    "This is not a very mature behaviour, Manali."

    "We are all in this together, trying to make this company successful, as well as a nice place to work."

    "Do you think this is a nice place to work for Donatello now?"

    manali "No, Sir."

    "And why not?"

    #manali embarassed

    manali "But why did he have to say it, Sir?"

    manali "He could just say he's not married, that's all, there was no need to talk about this...{w=0.5}thing."

    manali "That's {i}his{/i} fault."

    "Being gay?"

    #manali blushes

    narration "She blushes again."

    manali "No, Sir, not that! {w=0.5}Maybe. {w=0.5}I don't know."

    manali "But telling us, that's his fault."

    "So you prefer lies, or else you mock people?"

    manali "No, Sir."

    "This needs to stop, Manali, is this clear?"

    manali "Yes, Abhay Sir, I will stop."

    "And work with him, in peace and respect."

    manali "I will do my best, Sir."

    thinking "She'll do it, I'm confident about it."

    hide manali with dissolve

    thinking "But things won't ever be the same with Donatello..."

    $talk_manali_act3 = True

    menu:
        "Talk to someone else":
            jump .employees

label .scene17:
    scene bg office with dissolve

    show priyanka with dissolve

    priyanka "I don't care much, Abhay"

    #priyanka uninterrested

    "Then why? {w=0.25}Why you hurt someone if you don't care?"

    priyanka "..."

    priyanka "..."

    #priyanka thinking

    priyanka "He's betrayed us, Abhay{w=0.25}, that's why."

    "You mean you thought he was an abusive man, and now that you find out that he's not what you thought..."

    "You take this opportunity to bite him back?"

    priyanka "No, please, it's not that."

    priyanka "Of course he's been an idiot for a long time, that doesn't change the fact, but we thought he was like us, {w=0.25}normal."

    "My goodness, Priyanka, he {b}is{/b} normal, or maybe nobody is."

    priyanka "This is difficult to accept, Abhay, what will I say to my family? {w=0.25}They will want me to move."

    "So they were happy to let you stay when you stay when you were shamed for the way you dress."

    "But they will want you to move is someone being honest with you in the company?"

    priyanka "Maybe, I don't need to tell them."

    "Maybe yes, Priyanka, and you need to accept him as he is, the way he is."

    priyanka "...I will try my best, Abhay."

    hide priyanka with dissolve

    $talk_priyanka_act3 = True

    menu:
        "Talk to someone else.":
            jump .employees

label .scene18:
    scene bg office with dissolve

    show giti with dissolve

    "I must admit I was surprised by what you've done, Giti"

    giti "No need for surprise, Abhay Sir."

    "I mean, Donatello isn't exactly a nice person, he-"

    giti "He's not."

    giti "But if we are never nice to mean people, that doesn't leave many people to be nice to."

    "Ah! Ah!"

    "True, very true."

    giti "I am not a learned person, Abhay Sir, but I know we are all the same, and all equal."

    giti "White{w=0.25}, black{w=0.25}, gay{w=0.25}, not gay{w=0.25}, it is not different, Sir."

    "..."

    giti "..."

    "What should I do, Giti?"

    giti "Last year I had the same problem with the Transportation Department, Abhay Sir."

    "And what did you do?"

    giti "I talked to them, {w=0.25}I said{w=0.25} \"We need to respect each other\"{w=0.25}, they stopped after that."

    "If only that worked here."

    giti "It can't, Abhay Sir, here it's too serious, and there's no policy to protect Donatello."

    giti "In the office, people won't do anything without a policy, it's not like in the Transportation Department."

    "Would he {i}want{/i} that?"

    giti "I will check, Abhay Sir."

    $talk_giti_act3 = True

    menu:
        "Find out.":
            jump .scene19
        "Talk to someone else.":
            jump .employees

label .scene19:
    scene bg office with dissolve

    narration "The sound of the printer is relaxing sometimes, you think. You hear the sheets shuffle back and forth, as if the machine were purring. It smells of fresh ink, and of warm paper, lulling you to sleep."

    narration "You fight it to keep up with the day, drinking yet another cup of tea, surveilling the corridor through your open door."

    narration "Seeing Donatello walk straight to your office wakes you up instantly."

    show donatello with dissolve

    thinking "Up to something again."

    thinking "I hope it's good..."

    donatello "It doesn't work, Abhay!"

    "What doesn't work?"

    donatello "Nothing does, warnings, talking to the people, nothing."

    donatello "They simply won’t accept me, and won’t work with me anymore. This is all falling apart!"

    "And what's your solutionm then?"

    donatello "You are the HR Manager, Abhay, this is your responsibility."

    donatello "But fortunately I spoke with Giti, and she gave me  an idea."

    "Tell me."

    donatello "We need a policy, an inclusive policy, which recognizes the rights of homosexual employees when they face discrimination, and gives them equal opportunities."

    donatello "If this becomes part of our policy, they will change, Abhay."

    "I'm not sure I can, Donald, because-"

    donatello "Because {i}what{/i}?!"

    donatello "I will request it officially to the company headquarters."

    thinking "Would that be a solution ?"

    thinking "How will the others react to that?"

    thinking "Is that even legally possible?"

    menu:
        "Ask M. Rajkumar, the company's lawyer":
            jump .scene20
        "Ask the others.":
            jump .scene21

label .scene20:
    scene bg office with dissolve

    narration "You write to M. Rajkumar, the company’s Lawyer, and explain him the situation so that he can give you his advice. He answers a few hours later."

    mail "rajkumarrajkumarltd@gmail.com 
        To: abhay.chandrakant@cryptaloo.in
        Re: Inclusive Policy
        Dear M. Chandrakant,
        Since homosexuality is criminal in India, it is not possible to implement a policy protecting it at the office, cadit quaestio, and casus belli henceforthwith.
        With my very best regards,
        M. Rajkumar"

    thinking "A tricky situation."

    menu:
        "Reject Donatello's request.":
            jump .scene13
        "Ask the others.":
            jump .scene21


label .scene21:
    scene bg office with dissolve

    thinking "Who do I want to talk to?"

    menu:
        "Bapat." if talk_bapat_act3_2 == False:
            jump .scene22
        "Manali." if talk_manali_act3_2 == False:
            jump .scene23
        "Priyanka." if talk_priyanka_act3_2 == False:
            jump .scene24
        "Giti." if talk_giti_act3_2 == False:
            jump .scene25

label .scene22:
    scene bg office with dissolve
    show bapat with dissolve

    bapat "A policy?"

    bapat "A {i}policy{/i}?! And why not a bonus!"

    "It's just to protect him, Bapat"

    bapat "Oh yes? {w=0.25}Special rights now. A schedule, why not!"

    "You work here, Bapat, right?"

    bapat "I do, Abhay brother."

    "So if a policy is implemented, and approved at the highest level, you will have no choice, will you?"

    bapat "No I won’t, but it won’t happen, you just wait until the new CEO comes!"

    "So you'll stay?"

    bapat "Yes of course, why would I leave? He wants my job now, this Donaldino?"

    "See, the way you talk convinces me even more to draft it."

    bapat "Do whatever you want, Abhay, it won’t pass."

    $talk_bapat_act3_2 = True

    menu:
        "Talk to someone else." if talk_giti_act3_2 == False or talk_manali_act3_2 == False or talk_priyanka_act3_2 == False or talk_bapat_act3_2 == False:
            jump .scene21
        "Ask M. Rajkumar." if talk_giti_act3_2 == True:
            jump .scene26
        "Check the international policy." if talk_giti_act3_2 == True:
            jump .scene27

label .scene23:
    scene bg office with dissolve
    show manali with dissolve

    if talk_manali_act3:
        manali "I thought about what you've said to me the other day, Abhay Sir."
    else:
        manali "I thought a lot about all the situation with Donatello, Abhay Sir."

    "Oh yes?"

    manali "Yes, and I think I want to change now, I have not been very nice."

    "Yes, Manali, and thank you for this."

    "You would be OK with a policy protecting our employees from this kind of discrimination, then?"

    manali "Yes, I would, Sir, since I'm doing it already."

    $talk_manali_act3_2 = True

    menu:
        "Talk to someone else." if talk_giti_act3_2 == False or talk_manali_act3_2 == False or talk_priyanka_act3_2 == False or talk_bapat_act3_2 == False:
            jump .scene21
        "Ask M. Rajkumar." if talk_giti_act3_2 == True:
            jump .scene26
        "Check the international policy." if talk_giti_act3_2 == True:
            jump .scene27

label .scene24:
    scene bg office with dissolve
    show priyanka with dissolve

    "So here’s what I’m thinking, Priyanka."

    "I could add an inclusivity clause to our policy to see that everyone is putting their best efforts into accepting each other, as they are."

    priyanka "But we already do, Abhay, as long as they’re not too-"

    "No you don’t, Priyanka, think about Donatello."

    priyanka "But he’s mean anyway, why protect him?"

    "Because it’s not about him."

    priyanka "!"

    "It’s about everybody, people we don’t know yet, who will come in the future, and that the likes of Bapat will harass, and it’s about the image of our company."

    priyanka "But precisely, Abhay, the company’s image will suffer."

    "From {i}whom{/i}?"

    "We sell to the younger generations, don’t you think this can convey a positive message, I don’t know, like we’re Apple or something?"

    priyanka "Apple works with China, Abhay, and I am representative of the young generation."

    "All harassment is connected, Priyanka, you don’t get it."

    "Gay-shaming{w=0.25}, slut-shaming,{w=0.25} it’s the same!"

    "You, of all people, are a victim of this frame of mind already, don’t you see it?"

    priyanka "I will think about it, Abhay."

    $talk_priyanka_act3_2 = True

    menu:
        "Talk to someone else." if talk_giti_act3_2 == False or talk_manali_act3_2 == False or talk_priyanka_act3_2 == False or talk_bapat_act3_2 == False:
            jump .scene21
        "Ask M. Rajkumar." if talk_giti_act3_2 == True:
            jump .scene26
        "Check the international policy." if talk_giti_act3_2 == True:
            jump .scene27

label .scene25:
    scene bg office with dissolve

    show giti with dissolve

    giti "I have done my research, Abhay."

    "What research, tell me?"

    giti "The Penal Code says that homosexual sexual intercourse is illegal, not that being homosexual is criminal."

    "But-"

    giti "Wait, Abhay, wait. {w=0.25}Also I have seen that nowhere since 2013 this has been applied. {w=0.25}A policy is possible."

    giti "In fact, own own company CRYPTALOO, already has this policy  in the USA, and for Europe too. Such a policy isn’t illegal, after all. You can make one, Abhay."

    "And if I decide to make  it, maybe I can just copy the international policy, and-"

    giti "Yes, Abhay, that’s a good idea."

    thinking "Still, this is Giti talking, and she could be wrong in her interpretation of the law."

    thinking "Should I check CRYPTALOO's international policy, or ask M. Rajkumar for his advice?"

    $talk_giti_act3_2 = True

    menu:
        "Ask M. Rajkumar." if talk_giti_act3_2 == True:
            jump .scene26
        "Check the international policy." if talk_giti_act3_2 == True:
            jump .scene27
        "Talk to someone else." if talk_giti_act3_2 == False or talk_manali_act3_2 == False or talk_priyanka_act3_2 == False or talk_bapat_act3_2 == False:
            jump .scene21

label .scene26:

    narration "You write to M. Rajkumar, the company’s Lawyer, and tell him what Giti’s just told you, asking for his advice."

    mail "rajkumarrajkumarltd@gmail.com 
        To: abhay.chandrakant@cryptaloo.in
        Re: Re: Inclusive Policy
        Dear M. Chandrakant,
        Technically, your colleague is right, the Indian Penal Code only forbids the sexual intercourse de jure, not the fact of declaring oneself homosexual, which would be doli incapax, but we all know that there cannot be one without the other. Further, it is not because a Law hasn’t been applied that it is invalid, a vote must first happen to change, or cancel the Law accordingly so that you would always take a risk for the future of the company by drafting, and implementing this policy, which I don’t recommend.
        With my very best regards,
        M. Rajkumar"

    thinking "What should I do?"

    menu:
        "Check the international policy nevertheless":
            jump .scene27
        "Follow the lawyer's advice.":
            jump .scene13

label .scene27:
    scene bg office with dissolve

    narration "You can’t believe what you find  when you finally receive the international inclusivity policy from CRYPTALOO’s headquarters.{p}
                Not only is discrimination on the basis of sexual orientation forbidden, but it is severely punished as well, a rightful cause of the work contract’s termination, as is the protection of the person’s privacy."

    narration "There’s a lot more in this document, but you prefer to take one step at a time. You copy the international policy into the branch’s policy, and send it off to the whole comapny by email. Later, you forward this email to the new CEO."

    narration ""

    menu:
        "The aftermath.":
            jump .scene28

label .scene28:
    scene bg none with dissolve

    narration "Now that a policy has been passed, effective immediately, nobody dares harass Donatello anymore.{p}
                Some employees have sent emails to complain about you, and threatened to leave.{p}
                They’ve even found the new CEO’s email, and forwarded their complaints there. Let’s hope this move will be appreciated. Else you’re in big, big trouble."

    $act_3_ending_28 = True
    $act_3_completed = True

    return