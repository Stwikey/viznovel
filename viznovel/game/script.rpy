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
define villager1 = Character ('npc1')
define thief = Character('theif')
define unknown = Character('???')

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


    label village: 
        "after wandering around for a while you discover theres a village, finally people!"

        #scene goes to you entering 
        villager1 "PLACEHOLDER you're back? "

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

        villager1 "you are always the prankster huh?"
        
        player "yep! you know me obviously! speaking of know... do you know where my friends are?"

        villager1 "friends? you never had friends."

        player ""