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

    scene bg none

    $renpy.pause(3.0)

    narration "You are in a fool mood today.{p}
                The traffic was a nightmare to begin with,
                car after after car for miles under the flyover they’ve started to build in 2008,
                and never finished."

    narration "You’re supposed to be of the serene kind, always in control of your emotions, always poker-faced, but truth is this is all just a mask."

    narration "You’re no different from them, but you know how to pretend better.{p}
                Maybe being the Human Resources Manager is all about knowing what to hide, and how to hide it well."

    thinking "I should have worked in a casino. At least, I would have made some big bucks."

    show bg office
    with Dissolve(3.0)

    narration "When you reach the office, you’re a little bit late, and spill your tea as you hurry to your desk.{p}
                You swear under your breath, and keep striding to your place, where you find Giti waiting for you."

    show giti with dissolve

    abhay "What can I do for you, Giti Madam?"

    giti "I need to talk to you, Abhay Sir. I have been thinking a long time about this."

    abhay "Is this urgent?"

    giti "It is not, Abhay Sir, but now is as much a good time as another."

    menu:
        thinking "What do I answer her?"
        "\"Tell me, Giti. What happened?\"":
            jump .scene2
        "\"Not now, Giti, today's not a good day.\"":
            jump .scene3

label .scene2:
    giti "Abhay Sir, I have been working hard for Mr. Gopinath for the last three yea-"

    abhay "I know that."

    abhay "Your efforts are very appreciated, Giti."

    giti "Yes, Abhay Sir, also I have been working overtime in the evenings, and during weekends without even asking for compensatory leaves."

    abhay "You could have asked, I would have approved them, you know. Is this what-"

    show giti angry

    giti angry "No, Sir, please hear me out."

    giti angry "Not only have I worked hard, but I have accepted more and more responsibilities, "

    giti angry "like taking care of the transportation department, or of the security shift..."

    thinking "What could she want?{w=0.5} Compensation holidays?"

    thinking "Gopinath isn't looking over my shoulder so I could give them."

    thinking "Or maybe it's a promotion?"

    thinking "Wait, is she going to resign?{w=0.5} Is that what this is about?"

    show giti

    giti "Sir, are you listening to me?"

    abhay "Y-{w=0.5}yes of course, carry on."

    giti "So I was saying I didn't know why I never got the promotion while Bapat had one in just one year,"

    giti "but when I heard them, it all became clear."

    show giti sad

    giti sad "They said that they made sure that no women gets promoted, that only men can reach the top positions."

    abhay "Who?"

    show giti

    giti "I told you already, Ahbay Sir, Bapat, and Donatello, but little did they know that I was listening, and-"

    thinking "{b}Them again...{/b}"

    thinking "Or is she playing me, bouncing on the opportunity because of what happened with Priyanka?"

    abhay "So what do you want me to do, Giti?"

    show giti angry

    giti angry "I want to request a promotion, Abhay Sir, and your official answer."

    thinking "Really, {w=0.25}just like that."

    menu:
        thinking "Can I trust her?"
        "Approve her request.":
            jump .scene4
        "Reject her request.":
            thinking "This, the day after the Priyanka affair?{w=0.5} She's trying to take advantage of the situation. I should reject her request."
            jump .scene5
        "The game is on, I need to investigate.":
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

    menu:
        thinking "Looks like I need to answer her now."
        "Answer her.":
            jump .scene13

label .scene4:
    hide giti with dissolve

    thinking "Wait, is this the right thing to do?"

    thinking "I should take the time to think about the situation a little."

    thinking "Gopinath's away, the CEO's not here yet."

    thinking "This basically means I can do whatever I want but I'll still need to report to them and explain my decision afterwards."

    thinking "What about the team dynamics at the office?{w=0.5} Won't this disrupt it?"

    narration "You take some time to weight all the pros and cons and you answer her."

    menu:
        "Answer her.":
            jump .scene13

label .scene5:

    hide giti with dissolve

    narration "This is the expected decision, and you’re pretty confident that everyone at the office will understand it. This way, you preserve the balance of power, and make sure you won’t be bothered when the new CEO will come, and Mr. Gopinath will return."

    thinking "*sigh*{w=1} There are maybe other aspect to deal with."

    thinking "What about the team dynamics at the office?{w=0.5} Won't this disrupt it?"

    narration "You take some time to weight all the pros and cons and you answer her."

    menu:
        "Answer her.":
            jump .scene13

label .scene6:

    window hide

    show bg meeting_room with fade

    narration "You walk to the meeting room, pour yourself another tea, and weigh your options.{p}
                You could meet with Bapat or Donatello to get to the heart of it, and find out whether they’ve been actually pushing a sexist agenda as Giti says,{p}
                 or you could start with the other women to find out whether Giti is alone in this, or if they will support her."

    narration "Since the promotion has to be approved by Giti’s manager, Mr. Gopinath, you could also write him an email to ask whether he would approve, or reject it.{p}
                On the other hand, if Giti has told you the truth about the conversation she has overheard, it is possible that Bapat, and Donatello have influenced him, and writing him will lead to Giti’s rejection.{p}
                Still, you can’t bypass him, or can you?"

label .investigate:

    menu:
        thinking "I have many options here."
        "Talk with the other women?" if talk_women == False:
            jump .scene7
        "Talk with Bapat?" if talk_bapat == False:
            jump .scene8
        "Talk with Donatello?" if talk_donatello == False:
            jump .scene9
        "Write an email to Mr. Gopinath?" if email_act_2 == False:
            jump .scene10

label .scene7:
    $talk_women = True
    narration "You don't want to make it too formal, and wait until the lunch break to get a chance to catch up with them."

    window hide

    show bg lunch_room with fade

    narration "When you enter the canteen, both Priyanka, and Manali are present, each in a different corner of the room.
    The other employees are gathered together in the middle, and have started to eat, and talk."

    donatello "So that there are potholes everywhere."

    bapat smug "Ah, you just wait until the next elections, they will repair the roads then."

    donatello "Superpower in 2020."

    giti "I can't believe this, did you know they've found a crocodile in a hole of the road!"

    bapat angry "This is fake news, Giti!{w=0.5} I can't believe you fell for it."

    donatello "It's not fake, Bapat.{w=0.25} It's something concerned citizen have done, it's a plastic crocodile."

    giti angry "No, no, it was a real crocodile, Donald Sir!{w=0.5} It has even attacked a child!"

    bapat smug "A {i}crocodile child molester{/i} now, Giti, please think!"

    narration "With that, the conversation trails off, and you remember that you wanted to talk to the women."

    menu:
        thinking "Ok, which one first?"
        "Priyanka.":
            jump .scene11
        "Manali.":
            jump .scene12

label .scene8:

    window hide
    show bg meeting_room with dissolve

    show bapat with dissolve

    narration "You have summoned Bapat to the meeting room, not as relaxed as the canteen, but not as formal as your office.
                You don’t want him to feel like he’s being under scrutiny, but you need to keep this conversation private."  

    narration "You decide to play it clever."

    abhay "I need your advice Bapat."

    bapat "Of course, Abhay, whatever you need."

    abhay "I’m going through the evaluation files today, and planning internal evolutions for the staff, "

    abhay "Would you help me?"

    narration "Bapat nods, happy to be considered."

    show bapat happy

    abhay "Good."

    abhay "My first problem is that, judging from the efforts, and responsibilities taken this year,"

    abhay "The three employees which stand out are {w=0.25}Manali, {w=0.25}Priyanka, {w=0.25}and Giti."

    abhay "I'm not talking about your department of course."

    show bapat

    bapat "..."

    abhay "Obviously, I can't offer to promote all three, but I need to reward their efforts."

    bapat "Maybe you can promote Manali, Abhay?"

    abhay "Why only her"

    bapat "Abhay, if you promote the others, you will push women into the head management."

    bapat "We have enough problems right now."

    abhay "Why is that a problem?"

    bapat "Ah, they’re not like us, Abhay, "

    bapat "They’re full of gossip, and all, "

    bapat "They’re good housewife material, but none of us will accept being commanded by a woman."

    abhay "I see.{w=0.5} Thank you, Bapat."

    abhay "Now will you help me with the network?"

    narration "With that, you talk, and talk for long enough for Bapat to forget that you've asked about the women."

    hide bapat with dissolve

    thinking "He's gone now."

    $talk_bapat = True

    if not talk_bapat or not talk_donatelloor or not email_act_2 or not talk_women:
        thinking "I could take a decision right now or keep investigating."
    else:
        thinking "I have done enough investigating, it's time to take a decision."

    menu:
        "Take a decision now.":
            jump .scene13
        "Keep investigating." if not talk_women or not talk_donatello or not email_act_2:
            jump .investigate

label .scene9:

    window hide 

    show bg meeting_room with fade

    show donatello with dissolve

    narration "Obviously, Donatello doesn't know what to expect from this meeting.
                He looks a bit confused, and wary. You have to play it cautious, and beat about the bush a little"

    abhay "I need your advice, Donatello."

    donatello "Yes, of course, what is it?"

    abhay "I have a lot of paperwork to do for the next review of the sales department’s employees, and I don’t understand the sales figures."

    donatello "Show me that."

    narration "You hand him the sale reports."

    abhay "That's a lot of work, maybe Giti, or Priyanka can help you?"

    narration "You see him hesitating."

    abhay "What's the matter, Donatello?"

    donatello "Well, {w=0.25}Abhay, {w=0.25}you know I would rather trust my own analysis."

    donatello "Sales reviews are complex, and require a lot of experience."

    abhay "But Priyanka has been here longer than you, Donatello, why can’t she help?"

    donatello "Abhay, talking to clients is one thing, but this is high level managerial stuff-"

    abhay "And you think she can't do it?"

    donatello "She can’t, Abhay."

    donatello "She’s not fit for this level of responsibility."

    donatello "She may have received the same education, but she’s a woman,"

    donatello "It's a very different situation."

    abhay "I see."

    abhay "Thank you, Donatello."

    abhay "Can you get back to me with your analysis by tomorrow?"

    narration "With that, you talk, and talk for long enough for Donatello to forget what you just asked."

    hide donatello with dissolve

    thinking "What should I do now?"

    $talk_donatello = True

    if not talk_bapat or not talk_donatello or not email_act_2 or not talk_women:
        thinking "I could take a decision right now or keep investigating."
    else:
        thinking "I have done enough investigating, it's time to take a decision."

    menu:
        "Take a decision.":
            jump .scene13
        "Keep investigating." if not talk_women or not talk_bapat or not email_act_2:
            jump .investigate

label .scene10:
    window hide

    show bg office with fade

    narration "You decide to write to Mr. Gopinath. He’s Giti’s manager, after all, and you don’t want to bypass his authority, and take this decision alone."

    narration "There’s a chance that Bapat, and Donatello have influenced him, though, and you need to write this email in such a way that he will answer this issue without being offended, quite a feat in itself."

    narration "You take your time, and rewrite your email several times to find the correct tone, and to get to the point with tact."

    narration "You receive an automatic out-of-the-office answer minutes later, and never hear about it again"

    window hide

    show mail_icon_blink

    pause

    hide mail_icon_blink
    show mail_icon_open

    $mail_gopinath(("I am currently on leave, enjoying the warm beaches of Diu Island. I will answer you as soon as I reach my office back.\n"
        "If you have any urgent matter, kindly write to Mr. Chandrakant at the following email: {color=#0000FF}{u}abhay.chandrakant@cryptaloo.in{/u}{/color}.\n"
        "\nBest regards,\nMr. Gopinath\n"
        "{font=fonts/Oswald-Regular.ttf}{size=14}{k=-1}{color=#009fff}Adnan Gopinath, Administrative Director{/color}{/k}{/size}\n"
        "{size=12}{k=-1}Pearls Omaxe Building, Off # 1005, 10th Floor, First Tower{/k}{/size}\n"
        "{size=12}{k=-1}Netaji Subhash Place Complex, Pitampura, Delhi 110034, INDIA{/k}{/size}{/font}"))

    hide mail_icon_open

    pause 3.0

    thinking "What now?"

    if not talk_bapat or not talk_donatello or not email_act_2 or not talk_women:
        thinking "I could take a decision right now or keep investigating."
    else:
        thinking "I have done enough investigating, it's time to take a decision."

    menu:
            "Take a decision.":
                jump .scene13
            "Keep investigating." if not talk_women or not talk_bapat or not talk_donatello:
                jump .scene6

label .scene11:
    window hide
    show bg lunch_room with fade
    show priyanka smiling with dissolve

    narration "You sit next to Priyanka and engage in a small talk with her.{p}
                After a while, you decide to jump in."

    abhay "How come you've been working here for 2 years, and never asked for a promotion, Priyanka?"

    show priyanka

    priyanka "Because promotions have to be approved by the higher management, Abhay"

    priyanka "And they clearly told everyone that there won’t be any in my department for the next three years…"

    priyanka "So it's no use, you see?"

    abhay "But Bapat is in your department, and has been promoted, hasn't he?"

    priyanka "It's not the same."

    abhay "How so?"

    priyanka "..."

    abhay "How so, Priyanka?"

    priyanka "He’s friends with The Gopi, and The Donald—{w=0.5}Gopinath, and Donatello Sirs, I mean, and-"

    abhay "That shouldn't matter, this is a {i}company{/i}, not a club!"

    priyanka "Yes, Abhay, but it’s like that, and I’m a woman."

    priyanka "Have you ever seen a woman being promoted here?"

    abhay "Many of them."

    abhay "There's Vina from the Front Desk,{w=0.5}Karuna from the Distribution Department,{w=0.5}Shruti from-"

    show priyanka smiling

    priyanka smiling "But none from the Marketing,{w=0.5}the Sales Department,{w=0.5} or the Head Administration, Abhay, that’s what I’m telling you."

    thinking "I have heard enough."

    $talk_priyanka = True

    if talk_manali:
        if not talk_bapat or not talk_donatello or not email_act_2:
            thinking "I could talke to Manali, keep investigating or take a decision."
        else:
            thinking "Manali's the only one left."
    else:
        thinking "I have talked to both Manali and Priyanka."

    if not talk_bapat or not talk_donatello or not email_act_2 or not talk_women:
        thinking "I could take a decision right now or keep investigating."
    else:
        thinking "I have done enough investigating, it's time to take a decision."

    menu:
        "Talk to Manali." if not talk_manali:
            jump .scene12
        "Keep investigating." if not talk_bapat or not talk_donatello if not email_act_2:
            jump .investigate
        "Take a decision now":
            jump .scene13

label .scene12:
    window hide
    show bg lunch_room with dissolve
    show manali with dissolve

    narration "You catch up with Manali as she’s about to finish her lunch.{p}
                You take the time to grab a tray, pour yourself some spinach soup, sit next to her, and start talking about her department."

    abhay "I’ve heard it’s going well, congratulations."

    abhay "You’re doing a great job, handling the secretary, the security, and the transportation all together!"

    show manali smiling

    manali smiling "It’s Giti, Abhay Sir, she’s working so much, and she’s very efficient."

    abhay "It’s been what?{w=0.5} Three years now that she’s doing that?"

    narration "You drink a mouthful of soup, it’s cold already."

    manali smiling "Three years, Abhay Sir, and she never complains."

    abhay "Yet she’s never been promoted"

    show manali

    manali "...!"

    abhay "Manali, I will talk to M. Gopinath about it."

    narration "You take another spoon of soup, still looking at her, drink it with a grimace, and push the bowl aside on your tray."

    manali "You should, Sir, but he probably will not listen."

    abhay "And why is that?"

    manali "I don’t know, Sir, I just said that for no reason."

    abhay "Of course there's a reason, please tell me."

    manali "She’s got a very good position already, and maybe they don’t want to give her too much responsibilities because-"

    abhay "Because she's a woman?"

    show manali nervous

    manali nervous "I didn’t say that, Sir!"

    abhay "But you meant that."

    narration "She blushes."

    thinking "She did mean that."

    thinking "I have heard enough."

    $talk_manali = True

    if talk_priyanka:
        if not talk_bapat or not talk_donatello or not email_act_2:
            thinking "I could talke to Priyanka, keep investigating or take a decision."
        else:
            thinking "Priyanka's the only one left."
    else:
        thinking "I have talked to both Manali and Priyanka."

        if not talk_bapat or not talk_donatello or not email_act_2 or not talk_women:
            thinking "I could take a decision right now or keep investigating."
        else:
            thinking "I have done enough investigating, it's time to take a decision."

    menu:
        "Talk to Priyanka." if not talk_priyanka:
            jump .scene12
        "Keep investigating." if not talk_bapat or not talk_donatello if not email_act_2:
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
        "Write an email to M. Gopinath." if not email_act_2_2:
            jump .scene15
        "Ask M. Rajkumar's advice.":
            jump .scene16
        "Reject her request.":
            jump .scene17

label .scene14:
    window hide

    show bg office with dissolve

    narration "You call Giti to your office."

    show giti with dissolve

    narration "Once she's sat, you begin."

    abhay "I have decided to approve your promotion request, Giti."

    giti "...!"

    giti "T-Thank you, Abhay Sir."

    show giti smile

    giti smiling "Thank you, Abhay Sir, {b}thank you{/b}."

    abhay "*laughs*"

    abhay "About time, isn't it?{w=0.5} Things should change around here."

    giti "About time, Abhay Sir, about time, thank you."

    narration "When she leaves, you fall back into your chair, resting your head upon your hands above your neck."

    narration "Now, you’ll have to deal with the aftermath."

    menu:
        "The aftermath.":
            jump .scene18

label .scene15:
    window hide

    show bg office with dissolve
    narration "You write to M. Gopinath, asking him clearly and directly to take the matter into his hands so that you can escape the storm that will follow either decision you might take,
                receive an automatic out-of-the-office answer minutes later, and never hear about it again."

    window hide
    show mail_icon_blink

    pause

    hide mail_icon_blink
    show mail_icon_open

    $mail_gopinath(("I am currently on leave, enjoying the warm beaches of Diu Island. I will answer you as soon as I reach my office back.\n"
        "If you have any urgent matter, kindly write to Mr. Chandrakant at the following email: {color=#0000FF}{u}abhay.chandrakant@cryptaloo.in{/u}{/color}.\n"
        "\nBest regards,\nMr. Gopinath\n"
        "{font=fonts/Oswald-Regular.ttf}{size=14}{k=-1}{color=#009fff}Adnan Gopinath, Administrative Director{/color}{/k}{/size}\n"
        "{size=12}{k=-1}Pearls Omaxe Building, Off # 1005, 10th Floor, First Tower{/k}{/size}\n"
        "{size=12}{k=-1}Netaji Subhash Place Complex, Pitampura, Delhi 110034, INDIA{/k}{/size}{/font}"))

    hide mail_icon_open

    pause 3.0

    menu:
        "You really need to decide by yourself.":
            jump .decide

label .scene16:
    window hide

    show bg office with dissolve
    narration "You write to M. Rajkumar, the company’s Lawyer, and explain him the situation so that he can give you his advice."

    narration "He answers a few hours later."

    window hide
    show mail_icon_blink

    pause

    hide mail_icon_blink
    show mail_icon_open

    $mail_lawyer_act2_1(("Dear Mr. Chandrakant,\n\n"
        "If your Mrs. Shaikh Giti can prove the alleged discrimination she suffers {i}mutatis mutandis{/i}, the situation could lead to a case in court indeed, and involve liabilities, and damages as per the accessory of the main article to be continued {i}habeas corpus.{/i}\n"
        "In all actuality ({i}Ibid.{/i}), discrimination is very difficult to prove as she would require either several witnesses, or written proof of a constant pattern from the company’s side to support her claim."
        "Since she will find deprived of these proofs, it is most probable that she will not escalate as fees will discourage her from doing so as well.\n"
        "Unless you are certain that she has gathered said means of proof, I would advise to reject her plea, and act on the sole base of her professional merit and quality.\n"
        "Yours truly,\n"
        "Mr. Rajkumar\n\n"
        "Rajkumar & Rajkumar Ltd."))

    hide mail_icon_open

    pause 3.0

    

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
    window hide

    show bg none with fade
    narration "You’ve sent an email to inform everyone about Giti’s promotion, not forgetting to send a copy to M. Gopinath.{p}
                Bapat and Donatello, have stormed into your office several times since then, trying to prove their point, but you’re the HR Manager, and with M. Gopinath, and the new CEO away, there’s nothing they can do.{p}
                You surmise that M. Gopinath won’t be happy, and hope that the new CEO will understand your position. Time will tell."

    $act_2_ending_18 = True
    jump .end

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
        "Ask M. Rajkumar, The company's laywer, for his advice." if not email_act_2_3:
            jump .scene21
        "Ask M. Rajkumar for his advice again." if email_act_2_3:
            jump .scene21
        "Laugh and ignore the threat.":
            jump .scene22

label .scene20:
    narration "You call Giti to your office."

    show giti with dissolve

    narration "Once she's sat, you begin."

    abhay "I have decided to approve your promotion request, Giti."

    show giti angry

    giti angry "It's only fair, Abhay Sir."

    abhay "So you will drop this case, won’t you?"

    giti angry "Yes, Sir, I only want the promotion I should have had long ago."

    abhay "Well, you have it."

    abhay "Please send me the acknowledgement of cancellation for the case, and I will promote you as I said."

    giti angry "No, Abhay Sir, {w=0.5}you need to sign the promotion in counterpart with my Lawyer so that we are sure that it happens, and is registered."

    giti angry "At the same time, he will sign the cancellation in front of you, and provide you with the acknowledgement."

    thinking "She has obviously studied this."

    abhay "Okay, okay, kindly plan this meeting after working hours, and make it happen quick."

    menu:
        "The aftermath.":
            jump .scene18

label .scene21:
    narration "If there’s something the company’s Lawyer should be able to help you with, it’s dealing with a subpoena."

    narration "If you go to the court, he will be the one defending you after all."

    narration "You write him, explaining the situation, and joining a scanned copy of the subpoena. He answers almost immediately."


    $mail_lawyer_act2_2(("Dear Mr. Chandrakant,\n"
            "So far, all that we know is that Mrs. Shaikh Giti is suing the company on the basis of the Denial of Equal Opportunity. She says that she has collected proofs, but we have not seen these proofs as yet, and we might be in a position to challenge them if they seem weak.\n"
            "Only then will I know what our chances to win the trial are, and if they seem low, to open negotiations with her.\n"
            "If, from your position you can gather already that she will have a decent amount of solid proof, I advise you to promote her so that you can avoid paying for the damages she requests.\n"
            "If this isn’t the case, I advise you to proceed so that we can see what she has, and take appropriate action.\n\n"
            "Yours truly,\n"
            "M. Rajkumar\n"
            "Rajkumar & Rajkumar Ltd."))

    thinking "It's time to take my decision."

    menu:
        "Promote Giti.":
            jump .scene20
        "Ignore her.":
            jump .scene22

label .scene22:
    narration "You don’t even answer her. One simply doesn’t threaten the HR Manager."

label .scene23:
    window hide

    show bg none with fade

    narration "You can’t fire Giti because she sues the company, that in itself would open a whole new case against you so she stays, brooding, waiting for the trial.{p}
    The atmosphere of the office changes, there’s no more friendly banter now.{p}
    Bapat and Donatello are obviously on your side, you’re part of their gang now.{p}"

    narration "Surely, the new CEO will surely know how to handle a court case better than you, and everything will be fine again."

    $act_2_ending_23 = True

    jump .end

label .end:
    narration "Act 2 End"
    $act_2_completed = True

    window hide

    $renpy.call_screen("act_menu")

    return






















