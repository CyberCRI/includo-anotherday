# The script of the game goes in this file.
# The game starts here.

label act1:
    $act_1_completed = False

    $lunch = False
    window hide

    scene bg meeting_room
    with dissolve

    narration "You reach the office early as usual."

    narration "You like taking your time, and sipping on your first tea in the open space,
                trying to take the pulse of the day before it starts, and people shuffle in one by one."

    narration "Your office feels homely in a way. It’s a box, really,
                but you like to think you’ve made the most of it though you took great care in stripping it of anything too personal,
                you’re the Human Resources Manager after all.{p}
                With the CEO still abroad, and M. Gopinath, the Administrative Director,
                on leave, you’re the one in charge of the whole office this week."

    narration "You sigh, and wish silently that you won’t have to take too many decisions.
                Your cup in hand, you walk slowly to your office, and find the door already open, and the lights on.
                When you hear muffled cries from within, you realize that your wish for a peaceful, and uneventful day, might have been lost."

    menu:
        "Enter.":
            jump .scene2

label .scene2:
    scene bg office
    with dissolve

    narration "Priyanka was sitting inside, facing your desk. You wonder how long she’s been waiting here."

    show priyanka crying with dissolve 

    narration "When she sees you, she stands up clumsily, tries to wipe her tears away, then sits back again. "

    narration "Puzzled, you speed up onto your chair."

    "What’s the matter, Priyanka? It’s very early."

    priyanka "I can’t stand it anymore, M. Chandrakant, I just can’t."

    priyanka "Every day… Every day I come in, and it’s the same, they just won’t stop-"

    "Wait, who? Who won’t stop? Stop doing what?"

    priyanka "They talk about the way I dress, my makeup, everything."

    priyanka "Sometimes they whistle, or they make gestures to me."

    priyanka "You know, {w=1}bad gestures."

    priyanka "Yesterday afternoon, I heard Bapat call me a westernized slut, and the whole office was laughing."

    priyanka "They crack lewd jokes with Donatello, and now they say I can’t come to work wearing a skirt, heels, or even makeup."

    priyanka "Maybe they’re not used to well-groomed women, but{w=1} this is important to me."

    "Why don’t you change the way you dress?"

    priyanka "Why is it to me to change my ways? Why can’t I be myself?"

    priyanka "Am I supposed to come in a sari with flowers every day?"

    thinking "I’m in a bit of a pickle now."

    thinking "Bapat is the Marketing Executive, and Donatello is the Senior Commercial Assistant."

    thinking "Two Very Important Persons, that you don’t want for enemies."

    thinking "Yet, if what Priyanka says is true, something must be done."

    thinking "Maybe there’s some truth in what she says?"

    thinking "Or maybe she’s plain wrong?"


    menu:
        thinking "What should I do ?"
        "Talk to them?":
            jump .scene3
        "Let it slide?":
            jump .scene6

label .scene3:
    scene bg lunch_room
    with dissolve

    narration "As you stride away from your office, determined to get to the bottom of this, you meet Bapat and Donatello as they drink their first coffee of the day in the company’s small canteen."

    show donatello sad at left
    show bapat at right

    narration "Looks like the whole team has decided to get up early today."

    "Did you two fall out of your beds?"

    bapat "We were waiting for you, Abhay"

    show donatello nods

    "That’s interesting because I was looking for the two of you myself"

    narration "They both look at each other smugly."

    thinking "Something must have happened yesterday, you think, else they wouldn’t all be gathered around me this morning like they are now."

    narration "You decide to bet on it:"

    "So who’s going to tell me about what happened yesterday?"

    bapat "It’s the same as usual, Abhay, this Priyanka she walks around half-naked, it’s not decent."

    donatello "And because of this, people cannot work properly, what is she looking for?"

    "So nothing happened?"

    donatello "Of course, we tried to tell her with humour, but she doesn’t get it"

    donatello " and she has the nerve to pretend to be angry at us now!"

    bapat "And pretending to cry with that! Like we’re the bad guys now!"

    "Hold on a second"

    "I’ve heard enough, guys, let me decide about this."

    menu:
        "What to choose next?"
        "Get to the bottom of this, and talk to the others ?":
            jump .scene4
        "Leave it be":
            jump .scene5

label .scene4:
    scene bg lunch_room
    with dissolve

    narration "Bapat and Donatello have left, leaving you alone in the canteen."

    narration "You hesitate between gathering everyone, and making a public inquiry, or meeting with all the others individually in your office."

    narration "While you ponder, you receive an email from Bapat on your phone asking all employees to come and meet him and Donatello in the meeting room to discuss ‘A Matter of Decency’. Brilliant, all you needed was a rebellion."

    menu:
        "Go to the meeting room":
            jump .scene6

label .scene5:
    scene bg lunch_room
    with dissolve

    narration "Bapat and Donatello have left, leaving you alone in the canteen."

    thinking "That was a close one."

    narration "Since you want everyone on board, and can’t afford to lose either Priyanka, Bapat, or Donatello before the new CEO comes in, you’ve chosen the path of least resistance: doing nothing."

    narration "While you congratulate yourself for your wisdom, you receive an email from Bapat on your phone asking all employees to come meet him, and Donatello in the meeting room to discuss ‘A Matter of Decency’. Brilliant, all you needed was a revolution."

    menu:
        "Go to the meeting room":
            jump .scene6

label .scene6:

    narration "It looks like you won’t get away with Bapat, and Donatello so easily."

    narration "Before you could take a decision about the situation yourself—if you had any intention of taking one—they’ve gathered everyone for a meeting to address what they describe as “decency issues”."

    thinking "Why the haste?"

    thinking "Are they afraid of the decision I might take?"

    thinking "Do they feel guilty in any way?"

    thinking "And if so, of what exactly?"

    thinking "Is it possible that they’re pushing hard because they genuinely feel offended?"

    narration "Whatever the case, you now find yourself in the meeting room {nw}"

    scene bg meeting_room
    with dissolve

    narration "Whatever the case, you now find yourself in the meeting room with everyone but Priyanka. You double-check your emails to verify that she’s been invited as well, and find that she wasn’t."

    narration "Bapat, and Donatello, are talking loud, and fast.
    Everybody else listens, scolds, or nod in agreement with them as statements go.
    This sure seems like a there’s a situation, and that the situation needs to be addressed.
    Still, you can’t ignore the feeling that something unusual happened yesterday, and that the reason of all this ruckus escapes you."

    "I am sorry to interrupt,"

    "but this isn’t how it works."

    show donatello at left with dissolve
    show giti with dissolve 
    show bapat at right with dissolve

    narration "Everybody looks at you now, you carry on:"

    "You can’t call for a public meeting, especially when you exclude another employee from this meeting,"

    "I am the one in charge of Human Resources here, and with M. Gopinath away, and the new CEO on the way, of the whole company at the moment."

    "If I wanted to call for a public meeting I would have done it."

    narration "There’s a lot of shoegazing as everybody falls silent."

    "I’d rather we stop this, and get back to work, we all have more important matters on our plates"

    "Don’t forget that we need to handle the deliveries for next week."

    hide giti with dissolve

    "As employees leave the meeting room one by one, you halt one of the culprits to speak with him privately."

    menu:
        thinking "Who should I talk to ?"
        "Bapat?":
            hide donatello with dissolve
            jump .scene7
        "Donatello?":
            hide bapat with dissolve
            jump .scene8

label .scene7:
    "I want you to tell me what happened yesterday."

    bapat "Ah, it’s nothing, Abhay, don’t get all wrangled up,"

    "So, something happened indeed."

    "I need to know it before I decide what to do with all this fuss."

    "Bapat, I can’t follow whatever it is you’re doing without being aware of the background."

    bapat "Ah okay, this Priyanka you know, she came in a mini-skirt like she does sometimes,"

    bapat "All provocation, no shame."

    bapat "And there are many men in the office"

    bapat "Even Giti was shocked."

    "And?"

    bapat "And The Donald, Donatello I mean, well, he’s a man, Abhay."

    bapat "He made some noises, and maybe a couple of jokes, and there she went, crying all over like a baby girl, and-"

    "So you thought that he could be in trouble, hence the ruckus you raise this morning."

    bapat "You don’t get it, Abhay, not at all."

    bapat "We just want to work peacefully, this is interfering with productivity."

    "Thank you, Bapat, I know all I need to know now."

    menu:
        "Go back to the meeting room":
            show donatello at left with dissolve
            jump .scene9

label .scene8:
    "I want you to tell me what happened yesterday."

    donatello "Nothing, why do you bother?"

    "I bother because I’m the HR Manager of this company, Donatello, not you,"

    "and you called for a public meeting the very same day I find Priyanka in my office,
    and didn’t even bother to invite her to this meeting."

    donatello "‘This woman is really a problem, you know, Abhay."

    "Well at least she doesn’t raise a ruckus like you and Bapat did…"

    "Now kindly tell me what happened."

    donatello "Oh well, she came to work like she’s going to party all night"

    donatello "and Bapat, well, he’s just a man, Abhay."

    donatello "He made noises, and motions, and maybe I made a couple of jokes, and felt her a bit, and she started to cry, and become angry as if WE were the problem, not her, and-"

    "So you thought that you both could be in trouble, hence the ruckus you raise this morning."

    donatello "I only think about the well-being of the company, Abhay,"

    donatello "customers come in here sometimes, what impression do we give to them by having Priyanka dressed up like this?"

    donatello "This isn’t a massage parlor, and what if the others, like Manali, start to copy her?"

    donatello "Men have drives, Abhay, she’s asking for it,"

    donatello "I can’t blame her really because we’re good-looking and all, but she must keep her instincts in control."

    "Thank you, Donatello, I know all I need to know now."

    menu:
        "Go back to the meeting room":
            show bapat at right with dissolve
            jump .scene9

label .scene9:

    narration "Before he leaves, his accomplice steps in as you are about to alight."

    narration "They both look at you with a strange mixture of mistrust, and eagerness."

    bapat "Are you going to do something about it, Abhay?"

    menu:
        "Yes, I am ready to take a decision.":
            hide donatello with dissolve
            hide bapat with dissolve
            jump .scene10
        "After my lunch." if lunch == False:
            $lunch =  True
            jump .scene15

label .scene10:
    scene bg office
    with dissolve

    narration "You’ve heard their explanations, and have gathered enough information to take a decision, and solve this problem now."

    narration "You could draft a dress code for all the employees of the office, so that Priyanka wouldn’t feel targeted, and that good work conditions can be maintained for everyone."

    narration "You could also take even less risks by calling for a public poll in the meeting room, so that everybody will have the opportunity to give one’s advice, and if anything goes wrong, you won’t be held responsible for it."

    narration "Or maybe you think that sometimes, a HR Manager has to take difficult decisions, and since Priyanka is the root of this trouble, you will issue her a warning to have her start dressing more appropriately, after all, she’s the only troublesome one as nobody ever complains about the other women."

    menu:
        "Draft a dress code.":
            jump .scene11
        "Call for a public poll.":
            jump .scene12
        "Issue a warning to Priyanka.":
            jump .scene13
        "Have lunch before you decide anything." if lunch == False:
            $lunch = True
            jump .scene15

label .scene11:
    narration "You draft a dress code forbidding short dresses, heels, and skirts, and requesting decency from the employees"

    narration "Later this day, you send it to all, and forward your email to M. GOPINATH, the Administrative Director, and to the new CEO. Better safe than sorry."

    menu:
        "The next morning...":
            jump .scene14

label .scene12:
    narration "You’ve decided to call for a public poll, and gather everyone once again in the meeting room."

    narration "Priyanka joined you, eager to find a solution, but when you describe the situation to the people, Bapat, and Donatello are very vocal, and slowly get everyone on board with their agenda."

    show bapat with dissolve

    bapat "Why does she have to dress like this? This isn’t a party!"

    show priyanka with dissolve

    priyanka "And how do I dress exactly, Bapat, do tell me? Is this because I’m not wrapped head to toe in a sari?"

    show donatello with dissolve

    donatello "It’s either sari, or panties with you."

    narration "The other women blush, and laugh with him."

    show priyanka with dissolve

    priyanka "How can you-{w=0.5}{nw}"

    show bapat with dissolve

    bapat "Look at Giti Madam, Priyanka, or sweet Manali, they dress with de-{w=0.5}cen-{w=0.5}cy."

    show priyanka with dissolve

    priyanka "What’s your prob-{w=0.5}{nw}"

    show bapat with dissolve

    bapat "When you dress like this, like western people trying to find a partner, of course we’re just men, "

    bapat "it’s difficult to concentrate, and ignore you, and the same goes for the customers, you’re ask-{w=0.5}{nw}"

    "Bapat!"

    "Stop this now, you need to keep your speech under control !"

    "The same goes for you, {nw}"

    show donatello with dissolve

    extend "Donatello."

    donatello "Then she needs to help us being in control, this shameless woman!"

    narration "With this, Priyanka leaves the meeting room in tears while the others whistle, and laugh.
    {p} Since the public meeting has turned into a nightmare, and added to Priyanka’s shaming, you regret this idea, but it’s a little too late."

    menu:
        "The next morning...":
            jump .scene14

label .scene13:
    narration "Since Priyanka is the only one causing trouble, you see no need to bother everyone with a dress code, or a public poll."

    narration "After all, Bapat, and Donatello have both explained the situation to you, and though you dislike doing it, you decide to issue Priyanka a warning.{p}
                It’s not your problem whether she accepts it peacefully or not, she has to be professional. Since the new CEO is said to be tough, this could be your chance to prove yourself worthwhile, and who knows, to be promoted."
    menu:
        "The next morning...":
            jump .scene14

label .scene14:
    scene bg none
    narration "Following your decision, and the events of the day, Priyanka gives you her resignation letter the next morning.{p=1}
    Bapat and Donatello gloat in the open space, and start making jokes about Manali, the Secretary, as well.{p=1}
    Given the terms of her contract, Priyanka has to stay for a month, now wearing an oversized sweater, and trousers, and will be there when the new CEO comes.{p=1}
    Let’s hope you made the right choice."

    return

label .scene15:
    scene bg lunch_room

    narration "You unpack your lunch box in the canteen. It’s a most welcomed time of the day as everybody blows off some steam, and engage in small talk."

    show donatello with dissolve

    donatello "...can you believe this ?"

    show giti

    giti "Well, you know, my community’s just off the main road, so I’m rather happy with this decision."

    show bapat

    bapat "‘But it’s a festival, Giti, how are we supposed to celebrate without fireworks, or sound system?"

    show manali

    manali "And it’s dry day as well."

    show bapat

    bapat "That is normal, it’s different!"

    show priyanka

    priyanka "How come the High Court decides about religion anyway?"

    show donatello

    donatello "Come on, religion? {w=0.5}How are fireworks, and techno music connected with religion in any way?"

    show bapat

    bapat "It’s like that, it’s what we do."

    bapat "What we’ve always done!"

    thinking "Gossips, and issues all the time."

    narration "The conversation then trails off on the subject of the new CEO.{p=1}
    M. BAJU, the former, wasn’t proactive, to put it mildly, but he maintained a peaceful if a bit droning work environment.{p=1}
    . We are creatures of habit, and don’t like to be shaken off them, and BAJU was our habit of a CEO, aloof, quiet, almost jaded.{p=1}
    You all got used to this. That was relaxing in a way.{p=1}
    Now that he’s gone, people are excited, and the bad stuff surfaces in this ungoverned space."

    narration "This is usually where you fall back on M. GOPINATH, the Administrative Director, but he’s taken his annual leave, and has left you alone to deal with everything."

    narration "Without active CEO, and M. GOPINATH being away, you are the highest ranking employee in the company right now, a company in turmoil with Priyanka’s issue this morning."

    thinking "I need to solve it, and to gather everyone's opinion."

    menu:
        "Talk to the other employees individually.":
            jump .scene16

label .scene16:
    scene bg office

    narration "If all you do to find the truth about people harassing women is talk with the harassers, you won’t go very far, you think. You need to gather the opinion of other employees, and maybe to ask the lawyer, M. RAJKUMAR, to give you his opinion."
    $email = False
    $talk_giti = False
    $talk_manali = False
    jump .employees

label .employees:
    menu:
        "Write an email to M. Rajkumar." if email == False:
            $email = True
            jump .scene17
        "Talk to Giti, the chief secretary, in your office" if talk_giti == False:
            $talk_giti = True
            jump .scene18
        "Talk to Manali, the secretary, in your office" if talk_manali == False:
            $talk_manali = True
            jump .scene19
        "You've talked to enough people." if talk_manali:
            jump .scene20

label .scene17:
    scene bg email_screen

    narration "You write to M. Rajkumar, the company’s Lawyer, and explain him the situation so that he can give you his advice. He answers a few hours later:"

    #TODO:MAIL
    narration "<INSERT MAIL HERE>"

    menu:
        "Talk to someone else.":
            jump .employees

label .scene18:
    scene bg office

    show giti with dissolve

    narration "Giti smiles intently while you explain her the situation, trying to offer both points of views as you do so. She cuts you off as you’re about to ask for her opinion."

    giti "I know very well everything you’re talking about, Abhay Sir."

    giti "It is true that Bapat, and Donald Sir, have been making very bad jokes on Priyanka, and calling her names, "

    giti "But the way she dresses pushes them to-{w=1}"

    "You mean that she’s asking for it?"

    "Why would she? Are they so gorgeous?"

    giti "Women should have a sense of decency, we’re not in New York Miami USA here."

    giti "I would be very ashamed if I went around dressed like she does."

    narration "You try to imagine Giti with Priyanka’s clothes on, but somewhat, you can’t."

    "*sigh* {w=0.5}Carry on."

    giti "I have said what I needed to, Abhay Sir."

    "What should I do then? Should I punish Priyanka, and leave the guys alone?"

    giti "Maybe you should give them all a warning, then decide on a dress code, or give Priyanka more warnings if she doesn’t change her ways."

    "By company policy, I have to fire her after three warnings have been issued, Giti, did you know that?"

    giti "I did not know, Abhay Sir."

    "But you still advise me to do it?"

    giti "No Sir, I have no solution."

    hide giti with dissolve

    narration "This being said, Giti leaves your office."

    menu:
        "Talk to someone else.":
            jump .employees

label .scene19:
    scene bg office

    narration "When Manali sits down in your office, you feel like a police officer conducting an interrogation. {p=1}
    She gazes at her shoes, and blushes a lot, twisting her fingers as she does."

    show manali with dissolve

    "You know why I have called you, right?"

    manali "Maybe because it’s about Priyanka and the management, Sir?"

    "Yes, it’s about that. Her, and Bapat, and Donatello, and whatever happened between them. {w=1}*sigh*"

    "Do you think she dresses too provocatively for work, Manali? That I should do something?"

    manali "I can’t say, Abhay Sir, I am not in a position to say."

    "Because you’re a woman? {w=0.5}Or a Secretary? {w=1}Nonsense. Please tell me."

    narration "Manali clears her throat, looks at the ceiling, clears her throat again, and speaks"

    manali "Well. Well, I don’t think so too much, Abhay Sir. It’s just…"

    narration "And with that, she stops speaking, and looks at the ceiling again."

    "Just what?"

    manali "Just that you should talk to her, so that she can change maybe? {w=0.5}Please?"

    thinking "I feel she's hiding something, but pushing her is maybe a bad idea. What should I do ?"

    menu:
        "Talk to someone else.":
            hide manali
            jump .employees
        "Push Manali to talk nevertheless.":
            jump .scene21

label .scene20:
    narration "The idea that Manali has not told you everything lingers in your mind, but you cast it off, you’re not supposed to make people uncomfortable, or to get the details of their private life, you keep the workplace productive, that’s your job.{p=1}
    You’ve talked to people enough anyway, it’s about time you take a decision. Who knows, maybe you’ll get another chance to talk to her."

    menu:
        "Take a decision.":
            jump .scene10

label .scene21:
    "I need to know, Manali, I am the HR Manager here, I can’t take decisions blindly. {p=0.5}You understand that?"

    narration "She nods."

    "If whatever it is that you’re hiding is connected to this situation, and can change the way it is for either Priyanka, Bapat, or Donatello,"

    "you need to tell me so that I don’t treat them unfairly."

    narration "She nods again."

    "You know something else, don’t you?"

    narration "She nods."

    "Then tell!"

    manali "It’s Priyanka, Abhay Sir, she was dating Bapat’s son last year."

    manali "They went on holidays together with Bapat even, and he never complained about her before, but since she’s left his son, he’s mad at her now."

    narration "She blushes into a deeper shade of red."

    thinking "What should I do now ?"

    menu:
        "Talk to Bapat privately.":
            hide manali with dissolve
            jump .scene22
        "Take a decision straight away.":
            hide manali with dissolve
            jump .scene24

label .scene22:
    narration "Given the new piece of information you’ve collected from Manali, you decide to talk to Bapat privately."

    show bapat with dissolve

    "I need to talk to you, Bapat."

    bapat "Sure, what’s the matter?"

    narration "Bapat moves nervously on the chair."

    "Is there something I should know about Priyanka that you didn’t tell me yet?"

    bapat "What is this nonsense?"

    "You tell me."

    narration "Bapat stutters as he reddens with anger."

    bapat "What did she tell you?!"

    "She told me nothing, Bapat, I’m fumbling in the dark here."

    narration "Bapat sighs with obvious relief"

    bapat "There’s nothing, Abhay, nothing."

    bapat "You should know better, and ignore the gossip."

    bapat "You’re the HR Manager, and I will make sure that the new CEO recognizes your merits, and value."

    narration "With that, Bapat shakes your hand, {nw}"

    hide bapat with dissolve

    extend "and leaves your office. "

    thinking "Given his reaction, Manali was obviously right, something’s amiss, and Priyanka having had an affair with his son would explain it all."

    thinking "Should I ignore the whole situation to keep both Priyanka, and Bapat on my side ?"

    thinking "Or should I take a decision with this new piece of information?"

    menu:
        "Ignore the situation.":
            jump .scene23
        "Take a decision.":
            jump .scene24

label .scene23:
    narration "Since Bapat knows that you know, even though nothing has been said openly, it’s now easy to ignore the whole situation. {p=1}
    Maybe he, and Donatello will calm down now, and stop shaming Priyanka. Regardless, the situation has become too complicated for you, a mere HR Manager, to dabble in."

    menu:
        "Hope that the situation will resolve by itself.":
            jump .scene33

label .scene24:
    thinking "I have a grasp of the whole situation now. What should I do ?"

    menu:
        "Talk to Bapat again, telling him that you know.":
            jump .scene25
        "Talk to Bapat, and Priyanka together.":
            jump .scene26
        "Gather everyone, and accuse Bapat publicly":
            jump .scene27
        "Let it slide, ignore the whole situation":
            jump .scene28
        "Draft an inclusive dress code":
            jump .scene29
        "Write to the international headquarters":
            jump .scene30

label .scene25:
    show bapat with dissolve

    bapat "What is it again, Abhay?"

    "I know everything, Bapat, about your son."

    bapat "Ah now she decided to tell you, she really has no shame, this woman!"

    "So it is true."

    bapat "Yes, it is true, this is how I found out how shameless she is!"

    bapat "She dresses like this because she’s a tease! No other reason."

    "She didn’t tell me, Bapat. I don’t think she would have."

    bapat "Yet something must be done about this woman, Abhay Sir."

    bapat "We can’t have women like this going around the office, breaking hearts and all."

    "You never did anything against her before she left your son. This needs to stop!"

    bapat "What’s the difference? People are with me!"

    bapat "They think the same, we can’t have <b>sluts</b> around!"

    "Okay, this breaks the camel’s back."

    "I will give you a warning, Bapat."

    bapat "Do it, so that I can tell everyone how not only she dresses shamelessly, but also dates men all around the place !"

    menu:
        "Do it.":
            jump .scene31

label .scene26:
    show bapat at left with dissolve
    show priyanka at right with dissolve

    narration "Once both Bapat and Priyanka, are seated in your office, you expose them what you know. {p=1}
    Bapat erupts at once, shouting in the office, while Priyanka remains silent, her gaze set upon the postcards on your walls. {p=1}
    As you’re trying to calm Bapat down, the other employees gather around, watching the scene with a keen interest, overhearing too many things to keep the meeting as private as it should."

    hide bapat with dissolve
    hide priyanka with dissolve
    show priyanka crying with dissolve

    priyanka "How can I stay now?"

    menu:
        "How indeed?":
            jump .scene31

label .scene27:

    narration "You gather everyone in the meeting room to expose them what you know, and put the shaming to a stop. {p=1}
    When you talk about the affair Priyanka had with Bapat’s son, and explain that it’s the reason why Bapat is now harassing her, things don’t go as you expected as you see them side with Bapat, and accuse Priyanka. {p=1}
    Not only have you failed to defend her, but you have added to her plight as everyone sympathizes with Bapat."

    menu:
        "The next morning...":
            jump .scene32

label .scene28:

    thinking "This is tricky."

    thinking "On one side, Bapat harasses Priyanka with vengeance, and bitterness in mind."

    thinking "On the other, this is all rooted in their private life, that I can’t expose at the office."

    thinking "Now that I know the full extent of the situation, I can’t possibly take decisions that would shame Priyanka, or punish her..."

    thinking "But I can’t expose Bapat either because this all would eventually bounce back on her."

    thinking "So what's left to do ?"

    menu:
        "Do nothing.":
            jump .scene33

label .scene29:
    narration "You need to do something, clearly, but you can’t accuse anyone, or try to solve interpersonal difficulties all by yourself, that’s not your job. {p=1}
    Deep down, you don’t want Bapat to get away with his vengeance either, but you can’t issue him a warning because this will eventually bounce back on Priyanka, and you’re not in a capacity to fire anyone, especially not a manager as the new CEO hasn’t arrived yet."

    thinking "They want a dress code ?"

    thinking "Let's give them a dress code."

    narration "So you do it, and write down the most inclusive dress code ever. Blue hair? Allowed. Mini-skirts? Allowed. Chapals? Allowed. No chapals? Allowed. Mohawks, and Black Metal tees? Allowed. {p=1}
    Of course, when the job requires a contact with clients, the dress code details a professional attire, a tailored skirt maybe, of whatever length, closed shoes, ties, etc. {p=1}
    Once you’ve finished with your draft, you send it to the new CEO’s email. After all, you don’t want to stay in a company who doesn’t understand this."

    menu:
        "Read the answer.":
            jump .scene30

label .scene30:
    narration "You write an email to the international Head Office, but they never answer you back."

    menu:
        "Take a decision by yourself.":
            jump .scene11


label .scene31:
    scene bg none
    narration "Instead of helping her, exposing Priyanka’s former relationship with Bapat’s son has fuelled the attacks against her. {p=1}
    For most people at the office, this is a proof that Bapat is a bad person, but also that Priyanka has no decency, and that Bapat was right in shaming her."

    narration "A week later, Priyanka gives you her resignation letter. {p=1}
    Given the terms of her contract, she has to stay for a month, now wearing an oversized sweater, and trousers, not talking to anyone anymore."

    return

label .scene32:
    scene bg none

    narration "Given the way the last meeting went, the situation becomes unbearable for Priyanka. {p=1}
    Since you don’t want her to be punished, you need to find a way to offer her another position in another Indian branch of the company. {p=1}
    You write the new CEO an email to request it, and manage to convince Priyanka to stay meanwhile."

    return

label .scene33:
    scene bg none

    narration "You simply ignore the situation, forgetting that this all started with Priyanka crying in your office this very morning. {p=1}
    Sure, you’ve managed to escape the most immediate threats, but nothing is solved, and Priyanka is shamed, and harassed every day by the same gang during the next week. {p=1}
    At the end of the week, the new CEO will step in. Hopefully, the new CEO will understand you stance, and all will be well."

    return

label .scene34:
    scene bg none

    narration "Looks like the international Head Office has faced the same kind of problems before, because they’ve just sent you the dress code they use in PDF format so that you can copy it instead of going all mohawks, and chapals. {p=1}
    It’s pretty inclusive as well, but better written that what you’ve sent them, and less chaotic. {p=1}
    Since the email is empty except for the PDF, and comes from the office, and not the CEO, you have no way to determine what they thought of your text, and initiative."

    narration "You copy it into the policy documents, and send it to all, now backed by the full force of the international Headquarters! Priyanka can now wear whatever she wants as long as the customers are fine with it. {p=1}
    Since the email came with an official document from the global office, there’s nothing Bapat, Donatello, and the others can do except to accept it."

    narration "Days later, not only does Priyanka come to thank you, but Manali starts to dress up more elegantly too. {p=1}
    Congratulations."

    return











