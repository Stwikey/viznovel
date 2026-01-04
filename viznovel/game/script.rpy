''' 
summary 
you wake up having no past memories of your life, as you continue to adventure you 
realize that the people around you seem to already know you. you come to discover you are a dopple ganger! and your "other self"
is a super famous hero, but as you adventure you realize the true indentions of your "other self"
spoiler alert: ur other u is a morally grey person crazy! 
'''
#player character
define player = Character('player', color="#c8c8ff")

#npcs 
define v = Character('voice', color='#657aac')
define npc1 = Character ('npc1') #an old man
define npc2 = Character ('Charles')
define lil_boy = Character('fiz')
define thief = Character('theif')
define unknown = Character('???')

#crew 
define brennan = Character('brennan')

label start:
# scene open plains <- dont have image rn but just so u have idea 
    #start on a black screen and open as if eyes are opening 
    # put audio here as well like some peaceful music 

    player "*yawn* where am i?"
    
    "as you look around you realize that there isn't much of 
    anything to give you clues on where you could be "

    menu: 
        "look around and explore":
            jump explore

        "go back to sleep in hopes you regain your memories":
            jump sleep 
# player will find different bugs, something thats not existent irl (combos of animals scorpion beetle or something)
    label explore: 
        "sleep is for the weak!"
        "you spring up and begin looking around"
        player "there doesn't seem to be anyone here, and the more I look around the more i risk starvation or worse."
        menu: 
            "go into the forest":
                jump forest 

            "find civilization":
                jump village

# player has a dream and gathers information on their past 
    label sleep: 
        "you close your eyes and feel yourself drifting away"

        scene black
        with fade 

# note for later me to add player name 
        v "stop! get away from me please, PLACEHOLDER. you said this would stop after you invaded "

        player "huh? who are you..."

        "you reach out for no one "
    

    #MC meets a stranger in the forest, they act like they know you but you have no memory of them
    label forest:
        # turn bg into some forest 
        "You walk through the forest, unsure where you are travelling to."

        "You look around, hoping to identify some kind of landmark that can indetify this place."

        "As you step, insects scurry across, their form indescribable."

        player "okay, there seems to be a bunch creatures of some sort."

        "A voice cuts through the forest."

        v "PLACEHOLDER!!!!"

        "A shadow rushes through the trees."

        unknown "oh how i've MISSED YOU!"

        "The girl hugs you and you jump back in shock."

        menu:
            "do I know you?":
                jump question
            "stay silent":
                jump silent

    # if MC acts like they dont know her, she gets suspicious
    label question:
        "A hint of suspicion flickers over the girl's face, too quick to notice."
        
        unknown "oh comeee on! Are you seriously pretending to not know me? After all we've been through?"

        player "uhhh yeah, can you get off me now? I'm a busy man."

        "UNKNOWN steps back."

        unknown "ah, I see how it is. This is one of your silly pranks again huh?" #idk how to end this

        unknown "well I'll be off on my way then."

        "UNKNOWN leaps away into the bushes." 

        player "what an odd interaction."

        "You exit the forest."

        jump forest_end

    # she gets less suspisious maybe
    label silent:
        "..."

        unknown "heyyyyyy did you hear meee???"

        "You continue to stay silent, after all, yo mama told you not to talk to strangers."

        "after a while, UNKNOWN grows frustrated and disappears in a flash"

        "The rustles in the bushes grow quieter and she prances away."

        jump forest_end

    
    label forest_end:
        #cut back to unknown

        unknown "somethings off... PLACEHOLDER should've noticed when I tried to rob him earlier"

        unknown "his biceps have also gotten skinnier..."

        player "that was... interesting, i should turn back and head to a village"

        jump village


    label village: 
        "after wandering around for a while you discover theres a village, finally people!"

        #scene goes to you entering 
        npc1 "PLACEHOLDER you're back? "

        player "*i can't hear what name he's saying, its like its static or something*"

        "i don't know what to do..."
        
        menu: 
            "act natural":
                jump natural 

            "freak out":
                jump freak 
        # both natural and freak out path lead to the same conclusion of the guy just brushing you off and you learn about ur characters lore
    label natural: 
        player "haha yeah! it was difficult...? or easy...? you know, obviously because you've been expecting me"

        npc1 "you are always the prankster huh?"
        
        player "yep! you know me obviously! speaking of know... do you know where my friends are?"

        npc1 "friends? you never had friends."

        player "right! i hate all of you!"

        "there's something up with the people here..."

        npc1 "you seem to be acting weird, are you sure your okay?"

        player "yeah, just peachy."
        
        show npc1 scary looking 
        npc1 "i hope you don't forget your allies. especially after your success..."

        jump part_2

    label freak: 
        player "who are you how do you know me?"

        "you pick up the old man by the shoulders"
        
        show npc1 shocked 

        npc1 "please calm down, i don't know what is wrong with you but..."

        show npc1 angry scary looking 

        npc1 "you need to control yourself."

        npc1 "you saved the village and we are forever indebted to you... but i heed you to remember where you drew all that power from." #spelling? idk

        "you feel your heart race, just what in the world did the person before you do?"

        player "right..."

        show npc1 happy

        npc1 "i'm glad we've come to an understanding!"

        jump part_2
    
    # more exploration of the village, getting a feel for how people react to you as a person
    label part_2: 
        player "he was... odd"

        unknown "PLACEHOLDER I KNEW YOU COULD DO IT!"

        "a little boy's voice calls out from the distance as footsteps rapidly approach you."

        player "huh...?"

        show lil_boy happy
        unknown "TELL ME EVERYTHING! did you get me the gift you promised? or did you forget me?"

        show lil_boy sad 

        "you stand still trying to piece together what is happening..."

        #want lil boy to fade into the background while the player is thinking 

        "the people in this village all seem to revere you as some unsung hero of their time."

        "but that old guy from earlier, he seems to have it out for you? or maybe he's here to help."

        "what allies could i have that i must remember?"

        "i must've lost my memories in the adventure i was in"

        "i'm not sure who these people are but they must be important to me... or to the old me at the very least"

        "elsewhere..."

        npc1 "he seems... different Charles."

        npc2 "you worry too much old man, he's probably scattered from the mission. afterall if he's back that means..."

        npc1 "they won't be an issue anymore." #bold the word they later 

        "back to you" #lmao put better transistion here haha

        player "yeah, i'm sorry i'm just tired from... where i've been. because i go places. i'm sorry fiz."

        "huh... how did i know his name?"

        "it's like something is pushing me find what information i'm missing..."

        lil_boy "thats okay! just make sure to remember next time, i'm just happy you made it back safely."

        lil_boy "you stopped answering my messages, and i couldn't get my friend to scry on you either. i thought you..." 

        "fiz pauses as he starts tearing up." 

        "he runs to your waist as he engulphs you in a hug." #spelling

        player "i'm sorry. i promise i won't scare you like that again."

        show lil_boy playfully angry 
        lil_boy "you better not."

        show npc1 lightly scolding
        npc1 "okay fiz, leave the young adventurer alone. he has to rest as well."
        
        show lil_boy 
        lil_boy "okay fine... but you better come visit me soon!"

        hide lil_boy
        jump home

        #MC returns back to "his" house 
    label home: 
        player "i don't understand what is happening."

        player "the people here seem to like me. but i can't help but feel unsettled."

    #MC can choose to rummage around for clues or to look but not touch, 1 allows him to discover more but higher chance of suspicion while other not as much but no sus
        menu: 
            "rumamge through the drawers with no regard for cleanliness":
                jump reckless
            
            "leave everything untouched, but look around for clues.":
                jump careful

# this point onward there will be alternate pathways i think will figure out how to remember things later! 
    label reckless: 
        "you search through the house, opening drawers and " #cant thing right now fix later!!!!
        # main idea finds 
        # finds photos of "him" and a crew
        # finds documents that explain the exact mission he was sent on 
        #house is left messy will impact pt 3 gameplay 

    label careful: 
        #fill in later 
        # main idea finds: 
        # finds photo of him and his crew 

    label part_3: 
        "it's becoming late in the night"
        # MC sleeps but has dreams 
        "PLACEHOLDER, this is stupid. why do you insist on killing yourself for this mission it's not worth it!"
        v "i have to. PLACEHOLDER2 needs us, they ALL need us."

        "but you do it at the expense of ######"

        v "i'm sorry, but it must be done." 

        "you wake up in a cold sweat." 

        player "what was that?"

        "you rub your eyes, attempting to wake up more."

        "suddenly a knock at the door, makes you jump."

        "*KNOCK KNOCK KNOCK*"

        unknown "PLACEHOLDER I KNOW YOU'RE IN THERE!"

        unknown "I CAN'T BELIEVE YOU CAME BACK AND DIDN'T TELL ANY OF US! WE HAD TO FIND OUT THROUGH FIZ!"

        #meeting the orginal mcs crew eof adventurers 
        show brennan
        "you rush to the door, opening it to find a group of people you recognize from the photo. this must have been your crew."

        # this is different pathways comes into affect 
        # if player chose to be messy then brennan will notice immediately 
        # if player chose the sneaky looking then brennan will continue like nothing happened 

# place this in the sections later, going to learn this later 
        ''' 
        
        '''
    
