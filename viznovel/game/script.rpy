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
default messy = False
default trust_level = 0

#crew 
define brennan = Character('brennan')
#a carefree guy who cares about his adventuring party a lot, knows the orginal character the best and loves food
#flaw is that he is often reckless and thinks with his heart instead of his brain
define maryanne = Character('maryanne')
#genuinely doesnt really care about anything, super indifferent, the first to figure out you are the dopple ganger but because you dont cause trouble she doesnt care only cares about playing games
#flaw is that she cares but hides it so people think she lowkey heartlessss 
define annie = Character('annie')
#anxious girl who was worried when you lost contact with them all suddenly, worries about the party a lot and often 
#overly worries about things, leading to delayed actions during important moments
define lou = Character('lou') 
#keeps a level head for the party (keeps everyone in line)
#overly critical of others, and thinks with his brain and often ignores feelings 

#unknown labels 
define unknown_brennan = Character('???',color = '#e9535311')
define unknown_maryanne = Character('???',color = '#784cd811')
define unknown_annie = Character('???',color = '#3bb91f11')
define unknown_lou = Character('???',color = '#b11f1f11')

label start:
# scene open plains <- dont have image rn but just so u have idea 
    #start on a black screen and open as if eyes are opening 
    # put audio here as well like some peaceful music 

    player "*yawn* where am i?"
    
    "as you look around you realize that there isn't much of anything to give you clues on where you could be."

    "you try to recall your own name to no avail, you can't seem to remember anything other than what you find on your person."

    show notebook
    "a notebook with messy scrawled on writing with symbols you can't seem to read." #yk like hyroglphs and stuff like that! 

    "without any other clues you must decide your next choice of action."
    hide notebook

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

    unknown "hey~ did you hear meee???"

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

    player "*I can't hear what name he's saying, its like its static or something*"

    "I don't know what to do..."
    
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

    npc2 "you worry too much old man, he's probably scattered from the mission. after all, if he's back that means..."

    npc1 "they won't be an issue anymore." #bold the word they later 

    "back to you" #lmao put better transistion here haha

    player "yeah, i'm sorry i'm just tired from... where i've been. because i go places. i'm sorry fiz."

    "huh... how did i know his name?"

    "it's like something is pushing me find what information i'm missing..."

    lil_boy "thats okay! just make sure to remember next time, i'm just happy you made it back safely."

    lil_boy "you stopped answering my messages, and i couldn't get my friend to scry on you either. i thought you..." 

    "fiz pauses as he starts tearing up." 

    "he runs to your waist as he engulfs you in a hug." #spelling

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
    "At your home..."

    player "i don't understand what is happening."

    player "the people here seem to like me. but i can't help but feel unsettled."

#MC can choose to rummage around for clues or to look but not touch, 1 allows him to discover more but higher chance of suspicion while other not as much but no sus
    menu: 
        "rummage through the drawers with no regard for cleanliness":
            jump reckless
        
        "leave everything untouched, but look around for clues.":
            jump careful

# this point onward there will be alternate pathways i think will figure out how to remember things later! 

#MC finds a photo of "him" and a crew & documents, leaving the house to a mess
label reckless: 
    $ messy = True
    $ trust_level -= 1
    "you search through the house, opening drawers halfhazardly and disregarding the orginal organization of the place." 
    # main idea finds 
    # finds photos of "him" and a crew
    # finds documents that explain the exact mission he was sent on 
    #house is left messy will impact pt 3 gameplay 

    jump search

#MC finds a photo of him and his crew, leaving the house clean
label careful: 
    $trust_level += 1
    jump search

#menu for searching rooms
label search:
    menu:
        "start by checking the drawers":
            jump check_drawers
        "start by checking the bedroom":
            jump check_bedroom
        "start by checking the kitchen":
            jump check_kitchen

#searching through the house (add more)
label check_drawers:
    if messy:
        "you start by quickly rummaging through the drawers, sheets of papers flying out."
        
        "one of the papers circle's through the air, catching your eye"

        "it lands quietly, face up, revealing a photo and lines of words written in black ink"

        menu:
            "check the photo":
                jump photo
            "check the document":
                jump document
    else:
        "you open the drawers calmly, the wood quielty creaking, papers are neatly stacked on top of one another"

        "as you go through the layers of papers, you notice a photo that catches your eye"

        menu:
            "check the photo":
                jump photo

#checks the photo of the adventuring party
label photo:
    "your fingers brush over the photo, removing a soft layer of dust"

    "the photo is of 5 members with a big burly man in the center." #fix details of photo

    player "is that... me?" #assuming player knows what they look like

    player "but who are these people?"

    "you notice that each of the people in the photo carry a large sack, storing their weapons."

    "on the left stands a girl focused on a book instead of the camera, she wears over sized clothing that looks like it could swallow her whole while an axe hangs off her back."
    
    "the boy next to her has his hands around her and what you assume is a picture of you." #continue description will do later just wanted a skeleton

    player "an adventuring party?"

    player "\"my\"... adventuring party?"

    if messy:
        menu:
            "check document":
                jump document
    else:
        jump part_3

#checks the document of the quesst
label document:
    "you pick up the document that had fallen on the floor."

    menu:
        "read the document":
            jump read_document

label read_document:
    #i want mission reveal during food time so it is revealed to both messy and clean, the messy and clean is important for brennans sus later on though
    "you look down at the document to find that it is all the same type of writing you could not read earlier."

    "maybe pocketing this for later will be benifical."
    jump part_3

#look through the bedroom but find nothing
label check_bedroom:
    "you enter the bedroom. it feels familiar somehow."
    
    "you look around and see your bed neatly made. there are no hints of dust or cobwebs"
    
    "other than the bed, the room seems plain, as if the person living here had no personality"
    
    show player think

    player "\"i\" must've been here recently... this house is spotless"
    
    if messy: 
        "you begin by uncovering the bedsheets, but finding nothing."

        "you check under the bed but only seeing emptiness"
    
    else:
        "you silently observe the bedroom, but nothing stands out to you."

        "you peek under the bed but notice nothing"
    
    show player think

    player "hmmm... this room has nothing."

    player "lets check someplace else"

    jump search

#look through the kitchen but find nothing    
label check_kitchen:
    "you enter the kitchen, feeling a sense of... nostalgia?"

    "there's the stove and sink and the table is set nicely"

    "dishes are neatly lined up on the drying rack and in cupboards"

    "you feel a hint of satisfaction"

    player "\"i\" must be a clean person"

    if messy:
        "you start by opening the dishwasher, finding nothing but lines of plates and other utensils"

        "next, the cupboard, however nothing stands out to you"
    else:
        "you look through the kitchen, peering over to notice and unusual items, something to give you information."

        "but nothing appears to be out of place or outside of the ordinary."
    
    jump search
label part_3: 
    "it's becoming late in the night"
    # MC sleeps but has dreams 

    "you begin to fall into a deep sleep"

    "PLACEHOLDER, this is stupid. why do you insist on killing yourself for this mission it's not worth it!"
    v "i have to. PLACEHOLDER2 needs us, they ALL need us."

    "but you do it at the expense of ######"

    v "i'm sorry, but it must be done." 

    "you wake up in a cold sweat." 

    player "what was that?"

    "you rub your eyes, attempting to wake up more."

    "suddenly a knock at the door, makes you jump."

    "*KNOCK KNOCK KNOCK*"

    unknown_lou "PLACEHOLDER I KNOW YOU'RE IN THERE!"

    unknown_brennan "I CAN'T BELIEVE YOU CAME BACK AND DIDN'T TELL ANY OF US! WE HAD TO FIND OUT THROUGH FIZ!"

    #meeting the orginal mcs crew eof adventurers 
    show brennan

    "you rush to the door, opening it to find a group of people you recognize from the photo. this must have been your crew."

    if messy:
        jump part_3_messy
    else:
        jump part_3_clean

    # this is different pathways comes into affect 
    # if player chose to be messy then brennan will notice immediately 
    # if player chose the sneaky looking then brennan will continue like nothing happened 

label part_3_messy:
    unknown_brennan "PLACEHOLDER! i-"

    unknown_annie "!"

    "brennan narrows his eyes, scanning the room"

    "he begins to mutter quietly under his breath"
    
    unknown_brennan "why is everything... everywhere?!"

    you "uhh i can explain!"

    menu: # both lead to same result. 
        "tell the truth.":
            jump truth
        
        "come up with a lie.":
            jump lie
    
label truth:
    $ trust_level += 1
    you "i just don't remember anything. i woke up and somehow wandered here, and now i'm just trying to figure out what happened."

    unknown_brennan "..."

    unknown_maryanne "that was weak, even for your jokes."

    unknown_annie "not your best work PLACEHOLDER. it's okay you can get a better sense of humour hopefully..."

    unknown_brennan "annie was losing her mind over your dissapearance and you think these jokes are appropriate?" 

    annie "i was not losing my mind! i was just worried but we were all. even maryanne was!"

    maryanne "we are just coming up with false narratives aren't we?"

    brennan "come on you were all like \"brennan what if he doesn't come back!\"" 

    maryanne "i told you that in private!"

    jump part_4_messy

label lie: 
    $ trust_level -= 1

    you "i lost my glasses!"

    unknown_brennan "oh that's why you aren't wearing them anymore."

    unknown_maryanne "eh you look better without them."

    unknown_annie "maryanne you can't say that!"

    maryanne "i was told to be honest growing up annie."

    "maryanne rolls her eyes."

    annie "you are unbelievable."

    jump part_4_messy

#sussing MC for being messy
label part_4_messy:
    
    unknown_lou "okay okay, let's not be fighting and go to dinner already"
    
    brennan "you owe us some food now that you're loaded!"

    "you dig your hands into your pocket in a panic and find a pouch of gold in each one."

    you "*when did that get there...?*"

    "you had checked your pockets earlier but they weren't there before..."

    "something is wrong with this world..." 

    show brennan excited 

    brennan "SWEET YOU GOT LIKE DOUBLE THE PAYMENT!"

    unknown_lou "brennan, volume."

    brennan "sorry lou!"

    lou "let's just get on our way before it gets dark."

    "you walk out of your house, as brennan and lou whisper from behind you."

    show brennan and lou 

    brennan "there's something... wrong with PLACERHOLDER."

    lou "i noticed as well but chalked it up to time."

    brennan "i'm going to keep an eye on him, i think something messed with him during the hunt."

    lou "he wouldn't get hurt during the hunt though."

    brennan "yeah but... something's wrong."

    jump part_5

label part_3_clean:
    unknown_brennan "PLACEHOLDER! i was so worried."

    "you look at the group of people in front of you and them seem to be a slightly older version of the group from the photo."

    "you notice that they seem revlieved to see you, in particular the boy that just spoke." #spelling ahhhh 

    show brennan angry
    unknown_brennan "man i was stress eating like crazy, you owe me three containers of almonds now!"

    unknown_annie "brennan can you calm down, he's probably exhausted from the mission."

    show brennan arms up in surrender 

    brennan "okay okay fine! i'm just glad you're back man."

    unknown_maryanne "now that we know you aren't dead, you have to tell annie everything or else i think she'll explode or something."

    annie "no i won't maryanne! i was just... worried as well you know?"

    menu: 
        #normal route finds out again little to no information as you try to blend in with the group 
        "go along with them.":
            jump normal
        
        #you pry for more information but brennan becomes more sus of you 
        "try to pry for information":
            jump detective
label normal: 
    $ trust_level += 1
    you "i'm sorry, really i just... lost track of time. but i'm back!"

    "you scan their faces for any suspicion." 

    you "ummm..."

    brennan "oh i see you're just trying to get out of paying for that dinner you owe us!"

    annie "not cool! we helped you prepare for that mission, it's not our fault they said we couldn't follow. god knows lou would've just to make sure you survived."

    lou "it's not because i care about you, i just..."

    show lou looking not into your eyes 
    
    lou "...want to make sure we get the reward!"

    annie "yeah yeah whatever you softie."

    jump part_4_clean

# in this path player should learn more information that will help them make better choices in the future but not as much as messy search
label detective: 
    $ trust_level -= 1
    player "yeah the mission, what even was that task i mean it was so stupid, right?"

    brennan "yeah but they said it only had to be you, something along the lines of the \"chosen\" one."

    maryanne "glad that didn't get in your head or else you would've become even more intolerable than now."

    show lou serious face
    lou "but we all know what that mission really was."

    annie "stop. let's just stop talking about it."

    lou "face it. they wanted him to die."

    show brennan happy 
    brennan "but~ you didn't! and now we get to live our lives as heroes for the rest of our lives!"

    brennan "the history books are gonna remember us!"

    "maryanne approaches you, whispering in your ear."

    maryanne "between you and me, he was crying when you stopped replying to our messages." 

    "you couldn't help but feel a warm feeling in your stomach."

    "but along side it was guilt."

    "you forgot all about them." #again here we are still under the assumption that we are the dopple ganger and not that we just look like him

    player "i'll treat you to a meal"

    "you march out in a random direction, hoping that parts of your memory would come back to remind you."

    brennan "so... what we feeling today PLACEHOLDER?"

    "as you struggle to come up with a beliveable answer, you spot a large, colourful sign in the distant village that reads RACK OF RIBS FOR ONLY 230 SHELLS"

    menu:
        "Let's eat ribs!":
            jump ribs

        "Think about it longer":
            jump thinking

#goes to eat ribs but is sussed because it isn't a food MC would usually go for
label ribs:
    player "hmmm.. how about some ribs today?"

    annie "ribs? sounds tasty!"

    maryanne "...since when did you like ribs?"

    "lou and brennan exchange glances"

    player "oh no, i must've chosen the wrong answer..." #whisper

    menu:
        "play it off cooly":
            jump cooly
        "choose a different location":
            jump thinking

label cooly:
    player "haha yeah! why don't we try something new today!"

    maryanne "....alright then"

    jump rib_restaurant


#magically gets memory and trust level increases
label thinking:
    $ trust_level += 1

    "you start thinking frantically"

    player "what would \"i\" want to eat?" #whisper

    "suddenly, a thought, a craving appears in your mind"

    player "GOULASH"

    player "i want goulash"

    "brennan smiles widely. He puts his arm around you"

    brennan "now THATS the correct answer!"

    jump goulash_restaurant

label rib_restaurant:
    "you and the group sit down in an old, beat down rib restaurant"

    player "six servings of rack of ribs, thank you"

    "the server nods and shortly after, brings back heaps of ribs"

    annie "mmmmm smells good!"

    "you pull your plate closer to yourself, trying to avoid brennans eye that has been directed at you since you sat down"

    "you take a whiff of the ribs, immediately knowing how good the quality is, but you suddenly get hit with a small sense of nausea and repulsion"

    player "!"

    menu:
        "eat the ribs":
            jump eat
        "uhhh no thanks":
            jump no_eat

label eat:
    $ trush -= 1

    "you dive into the ribs, eating it hungrily while ignoring the uncomfortable feeling in the back of your throat"

    "you raise your head slightly, just enough to see your crew staring at you, not touching their food"

    maryanne "wow."

    annie "i didn't know you liked ribs"

    menu:
        "come up with a lie":
            jump lie
        "play it off":
            jump play_it_off

label lie:
    $ trust -=1 
    player "haha! it must have been the battle, i've changed a lot since then"

    "annie looks worried"

    annie "yeah, we all did"

label play_it_off:
    $ trust += 1
    player "haha! get PRANKED"

    player "i've always loved ribs, i just lied to you guys and you fell for it!"

    brennan "WHATT? YOU KNOW I LOVE RIBS! and we always ate GOULASH instead"

    brennan "we could've ate ribs all those times back then!"

    player "yeah well, you should've known better"


label goulash_restaurant:
    "you and the crew sits down in the goulash restaurant"

    player "five servings of the original goulash please"

    server "of course, sir"

    "when the food arrives, you instantly get hit with a familiar and heartwarming smell"

    player "mmmmm, now THATS what i'm talking about"

    "the crew digs in, eating so quickly that you eat in silence"

    brennan "nothing is better than a good bowl of goulash"

    annie "it really brings back memories! i'm so glad i got to eat with you all again"

# goes to dinner and learn about the backstory of the mission 


label part_4_clean: 
    "e"

#mc was sent on a basically suicide mission where he had to kill a lot of people that were planning to take resources that the village he lives in needs to survive
#its like in transformers where the dinobots and autobots both need the blue liquid thing to survive but they did unjust things like morally grey mission 
#the whole party understands the politics associated because the village is known for having strong fighters so the "higher ups" rely on them to solve their issues through brutal force
label part_5: 
    "e"


    