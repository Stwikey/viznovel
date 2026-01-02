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
define voice = Character('v', color='#657aac')
define villager1 = Character ('npc1')

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
        player "there doesn't seem to be anyone here, and the more i look around the more i risk starvation or worse."
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
        v "stop! get away from me please, @#$%$. you said this would stop after you envaded "

        player "huh? who are you..."

        "you reach out for no one "
    
    label forest:
        # turn bg into some forest 
        "okay there seems to be a bunch creatures of some sort"
    
    label village: 
        "after wandering around for a while you discover theres a village, finally people!"

        #scene goes to you entering 
        npc1 "@#$%$ you're back? "

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

        player ""