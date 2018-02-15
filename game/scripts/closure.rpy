
label closure:
    $show_quick_menu = True
    
    window hide

    scene bg none with dissolve 

    stop music fadeout 1.0

    stop background fadeout 1.0

    $renpy.pause(3.0)

    scene bg closure_empty with dissolve 

    play music "music/Kai_Engel_Brand_New_World.ogg" fadein 1.0 fadeout 1.0

    narration "The big day has finally come."

    narration "You're all gathered together, fidgeting as you wait for Ashwini, your new CEO, to step in."

    play background "music/closure_crowd.ogg" fadein 3.0

    narration "You can't help forming a picture in your mind, an ideal of what CEOs are, and how they should behave, dress, and speak.
                This one especially comes straight from the international headquarters.
                Modern, business-oriented, with a low loud voice, you think."

    narration "You're all nervous, of course, since there's much at stake. In one sweep of the hand, a CEO could kick Bapat, Giti, or yourself."

    narration "You've taken a lot of decisions lately, changed a lot of things for good, or for worse, and you feel like your fate is hanging in the balance."

    narration "You see M. Gopinath from the corner of your eye, wearing a brand new tan like a new suit, white teeth out like a ravenous tiger, and you wonder where he's been all this time."

    show bg closure_ashwini

    narration "Everybody stands up as the door opens, staring at the makeshift stage, and at the microphone. A middle-aged woman in a sari steps in, smiling."

    show bapat at center, talking
    with dissolve

    bapat "False alert!"

    hide bapat with dissolve

    narration "Bapat says this as he sits down, but the woman stares at him, stone cold, and walks straight to the microphone. Bapat stands up, sweating profusely as the woman starts to speak."

    play background "music/applause.wav" fadein 3.0 noloop

    show ashwini dark at not_talking, center_left
    with Dissolve (3.0)

    thinking "{i}Ashwini{/i}, of course!"

    thinking "Ashwini, why on Earth did I think the CEO was a man?!"

    show ashwini smiling at talking

    ashwini "Good morning everybody. My name is Ashwini Baghyashree."

    ashwini "I am very happy to see you all gathered here today,"

    ashwini "As CRYPTALOO India is entering a new phase with the full support and guidance of our International Headquarters."

    show ashwini
    with dissolve

    ashwini "Having worked here for many years, you have paved the ground for CRYPTALOO's future successes."

    ashwini "And will play an important role in the developments to come."

    show ashwini smiling
    with dissolve

    ashwini "For this, I want to thank you all."

    narration "She pauses. You wonder what's coming next."

    ashwini "I am here to take CRYPTALOO India to the next level with the planned extension of four offices around the country,"

    ashwini "And to help CRYPTALOO India to enter the global market, and culture."

    ashwini "I have followed the recent developments of the past weeks, and I must say that as far as global culture is concerned, I have been surprised!"

    if act_1_ending_14 == True or act_1_ending_33 == True:
        show ashwini disappointed
        with dissolve

        ashwini disappointed "I was saddened to learn that a woman could be shamed in your office without any reaction from its head management."

        ashwini disappointed "By laying the fault on Priyanka, or letting it happen, you have actually taken sides with the harassers against the victim."

        ashwini disappointed "This is not how the culture can change, and this casts a bad light on the company in general."
    elif act_1_ending_31 == True or act_1_ending_32 == True:
        narration "Ashwini looks at you straight in the eyes, and speaks."

        ashwini "M. Chandrakant, I know that you did what you thought was right, but you're not the company's psychologist."

        ashwini disappointed "And trying to meddle with the employee’s private life as you did when Priyanka was having troubles didn't help to solve the situation{w=0.25}, to say the least."

        ashwini "We can't confuse private and professional life, or let people take advantage of private informations."

        narration "She looks at Bapat sideways, and continues."

        ashwini "In that case, you should have reported the situation, ensured Priyanka of your support, and taken a firm action to stop the shaming she was facing."
    elif act_1_ending_34 == True:
        show ashwini smiling
        with dissolve

        ashwini "I must say I'm impressed, M. Chandrakant."

        ashwini "Not only did you resolve the situation caused by Priyanka's shaming by implementing a dress code that can’t be disputed since it applies to all of CRYPTALOO’s branches,"

        ashwini "But you have also laid the ground for future policies towards inclusiveness, and tolerance masterfully!"
    else:
        "<Error: Act 1 Ending Missing>"

    if act_2_ending_18 == True:
        show ashwini smiling
        with dissolve

        ashwini smiling "On another subject, I am happy to see that Giti has been promoted."

        show ashwini
        with dissolve

        ashwini "It was about time Madam Shaikh was rewarded for her efforts, and takes on more responsibilities with us."

        ashwini "Too long have we seen people thriving on titles, and positions, while the groundwork was done by someone else, this needs to change."
    elif act_2_ending_23 == True:
        show ashwini disappointed
        with dissolve

        ashwini disappointed "Unfortunately, we now have a lawsuit on our hands because you didn't hear Madam Shaikh's legitimate request out, M. Chandrakant."

        show ashwini
        with dissolve

        ashwini "If I'm not mistaken, she was leading the Transportation Department in addition to her job, and took many responsibilities that weren't her own."

        show ashwini disappointed
        with dissolve

        ashwini "Why would you ignore her request for a promotion, was it undeserved?"

        show ashwini dark at not_talking

        abhay "I-I{w=0.25}, err-{w=0.25}, I wasn't,{w=0.25} I don't know."

        show ashwini disappointed at talking

        ashwini disappointed "Yes, I know you don't know, M. Chandrakant, because you didn't consider her situation, or her value for the company, and now I must defuse this trial."
    else:
        "<Error: Act 2 Ending Missing>"

    if act_3_ending_10 == True:
        show ashwini
        with dissolve

        ashwini "This being said, I have been informed of an employee of this company, who had to face a difficult situation because of his sexual orientation."

        ashwini "While I support and endorse your views on inclusiveness on this matter, M. Chandrakant..."

        show ashwini disappointed
        with dissolve

        ashwini disappointed "The way you've dealt with the employees' reactions to this situation was rather harsh, even repressive."

        ashwini disappointed "Since this is a delicate matter, you should have tried to listen more, and gradually bring the employees over to your views, "

        ashwini disappointed "Instead of punishing them, and reinforcing their prejudices."

        ashwini disappointed "That wasn't very skillful, M. Chandrakant, and I withdraw the collective warning you have issued at that time."
    elif act_3_ending_13 == True:
        show ashwini disappointed
        with dissolve

        ashwini disappointed "This being said, I have been informed of an employee of this company, who had to face a difficult situation because of his sexual orientation."

        ashwini disappointed "I am well aware that this was a delicate situation."

        ashwini disappointed "But the least you could have done, M. Chandrakant, was to provide him with your support and understanding instead of howling with the wolves."

        ashwini disappointed "I am truly disappointed."
    elif act_3_ending_28 == True:
        show ashwini
        with dissolve

        ashwini "This being said, I have been informed of the situation of an employee of this company, who had to face a difficult situation because of his sexual orientation."

        show ashwini smiling
        with dissolve

        ashwini smiling "You have surprised me, M. Chandrakant, I must say, when you decided to apply the international policy to our Indian branch."

        show ashwini
        with dissolve

        ashwini "It wasn't your call to establish a new policy all by yourself though I understand you did it to defuse a potentially disruptive situation."

        show ashwini smiling
        with dissolve

        ashwini smiling "I appreciate your efforts."

        show ashwini
        with dissolve

        ashwini "I still need time to consider how to apply the international policy to our branch..."

        ashwini "...But in the meantime I assure all of you that no employee will be discriminated against in this company for his sexual orientation."
    else:
        "<Error: Act 3 Ending Missing>"

    if act_4_ending_10 == True:
        show ashwini disappointed
        with dissolve

        ashwini "Last but not least, I must remind you, M. Chandrakant, that India is a secular country!"

        show ashwini
        with dissolve

        ashwini "How on Earth did you come to the conclusion..."

        ashwini "...That you could fire an employee because she wouldn't want to participate to a religious ceremony?"

        ashwini "This is not a temple, this is a corporate office!"

        ashwini "An individual's religion shouldn't matter at the office, and if we believe in our Constitution, it shouldn't even matter anywhere in India!"
    elif act_4_ending_25 == True:
        show ashwini
        with dissolve

        ashwini "Last but not least, I wonder why you didn't accept to give your employees a room for their prayers, M. Chandrakant?"

        ashwini "Is that because you think that religion should have no say at all in the company?"

        show ashwini disappointed
        with dissolve

        ashwini disappointed "If this is the case, then why is the shrine still in the entrance?"

        show ashwini
        with dissolve

        ashwini "It's either all or none, M. Chandrakant, we can't pick and choose, and force our individual beliefs on others."
    elif act_4_ending_26 == True or act_4_ending_28 == True:
        show ashwini
        with dissolve

        ashwini "Last but not least, I must say that I approve your giving the employees a space for their prayers, M. Chandrakant."

        show ashwini smiling
        with dissolve

        ashwini smiling "We all work in the same company, but are different people, and we need to welcome everyone as they are regardless of their faith."
    else:
        "<Error: Act 4 Ending Missing>"

    menu:
        "The Conclusion.":
            jump .ending

label .ending:
    show ashwini
    with dissolve 

    ashwini "As you all can see, our small family is changing, and expanding."

    ashwini "This means that there will be new opportunities for all of you, and new ways of working together."

    ashwini "Some of you will feel pushed, and will resent the changes, while others will embrace them."

    show ashwini smiling
    with dissolve

    ashwini smiling "I want to let you know that I will always be available to listen to you, to help, and to support you."

    show ashwini
    with dissolve

    ashwini "In order to prove these words, I am not taking any action today except for one."

    ashwini "Change is a process, it takes time and understanding, "

    ashwini "And I will give you plenty of those so that you can adjust and determine by yourself how to cope with these changes and new work environment."

    narration "You raise your hand."

    show ashwini dark at not_talking

    abhay "Madam, you said you would take one action, which is it?"

    show ashwini at talking

    ashwini "Oh yes, that."

    ashwini "M. Gopinath, can you step forward please?"

    narration "M. Gopinath seems surprised, and moves forward."

    ashwini "Where were you all this time?{w=0.5} Why didn't you answer your emails?"

    show ashwini disappointed
    with dissolve

    ashwini "You know that you were supposed to be back last week, didn't you?"

    narration "M. Gopinath blushes, and growls something that you can't hear."

    ashwini "You are fired, M. Gopinath."

    pause 2

    

    thinking "I see."

    thinking "Kind words, and a display of power, times are going to be interesting."

    ashwini "M. Chandrakant, I have a few words for you as well."

    show ashwini with dissolve

    if (act_1_ending_14 == True or act_1_ending_33 == True) and act_2_ending_23 == True and act_3_ending_13 == True and act_4_ending_10 == True:
        jump .bad_ending
    elif act_1_ending_34 == True and act_2_ending_18 == True and act_3_ending_28 == True and (act_4_ending_26 == True and act_4_ending_28 == True):
        jump .good_ending
    else:
        jump .mixed_ending

label .bad_ending:
    show ashwini disappointed
    with dissolve

    ashwini disappointed "You have managed to achieve the feat of getting the company sued, an employee quitting, "

    ashwini disappointed "And to change dramatically the atmosphere for the worst in just one week."

    ashwini disappointed "I must say I didn’t think it was possible to be lacking empathy to this extent."

    ashwini disappointed "With M. Gopinath away, you had an opportunity to show what you were capable of, and, well, you did."

    show ashwini
    with dissolve

    

    thinking "Wrong. Wrong. Wrong. I got it all wrong!"

    narration "You thought that you would be congratulated for your hard but necessary decisions, and it sure looks like you’re not going to be."

    ashwini "I will try to connect with Giti, and to offer her to become our new Human Resources Manager."

    ashwini "It’s been a long time she should have been promoted."

    

    thinking "{i}What!{/i}"

    show ashwini smiling
    with dissolve

    ashwini smiling "If you accept, you can be her assistant, M. Chandrakant{w=0.25}, maybe you’ll learn from her."

    show ashwini
    with dissolve

    ashwini "If it doesn’t suit you, you’re free to resign."

    

    thinking "{i}Just.{w=1} Like.{w=1} That.{/i}"

    narration "You redden with anger, and prepare yourself to answer this infamy when the thought hits you like a bullet:{p}
    {\i}What if she has a point?{w=0.5} What if you stayed indeed?{w=0.5}{i} That would be a whole new story, yet to be written."

    jump .end

label .good_ending:
    ashwini "With M. Gopinath away, and myself still abroad, the fate of the whole Indian branch was lying upon your shoulders, M. Chandrakant."

    ashwini "Weaker, less resolute men would have left the situations to fester, and waited for my coming."

    show ashwini smiling
    with dissolve

    ashwini smiling "But this is not what you did."

    ashwini smiling "Instead, you took upon you to solve everything as you could, listened to everyone, and tried to find the most inclusive solutions with an open mind."

    show ashwini smiling dark at not_talking

    narration "You blush."

    abhay "T-That's only-"

    show ashwini smiling at talking

    ashwini smiling "I am very impressed, and happy to see such qualities of both management, and empathy, in you."

    ashwini smiling "For this reason, I would like to offer you M. Gopinath’s position in this branch,"

    ashwini smiling "And to commend you for management training sessions at our International Headquarters."

    show ashwini smiling dark at not_talking

    show ashwini dark with dissolve

    narration "You feel a bit tipsy, and a bit proud. Just a week ago, you were reaching the office with a pang of anxiety, knowing that you would be the one in charge, and now it seems that you’ve been successful all the way."

    thinking "{i}Administrative Director?{w=1} Me?{/i}"

    show ashwini at talking

    ashwini "M. Chandrakant?"

    narration "She was talking while you were trying to make sense out of her words."

    show ashwini dark at not_talking

    abhay "Yes, Madam?"

    show ashwini smiling dark
    with dissolve

    show ashwini smiling at talking

    ashwini "I've asked you a question, {w=0.25}do you accept this position?"

    show ashwini smiling dark at not_talking

    abhay "YES!"

    abhay "YES, MADAM!"

    narration "And everybody laughs."

    jump .end

label .mixed_ending:
    ashwini "You did what you could, M. Chandrakant."

    ashwini "I know that you were alone in here with M. Gopinath on leave, and myself away. I know that it wasn’t easy."

    show ashwini dark at not_talking

    abhay "Yes, Madam.{w=0.25} I did my best, and-"

    show ashwini at talking

    ashwini "Your best wasn’t enough, M. Chandrakant."

    ashwini "Because I now have to deal with the aftermath of all this in spite of the good decisions you have taken here and there."

    show ashwini dark at not_talking

    abhay "Yes, Madam..."

    narration "You blush."

    show ashwini at talking

    ashwini "Since I’m here now, I am confident that these mistakes can be corrected."

    ashwini "And that we can proceed together without leaving any of us on the side of the road{w=0.25}, not even you M. Chandrakant."

    ashwini "But you will need to learn."

    show ashwini at not_talking

    abhay "I will, Madam, I promise, you'll see-"

    show ashwini at talking 

    ashwini smiling "This is a story that remains to be written. M. Chandrakant."

    jump .end

label .end:
    hide ashwini with dissolve

    show bg none with Dissolve(3.0)
    
    narration "CRYPTALOO - Another Day End"

    $renpy.hide("narration_background")

    show bg end_game with Dissolve(3.0)

    pause


    return













