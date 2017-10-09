# The script of the game goes in this file.
# The game starts here.

label act2:
    $act_2_completed = False
    $talk_bapat = False
    $talk_women = False
    $talk_donatello = False
    $email_act_2 = False
    $email_act_2_2 = False
    $email_act_2_3 = False
    $talk_manali = False
    $talk_priyanka = False

    $act_2_ending_18 = False
    $act_2_ending_23 = False

    window hide 
    scene bg office with dissolve

    narration "You are in a fool mood today.{p}
                The traffic was a nightmare to begin with,
                car after after car for miles under the flyover they’ve started to build in 2008,
                and never finished."

    narration "You’re supposed to be of the serene kind, always in control of your emotions, always poker-faced, but truth is this is all just a mask."

    narration "You’re no different from them, but you know how to pretend better.{p}
                Maybe being the Human Resources Manager is all about knowing what to hide, and how to hide it well."

    thinking "I should have worked in a casino. At least, I would have made some big bucks."

    narration "When you reach the office, you’re a little bit late, and spill your tea as you hurry to your desk.{p}
                You swear under your breath, and keep striding to your place, where you find Giti waiting for you."

    show giti with dissolve

    "What can I do for you, Giti Madam?"

    giti "I need to talk to you, Abhay Sir. I have been thinking a long time about this."

    "Is this urgent?"

    giti "It is not, Abhay Sir, but now is as much a good time as another."

    thinking "What do I answer her?"

    menu:
        "\"Tell me, Giti. What happened?\"":
            jump .scene2
        "\"Not now, Giti, today's not a good day.\"":
            jump .scene3

label .scene2:
    giti "Abhay Sir, I have been working hard for M. Gopinath for the last three yea-"

    "I know that."

    "Your efforts are very appreciated, Giti."

    giti "Yes, Abhay Sir, also I have been working overtime in the evenings, and during weekends without even asking for compensatory leaves."

    "You could have asked, I would have approved them, you know. Is this what-"

    giti "No, Sir, please hear me out."

    giti "Not only have I worked hard, but I have accepted more and more responsibilities, "

    giti "like taking care of the transportation department, or of the security shift..."

    thinking "What could she want? Compensation holidays?"

    thinking "Gopinath isn't looking over my shoulder so I could give them."

    thinking "Or maybe it's a promotion?"

    thinking "Wait, is she going to resign? Is that what this is about?"

    giti "Sir, are you listening to me ?"

    "Y-{w=0.5}yes of course, carry on."

    giti "So I was saying I didn't know why I never got the promotion while Bapat had one in just one year,"

    giti "but when I heard them, it all became clear."

    giti "They said that they made sure that no women gets promoted, that only men can reach the top positions."

    "Who?"

    giti "I told you already, Ahbay Sir, Bapat, and Donatello, but little did they know that I was listening, and-"

    thinking "{b}Them again...{/b}"

    thinking "Or is she playing me, bouncing on the opportunity because of what happened with Priyanka ?"

    "So what do you want me to do, Giti?"

    giti "I want to request a promotion, Abhay Sir, and your official answer."

    thinking "Really, {w=0.25}just like that."

    thinking "Can I trust her ?"

    menu:
        "Approve her request":
            jump .scene4
        "Reject her request":
            thinking "This, the day after the Priyanka affair? She's trying to take advantage of the situation. I should reject her request."
            jump .scene5
        "The game is on, I need to investigate":
            jump .scene6

label .scene3:
    hide giti with dissolve

    narration "Giti left with a harsh face."

    thinking "She can make all the faces she wants, I couldn't care less."

    menu:
        "Watch stupid videos on YouTube.":
            narration "You slouch into your chair, watching YouTube videos about dancing parrots."

    narration "No CEO, no Administrative Direction, nothing, and you need to relax a bit after the worrisome dress code affair."

    thinking "Hey, whatever works."

    thinking "Some people do yoga, others run on the side of the road in the morning."

    thinking "I watch stupid videos."

    narration "After a particulary exalted dance sequence on {b}Tu Meri Bang Bang!{/b} featuring no less than a blue parrot,
    you open your email, and find a message from Giti formally requesting a promotion."

    narration "She stresses on all the overtime she did during the last three years,
    and all the new responsibilities she's been given by M. Gopinath,
    and requests your formal answer at the earnest."

    thinking "Now, that sound ominous, almost a threat, what's the hurry?"

    thinking "Looks like I need to answer her now."

    menu:
        "Answer her.":
            jump .scene13

label .scene4:
    hide giti with dissolve

    thinking "Wait, is this the right thing to do ?"

    thinking "I should take the time to think about the situation a little."

    thinking "Gopinath's away, the CEO's not here yet."

    thinking "This basically means I can do whatever I want but I'll still need to report to them and explain my decision afterwards."

    thinking "What about the team dynamics at the office? Won't this disrupt it?"

    narration "You take some time to weight all the pros and cons and you answer her."

    menu:
        "Answer her.":
            jump .scene13

label .scene5:
    hide giti with dissolve

    narration "This is the expected decision, and you’re pretty confident that everyone at the office will understand it. This way, you preserve the balance of power, and make sure you won’t be bothered when the new CEO will come, and M. Gopinath will return."

    narration "You sigh."

    thinking "There are maybe other aspect to deal with."

    thinking "What about the team dynamics at the office? Won't this disrupt it?"

    narration "You take some time to weight all the pros and cons and you answer her."

    menu:
        "Answer her.":
            jump .scene13

label .scene6:
    show bg meeting_room with dissolve

    narration "You walk to the meeting room, pour yourself another tea, and weigh your options.{p}
                You could meet with Bapat or Donatello to get to the heart of it, and find out whether they’ve been actually pushing a sexist agenda as Giti says,{p}
                 or you could start with the other women to find out whether Giti is alone in this, or if they will support her."

    narration "Since the promotion has to be approved by Giti’s manager, M. Gopinath, you could also write him an email to ask whether he would approve, or reject it.{p}
                On the other hand, if Giti has told you the truth about the conversation she has overheard, it is possible that Bapat, and Donatello have influenced him, and writing him will lead to Giti’s rejection.{p}
                Still, you can’t bypass him, or can you?"

    thinking "I have many options here."

label .investigate:

    menu:
        "Talk with the other women?" if talk_women == False:
            jump .scene7
        "Talk with Bapat?" if talk_bapat == False:
            jump .scene8
        "Talk with Donatello?" if talk_donatello == False:
            jump .scene9
        "Write an email to M. Gopinath?" if email_act_2 == False:
            jump .scene10

label .scene7:
    $talk_women = True
    narration "You don't want to make it too formal, and wait until the lunch break to get a chance to catch up with them."

    show bg lunch_room with dissolve

    narration "When you enter the canteen, both Priyanka, and Manali are present, each in a different corner of the room.
    The other employees are gathered together in the middle, and have started to eat, and talk."

    donatello "So that there are potholes everywhere."

    bapat "Ah, you just wait until the next elections, they will repair the roads then."

    donatello "Superpower in 2020."

    giti "I can't believe this, did you know they've found a crocodile in a hole of the road!"

    bapat "This is fake news, Giti! I can't believe you fell for it."

    donatello "It's not fake, Bapat. It's something concerned citizen have done, it's a plastic crocodile."

    giti "No, no, it was a real crocodile, Donald Sir! It has even attacked a child!"

    bapat "A {i}crocodile child molester{/i} now, Giti, please think!"

    narration "With that, the conversation trails off, and you remember that you wanted to talk to the women."

    thinking "Ok, which one first?"

    menu:
        "Talk to Priyanka?":
            jump .scene11
        "Talk to Manali?":
            jump .scene12

label .scene8:
    $talk_bapat = True
    show bg meeting_room with dissolve

    show bapat with dissolve

    narration "You have summoned Bapat to the meeting room, not as relaxed as the canteen, but not as formal as your office.
                You don’t want him to feel like he’s being under scrutiny, but you need to keep this conversation private."  

    narration "You decide to play it clever."

    "I need your advice Bapat."

    bapat "Of course, Abhay, whatever you need."

    "I’m going through the evaluation files today, and planning internal evolutions for the staff, "

    "Would you help me?"

    narration "Bapat nods, happy to be considered."

    "Good."

    "My first problem is that, judging from the efforts, and responsibilities taken this year,"

    "The three employees which stand out are {w=0.25}Manali, {w=0.25}Priyanka, {w=0.25}and Giti."

    "I'm not talking about your department of course."

    narration "Bapat grunts."

    "Obviously, I can't offer to promote all three, but I need to reward their efforts."

    bapat "Maybe you can promote Manali, Abhay?"

    "Why only her"

    bapat "Abhay, if you promote the others, you will push women into the head management."

    bapat "We have enough problems right now."

    "Why is that a problem?"

    bapat "Ah, they’re not like us, Abhay, "

    bapat "They’re full of gossip, and all, "

    bapat "They’re good housewife material, but none of us will accept being commanded by a woman."

    "I see.{w=0.5} Thank you, Bapat."

    "Now will you help me with the network?"

    narration "With that, you talk, and talk for long enough for Bapat to forget that you've asked about the women."

    hide bapat with dissolve

    thinking "He's gone now."

    if talk_bapat == False or talk_donatello == False or email_act_2 == False or talk_women == False:
        thinking "I could take a decision right now or keep investigating."
    else:
        thinking "I have done enough investigating, it's time to take a decision."

    menu:
        "Take a decision now.":
            jump .scene13
        "Keep investigating." if talk_women = False or talk_donatello = False or email_act_2 = False:
            jump .investigate

label .scene9:
    $talk_donatello = True

    show bg meeting_room with dissolve
    show donatello with dissolve

    narration "Obviously, Donatello doesn't know what to expect from this meeting.
                He looks a bit confused, and wary. You have to play it cautious, and beat about the bush a little"

    "I need your advice, Donatello."

    donatello "Yes, of course, what is it?"

    "I have a lot of paperwork to do for the next review of the sales department’s employees, and I don’t understand the sales figures."

    donatello "Show me that."

    narration "You hand him the sale reports."

    "That's a lot of work, maybe Giti, or Priyanka can help you?"

    narration "You see him hesitating."

    "What's the matter, Donatello?"

    donatello "Well, {w=0.25}Abhay, {w=0.25}you know I would rather trust my own analysis."

    donatello "Sales reviews are complex, and require a lot of experience."

    "But Priyanka has been here longer than you, Donatello, why can’t she help?"

    donatello "Abhay, talking to clients is one thing, but this is high level managerial stuff-"

    "And you think she can't do it?"

    donatello "She can’t, Abhay."

    donatello "She’s not fit for this level of responsibility."

    donatello "She may have received the same education, but she’s a woman,"

    donatello "It's a very different situation."

    "I see."

    "Thank you, Donatello."

    "Can you get back to me with your analysis by tomorrow?"

    narration "With that, you talk, and talk for long enough for Donatello to forget what you just asked."

    hide donatello with dissolve

    thinking "What should I do now ?"

    if talk_bapat == False or talk_donatello == False or email_act_2 == False or talk_women == False:
        thinking "I could take a decision right now or keep investigating."
    else:
        thinking "I have done enough investigating, it's time to take a decision."

    menu:
        "Take a decision.":
            jump .scene13
        "Keep investigating." if talk_women = False or talk_bapat = False or email_act_2 = False:
            jump .investigate

label .scene10:
    show bg email

    narration "You decide to write to M. Gopinath. He’s Giti’s manager, after all, and you don’t want to bypass his authority, and take this decision alone."

    narration "There’s a chance that Bapat, and Donatello have influenced him, though, and you need to write this email in such a way that he will answer this issue without being offended, quite a feat in itself."

    narration "You take your time, and rewrite your email several times to find the correct tone, and to get to the point with tact."

    narration "You receive an automatic out-of-the-office answer minutes later, and never hear about it again"

    email "adnan.gopinath@cryptaloo.com 
                To: abhay.chandrakant@cryptaloo.in
                Out of the Office
                I am currently on leave, enjoying the warm beaches of Diu Island. I will answer you as soon as I reach my office back. If you have any urgent matter, kindly write to M. Chandrakant at the following email: abhay.chandrakant@cryptaloo.in.
                Best regards,
                M. Gopinath"


    thinking "What now?"

    if talk_bapat == False or talk_donatello == False or email_act_2 == False or talk_women == False:
        thinking "I could take a decision right now or keep investigating."
    else:
        thinking "I have done enough investigating, it's time to take a decision."

    menu:
        "Take a decision.":
            jump .scene13
        "Keep investigating." if talk_women = False or talk_bapat = False or talk_donatello = False:
            jump .scene6

label .scene11:
    show bg lunch_room with dissolve
    show priyanka with dissolve

    narration "You sit next to Priyanka and engage in a small talk with her.{p}
                After a while, you decide to jump in."

    "How come you've been working here for 2 years, and never asked for a promotion, Priyanka?"

    priyanka "Because promotions have to be approved by the higher management, Abhay"

    priyanka "And they clearly told everyone that there won’t be any in my department for the next three years…"

    "But Bapat is in your department, and has been promoted, hasn't he?"

    priyanka "It's not the same."

    "How so ?"

    priyanka "..."

    "How so, Priyanka ?"

    priyanka "He’s friends with The Gopi, and The Donald—{w=0.5}Gopinath, and Donatello Sirs, I mean, and-"

    "That shouldn't matter, this is a {i}company{/i}, not a club!"

    priyanka "Yes, Abhay, but it’s like that, and I’m a woman."

    priyanka "Have you ever seen a woman being promoted here?"

    "Many of them."

    "There's Vina from the Front Desk,{w=0.5}Karuna from the Distribution Department,{w=0.5}Shruti from-"

    priyanka "But none from the Marketing,{w=0.5}the Sales Department,{w=0.5} or the Head Administration, Abhay, that’s what I’m telling you."

    thinking "I have heard enough."

    $talk_priyanka = True

    if talk_manali == True:
        if talk_bapat == False or talk_donatello == False or email_act_2 == False:
            thinking "I could talke to Manali, keep investigating or take a decision."
        else:
            thinking "Manali's the only one left."
    else:
        thinking "I have talked to both Manali and Priyanka."

        if talk_bapat == False or talk_donatello == False or email_act_2 == False or talk_women == False:
            thinking "I could take a decision right now or keep investigating."
        else:
            thinking "I have done enough investigating, it's time to take a decision."

    menu:
        "Talk to Manali." if talk_manali == False:
            jump .scene12
        "Keep investigating." if talk_bapat == False or talk_donatello == False if email_act_2 == False:
            jump .investigate
        "Take a decision now":
            jump .scene13

label .scene12:
    show bg lunch_room with dissolve
    show manali with dissolve

    narration "You catch up with Manali as she’s about to finish her lunch.{p}
                You take the time to grab a tray, pour yourself some spinach soup, sit next to her, and start talking about her department."

    "I’ve heard it’s going well, congratulations."

    "You’re doing a great job, handling the secretary, the security, and the transportation all together!"

    manali "It’s Giti, Abhay Sir, she’s working so much, and she’s very efficient."

    "It’s been what? Three years now that she’s doing that?"

    narration "You drink a mouthful of soup, it’s cold already."

    manali "Three years, Abhay Sir, and she never complains."

    "Yet she’s never been promoted"

    "Manali, I will talk to M. Gopinath about it."

    narration "You take another spoon of soup, still looking at her, drink it with a grimace, and push the bowl aside on your tray."

    manali "You should, Sir, but he probably will not listen."

    "And why is that?"

    manali "I don’t know, Sir, I just said that for no reason."

    "Of course there's a reason, please tell me."

    manali "She’s got a very good position already, and maybe they don’t want to give her too much responsibilities because-"

    "Because she's a woman?"

    manali "I didn’t say that, Sir!"

    "But you meant that."

    show manali blushing

    pause 2

    thinking "She did mean that."

    thinking "I have heard enough."

    $talk_manali = True

    if talk_priyanka == True:
        if talk_bapat == False or talk_donatello == False or email_act_2 == False:
            thinking "I could talke to Priyanka, keep investigating or take a decision."
        else:
            thinking "Priyanka's the only one left."
    else:
        thinking "I have talked to both Manali and Priyanka."

        if talk_bapat == False or talk_donatello == False or email_act_2 == False or talk_women == False:
            thinking "I could take a decision right now or keep investigating."
        else:
            thinking "I have done enough investigating, it's time to take a decision."

    menu:
        "Talk to Priyanka." if talk_priyanka == False:
            jump .scene12
        "Keep investigating." if talk_bapat == False or talk_donatello == False if email_act_2 == False:
            jump .investigate
        "Take a decision now":
            jump .scene13

label .scene13:
    thinking "I guess I know enough by now."

    thinking "Since Giti sounded very eager to receive an answer in earnest, I need to take a decision."

    thinking "I could approve her promotion, or reject it myself..."

    thinking "I could try to write to M. Gopinath and ask him to decide instead."

    thinking "Or maybe I should ask M. Rajkumar. He's the company lawyer, he may have some advice."

    thinking "Decisions, decisions..."

label .decide:

    menu:
        "Approve her promotion.":
            jump .scene14
        "Write an email to M. Gopinath." if email_act_2_2 == False:
            jump .scene15
        "Ask M. Rajkumar's advice.":
            jump .scene16
        "Reject her request.":
            jump .scene17

label .scene14:
    show bg office with dissolve

    narration "You call Giti to your office."

    show giti with dissolve

    narration "Once she's sat, you begin."

    "I have decided to approve your promotion request, Giti."

    show giti surprised

    giti "T-Thank you, Abhay Sir."

    show giti smile

    giti "Thank you, Abhay Sir, {b}thank you{/b}."

    "Hahaha !"

    "About time, isn't it? Things should change around here."

    giti "About time, Abhay Sir, about time, thank you."

    narration "When she leaves, you fall back into your chair, resting your head upon your hands above your neck."

    narration "Now, you’ll have to deal with the aftermath."

    menu:
        "The aftermath.":
            jump .scene18

label .scene15:
    show bg office with dissolve
    narration "You write to M. Gopinath, asking him clearly and directly to take the matter into his hands so that you can escape the storm that will follow either decision you might take,
                receive an automatic out-of-the-office answer minutes later, and never hear about it again."

    email "adnan.gopinath@cryptaloo.com 
            To: abhay.chandrakant@cryptaloo.in
            Out of the Office
            I am currently on a pilgrimage to Kailash Mountain. I will answer you as soon as I reach my office back. If you have any urgent matter, kindly write to M. Chandrakant at the following email: abhay.chandrakant@cryptaloo.in.
            Best regards,
            M. Gopinath"

    $email_act_2_2 = True

    menu:
        "You really need to decide by yourself.":
            jump .decide

label .scene16:
    show bg office with dissolve
    narration "You write to M. Rajkumar, the company’s Lawyer, and explain him the situation so that he can give you his advice."

    narration "He answers a few hours later."

    email "rajkumarrajkumarltd@gmail.com 
        To: abhay.chandrakant@cryptaloo.in
        Re: Promotion and Discrimination
        Dear M. Chandrakant,
        If your Mrs. Shaikh Giti can prove the alleged discrimination she suffers mutatis mutandis, the situation could lead to a case in court indeed, and involve liabilities, and damages as per the accessory of the main article to be continued habeas corpus. In all actuality (Ibid.), discrimination is very difficult to prove as she would require either written proofs, several witnesses, or written proof of a constant pattern from the company’s side to support her claim. Since she will find deprived of these proofs, it is most probable that she will not escalate as fees will discourage her from doing so as well. Unless you are certain that she has gathered said means of proof, I would advise to reject her plea, and act on the sole base of her professional merit and quality.
        Yours truly,
        M. Rajkumar
        Rajkumar & Rajkumar Ltd."

    $email_act_2_3 = True

    menu:
        "Time to take a decision.":
            jump .decide

label .scene17:
    narration "If you had promoted everyone who threatened you, everybody would be CEO by now.{p}
                This is not how it works."

    narration "Further, a promotion is not only a matter of doing overtime, and taking responsibilities, it’s about the person’s capacity to do take up complex challenges."

    narration "The least you can say is that Giti is not showing this capacity by trying to accuse Bapat and Donatello, and giving you ultimatums to promote her while her manager is away."

    narration "You write her an email, telling her dryly that her request is rejected."

    thinking "What a terrible day"

    menu:
        "And it's not over yet.":
            jump .scene19

label .scene18:
    narration "You’ve sent an email to inform everyone about Giti’s promotion, not forgetting to send a copy to M. Gopinath.{p}
                Bapat and Donatello, have stormed into your office several times since then, trying to prove their point, but you’re the HR Manager, and with M. Gopinath, and the new CEO away, there’s nothing they can do.{p}
                You surmise that M. Gopinath won’t be happy, and hope that the new CEO will understand your position. Time will tell."

    $act_2_ending_18 = True
    $act_2_completed = True
    return

label .scene19:
    narration "A few hours later, someone knocks at your door, and hands you a piece of paper before leaving.{p}
                The paper bears several stamps, and signs, a subpoena."

    narration "Giti has decided to sue on the basis of Denial of Equal Opportunity, which has the same legal consequences as harassment.{p}
                The subpoena mentions a constant pattern of exclusion, and several witnesses.{p}
                Further, she asks for damages for the last three years’ overtime, and increased responsibilities without compensation, and requests the court to enforce the promotion she’s been asking in vain."

    thinking "Looks like she's been prepared all along."

    menu:
        "You can't risk a trial, promote her.":
            jump .scene20
        "Ask M. Rajkumar, The company's laywer, for his advice." if email_act_2_3 == False:
            jump .scene21
        "Ask M. Rajkumar for his advice again." if email_act_2_3 == True:
            jump .scene21
        "Laugh and ignore the threat.":
            jump .scene22

label .scene20:
    narration "You call Giti to your office."

    show giti with dissolve

    narration "Once she's sat, you begin."

    "I have decided to approve your promotion request, Giti."

    giti "It's only fair, Abhay Sir."

    "So you will drop this case, won’t you?"

    giti "Yes, Sir, I only want the promotion I should have had long ago."

    "Well, you have it."

    "Please send me the acknowledgement of cancellation for the case, and I will promote you as I said."

    giti "No, Abhay Sir, {nw=0.5}{nw}you need to sign the promotion in counterpart with my Lawyer so that we are sure that it happens, and is registered."

    giti "At the same time, he will sign the cancellation in front of you, and provide you with the acknowledgement."

    thinking "She has obviously studied this."

    "Okay, okay, kindly plan this meeting after working hours, and make it happen quick."

    menu:
        "The aftermath.":
            jump .scene18

label .scene21:
    narration "If there’s something the company’s Lawyer should be able to help you with, it’s dealing with a subpoena."

    narration "If you go to the court, he will be the one defending you after all."

    narration "You write him, explaining the situation, and joining a scanned copy of the subpoena. He answers almost immediately."

    email "rajkumarrajkumarltd@gmail.com 
            To: abhay.chandrakant@cryptaloo.in
            Re: Subpoena/Giti Shaikh
            Dear M. Chandrakant,
            So far, all that we know is that Mrs. Shaikh Giti is suing the company on the basis of the Denial of Equal Opportunity. She says that she has collected proofs, but we have not seen these proofs as yet, and we might be in a position to challenge them if they seem weak. Only then will I know what our chances to win the trial are, and if they seem low, to open negotiations with her. If, from your position you can gather already that she will have a decent amount of solid proof, I advise you to promote her so that you can avoid paying for the damages she requests. If this isn’t the case, I advise you to proceed so that we can see what she has, and take appropriate action.
            Yours truly,
            M. Rajkumar
            Rajkumar & Rajkumar Ltd."

    thinking "It's time to take my decision."

    menu:
        "Promote Giti.":
            jump .scene20
        "Ignore her.":
            jump .scene22

label .scene22:
    narration "You don’t even answer her. One simply doesn’t threaten the HR Manager."

label .scene23:
    narration "You can’t fire Giti because she sues the company, that in itself would open a whole new case against you so she stays, brooding, waiting for the trial.{p}
    he atmosphere of the office changes, there’s no more friendly banter now.{p}
    Bapat and Donatello are obviously on your side, you’re part of their gang now.{p}"

    narration "Surely, the new CEO will surely know how to handle a court case better than you, and everything will be fine again."

    $act_2_ending_23 = True
    $act_2_completed = True
    return






















