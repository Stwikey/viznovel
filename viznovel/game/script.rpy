''' 
summary 
you wake up having no past memories of your life, as you continue to adventure you 
realize that the people around you seem to already know you. you come to discover you are a dopple ganger! and your "other self"
is a super famous hero, but as you adventure you realize the true indentions of your "other self"
spoiler alert: ur other u is a morally grey person crazy! 
'''
#player character
define player = Character('you', color="#c8c8ff")
define you = Character('[name]')


#dopple ganger

define og = Character('*****') #keep as ***** because the goal isnt to find out the name

#npcs 
define v = Character('voice', color='#a6b4d3')
define npc1 = Character ('old man') #an old man
define npc2 = Character ('Charles')
define lil_boy = Character('fiz')
define unknown = Character('???')
define server = Character ('Server')

#variables
default messy = False
default trust_level = 0
default document = False
default friendly_og = False
default stuffed_elephant = False 
default glasses = False
default rope = False 
default took_nothing = False 
default forestpick = False

#evil guys 
define evil1 = Character ('Viktor')
define evil2 = Character('Wagner')

#constants
define fade = Fade(0.5, 0.0, 0.5)

#black market vendors
define vendor1 = Character('garry')
define vendor2 = Character('john')

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
define cassia = Character('cassia')
#idk relationship to mc, the thief that tries to rob mc in the beginning (cypher from hsr vibes)
#unknown labels 
define unknown_brennan = Character('???',color = '#e9535311')
define unknown_maryanne = Character('???',color = '#784cd811')
define unknown_annie = Character('???',color = '#3bb91f11')
define unknown_lou = Character('???',color = '#b11f1f11')
define unknown_cassia = Character('???')

#character images
#brennan
image brennan normal  = Transform("brennan normal.png", zoom = 0.7)
image brennan talking  = Transform("brennan talking.png", zoom = 0.7)
image brennan scared = Transform("brennan scared.png", zoom = 0.7)

label start:
    scene bg grass lands with fade
    menu:
        "where am i?":
            player "where am i?"
        "who let me sleep on the ground?":
            player "who let me sleep on the ground?"
    
    "as you look around you realize that there isn't much of anything to give you clues on where you could be."

    "you try to recall your own name to no avail, you can't seem to remember anything other than what you find in your pockets."

    scene bg notebook
    "a notebook with messy scrawled on writing with symbols you can't seem to read." #yk like hyroglphs and stuff like that! 

    "without any other clues you must decide your next choice of action."
    scene bg grass lands

    menu: 
        "look around and explore":
            jump explore

        "go back to sleep in hopes you regain your memories":
            jump sleep 

label explore: 
    "sleep is for the weak!"

    "you spring up and begin looking around"

    player "there doesn't seem to be anyone here, and the more I look around the more i risk starvation, or worse."
   
    menu: 
        "go into the forest":
            jump forest 

        "find civilization":
            jump village

# player has a dream and gathers information on their past 
label sleep: 
    scene black with dissolve
    "you close your eyes and feel yourself drifting away"

    scene bg dream1 with fade
    #show 

    "???" "stop! get away from me please, *****. this was just a misunderstanding!"

    menu:
        "huh? who are you?":
            player "huh? who are you?"
        
        "what's happening?":
            player "what's happening?"

    "you reach out for no one."

    "???" "how did you even make it up here?"

    "???" "you stole some too didn't you?"

    menu: 
        "stole?":
            player "stole? what got stolen?"

    "it seems like no one can hear you"

    og "i finally understand, why you keep sending people to die for this stuff."

    "???" "you... hahahaha"

    "the man on the floor starts cackling."

    "???" "you are no better."

    og "at least i don't pretend like i am."

    "you feel yourself waking up."

    scene bg grass lands 

    menu:
        "try to dig for more clues":
            player "erm..."

            "you try to will yourself to remember more but end up just looking constipated."

        "start exploring elsewhere.":
            player "i should start going somewhere else."

    "there isn't much left to do here now."

    menu:
        "go into the forest.":
            jump forest 

        "find civilization.":
            jump village

#MC meets a stranger in the forest, they act like they know you but you have no memory of them
label forest:
    # turn bg into some forest 
    $forestpick = True 
    scene bg forest_clearing
    "you walk through the forest, unsure where you are travelling to."

    "you look around, hoping to identify some kind of landmark that can indetify this place."

    "as you step, insects scurry across, their form indescribable."

    "there seems to be a bunch creatures of some sort."

    "a voice cuts through the forest."

    unknown "*****"

    "a shadow rushes through the trees."

    show cassia happy 

    unknown "oh how i've MISSED YOU!"

    "the girl hugs you and you jump back in shock."

    menu:
        "do i know you?":
            player "do i know you?"
            jump question

        "stay silent.":
            player "..."
            jump silent

label question:
    show cassia confused 
    "a hint of suspicion flickers over the girl's face, too quick to notice."

    show cassia happy
    unknown_cassia "oh come on! are you seriously pretending to not know me? after all we've been through?"

    player "uhhh yeah, can you get off me now? i'm a busy man."

    "she steps back."

    unknown_cassia "ah, I see how it is. this is one of your silly pranks."

    unknown_cassia "not very funny."

    menu:
        "i thought it was funny.":
            player "i thought it was funny."
        "kekekekeke":
            "you let out a weird laugh."
            player "kekekekeke"
    
    unknown_cassia "whatever, i have places to be."

    "the strange girl leaps away into the bushes." 

    player "she seemed to know me?"

    "you decide to exit the forest."

    jump forest_end

# she gets less suspisious maybe
label silent:
    "..."

    unknown "hey~ did you hear meee???"

    "you continue to stay silent, after all, your mom always told you not to talk to strangers."

    "or at least that's what you think your mom would have told you, if you remembered who your mom was or who you were."

    "after a while, she grows frustrated and disappears in a flash."

    hide cassia

    "the rustles in the bushes grow quieter and she prances away."

    jump forest_end

label forest_end:
    #cut back to unknown
    scene black with fade
    unknown_cassia "somethings off... ***** should've noticed when I tried to rob him earlier"

    unknown_cassia "his biceps have also gotten skinnier..."

    scene bg forest_clearing
    player "that was... interesting."
    menu: 
        "find clues on who you are.":
            jump village

        "go find civilization.":
            jump village

label village: 
    scene bg grass lands
    "after wandering around for a while you discover theres a village, finally people!"

    scene bg village
    #scene goes to you entering 
    show npc1
    npc1 "***** you're back?"

    "you can't hear what name he's saying, the only noise you hear is static."

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

    "the old man looks at you weird."

    npc1 "you do know i was joking right?"

    menu:
        "act natural.":
            player "of course i do."

            player "i'm just playing along."

        "???":
            player "yeppers!"

            npc1 "yeppers?"

            player "haha just something i learned on the road!"

            npc1 "okay..."

    "there's something up with the people here..."

    npc1 "you seem to be acting weird, are you sure your okay?"

    player "yeah, just peachy."
    
    npc1 "we didn't expect you to return, to be quite honest."

    npc1 "*****, we are glad you have returned. really, we are."

    jump part_2

label freak: 
    player "who are you how do you know me?"

    "you pick up the old man by the shoulders"
    
    show npc1 

    npc1 "please calm down, i don't know what is wrong with you but..."

    show npc1 

    npc1 "you need to control yourself."

    npc1 "you earned the village great honor, but please remember to calm down before i call brennan." 

    "you feel your heart race, just what in the world did the person before you do?"

    menu:
        "right, got it.":
            player "right, got it."

    show npc1

    npc1 "i'm glad we've come to an understanding!"

    jump part_2

# more exploration of the village, getting a feel for how people react to you as a person
label part_2: 
    scene bg village 
    "you finally part ways with the old man, continuing to walk."

    unknown "***** I KNEW YOU COULD DO IT!"

    "a little boy's voice calls out from the distance as footsteps rapidly approach you."

    menu:
        "huh?":
            player "huh?"

    show lil_boy happy
    unknown "TELL ME EVERYTHING! did you get me the gift you promised? or did you forget about me?"

    show lil_boy sad 

    "you stand still trying to piece together what is happening..."

    #want lil boy to fade into the background while the player is thinking 

    "the people in this village all seem to revere you as some unsung hero of their time."

    "but that old guy from earlier, he seems to have it out for you? or maybe he's here to help."

    "what allies could i have that i must remember?"

    "i must've lost my memories in the adventure i was in."

    "i'm not sure who these people are but they must be important to me... or to the old me at the very least?"

    scene bg village with fade 

    "elsewhere..."

    npc1 "he seems... different charles."

    npc2 "you worry too much old man, he's probably scattered from the mission. after all, if he's back that means..."

    npc1 "they won't be an issue anymore." 

    scene village with fade 
    show lil_boy sad 

    player "yeah, i'm sorry i'm just tired from... where i've been. because i go places. i'm sorry fiz."

    "huh... how did i know his name?"

    "it's like something is pushing me find what information i'm missing..."

    lil_boy "thats okay! just make sure to remember next time, i'm just happy you made it back safely."

    lil_boy "you stopped answering my messages, and i couldn't get my friend to scry on you either. i thought you..." 

    "fiz pauses as he starts tearing up." 

    "he runs to your waist as he engulfs you in a hug." 

    player "i'm sorry. i promise i won't scare you like that again."

    show lil_boy happy 
    lil_boy "you better not."

    show npc1 lightly scolding
    npc1 "okay fiz, leave the young adventurer alone. he has to rest as well."
    
    show lil_boy 
    lil_boy "okay fine... but you better come visit me soon!"

    hide lil_boy
    jump home

    #MC returns back to "his" house 
label home: 
    scene bg home with fade
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
        
        "two of the papers circle's through the air, catching your eye."

        "they land quietly, face up, revealing a photo and paper with lines of words written in black ink."

        menu:
            "check the photo.":
                jump photo
            "check the document.":
                jump document
    else:
        "you open the drawers calmly, the wood quietly creaking, papers are neatly stacked on top of one another."

        "as you go through the layers of papers, you notice a photo that catches your eye."

        menu:
            "check the photo":
                jump photo

#checks the photo of the adventuring party
label photo:
    scene bg photo
    "your fingers brush over the photo, removing a soft layer of dust"

    "the photo is of 6 members with a big burly man in the center." #fix details of photo

    player "is that... me?" #assuming player knows what they look like

    player "but who are these people?"

    "you notice that each of the people in the photo carry a large sack, storing their weapons."

    "a girl is taking a selfie in front of a group of people."

    "on the left stands a girl focused on a book instead of the camera, she wears over sized clothing that looks like it could swallow her whole while an axe hangs off her back."
    
    "the boy next to her has his hands around her and what you assume is a picture of you." 
    
    "to the right another girl stands, anxiously pulling at the ends of her sleeves."

    "finally the boy standing next to her holds a serious expression, staring at the camera with a straight face."

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
    $ document = True 
    jump part_3

#look through the bedroom but find nothing
label check_bedroom:
    scene bg bedroom
    "you enter the bedroom. it feels familiar somehow."
    
    "you look around and see your bed neatly made. there are no hints of dust or cobwebs"

    "a stuffed elephant lies next to the pillow. it looks worn from years of usage."
    
    "other than that, the room seems plain, as if the person living here had no personality."

    player "\"i\" must've been here recently... this house is spotless"
    
    if messy: 
        "you begin by uncovering the bedsheets, but finding nothing."

        "you check under the bed but only seeing emptiness."
    
    else:
        "you silently observe the bedroom, but nothing stands out to you."

        "you peek under the bed but notice nothing."

    player "hmmm... this room has nothing."

    player "lets check someplace else"

    jump search

#look through the kitchen but find nothing    
label check_kitchen:
    "you enter the kitchen, feeling a sense of... nostalgia?"

    "there's the stove and sink and the table is set nicely"

    "dishes are neatly lined up on the drying rack and in cupboards"

    "you feel a hint of satisfaction"

    "there seems to be a recipe for goulash on the fridge."

    player "\"i\" must be a clean person"

    if messy:
        "you start by opening the dishwasher, finding nothing but lines of plates and other utensils"

        "next, the cupboard, however nothing stands out to you"
    else:
        "you look through the kitchen, peering over to notice and unusual items, something to give you information."

        "but nothing appears to be out of place or outside of the ordinary."
    
    jump search

label part_3: 
    "it's becoming late in the night."
    # MC sleeps but has dreams 

    "you decide to lay on your bed and begin to fall into a deep sleep."

    menu: 
        "cozy up to the stuffed elephant.":
            "you snuggled up next to the elephant, falling asleep quickly."

        "push the elephant off the bed.":
            "you reach to push the elephant off the bed."

            "you miss and end up falling out of bed instead."

            "you decide that it's best to just snuggle next to the elephant instead of being a heartless monster."

    scene black with fade 
    unknown_brennan "*****, why did you lie to us? to me?"

    og "i knew you'd stop me if i told you."

    unknown_annie "this isn't fair."

    unknown_cassia "you didn't want to consider any of our opinions on the matter either?"

    unknown_brennan "*****, this is stupid. why do you insist on killing yourself for this adventure it's not worth it!"

    og "if it wasn't me, it was going to be one of you!"

    unknown_lou "if you go through with this \"adventure\", it will be your last."

    og "i'm sorry."

    "the voice fades away."

    "you wake up in a cold sweat." 

    player "what was that?"

    "you rub your eyes, attempting to wake up more."

    "suddenly a knock at the door, makes you jump."

    unknown_lou "***** I KNOW YOU'RE IN THERE!"

    unknown_brennan "I CAN'T BELIEVE YOU CAME BACK AND DIDN'T TELL ANY OF US! WE HAD TO FIND OUT THROUGH FIZ!"

    #meeting the orginal mcs crew eof adventurers 

    "you rush to the door" 

    #figure out placement when all models are made 
    show brennan normal at left
    #show maryanne normal at middle 
    show annie normal at right 
    #show lou_normal at middle right 

    "opening it to find a group of people you recognize from the photo. this must have been your crew."

    if messy:
        jump part_3_messy
    else:
        jump part_3_clean

    # this is different pathways comes into affect 
    # if player chose to be messy then brennan will notice immediately 
    # if player chose the sneaky looking then brennan will continue like nothing happened 

label part_3_messy:
    show brennan talking at right
    unknown_brennan "*****! i-"

    show brennan normal

    unknown_annie "!"

    "brennan narrows his eyes, scanning the room"

    "he begins to mutter quietly under his breath"
    show brennan talking at right 
    unknown_brennan "why is everything... everywhere?!"
    show brennan normal 

    player "uhh i can explain!"

    menu: # both lead to same result. 
        "tell the truth.":
            jump truth
        
        "come up with a lie.":
            jump lie
    
label truth:
    $ trust_level += 1
    player "i just don't remember anything. i woke up and somehow wandered here, and now i'm just trying to figure out what happened."

    unknown_brennan "..."

    unknown_maryanne "that was weak, even for your jokes."

    unknown_annie "not your best work *****. it's okay you can get a better sense of humour hopefully..."

    unknown_brennan "annie was losing her mind over your dissapearance and you think these jokes are appropriate?" 

    annie "i was not losing my mind! i was just worried but we were all. even maryanne was!"

    maryanne "we are just coming up with false narratives aren't we?"

    brennan "come on you were all like \"brennan what if he doesn't come back!\"" 

    maryanne "i told you that in private?"

    maryanne "why are you airing out my business?"

    jump part_4_messy

label lie: 
    $ trust_level -= 1

    player "i lost my glasses!"

    unknown_brennan "oh that's why you aren't wearing them anymore."

    unknown_maryanne "eh you look better without them. glad we made you take them off for that photo."

    unknown_annie "maryanne you can't say that!"

    maryanne "i was told to be honest growing up annie."

    "maryanne rolls her eyes."

    annie "you are unbelievable."

    jump part_4_messy

#sussing MC for being messy
label part_4_messy:
    
    unknown_lou "okay okay, let's not be fighting and go to dinner already, brennan was most excited for that."
    
    brennan "you owe us some food now that you're loaded!"

    "you dig your hands into your pocket in a panic and find a pouch of gold in each one."

    "when did that get there...?"

    "you had checked your pockets earlier but they weren't there before..."

    "something is wrong with this world." 

    show brennan normal 

    brennan "SWEET YOU GOT LIKE DOUBLE THE PAYMENT!"

    unknown_lou "brennan, volume."

    brennan "sorry lou!"

    lou "let's just get on our way before it gets dark."

    "you walk out of your house, as brennan and lou whisper from behind you."

    show brennan and lou 

    brennan "there's something... wrong with *****."

    lou "i noticed as well but chalked it up to time."

    brennan "i'm going to keep an eye on him, i think something messed with him during the hunt."

    lou "he wouldn't get hurt during the hunt though."

    brennan "yeah but... something's wrong."

    maryanne "i'm hungry can we walk faster... ugh."

    brennan "yeah, ***** you decide."

    "brennan stares at you suspicously."

    jump ribs

label part_3_clean:
    unknown_brennan "*****! i was so worried."

    "you look at the group of people in front of you and them seem to be a slightly older version of the group from the photo."

    "you notice that they seem relieved to see you, in particular the boy that just spoke." 

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
    player "i'm sorry, really i just... lost track of time. but i'm back!"

    "you scan their faces for any suspicion." 

    player "ummm..."

    brennan "oh i see you're just trying to get out of paying for that dinner you owe us!"

    annie "not cool! we helped you prepare for that mission, it's not our fault they said we couldn't follow. god knows lou would've just to make sure you survived."

    lou "it's not because i care about you, i just..."

    show lou looking not into your eyes 
    
    lou "...want to make sure we get the reward!"

    annie "yeah yeah whatever you softie."

    brennan "come on let's just go to eat! what's the plan?"

    jump thinking

# in this path player should learn more information that will help them make better choices in the future but not as much as messy search
label detective: 
    $ trust_level -= 1
    player "yeah the mission, what even was that task i mean it was so stupid, right?"

    brennan "you volunteered."

    brennan "went behind our backs to do it too, don't think we forgot about that."

    annie "yeah then you went on about how if you came back you'd be \"the choosen one\""

    maryanne "glad that didn't get in your head or else you would've become even more intolerable than now."

    show lou serious face
    lou "but we all know what that mission really was."

    annie "stop. let's just stop talking about it."

    lou "face it. they were trying to kill him."

    show brennan happy 
    brennan "but~ he didn't die! and now we get to live the rest of our lives in peace."

    brennan "the history books are gonna remember us!"

    "maryanne approaches you, whispering in your ear."

    maryanne "between you and me, he was crying the entire time you were gone." 

    "you couldn't help but feel a warm feeling in your stomach."

    "but along side it was guilt."

    "you forgot all about them."

    player "i'll treat you to a meal!"

    "you march out in a random direction, hoping that parts of your memory would come back to remind you."

    brennan "so... what we feeling today *****?"

    "as you struggle to come up with a believable answer, you spot a large, colourful sign in the distant village that reads \"RACK OF RIBS FOR ONLY 18 GOLD\""

    menu:
        "let's eat ribs!":
            jump ribs

        "think about it longer.":
            jump thinking

#goes to eat ribs but is sussed because it isn't a food MC would usually go for
label ribs:
    show annie at right 
    show maryanne at left

    player "hmmm.. how about some ribs today?"

    annie "ribs? sounds tasty!"

    maryanne "...since when did you like ribs?"

    "lou and brennan exchange glances."

    "must've been the wrong answer."

    menu:
        "play it off cooly.":
            jump cooly
        "choose a different location.":
            jump thinking

label cooly:
    player "haha yeah! why don't we try something new today!"

    maryanne "...alright then?"

    jump rib_restaurant


#magically gets memory and trust level increases
label thinking:
    $ trust_level += 1

    "you start thinking frantically."

    player "what would \"i\" want to eat?" #whisper

    "suddenly, a thought, a craving appears in your mind."

    menu: 
        "I WANT GOULASH!":
            player "I WANT GOULASH!"

    "brennan smiles widely. he puts his arm around you."

    brennan "now THAT'S the correct answer!"

    jump goulash_restaurant

label rib_restaurant:
    "you and the group sit down in an old, beat down rib restaurant."

    "maybe thats why it was on sale."

    player "six servings of rack of ribs, thank you"

    "the server nods and shortly after, brings back heaps of ribs"

    annie "mmmmm smells good!"

    "you pull your plate closer to yourself, trying to avoid brennans eye contact that has been directed at you since you sat down."

    "you take a whiff of the ribs, immediately knowing how good the quality is, but you suddenly get hit with a small sense of nausea and repulsion."

    player "!?"

    menu:
        "eat the ribs.":
            jump eat
        "uhhh no thanks.":
            jump no_eat

label eat:
    $ trust_level -= 1

    "you dive into the ribs, eating it hungrily while ignoring the uncomfortable feeling in the back of your throat."

    "you raise your head slightly, just enough to see your crew staring at you, not touching their food."

    maryanne "wow."

    annie "i didn't know you liked ribs?"

    menu:
        "come up with a lie":
            jump lie2
        "play it off":
            jump play_it_off

label lie2:
    $ trust_level -=1 
    player "haha! it must have been the hunt, i've changed a lot since then"

    "annie looks worried."

    annie "yeah, we all did..."

    "lou clears his throat, attempting to shift topics."

    lou "we should go to the burial."

    "now if that wasn't supposed to give you whiplash, not sure what would."

    "you keep yourself composed."

    brennan "oh yeah, we need to catch you up on what you missed *****."

    jump part_5

label play_it_off:
    $ trust_level += 1
    player "haha! get PRANKED!"

    player "i've always loved ribs, i just lied to you guys and you fell for it!"

    brennan "what?! you know i love ribs but you never could stomach them and we had to eat goulash instead."

    brennan "we could've ate ribs all those times back then!"

    player "yeah well, you should've known better"

    "after a while of eating lou clears his throat, gaining everyones attention."

    lou "we should go to the burial."

    brennan "oh yeah, we need to catch you up on what you missed *****."

    jump part_5

label goulash_restaurant:
    "you and the crew sits down in the goulash restaurant"

    player "five servings of the original goulash please"

    server "of course, sir"

    "when the food arrives, you instantly get hit with a familiar and heartwarming smell"

    player "mmmmm, now THAT'S what i'm talking about"

    "the crew digs in, eating so quickly that you eat in silence."

    brennan "nothing is better than a good bowl of goulash!"

    annie "it really brings back memories! i'm so glad i got to eat with you all again."

    "as you sit and eat the goulash, brennan starts talking."

    brennan "um. i don't want to remind you of bad memories, but could you tell us... about how it went?"

    player "haha... yeah, um i'm just not comfortable with talking about it right now."

    annie "yeah... it's just-"

    lou "to get to the point already, we need to go visit the burial."

    player "huh? why?" #advantage for lying properly 

    maryanne "wow one big mission and you forget."

    "she rolls her eyes playfully."

    brennan "remember? death mission? we had a whole burial for you before you left."

    menu: 
        "oh right.":
            player "oh yeah... let's just pay and get out."
            jump part_5

label part_5: 
    "while walking on the way you can't help but pry for what happened."

    player "guys..."

    menu:
        "why did they send me on that hunt.":
            player "why didn't hey send me on that... hunt?"

    "brennan's face turns dark."

    brennan "they didn't send you."

    "lou elbows brennan."

    lou "hey cut it out. not the time."

    annie "let's not pretend we don't know the politics behind it."

    maryanne "it's in the past, what matters is that he returned, shouldn't we be happy about that?"

    "the party continues to walk towards the cemetary."

    "you began trying to piece together information."

    menu:
        "did \"i\" choose to go then?":
            "you were left wondering what caused you to make that choice."

    "brennan begins to walk next to you, allowing the rest of the group to walk ahead."

    show brennan serious
    brennan "i don't know what you faced, well... i have a rough idea. but i just want you to know you can talk to me, you know that right?"

    player "yeah, of course. i just..."

    player "ever since i got back i've been feeling scrambled."
    
    brennan "no that makes sense, anyone would feel that way if they had to do what you did."

    player "can i tell you something..."

    brennan "always."

    menu: 
        "tell brennan the truth.":
            player "i can't remember anything."

    if trust_level >= 2: 
        brennan "..."

        brennan "oh. that's why you haven't been all the way here."

        player "..."

        "brennan stops walking, and stares at you."

        brennan "i figured something was up."

        brennan "thought it was because of what i gave you before you left."

        brennan "well maybe that's what causes it, i told you only to use it if you're dying."

        brennan "so i guess you did \"die\" huh?"

        show brennan getting upset 
        menu:
            "i don't understand.":
                player "i'm sorry, i don't understand."

        brennan "you always tell me when your coming back. you always reply to my messages, you always bring me back almonds even when your dead tired."

        brennan "but you didn't this time."

        brennan "*****... why didn't you tell me sooner?"

        menu:
            "i couldn't dissapoint you guys.":
                player "i- i just i couldn't dissapoint you guys." 

                player "you were just all so excited to see me again."

                player "i couldn't... i couldn't tell you the truth."

            "i thought i could figure it out myself.":
                player "i thought i could figure it out myself."

                player "i snooped around my own house, looking for clues even."

        brennan "..."

        brennan "i believe you."

        brennan "there's still some part of you that remembers, i can see it in your face."

        brennan "or at least, something that's leading you in the right direction."

        show brennan thinking 

        brennan "something happened during the hunt."

        brennan "everyone believed in you, really we all did."

        brennan "but we all thought you'd never return."

        brennan "do you remember what happened?"

        menu: 
            "i don't remember anything.":
                player "i don't remember anything, not even my own name."

        brennan "your name? but we've been saying it all day."

        player "but for some reason, all i hear is static. like a big censor or something."

        "brennan whispers under his breath you can't hear, before saying your name."

        brennan "*****?"

        player "i can't hear anything, i'm sorry."

        brennan "it's alright, we can figure this out together. just like old times."

        show brennan happier 

        brennan "then you'll be back to your old self in no time!"

        brennan "we just gotta get you back into the groove of things."

        "a part of you was comforted by that fact, but the other part knew that even brennan wasn't sure you would remember."

    else:
        brennan "..."

        brennan "i know your secret, and this isn't it."

        player "???"

        brennan "you aren't *****."

        player "..."

        brennan "you haven't been, and i know that."

        brennan "your memory has been terrible and i just chalked it up to you being stressed."

        brennan "i kept making excuses for you in my head to rationalize why you were acting you way you were."

        brennan "we shouldn't be adventuring with you anymore."

        brennan "the ***** we knew died in that hunt."

        player "brennan please i can explain-"

        show brennan upset tears in eyes 
        brennan "stop... talking."

        show brennan wiping away his tears
        brennan "damn it, you even sound like him."

        brennan "listen, we can pretend everything is okay for one more day, but by tommorow your gone. you hear me?"
        menu:
            "...":
                player "..."

            "please just hear me out.":
                player "please just hear me out."

                brennan "didn't i already tell you to stop."

        brennan "i want you gone. i can't... you can't stay here."

        player "brennan... i'm sorry."

        brennan "i just don't think i can be around you... especially when you look just like him."

        menu: 
            "i didn't mean to offend you":
                player "brennan, i don't mean any harm i promise. i just want to remember what happened!"

        "you plead, if you were to leave the village all hopes in remembering the past would be gone."

        brennan "fine. whoever you are. because i know..."

        brennan "i know MY *****, wouldn't forget."

        brennan "he would never."

        hide brennan 

    "brennan walks away from you to join the rest of the group. you stay behind trying to process what just happened."

    "at least someone knows now, information should come easier..."

    "or that is the idea." 

    jump part_6

# cemetary scene now that brennan knows information from him is more specific to what happened as he is trying to jog your memory 
#broken trust brennen will be more snarky and angry (his heart guides him versus his head)
#trustful brennan will be a lot more useful, he is trying his best to help you and will explain concepts in more detail ie. esstitally spelling out to the mc what is happening/happened
label part_6: 
    "as you arrive to the burial, a large mountain of dirt stood in front of you." 

    "the grave has a wooden cross stuck at the front, the grass around it well taken care of with fresh flowers planted near."

    "you glance at the signage only to be met with the same writing you could never read."

    "from the headstone you can deduct what your name should look like... but you still can't read it."

    maryanne "sorry we buried you, thought you wouldn't return."

    "lou hits maryanne on the shoulder."

    maryanne "hey he thought so too!"

    "she points a finger at you."

    lou "sorry, it's just..."

    annie "after we lost contact with you, we thought it was over. like for real."

    annie "of course there was never a body to bury but, we just wanted somewhere to visit."

    lou "a place where we could go to."

    annie "so it looks a bit nicer than when you last saw it."

    brennan "you know..."

    brennan "because you went on the hunt, and thought you would die. so you told us to fake burry you."

    "you aren't stupid, you could tell that brennan was spelling things out for you."

    maryanne "kekeke, you were all goofy with it too."

    maryanne "\"remember me as a super strong handsome guy... bleh\""

    "the party smiles at the memory."

    annie "the hunt is stupid. there's too many dangers and we never even reap the rewards of the thing."

    brennan "i mean the payment isn't nothing."

    annie "yeah but it's nothing in comparison to you know... death?"

    lou "hey! i sent ***** with the best possible route, statistically it was the highest it would've ever been."

    annie "but maybe if i sent you with more food you wouldn't have come back so much slimmer."

    show annie worried #this is where her like indecisivness leads to delayed action 

    brennan "the hunt is necessary." 

    annie "no it's not."

    maryanne "it's a scam. we all know it."

    if trust_level >= 2:
        # brennan will fully explain the hunt
        brennan "it's controversial but what isn't?"

        brennan "i tried finding out what i could, but ever since... getting kicked. i can't really figure out much."

        scene black with fade 

        brennan "all i know is that we weren't always like this..."

        show viktor and wagner 

        brennan "we didn't need it."

        show adventures finding the very first source of mad honey 

        brennan "but once they started, they couldn't live without it."

        brennan "it changed them."

        brennan "the bees use specific flowers only found on the melissa region."

        brennan "consuming even just a tablespoon leads to godlike powers, all of a sudden you feel stronger, wiser, your reaction time is lightning speed."

        brennan "but it changes how you think. makes you act irrationally and selfishly."

        annie "and after that it's anyones guess." 

        maryanne "they say it's for our protection, so that we have a constant supply of food, water, etc. but we all know what that really means."

        lou "blackmail. they've hated us ever since didn't kick brennan out like they did."

        "brennan looks away. kicking at a rock."
    
    else: 
        #brennan refuses to explain the hunt. 
        brennan "yeah we SHOULD all know it."

        "brennan stares at you. he has something he wants to say but is holding back."
   
    show brennan upset 
    brennan "it isn't fair. the only reason you went is because you volunteered."

    lou "calm down brennan, we get it."

    show brennan shouting 
    brennan "no you don't!"

    brennan "***** DIDN'T HAVE TO GO!"

    brennan "HE CHOSE TO!"

    "annie slaps brennan in the face."

    "BAM."

    annie "if he didn't choose to go they would've sent you, or me, or god knows who."

    annie "we all know they don't care about us."

    annie "god brennan, i know you blame yourself but you need to move past it."

    annie "***** is here now and that's all that matters."

    if trust_level >= 2:
        brennan "yeah your right. sorry."

        annie "everything's gonna be okay."

        "the world seems to react, there's cracks in the sky that appear in your vision. as if the world was telling you otherwise."

        "it seems like the others don't notice the cracks. only visable to you."

    else:
        brennan "yeah, \"he's\" here."

        "the world seems to react."

        "you hear a voice, almost like a whisper in your ear."

        "???" "stupid stupid stupid. and i'm just supposed to watch now?"

    "the group stares silently at the makeshift grave for a moment until lou cuts through the silence."

    lou "let's return home, shall we? it's getting dark now." 

    "lou pats annie reassuringly on her back and they slowly start walking to the direction of the village." 

    "slowly, the rest of the group follows until only you and brennan remain."

    brennan "i..."

    brennan "i'm sorry."

    menu:
        "no i understand it must be hard.":

            player "no i understand it must be-"

        "i don't mean to forget.":
            player "i don't mean to for-"

    brennan "stop talking."

    if trust_level >= 2:
        brennan "it's just... it's all my fault you don't remember."

        brennan "they were going to take me back and there was no stopping it."

        brennan "but then you decided to be the hero."

        show brennan upset

        brennan "i should've told you to take it back."

        brennan "but the rest of the party wouldn't let me."

        brennan "lou would never let me do something that stupid."

        menu:
            "why would that be stupid?":
                brennan "because then they would've took me back."

                brennan "back to where i ran away from."

    brennan "we tried our best to prepare you."

    brennan "maryanne stopped playing her little games, annie was running around the village gathering anything she could."

    brennan "and i..."

    brennan "...i gave you the stupid honey."

    brennan "i was so angry."

    brennan "so... so angry."

    brennan "i stole. i stole from the kingdom."

    show flashback
    brennan "because we all knew you wouldn't survive. lou was losing his mind, maryanne was trying her hardest to pick up the slack."

    brennan "it's was stupid."

    if trust_level >=2:
        brennan "but maybe thats why you don't remember."

        brennan "because i caused it to happen."

    else:
        brennan "maybe that's why..."

        brennan "you aren't you."

    hide brennan 

    "he starts walking ahead. you walk next to him but don't speak."
    
    "you reach the village as brennan drops you off at your house."

    brennan "you live here by the way."

    if trust_level >= 2:
        show brennan bashful 

        brennan "i didn't know if you would remember."
    
    else:
        show brennan annoyed

        brennan "you wouldn've known if you remembered."

        menu:
            "...":

                brennan "whatever bye."
        
            "bashing me won't bring my memories back.":
                brennan "..."

                brennan "whatever man."

    scene black with fade 
    "you walk into your house and decide to rest for the night."

    scene bg bedroom 
    "you wake up, still groggy, to the sun shining in your face."

    menu:
        "leave":
            jump leave
        "stay":
            jump stay
label stay:
    "you lay around in bed for longer."

    player "i should get up."

    jump leave

label leave:
    "you quietly tiptoe through the house, something about the mornings makes you feel like you should be quiet."

    "you take one last glance behind you, before opening the door and getting hit in the face with a gust of fresh wind."

    jump forest_2

label forest_2:
    "something pulls you towards the woods."

    "you walk in the direction of the forest, not sure what you are hoping to find, but hopefully something."

    if forestpick == True:
        "you suddenly remember the girl you "

        player "that girl that was here before... I wonder who she was to \"me\""

    unknown_cassia "oh? i guess brennan was right huh?"

    unknown_cassia "that's odd 'cus he usually isn't"

    "you jolt by the touch of someone poking your shoulder and turn around to look over your shoulder."
    
    if forestpick == True:
        player "speak of the devil."

    unknown_cassia "i KNEW it! something was odd about you."

    unknown_cassia "you really aren't ***** are you?"

    player "..."

    unknown_cassia "stop pretending you don't know"

    "the girl uncrumples a scroll and holds it to your face for you to read"

    "the scroll reads..."
    
    scene scroll 

    "you still can't read."

    scene forest_clearing
    show cassia 

    player "i can't read."

    "the girl crumples the scroll back up and tosses it over her shoulder and rolls her eyes"

    unknown_cassia "it says that \"you\" aren't you. you know?"

    menu: 
        "so many you's":
            player "you said you like 10 times what are you going on about?"

    if trust_level >= 2:

        unknown_cassia "brennan gave this to me, didn't trust it at first but now seeing you..."

        unknown_cassia "starting to think it's actually real."
    
    else: 
        unknown_cassia "a guy you might know gave this to me. said you were a goner."

        unknown_cassia "thought he was joking at first but now seeing you..."

    menu:
        "who are you?":
            jump who_are_you
        "who am i?":
            jump who_am_i

label who_are_you:
    unknown_cassia "number one rule of an adventurer is to NOT give out information for free."

    unknown_cassia "what makes you think i can trust you?"

    menu:
        "i have money.":
            jump i_have_money
        "tell the truth.":
            jump tell_the_truth

label who_am_i:
    unknown_cassia "YOU? what makes you think i know who you are if YOU don't even know who you are?"

    player "i mean, who was \"i\"."

    "the girl scrunches her face, annoyed."

    unknown_cassia "now why would i tell you anything?"

    menu:
        "i have money.":
            jump i_have_money
        "tell the truth.":
            jump tell_the_truth

label tell_the_truth:
    player "i don't remember anything."

    "she stands there unimpressed."

    player "i need help."

    unknown_cassia "and that's a me problem how?"

    player "please?"

    unknown_cassia "hmmm... i don't speak without a price."

    unknown_cassia "you think information grows on trees?"

    menu: 
        "i have money":
            jump i_have_money

label i_have_money:
    "you pull out the pouch of gold coins still left in your pocket"

    player "is this enough?"

    "the girl's face lights up almost instantly"

    unknown_cassia "WOAH YOU'RE LOADED!"

    "the girl snatches the pouch quicker before you can react" #she could probably run away with the money but also wants to know whats up with mc 

    player "hey-!"

    cassia "i'm cassia nice to meet you by the way i have a 101-100 win lose score against you right now."

    cassia "well since it's \"you\" and not you i guess i have a 1-0 score."

    player "what?"

    cassia "come, let's go somewhere more quieter, i have a bounty on my head right now."

    player "!?"

    "you follow cassia through the forest, not sure where you are going but you have a feeling you can trust her."

    jump travelling

label travelling:
    "cassia leads you to night market."

    "although, during the day it stands to be filled with less... obvious illegal activites."

    "cassia sits down in one of the wooden chairs and starts counting the coins in her pouch of money"

    cassia "with this i might be able to finally bail a certain hibernating guy out of debt kekekeke." #HAHAH KEKEKEKEKEKE

    player "answer my question."

    "cassia sighs."

    cassia "alright *****,"

    cassia "mad honey is said to give you the powers that only gods can wield."

    cassia "information is limited, if the general public found out?"

    cassia "the whole system would collapse."

    cassia "what's up with you *****?"

    menu:
        "i can't hear my own name.":
            player "yeah... i can't hear my own name, it just sounds like muffled and i can't make out anything."

        "what's my name?":
            player "tell me my name."

            cassia "*****?"

            player "i can't hear nadda."

    cassia "so you can't hear your name at all?"

    player "yeah... its like static. i also can't read it either. or i guess read in general. all the writing looks like gibberish." #mc cant read just like me frfr 

    "cassia thinks for a moment, before a smug grin slowly appears on her face."

    cassia "hey ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** ***** *****!"

    "you stare at her, unimpressed."

    cassia "oh~ *****"

    "you push her away from you." 

    if trust_level <= 2:
        player "i've been meaning to ask"

        menu: 
            "ask about the quest":
                jump discussion
    
    else:
        player "do you happened to know more about... the old me?"

        cassia "hmmm..."

        cassia "well you were really nice, a bit stupid like you are now but, in a more endearing way."

        player "..."

        cassia "we were like super close. which is why i found it quite odd when you didn't tell us you were coming back?"

        menu: 
            "why weren't you with everyone earlier?":
                player "how come at my door, everyone was there but you?"

                cassia "not my fault! blame the stupid bear, i was dealing with some... let's say not so lovely company that may or may not have put a bounty on my head."

                player "?!"

                cassia "so i guess he didn't tell you everything everything like he said he would."

        player "could you tell me a bit about me more?"

        player "i was sent on a quest or the hunt, heard of it before?"

        cassia "oh yeah that."

        cassia "the information is all hush hush you know?"

        cassia "i don't really know why, no one does, but it's all for some mad honey resource."

        player "yeah brennan filled me in."

        cassia "i'm surprised he doesn't resent you or something."

        cassia "especially after the stunt you pulled."

        player "and that was...?"

        cassia "you went behind his back and basically died."

        player "oh... right."

        cassia "well you're back now, albeit a bit different."

        player "different?"

        cassia "yeah like... you look like you were reborn or something."

        cassia "you're you but not?"

        player "oh."

        cassia "anyways you should work on learning how to read, it would help you out a ton."

        player "uhhh got any suggestions on reading materials?"

        cassia "i don't know go home and pick up a book."

        "cassia waves you goodbye as she wanders back into the forest."

        "you decide its better to head home, after all maybe you could learn to read."

        "as you step back in you feel an overwhelming urge to sleep."

        jump part_7

label discussion:
    player "do you have any idea what happened to me? or what quest i went on" 

    cassia "i only know that you had to go in search of something."

    cassia "annie, lou, maryanne, and brennan kept a good hush hush about it."

    cassia "said they didn't want me involved because i already had a criminal history and it could land me in more hot water with what they were planning."

    cassia "i ran a few errands tho, grabbed stuff from out of town and all that."

    cassi "but as far as i know you just... disappeared"

    player "...i'm sorry"

    show cassia smile

    cassia "it's okay, i mean, it wasn't you"

    cassia "i think the only people that know about everything is the rest of the party."

    cassia "wish i could help ya but i was already in hot water at the time so i couldn't know."

    menu:
        "i doubt brennan is going to tell me anything.":
            cassia "yeah mr. grump face isn't the biggest fan of you right now huh?"

    cassia "we should just consider going to the night market, those shady guys know everything."

    "cassia leads you through the forest, a series of twists and turns you wouldn't be able to remember even if you tried."

    jump night_market 

label night_market: 
    scene bg nightmarket 
    show cassia 
    cassia "we might be able to find out more if we stay here."

    cassia "this place isn't... the nicest towards newbies."

    cassia "just follow my lead yeah?"

    "as the sun looms over you, the hooded figures around the market lurk in the shadows."

    player "they don't seem... very big on talking..."

    cassia "well it is called the NIGHT market for a reason."

    menu:
        "let's wait until nightfall.":
            jump nightime

        "let's just ask them now.":
            jump daytime
label daytime:
    scene bg nightmarket
    "you continue to push forward even though the sun shines down."

    "the market is mostly empty except for a few vendors."

    cassia "MARCUS MY MAN!"

    vendor1 "my name is garry."

    cassia "oh what?"

    vendor2 "psst cass over here!"

    "you hear heavy foot steps behind you, a figure placing a hand on your shoulder."

    vendor2 "and who might you be..."

    cassia "he's with me! we are trying to find out information about... the hunt."

    vendor2 "shhh not so loud."

    vendor2 "come with me."

    "you follow him to a booth in the back."

    vendor2 "i can't help you a lot but..."

    vendor2 "i hear there's a guy, he knows all about it but he's only here tonight."

    player "how does he know?"

    vendor2 "we don't ask questions, i just know that he paid a great price for something..." #hint to brennan! 

    vendor2 "so he's selling off information about the hunt to repay the price."

    cassia "we should come back at night."

    menu: 
        "return at night":
            jump nighttime

label nighttime:
    "you come back with cassia at night, the market is filled with people, all concealing their identity."

    player "everyone looks like they have something to hide?"

    cassia "that's because they do. you only do shady business here."

    cassia "there's a sign over there."

    "you look at the sign, you still can't read. it seems as though cassia forgot about that."

    player "i still can't read."

    cassia "i forgot you're stupid now."

    cassia "it says \'HUNTing equipment for a PRICE\'"

    player "uhhh we don't need hunting equipment."

    "cassia hits you in the shoulder."

    cassia "no you idiot it's the guy who knows about the hunt."

    "you walk towards the booth."

    cassia "wait before we actually start talking to people, take this."

    "she hands you a cloak, and pulls up her hood to cover her face."

    player "???"

    cassia "to cover yourself. we don't know anyone here and we don't want to. we just want information."

    player "okay cool cool cool, i can do that."

    cassia "after that response no. you are banned from talking."

    player "no fair!"

    cassia "nope i decided. you are just here to be the muscle in case things go south."

    player "fine."

    "you walk to the front of the booth to be meeted with another hooded figure."

    cassia "..."

    unknown_brennan "..."

    "the vendor points towards a sign."

    "you still can't read."

    "cassia moves to place a bag of coins on the table. the same bag she stole from you earlier."

    "you see the vendor perk up a bit in surprise."

    unknown_brennan "thank you for the business. it'll be my last day here so you are lucky."

    cassia "we want to know everything."

    unknown_brennan "and i'll gladly tell you."

    "a rune appears in front of you as the vendor begins his story. the magic feels... familliar."

    unknown_brennan "the hunt... was controversial but they were going to stop at nothing to get what they needed."

    scene bg story1 

    unknown_brennan "we weren't always like this..."

    unknown_brennan "we didn't need it."

    show evil1
    show evil2
    unknown_brennan "but once they started, they couldn't live without it."

    hide evil1
    hide evil2
    unknown_brennan "the bees use specific flowers only found on the montune region."

    unknown_brennan "consuming even just a tablespoon leads to godlike powers, all of a sudden you feel stronger, wiser, you reaction time is lightning speed."

    unknown_brennan "and after that... it's anyones guess."

    unknown_brennan "they say it's for our protection, so that we have a constant supply of food, water, etc. but we all know what that really means."

    player "..."

    cassia "so it's a suicide mission all for some honey?"

    unknown_brennan "they were eyeing someone for the job before..."

    "the vendor stops talking."

    unknown_brennan  "...it was taken by someone else last minute."

    cassia "do you happen to know what happened on the latest hunt?"

    unknown_brennan "*chuckles*, god i wish i did. but the guy they sent on it doesn't remember a thing."

    cassia "thank you for your time."

    "you both walk away."

    cassia "so the higher ups send some lab rat to go do their dirty work."

    player "i still can't remember anything. nothing from the quest or mission or whatver it was."

    "you can feel yourself growing angry." #DANIEL TIGER CORE LMAO 

    menu:
        "try to calm down.":
            jump calmdown 

        "screw this, get angry!":
            jump gointoarage

label calmdown:
    "you breathe in and out."

    cassia "are you okay?"

    player "i just..."

    "you continue to breathe but can't help what happens next."

    jump gointoarage

label gointoarage:
    "your body experiences hot flashes, as you can feel yourself physically grow."

    player "I JUST DON'T UNDERSTAND!"

    player "I DIDN'T ASK TO LOSE MY MEMORIES AND NOW BRENNAN'S UPSET AT ME AND FOR SOME REASON THAT KILLS ME."

    player "IT HURTS."

    player "it hurts."

    player "my friends expect me to be someone that i'm not."

    player "and i don't even remember my friends."

    player "man he was right. i should just leave the village and start a new life."

    cassia "..."

    cassia "we made good progress today though."

    cassia "we'll recover those memories one way or another."

    "you part ways with cassia for the day and return back to \"your\" house."

    jump part_7

label part_7: 
    "you lie down in your bed."

    "you close your eyes, drifting off to sleep."
    
    scene bg dream1
    v "even in death you are blessed."

    og "i miss them."

    v "that is known, but you cannot return."

    og "i wish i could've said goodbye at the very least."

    v "maybe we can find a workaround."

    "the figure lifts something up to the other"

    og "i can't. that would destroy them."

    v "this is the best solution that i have..."

    og "fine. but, how will they know?"

    v "they'll know."

    "BANG BANG BANG" 

    annie "hello? come on and answer the door already!"

    scene bg bedroom
    menu:
        "answer the door":
            jump door

        "don't answer the door":
            jump door
    
label door:
    annie "come to the door already, no point in hiding!"

    "i guess there's no hiding from this."

    show annie 
    "you get up and open the door to find annie there."

    player "???"

    annie "brennan wanted me to give you this."

    "she hands you a box."

    player "what is this?"

    annie "don't know, he told me specifically not to open it."

    player "uh... thanks?"

    "annie stands there like she's expecting something."

    menu: 
        "give her money.":
            jump give_money_to_annie
        
        "stare back at her.":
            jump stare_at_annie

label give_money_to_annie:
    annie "what the heck. i don't want that."

    player "???"

    annie "..."

    player "just prankin' you!"

    jump door_pt2

label stare_at_annie:
    "stare back at her."

    annie "..."

    player "..."

    "annie blinks."

    player "HAH I WIN!"

    jump door_pt2

label door_pt2:
    annie "he was right."

    "she turns away and leaves."

    player "does she know? did brennan tell everyone?"

    "you look at the box in your hands. maybe it could provide you with the answers you were seeking."

    menu:
        "open the box.":
            jump open_the_box

label open_the_box:
    "opening the box you see a number of objects."

    "photos of you when you were younger, a trinket, and a dirty rag."

    jump choices

label choices:
    menu:
        "look at the photo.":
            jump childhood_photo

        "look at the trinket.":
            jump trinket

        "look at the dirty rag.":
            jump dirty_rag

        "put the box away":
            jump part_8

label childhood_photo:
    "touching the photo, visions appear in your head."

    show expression happy
    "children run around the field."

    "you look down to see your hands are also that of a childs."

    brennan "***** come here!"

    "that voice sounded like brennan's except a lot younger."

    og "coming!"

    "your body starts moving without your permission."

    "as you continue to run you see the rest of your friends."

    "they look significantly younger."

    maryanne "my parents said if i did really good on the next evaluation then they'll get me that new game!"

    lou "no fair! ugh my parents said that i can only get books. what if i become a big nerd."

    cassia "you already are~"

    "lou starts chasing cassia around."

    lou "get back over here!"

    player "... it seems like everyone is happy..."

    player "lou seems a lot more carefree."

    player "annie seems to be worry free."

    player "maryanne seems to actually have emotions."

    maryanne "are you done staring? come on we said we wouldn't be late today."

    og "sorry just let me take a photo the leaves make it look pretty!"

    "you feel yourself pull out a camera and snap a photo"

    og "perfect!"

    "you feel yourself move through time. this time you are back in the village."

    show brennan 
    og "here... um. i have to leave on the quest in a bit but i wanted you to have this."

    brennan "why are you acting like you aren't coming back."

    og "you know the reality of this."

    brennan "who cares what lou said!"

    brennan "numbers can tell you what's likely to happen but not what will!"

    brennan "i can't believe you're giving up."

    og "i'm not giving up. i just... i know myself well"

    brennan "it's not fair."

    jump choices

label trinket:
    "you pick up the trinket."

    annie "lookie here!"

    annie "i got this for scoring all perfect on the last assessment."

    lou "so what i could score that in my sleep."

    annie "yeah which is why it's not that big of a deal to you."

    annie "maryanne look!"

    maryanne "..."

    cassia "save your breath, ever since she got that game she's been gone."

    "cassia snatches maryannes game out of her hands."

    maryanne "HEY I WAS PLAYING WITH THAT!"

    "brennan bursts out laughing, putting an arm around your shoulder."

    annie "hey lesser of the two ann's here look at what i got!"

    "maryanne pauses her chase of cassia to look."

    maryanne "oh neat what even is that?"

    annie "uhh... actually i'm not sure."

    og "looks like a..."

    #looks like one of those rorschach test 
    menu: 
        "looks like a bear.":
            jump bear

        "looks like a late 1800's painting of the esteemed dr. louis pierre wilson teaching a class to a group of depressed university students.":
            jump louispierre

label bear: 
    og "that looks like a bear."

    annie "i mean i guess if i tilt my head i can see it."

    brennan "yeah i see it, the nose is right there."

    maryanne "and the excess squiggles?"

    og "just ignore those."

    jump choices 

label louispierre:
    og "looks like a late 1800's painting of the esteemed dr. louis pierre wilson teaching a class to a group of depressed university students."

    maryanne "what are you going on about."

    og "no look do you not see it?" 

    lou "no."

    maryanne "yeah... yeah, yeah no this is crazy how did you even come up with that."

    cassia "no no, i see it."

    og "really?"

    cassia "nah."

    "you feel yourself become flustered."

    og "uh... yeah okay fine i was onto nothing."

    jump choices 

label part_8: 
    player "..."

    player "i remember..."

    player "I REMEMBER!"

    player "not everything makes sense but i remember these moments as if i was there."

    player "i need to talk to someone."

    menu: #"all roads lead to sepsis" but in this case brennan
        "talk to brennan.":
            jump brennan

        "talk to annie":
            jump annie

        "talk to lou":
            jump lou

        "talk to maryanne":
            jump maryanne

        "talk to cassia":
            jump cassia 
label annie:
    "you run to catch up with annie."

    "you see her in the far distance before shouting."

    player "annie! annie!"

    annie "???"

    annie "oh it's you."

    player "i remember. not what happened but i remember you guys"

    annie "you forgot?"

    "you sweatdrop and realize you actually never told anyone other than cassia that you're memory failed you."

    "well that and brennan finding out on his own."

    player "oh right."

    "you explain everything that has happened."

    annie "that explains why brennan was acting so weird around you."

    player "oh, so you noticed?"

    annie "yeah. well, i eventually caught on."

    player "i'm sorry."

    annie "no, it's not your fault. it's ours."

    player "???"

    annie "i think you should talk to brennan."

    player "alright."

    "you walk away."

    menu: 
        "talk to brennan.":
            jump brennan

        "talk to lou":
            jump lou

        "talk to maryanne":
            jump maryanne

        "talk to cassia":
            jump cassia 

label lou:
    player "HEY LOU!"
    
    "you run to see him walking presumably back to his house."

    lou "???"

    lou "oh *****."

    player "i remember!"

    lou "oh. yeah. he did tell me about this, but hearing you say it really makes it true."

    player "oh."

    player "so brennan told you all?"

    lou "it's best you go talk to brennan."

    "you walk away."

    menu:
        "talk to brennan.":
            jump brennan

        "talk to annie":
            jump annie

        "talk to maryanne":
            jump maryanne

        "talk to cassia":
            jump cassia 

label maryanne:
    "you walk over to see maryanne laying by a tree, engrossed in her video game."

    player "maryanne!"

    maryanne "..."

    player "hello?"

    maryanne "oh! what's up?"

    player "i remember!"

    maryanne "sure you do bud."

    player "???"

    maryanne "i knew the whole time you aren't you."

    player "i mean i am now."

    maryanne "no you aren't."

    maryanne "you aren't *****."

    player "yeah i know, but i'm remembering who i was now."

    maryanne "you still don't understand."

    maryanne "the only reason i havent told anyone is because you haven't hurt anyone."

    maryanne "and because... for selfish reasons i couldn't accept that you were gone."

    "you stood in front of her confused."

    player "i'm sorry, but i'm back now."

    maryanne "sure \"you\" are."

    maryanne "maybe you should go talk to brennan."

    player "ah okay."

    menu:
        "talk to brennan.":
            jump brennan

        "talk to annie":
            jump annie

        "talk to lou":
            jump lou

        "talk to cassia":
            jump cassia 

label cassia:
    "you run into the forest, the twigs hitting you in the face as you shout."

    player "CASSIA!"

    "the trees shook as a gust of wind blew."

    cassia "*****, i'm glad you came here i was jsut about to come find you."

    player "cassia i rem-"

    "she cuts you off"

    cassia "you have to find brennan."

    player "what?"

    cassia "he's missing, everyone's been worried sick."

    player "what? how?"

    cassia "no one's seen him since this morning."

    "you run back to the village"

    menu:
        "find to brennan.":
            jump brennan

        "talk to annie":
            jump annie

        "talk to lou":
            jump lou

        "talk to maryanne":
            jump maryanne

label brennan:
    player "i need to talk to brennan."

    "you run in the direction of his house. or at least where you think his house is."

    player "BRENNAN! BRENNAN!"

    "you run up to his house, knocking on the door."

    player "i'm sorry i forgot but i remember now."

    "..."

    "there comes no reply."

    player "???"

    player "brennan? are you there?"

    "you look around the villge and see no one around."

    player "annie? lou? maryanne? cassia? someone?"

    player "anyone?"

    "you look up at the sky and see cracks forming"

    "your head hurts."

    "you grip onto your hair, pulling at it to distract you from the headache that is forming in your head."

    player "what is happening."

    "you can't think as your vision starts to blur."

    player "what... is... going on?"

    #fade with black

    jump part_9

label part_9: 
    v "i told you it would be too much."

    og "..."

    v "he can't handle it."

    og "..."

    og "but i need them to know."

    v "you didn't NEED them to know"

    og "I DID!"

    og "they mean everything to me."

    player "hello?"

    v "!!!"

    og "!!!"

    og "how are you here?"

    player "uh where even is here?"

    v "the _____"

    player "???"

    v "oh, for the living you can't hear."

    v "there are somethings that are redacted."

    v "they stay that way for a reason."

    og "yeah which is why you can't hear \"your\" name."

    player "why do you say it as if it's not?"

    v "you cannot say *****."

    og "why not."

    "you hear him getting angry."

    og "i can't do this, i can't do that. why? what's stopping me."

    v "..."

    v "i cannot say."

    og "exactly, you can't even tell me!"

    og "i spent all this time watching and waiting."

    v "calm down ***** you are going to throw everything you worked so hard for away."

    og "i don't care. you don't understand. this isn't just another life for me."

    og "it's mine!"

    og "and HE gets to continue living it?"

    "the man points a figure at you."

    "looking at him carefully you see that he looks like you."

    "except, he has more scars on him, his body is more worked out."

    "he has more of a build than you do. he looked... just like you."

    player "what is going on?"

    v "you cannot afford to say anything anymore."

    og "i- you can't stop me!"

    "the man lunges for the other."

    menu:
        "help the other you.":
            jump help_other_you
        
        "stand there and watch.":
            jump do_nothing

label help_other_you:
    "you see the other you get pinned down, seemingly significantly weaker than the man on top of him."

    "you run and push him off."

    og "nice work other me."

    v "you don't understand what forces you are playing with, you cannot keep this up."

    og "i know."

    "before you have a second to react, or to stop, you see \"you\" raise your hand before blasting the other in the face."

    og "now that he's finally taken care of."

    show og happy 

    og "we have much to discuss."

    og "..."

    "suddenly he bursts out laughing."

    og "kekekeke, man i cannot keep that facade up."

    og "that just isn't me, or i guess you figured that out through my friends right?"

    player "???"

    og "yeah i'm sorry i just really got angry for a moment."

    og "i'm still not all the way there ever since the hunt, you'd think all my issues would be cleared now because i'm dead but *sigh*."

    $ friendly_og = True

    jump part_10

label do_nothing:
    "you stand there and watch the struggle."

    #figure out if a scene can be animated here

    og "now that he's finally taken care of..."

    show og scary face 

    og "aren't you just useless hm?"

    player "um... i'm sorry i just..."

    menu:
        "i felt like it wasn't my place to get involved.":
            jump appease
        
        "...":
            jump nothing

label appease: 
    og "hmm, yeah good point."

    show og netural 

    og "well we have much to discuss"

    jump part_10

label nothing:
    og "..."

    og "didn't know other me was such a loser."

    og "come on do something already."

    og "all you've been doing is just reacting to the things around you, where's that fighting spirit huh?"

    og "what you push it all onto \"your\" friends?"

    og "they don't care about you."
    
    og "not after finding out the real truth."

    menu:
        "punch him.":
            jump punch_og
        
        "do nothing":
            jump do_nothing_again

label do_nothing_again:
    og "wow, i really must've chosen the wrong soul for this."

    og "and i thought you would have really begged for an opportunity like this."

    og "after all, you last life ended early."

    og "whatever."

    jump part_10

label punch_og:
    "you aren't going to stand here and take this from this guy."

    "you raise your hand and punch him in the face."

    "SMACK"

    og "..."

    og "maybe you do know how to throw a punch kekeke."

    player "???"

    show og happy 

    og "man i tried being all tough and stuff but that isn't me."

    $ friendly_og = True
    jump part_10

label part_10: 
    if friendly_og == True:
        show og happy
        og "i should probably tell you everything."

        hide og 
        #show flip of images of the hunt 

        og "my name is *****."

        og "you might be under the impression that that's your name."

        og "you'd be wrong."

        og "but, we can get into the details of that later."

        og "i'm not sure how long you'll be here, so i'll make this short."

    else: 
        og "i don't know how long you'll be here before they drag you back down."

        og "but at this rate..."

        og "maybe i could replace you."

        og "after all you are... a lesser version."

    og "you should know by now that you, or whoever you think you are. that's not you."

    og "i'm sorry."

    og "it's my fault you can't rest."

    player "rest...?"

    og "you aren't technically... alive?"

    player "what."

    og "here's the thing, i might of maybe sorta grabbed your soul before you know... stuffing it into a vessel."

    player "WHAT?"

    show og nervous 

    og "haha enough about that though!"

    menu:
        "pry further.":
            jump tell_me_now

        "just allow him to keep going.":
            jump leave_it

label leave_it:
    og "i died on the hunt."

    og "i failed."

    #show images of the hunt in the background 

    og "i could tell from the looks on their faces when i volunteered, we all knew what that meant."

    og "no one ever returns."

    og "but if i didn't go, if i didn't volunteer."

    show og tearing up 

    og "they would've picked brennan."

    og "he'll deny it."

    og "he kept saying"

    og  "\"no way they'll choose any of us! maryanne doesn't train, annie's build like a twig, cassia has a criminal record, and lou is all brains no brawns\""

    show brennan

    og "but we all knew."

    og "they were going to choose him."

    og "and for some reason i'll never understand, he was going to let them?"

    og "man he sucks."

    og "but i love him so."

    player "!!!"

    og "...he gave me mad honey before i left."

    #flash to the scene 

    og "where did you get this from?"

    brennan "don't worry about it."

    brennan "please just, return to the village?"

    og "i-"

    brennan "just say you will."

    brennan "even if you think it's a lie."

    og "i'll return to you."

    brennan "..."

    og "..."

    #flash back to present 

    og "i never did get the chance to return."

    menu:
        "you shouldn't have volunteered":
            jump mean_hater 
        "how did you die?":
            jump hunt_story

label tell_me_now:
    player "no, i want to know about me."

    player "you keep avoiding the topic of me."

    og "..."

    og "i know, and i'm sorry but i don't know much about you prior to now."

    og "i will tell you what i know, but i first need to tell you how you got here to begin with."

    jump leave_it

label mean_hater:
    player "they should've gone with brennan, then maybe he wouldn't have died."

    player "volunteering was stupid."

    og "..."

    og "yeah i guess."

    jump hunt_story

label hunt_story: 
    og "i had to climb up a mountain, it's always raining in that region."

    og "the floors become slippery and you can't grip onto anything."

    og "before even reaching a quarter of the way through, i had fallen countless of times."

    og "they told me i HAD to find \"mad honey\" whatever that is."

    og "lou did his research, he told me everything and anything i would need to know."

    #flash back
    lou "you should bring a torch with you, the smoke with prevent them from communicating with each other."

    og "but he didn't account for me consuming it."

    #flash back scene change 
    brennan "just, if you are in a pickle. take some."

    og "what? where did you even get this."

    brennan "don't worry about it."

    brennan "they say you get powers, you get stronger, faster, whatever."

    brennan "it's just... a safety net. a just in case."
    
    #flash to mountain

    og "i ended up using it."

    og "i had to."

    og "within minutes i felt it hit."

    og "at first i thought i was going to die."

    og "my body started sweating rapidly, i couldn't make sense of anything."

    og "i laid there on the ground until it passed."

    og "after i felt like i was on a high, my muscles no longer ached and the rain felt like a mere inconvience."

    og "i made it up the mountain in record time."

    og "but what they don't tell you is what's waiting for you up there."

    og "it was a planned sacrifice."

    og "they waited with their swords, by the time any regular person gets up to the hill they collpase."

    og "but because of the honey flowing through me, i felt as good as new."

    og "better even."

    og "turns out..."

    og "when you have something like that in your system."

    og "you can't get enough of it."

    og "i beat them. obviously."

    "you see as his gaze gets lost in the distance."

    menu: 
        "try to snap him out of it.":
            jump snap_out 

label snap_out:
    player "hey you okay?"

    "you wave a hand in front of his face."

    og "sorry."

    og "i got distracted."

    og "yeah, so i volunteered."

    menu: 
        "but how did you... yk?":
            jump og_death
        
        "you still haven't told me how you died and why the heck i'm here.":
            jump og_death

label og_death: 
    og "oh yeah... sorry."

    og "after... killing them."

    og "i harvested the rest of the honey."

    og "well tried to kinda got stung a bunch."

    og "i was going to return to the village, share what i gathered."

    og "rub it in annie's face for being so worried, tell lou that his calculations were right, buy maryanne a new video game with the money i got,"

    og "i was going to thank brennan, tell him i owed him one big time."

    og "but it turns out i didn't really do a good job on the killing part."

    og "maybe it was because i hadn't ever done a murder before."

    og "i was gone before i even knew what hit me."
    
    og "maybe i was asking for it at that point."

    og "i mean i was the one that volunteered."
    
    og "it's just, nothing seemed... fun anymore?"
    
    og "we went on every adventure, every journey, did things that no one our age has ever done."
    
    og "became village heroes for a short period of time."
    
    og "everything that i used to find joy in..."
    
    og "got stale."
    
    og "i kept putting my friends in greater and greater danger because of my own selfishness."
    
    og "so i stopped."
    
    og "ugh i was so stupid."

    "you see ***** gesture towards the body of the other person."

    og "that thing took pity on me."

    og "nice i guess, but thought it was funny to make me watch."

    menu:
        "watch what?":
            jump og_death_pt2

label og_death_pt2:
    player "watch what?"

    og "..."

    og "it was going to make me watch you let him die."

    menu:
        "who die?":
            og "..."

            "he doesn't answer you."

    og "i have nothing against you, even if you are taking my life and acting as if it's your own."

    og "but i really do hate you."

    menu:
        "i won't let anyone die.":
            jump og_death_pt3
        "i would never do something like that.":
            jump og_death_pt3

label og_death_pt3:
    og "you don't get to decide that."

    "before you could ask further you felt your head begin to hurt again."

    og "are... are you okay?"

    "you couldn't form any words, the only thing that came out was a groan."

    player "AUGH"

    og "shoot, you're leaving to go back."

    og "brennan was taken by the same people that killed me, tell everyone in the party to head towards kallisto."

    "you look at him confused."

    menu:
        "go back to the world of the living.":
            jump og_death_pt4
        "stay.":
            jump ending1

label ending1: 
    player "no. i want to stay!"

    og "???"

    "are you sure you want to stay?"
    
    menu:
        "stay.":
            player "i need to find out more about me. i can't just live your life."

        "leave.":
            "the shooting pain returns to your head."

            player "AUGH!"

            og "head to kallisto!"

            jump og_death_pt4
    
    og "..."

    og "alright, i guess we can see what we can do from here."

    og "is your brain alright?"

    menu: 
        "yeah it's fine now.":
            player "yeah i think i'm okay now."

        "nah still hurts.":
            player "still hurts."

    og "we can figure it out."

    "you follow the other you, not sure where you are going but you were going to find out answers."

    "plus who needs to know the rest of a story when you can write your own."

    return 

label og_death_pt4:
    og "they'll know what you mean!"

    og "and please for the love of all that is good please-"

    #fade with black 

    "you wake up lying on the floor, annie looking worriedly over you."

    annie "are you okay?"

    "you could only groan out a word."

    player "kallisto."

    annie "???"

    "you grab her by the shoulders, shaking her a bit."

    player "we need to go to kallisto!"

    annie "!!!"

    "you see her face become shocked before returning with a serious look."

    annie "i'll tell the others, you start taking what you need from your house."

    jump part_11

label part_11:
    "you return back to \"your\" house."

    "now that you know that you aren't whatever everyone keeps calling you."

    "you can't help but wonder what your name is."

    "maybe you should just give yourself a name."

    $name = renpy.input("what will you name yourself?", length=20).lower()

    you "hmmm. [name]."

    you "i like the sound of that."

    "you look around your house and pack the necessities."

    you "i can only fit so much in my bag so i'll have to make a choice."

    menu:
        "take rope with you.":
            jump take_rope

        "take \"your\" glasses":
            jump take_glasses

        "take the stuffed elephant with you.":
            jump take_elephant

        "take nothing":
            jump took_nothing

label take_rope: 
    you "this will come in handy."
    $rope = True 
    jump part_11a

label take_glasses:
    you "they aren't mine, but maybe they will come in handy."
    $glasses = True 
    jump part_11a

label take_elephant:
    you "cute, not sure how it'll help but you never know."
    $stuffed_elephant = True 
    jump part_11a

label took_nothing:
    you "the less stuff i have, the lighter my bag."
    $took_nothing = True
    jump part_11a

label part_11a:
    "you do one final sweep of the house before running to meet up with the group."

    "you see lou up ahead writing furiously on a piece of paper."

    cassia "you need to calm down."

    lou "no, this means that there isn't enough time so i'm making time."

    annie "you can't make time!"

    lou "yes i can! we can take a shorter path."

    "as you approach they take notice of your arrival."

    annie "we have to get moving, at this rate he'll be a goner."

    show annie scared 

    "maryanne hits annie in the side of her head."

    annie "ow!"

    maryanne "no ones turning to the dark side, we'll be fine. he'll be fine."

    "you open you mouth to talk but annie shoots you a strange look."

    annie "i didn't forget what brennan told me about you."

    menu:
        "stare at her back.":
            jump stare

        "reintroduce yourself with your new name.":
            jump reintroduction

label stare:
    "you stare at her."

    you "..."

    annie "..."

    you "..."

    lou "can you guys stop staring at each other and get a move on?"

    jump part_12

label reintroduction:
    you "hi my name is-"

    annie "i don't care."

    "you are caught off-guard. this isn't the annie you were used to."

    lou "quit talking we have to start moving."

    jump part_12 

label part_12:
    "the group continues to travel, you don't really know where you are going so when you get ahead of the group you end up having to circle back awkwardly."

    maryanne "this better be worth it, brennan better buy me like 100 games after this."

    cassia "if he's still there to buy you the games."

    lou "knock it off. now isn't the time to argue."

    "you have no idea what is going on."

    "you consider telling them the truth."

    menu:
        "tell them the truth.":
            jump tell_truth

        "lie to them":
            jump tell_lie 

label tell_truth:
    you "guys before we go."

    "everyone pauses in their footsteps, lou seemingly annoyed."

    lou "what did i say? we don't have time for this."

    you "just listen to me!"

    you "i-"

    you "i'm not *****!" #maybe go back and use wattsons kinetic text tags to make text more interesting here

    annie "..."

    annie "yeah."

    annie "you didn't think i wouldn't have told everyone by now?"
    
    you "oh."

    lou "that's what you stopped us for?"

    lou "get over yourself, brennan's in trouble let's get back to moving."

    "the group continues moving leaving you standing there a bit shocked and embarssed."

    "cassia approaches you"

    cassia "what's your name now?"

    you "[name]..."

    cassia "nice to meet yout [name]."

    #fade with black

    jump part_13

    
label tell_lie:
    "a shooting pain goes through your head."

    you "stupid whatever his name is."

    menu:
        "tell them the truth.":
            jump tell_truth
        
        "tell them the truth":
            jump tell_truth 

label part_13: 
    scene bg kallisto 
    show evil1 at left 
    show evil2 at right 
    "???" "and now..."

    "???" "we are thankful to be joined by a special guest today!"

    "???" "brennan..."

    annie "what do we do [name]?"

    menu:
        "hide and watch what happens.":
            you "i think we should take cover and watch for now."
            jump hide_and_watch

        "charge in and free brennan.":
            you "we need to free him now."
            jump attack_now

label hide_and_watch:
    brennan "i already told you what i know!"

    evil1 "there isn't much you could tell us that we wouldn't already know..."

    evil1 "your majesty..."

    lou "what?"

    "you watch lou's face twist in confusion before his fists clench."

    evil2 "you've done a good job prince, tricking that poor little adventurer to go in your place?"

    evil2 "cowards way out."

    brennan "..."

    evil1 "you steal from the capital, you get your so called \"best friend\" killed, so now why are you still trying to hard to deny your path?"

    evil2 "your... destiny."

    brennan "because you both are evil."

    evil1 "how could you speak about your parents that way."

    evil2 "yes your oh so adoring parents."

    brennan "i didn't steal for no good reason and i didn't get ***** killed!"

    brennan "ALSO YOU BOTH SUCK!"

    "you watch brennan struggle."

    brennan "you both sent him on a death mission! you knew he was going to go on my behalf!"

    brennan "you just couldn't stand the fact that someone might rival your power without the use of mad honey!"

    "the crowd of people gasp."

    evil1 "son you are speaking nonsense."

    "person in crowd" "nono please let him continue talking i live for family drama!"

    evil1 "mad honey is not used freely. it is soley for the protection of the nation."

    brennan "come on pops, we all know you're a liar."

    evil1 "i just want what's best for you."

    brennan "correction, you WANTED what was best for you!"

    brennan "now you've turned into... this."

    brennan "just let me go."

    evil2 "i think you are mistaken son."

    evil1 "everyone, i'm so sorry for the chit chat."

    evil1 "we will get on with the event."

    "from his pocket, he pulls out jar of honey."

    "there was something about that honey that made it glow."

    annie "is that-"

    lou "it is."

    "you start to feel sick."

    "it's like your body remembers what your mind doesn't."

    "you watch as brennan thrashes against the restraints."

    brennan "hey, get that away from me!"

    evil2 "but you were so ready to share it with your friend..."

    evil2 "it's your turn our dear son."

    "you watch brennans face morph into one of pure horror."

    brennan "NO WAIT PLEASE-"

    evil1 "you survived this long without it."

    evil2 "now let's see what you become with it."

    menu: 
        "look away":
            "you can't."

        "run towards him.":
            "your legs are frozen."

        "shout for help, for anyone to stop it.":
            "nothing comes out."
    
    "you watch as they pry his jaw open."

    "come on, you need to act."

    menu:
        "force yourself to move.":
            "your fist clench."

    jump attack_now

label attack_now:
    "you lunge at the man."

    og "COME ON GO STOP THEM!"

    "a voice rings through your ears and you feel stronger."

    "you dash from the bushed at lightning speeds."

    evil1 "!!!"

    evil2 "what the-"

    menu:
        "kick him in the face.":
            "you strike a kick at his face. the honey falling from his hand."

        "slap him like one of those over dramatized tv shows.":
            "you slap him while the crowd in the background gasps. the honey falls from his hand."

    "person in crowd" "OH MY GOD RUN!"

    "people start running in all different directions."

    "brennan looks up at you with a grateful look on his face before shouting."

    brennan "everyone listen! the honey is just so the wealthy stay weathly! they don't care about you or what you want!"

    "person in crowd" "we already knew that!"

    annie "???"

    lou "then why are you still going along with it?"

    "person in crowd" "i just wanted to be apart of something!"

    menu:
        "uhh you can come live at the village?":
            "person in crowd" "oh actually?"
        
    "another voice perks up."

    "like all of us?"

    maryanne "sure?"

    evil1 "even us?"

    "he gestures towards himself and wagner."

    menu: 
        "maybe not you guys.":
            you "maybe not you guys."

            evil1 "hey that's not fair she made-"

            evil2 "you need to calm down."

        "sure?":
            you "i guess we could make room?"

            evil1 "WOO!!"

            evil2 "but what happens to our castle? and like empire we've built."

            evil1 "i guess we sell it on ebay?"

            evil2 "yeah that works."

    annie "so then what did we learn from this... mission?"
    jump ending2

label ending2:
    menu:
        "some people just need to be hit in the face.":
            you "some people just need to be hit in the face."

        "everything is meaningless, nothing matters in the end.":
            you "everything is meaningless, nothing matters in the end."

    annie "no. i really doubt that is the lesson."

    "you look at brennan to check if he is okay."

    brennan "what's got you so worried?"

    menu:
        "i'm sorry i replaced your friend.":
            you "i'm sorry i replaced your friend."

            brennan "..."

            brennan "it's okay, he probably was laughing to himself about all of this."

            "a voice rings through your head."

            og "YOU BET I WAS!"

            "brennan looks at you clueless. he seemed to not have noticed anything."

            you "yeah he is."

            brennan "we should rejoin the rest of the gang."

            "he points towards everyone else talking."

        "i should leave.":
            you "i should leave."
            
            brennan "no please stay."

            brennan "i know you aren't him, but i'd like to get to know you."

            brennan "after all, you are apart of the party now."

            "he points towards everyone else talking."

    cassia "so is everyone just going to ignore the fact that they caused mass destruction and killed a bunch of people?"

    "she points towards the formerly known villans in confusion."

    menu: 
        "the lion does not concern himself with the opinions of sheep":
            you "the lion does not concern himself with the opinions of sheep"

            "cassia hits you in the face."

            you "OW?"

            cassia "whatever i'm gonna tell lou to lock them up or something."

            cassia "maybe that will clear the bounty on my head?"

            "she laughs as she walks away."

        "nah it's fine.":
            you "nah it's fine."

            you "this is the happily ever after, nothing can go wrong."

            "cassia hits you in the face."

            you "OW?"

            cassia "whatever i'm gonna tell lou to lock them up or something."

            cassia "maybe that will clear the bounty on my head?"

            "she laughs as she walks away."

    "you look up at the sky, there are still many unanswered questions."

    "you look turn to look at your new friends."

    "maybe they can help you find the answers."

    scene black with fade

    "until next time!"

    return