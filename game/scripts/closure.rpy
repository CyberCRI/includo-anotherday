
label closure:
    narration "The big day has finally come."

    narration "You're all gathered together, fidgeting as you wait for Ashwini, your new CEO, to step in."

    narration "You can't help forming a picture in your mind, an ideal of what CEOs are, and how they should behave, dress, and speak.
                This one especially comes straight from the international headquarters.
                Modern, business-oriented, with a low loud voice, you think."

    narration "You're all nervous, of course, since there's much at stake. In one sweep of the hand, a CEO could kick Bapat, Giti, or yourself."

    narration "You've taken a lot of decisions lately, changed a lot of things for good, or for worse, and you feel like your fate is hanging in the balance."

    narration "You see M. Gopinath from the corner of your eye, wearing a brand new tan like a new suit, white teeth out like a ravenous tiger, and you wonder where he's been all this time."

    narration " Everybody stands up as the door opens, staring at the makeshift stage, and at the microphone. A middle-aged woman in a sari steps in, smiling."

    bapat "False alert!"

    narration "Bapat says this as he sits down, but the woman stares at him, stone cold, and walks straight to the microphone. Bapat stands up, sweating profusely as the woman starts to speak."

    thinking "{i}Ashwini{/i}, of course!"

    thinking "Ashwini, why on Earth did I think the CEO was a man ?!"

    ashwini "Good morning everybody. My name is Ashwini Baghyashree."

    ashwini "I am very happy to see you all gathered here today, as CRYPTALOO India is entering a new phase with the full support and guidance of our International Headquarters."

    ashwini "Having worked here for many years, you have paved the ground for CRYPTALOO's future successes, and will play an important role in the developments to come."

    ashwini "For this, I want to thank you all."

    narration "She pauses. Everybody applauses. You wonder what's coming next."

    ashwini "I am here to take CRYPTALOO India to the next level with the planned extension of four offices around the country, and to help CRYPTALOO India to enter the global market, and culture."

    ashwini "I have followed the recent developments of the past weeks, and I must say that as far as global culture is concerned, I have been surprised!"

    if act_1_ending_14 == True or act_1_ending_33 == True:
        ashwini "I was saddened to learn that a woman could be shamed in your office without any reaction from its head management."

        ashwini "By laying the fault on Priyanka, or letting it happen, you have actually taken sides with the harassers against the victim."

        ashwini "This is not how the culture can change, and this casts a bad light on the company in general."
    elif act_1_ending_31 == True or act_1_ending_32 == True:
        narration "Ashwini looks at you straight in the eyes, and speaks."

        ashwini "M. Chandrakant, I know that you did what you thought was right, but you're not the company's psychologist."

        ashwini "And trying to meddle with the employee’s private life as you did when Priyanka was having troubles didn't help to solve the situation{w=0.25}, to say the least."

        ashwini "We can't confuse private and professional life, or let people take advantage of private informations."

        narration "She looks at Bapat sideways, and continues."

        ashwini "In that case, you should have reported the situation, ensured Priyanka of your support, and taken a firm action to stop the shaming she was facing."
    elif act_1_ending_34 == True:
        ashwini "I must say I'm impressed, M. Chandrakant."

        ashwini "Not only did you resolve the situation caused by Priyanka's shaming by implementing a dress code that can’t be disputed since it applies to all of CRYPTALOO’s branches,"

        ashwini "But you have also laid the ground for future policies towards inclusiveness, and tolerance masterfully!"
    else:
        "<Error: Act 1 Ending Missing>"

    if act_2_ending_18 == True:
        ashwini "On another subject, I am happy to see that Giti has been promoted."

        ashwini "It was about time Madam Shaikh was rewarded for her efforts, and takes on more responsibilities with us."

        ashwini "Too long have we seen people thriving on titles, and positions, while the groundwork was done by someone else, this needs to change."
    elif act_2_ending_23 == True:
        ashwini "Unfortunately, we now have a lawsuit on our hands because you didn't hear Madam Shaikh's legitimate request out, M. Chandrakant."

        ashwini "If I'm not mistaken, she was leading the Transportation Department in addition to her job, and took many responsibilities that weren't her own."

        ashwini "Why would you ignore her request for a promotion, was it undeserved?"

        "I-I{w=0.25}, err-{w=0.25}, I wasn't,{w=0.25} I don't know."

        ashwini "Yes, I know you don't know, M. Chandrakant, because you didn't consider her situation, or her value for the company, and now I must defuse this trial."
    else:
        "<Error: Act 2 Ending Missing>"

    if act_3_ending_10 == True:
        ashwini "This being said, I have been informed of an employee of this company, who had to face a difficult situation because of his sexual orientation."

        ashwini "While I support and endorse your views on inclusiveness on this matter, M. Chandrakant, the way you've dealt with the employees' reactions to this situation was rather harsh, even repressive."

        ashwini "Since this is a delicate matter, you should have tried to listen more, and gradually bring the employees over to your views instead of punishing them, and reinforcing their prejudices."

        ashwini "That wasn't very skillful, M. Chandrakant, and I withdraw the collective warning you have issued at that time."
    elif act_3_ending_13 == True:
        ashwini "This being said, I have been informed of an employee of this company, who had to face a difficult situation because of his sexual orientation."

        ashwini "I am well aware that this was a delicate situation, but the least you could have done, M. Chandrakant, was to provide him with your support and understanding instead of howling with the wolves."

        ashwini "I am truly disappointed."
    elif act_3_ending_28 == True:
        ashwini "This being said, I have been informed of the situation of an employee of this company, who had to face a difficult situation because of his sexual orientation."

        ashwini "You have surprised me, M. Chandrakant, I must say, when you decided to apply the international policy to our Indian branch."

        ashwini "It wasn't your call to establish a new policy all by yourself though I understand you did it to defuse a potentially disruptive situation.{w=0.25}  I appreciate your efforts."

        ashwini "I still need time to consider how to apply the international policy to our branch,"

        ashwini "But in the meantime I assure all of you that no employee will be discriminated against in this company for his sexual orientation."
    else:
        "<Error: Act 3 Ending Missing>"

    if act_4_ending_10 == True:
        ashwini "Last but not least, I must remind you, M. Chandrakant, that India is a secular country!"

        ashwini "How on Earth did you come to the conclusion that you could fire an employee because she wouldn't want to participate to a religious ceremony?"

        ashwini "This is not a temple, this is a corporate office!"

        ashwini "An individual's religion shouldn't matter at the office, and if we believe in our Constitution, it shouldn't even matter anywhere in India!"
    elif act_4_ending_25 == True:
        ashwini "Last but not least, I wonder why you didn't accept to give your employees a room for their prayers, M. Chandrakant?"

        ashwini "Is that because you think that religion should have no say at all in the company?"

        ashwini "If this is the case, then why is the shrine still in the entrance?"

        ashwini "It's either all or none, M. Chandrakant, we can't pick and choose, and force our individual beliefs on others."
    elif act_4_ending_26 == True or act_4_ending_28 == True:
        ashwini "Last but not least, I must say that I approve your giving the employees a space for their prayers, M. Chandrakant."

        ashwini "We all work in the same company, but are different people, and we need to welcome everyone as they are regardless of their faith."
    else:
        "<Error: Act 4 Ending Missing>"

    menu:
        "The Conclusion.":
            jump .ending

label .ending:
    ashwini "As you all can see, our small family is changing, and expanding."

    ashwini "This means that there will be new opportunities for all of you, and new ways of working together."

    ashwini "Some of you will feel pushed, and will resent the changes, while others will embrace them."

    ashwini "I want to let you know that I will always be available to listen to you, to help, and to support you."

    ashwini "In order to prove these words, I am not taking any action today except for one."

    ashwini "Change is a process, it takes time and understanding, and I will give you plenty of those so that you can adjust and determine by yourself how to cope with these changes and new work environment."

    narration "You raise your hand."

    "Madam, you said you would take one action, which is it?"

    ashwini "Oh yes, that."

    ashwini "M. Gopinath, can you step forward please?"

    narration "M. Gopinath seems surprised, and moves forward."

    ashwini "Where were you all this time? {w=0.25}Why didn't you answer your emails?"

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
    ashwini "You have managed to achieve the feat of getting the company sued, an employee quitting, and to change dramatically the atmosphere for the worst in just one week."

    ashwini "I must say I didn’t think it was possible to be lacking empathy to this extent."

    ashwini "With M. Gopinath away, you had an opportunity to show what you were capable of, and, well, you did."

    thinking "Wrong. Wrong. Wrong. I got it all wrong!"

    narration "You thought that you would be congratulated for your hard but necessary decisions, and it sure looks like you’re not going to be."

    ashwini "I will try to connect with Giti, and to offer her to become our new Human Resources Manager."

    ashwini "It’s been a long time she should have been promoted."

    thinking "{i}What!{/i}"

    ashwini "If you accept, you can be her assistant, M. Chandrakant{w=0.25}, maybe you’ll learn from her."

    ashwini "If it doesn’t suit you, you’re free to resign."

    thinking "{i}Just.{w=1} Like.{w=1} That.{/i}"

    narration "You redden with anger, and prepare yourself to answer this infamy when the thought hits you like a bullet:{p}
    {\i}What if she has a point?{w=0.5} What if you stayed indeed?{w=0.5} That would be a whole new story, yet to be written."

    return

label .good_ending:
    ashwini "With M. Gopinath away, and myself still abroad, the fate of the whole Indian branch was lying upon your shoulders, M. Chandrakant."

    ashwini "Weaker, less resolute men would have left the situations to fester, and waited for my coming, but this is not what you did."

    ashwini "Instead, you took upon you to solve everything as you could, listened to everyone, and tried to find the most inclusive solutions with an open mind."

    narration "You blush."

    "T-That's only-"

    ashwini "I am very impressed, and happy to see such qualities of both management, and empathy, in you."

    ashwini "For this reason, I would like to offer you M. Gopinath’s position in this branch, and to commend you for management training sessions at our International Headquarters."

    narration "You feel a bit tipsy, and a bit proud. Just a week ago, you were reaching the office with a pang of anxiety, knowing that you would be the one in charge, and now it seems that you’ve been successful all the way."

    thinking "{i}Administrative Director? Me?{/i}"

    ashwini "M. Chandrakant?"

    narration "She was talking while you were trying to make sense out of her words."

    "Yes, Madam?"

    ashwini "I've asked you a question, {w=0.25}do you accept this position?"

    "YES!"

    "YES, MADAM!"

    narration "And everybody laughs."

label .mixed_ending:
    ashwini "You did what you could, M. Chandrakant."

    ashwini "I know that you were alone in here with M. Gopinath on leave, and myself away. I know that it wasn’t easy."

    "Yes, Madam.{w=0.25} I did my best, and-"

    ashwini "Your best wasn’t enough, M. Chandrakant, because I now have to deal with the aftermath of all this in spite of the good decisions you have taken here and there."

    "Yes, Madam..."

    narration "You blush."

    ashwini "Since I’m here now, I am confident that these mistakes can be corrected,"

    ashwini "And that we can proceed together without leaving any of us on the side of the road{w=0.25}, not even you M. Chandrakant."

    ashwini "But you will need to learn."

    "I will, Madam, I promise, you'll see-"

    ashwini "This is a story that remains to be written. M. Chandrakant."













