''' 
summary 
you wake up having no past memories of your life, as you continue to adventure you 
realize that the people around you seem to already know you. you come to discover you are a dopple ganger! and your "other self"
is a super famous hero, but as you adventure you realize the true indentions of your "other self"
spoiler alert: ur other u is a morally grey person crazy! 
'''
#player character
define player = Character('player', color="#c8c8ff")

#dopple ganger

define og = Character('???') #come up with name later 

#npcs 
define v = Character('voice', color='#657aac')
define npc1 = Character ('npc1') #an old man
define npc2 = Character ('Charles')
define lil_boy = Character('fiz')
define cassia_unknown = Character('???')
define unknown = Character('???')
default messy = False
default trust_level = 0
default document = False

#black market vendors
define vendor1 = Character('garry')
define vendor2 = Character('john')
define vendor3 = Character('wagner')

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
    
    unknown_cassia "oh comeee on! Are you seriously pretending to not know me? After all we've been through?"

    player "uhhh yeah, can you get off me now? I'm a busy man."

    "UNKNOWN steps back."

    unknown_cassia "ah, I see how it is. This is one of your silly pranks again huh?" #idk how to end this

    unknown_cassia "well I'll be off on my way then."

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
        
        "one of the papers circle's through the air, catching your eye."

        "it lands quietly, face up, revealing a photo and lines of words written in black ink."

        menu:
            "check the photo":
                jump photo
            "check the document":
                jump document
    else:
        "you open the drawers calmly, the wood quielty creaking, papers are neatly stacked on top of one another."

        "as you go through the layers of papers, you notice a photo that catches your eye."

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
    $ document = True 
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

    unknown_annie "not your best work PLACEHOLDER. it's okay you can get a better sense of humour hopefully..."

    unknown_brennan "annie was losing her mind over your dissapearance and you think these jokes are appropriate?" 

    annie "i was not losing my mind! i was just worried but we were all. even maryanne was!"

    maryanne "we are just coming up with false narratives aren't we?"

    brennan "come on you were all like \"brennan what if he doesn't come back!\"" 

    maryanne "i told you that in private!"

    jump part_4_messy

label lie: 
    $ trust_level -= 1

    player "i lost my glasses!"

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

    player "*when did that get there...?*"

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

    maryanne "i'm hungry can we walk faster... ugh."

    brennan "yeah, PLACEHOLDER you decide."

    jump ribs

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

    brennan "come on let's just go to eat! what's the plan?"

    jump thinking

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
        "let's eat ribs!":
            jump ribs

        "think about it longer":
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

    player "i want goulash."

    "brennan smiles widely. He puts his arm around you"

    brennan "now THAT'S the correct answer!"

    jump goulash_restaurant

label rib_restaurant:
    "you and the group sit down in an old, beat down rib restaurant"

    player "six servings of rack of ribs, thank you"

    "the server nods and shortly after, brings back heaps of ribs"

    annie "mmmmm smells good!"

    "you pull your plate closer to yourself, trying to avoid brennans eye contact that has been directed at you since you sat down"

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

    annie "i didn't know you liked ribs?"

    menu:
        "come up with a lie":
            jump lie2
        "play it off":
            jump play_it_off

label lie2:
    $ trust -=1 
    player "haha! it must have been the battle, i've changed a lot since then"

    "annie looks worried."

    annie "yeah, we all did..."

    "lou clears his throat, attempting to shift topics."

    lou "we should go to the cemetary."

    brennan "oh yeah, we should pay our respects at the very least. especially you PLACEHOLDER."

    jump part_5

label play_it_off:
    $ trust += 1
    player "haha! get PRANKED"

    player "i've always loved ribs, i just lied to you guys and you fell for it!"

    brennan "WHATT? YOU KNOW I LOVE RIBS! and we always ate GOULASH instead"

    brennan "we could've ate ribs all those times back then!"

    player "yeah well, you should've known better"

    "after a while of eating lou clears his throat, gaining everyones attention."

    lou "we should go to the cemetary."

    brennan "oh yeah, we should pay our respects at the very least."

    jump part_5

label goulash_restaurant:
    "you and the crew sits down in the goulash restaurant"

    player "five servings of the original goulash please"

    server "of course, sir"

    "when the food arrives, you instantly get hit with a familiar and heartwarming smell"

    player "mmmmm, now THATS what i'm talking about"

    "the crew digs in, eating so quickly that you eat in silence"

    brennan "nothing is better than a good bowl of goulash!"

    annie "it really brings back memories! i'm so glad i got to eat with you all again"

    "as you sit and eat the goulash, brennan starts talking."

    brennan "um. i don't want to remind you of bad memories, but could you tell us about... what happened."

    player "haha... yeah, um i'm just not comfortable with talking about it right now."

    annie "yeah... it's just umm..."

    lou "to get to the point already, we need to go visit the cemetary."

    player "huh? why?" #advantage for lying properly 

    maryanne "wow one big mission and you forget."

    "she rolls her eyes playfully."

    brennan "you need to go repent before the gods strike a curse on you or something. just a superstition but you were always big about that stuff."

    player "yeah. let's just pay and get out."

#mc was sent on a basically suicide mission where he had to kill a lot of people that were planning to take resources that the village he lives in needs to survive
#its like in transformers where the dinobots and autobots both need the blue liquid thing to survive but they did unjust things like morally grey mission 
#the whole party understands the politics associated because the village is known for having strong fighters so the "higher ups" rely on them to solve their issues through brutal force
label part_5: 
    "while walking on the way you can't help but pry for what happened."

    player "guys..."

    menu:
        "why did they send me on that mission":
            jump mission

label mission:
    brennan "no one wanted you to go man, we all told you not too. even maryanne."

    annie "politics is confusing, but they said you were the best for the job. i mean, if you didn't go we would've all died."

    "the party continues to walk towards the cemetary."

    "you began trying to piece together information."

    player "*so then i wanted to go?*"

    "brennan begins to walk next to you, allowing the rest of the group to walk ahead."

    show brennan serious
    brennan "i don't know what you faced, well... i have a rough idea. but i just want you to know you can talk to me, you know that right?"

    player "yeah, of course. i just..."

    player "ever since i got back i've been feeling scrambled."
    
    brennan "no that makes sense, anyone would feel that way if you they had to do what you did."

    player "can i tell you something..."

    brennan "always."

    menu: 
        "tell brennan the truth.":
            jump memoryloss 

label memoryloss: 
    player "i can't remember anything."

    if trust_level >= 3: #i dont even know if this number is possible 
        brennan "..."

        brennan "oh. that's why you haven't been all the way here."

        player "..."

        "brennan stops walking, and stares at you."

        brennan "you always tell me when your coming back. you always reply to my messages, you always bring me back almonds even when your dead tired."

        brennan "but you didn't this time."

        brennan "PLACEHOLDER... why didn't you tell me sooner?"

        player "i- i just i couldn't dissapoint you guys." #spelling ? 

        player "you were just all so excited to see me again."

        player "i couldn't... i couldn't tell you the truth."

        brennan "..."

        brennan "i believe you."

        brennan "there's still some part of you that remembers, i can see it in your face."

        show brennan thinking 

        brennan "something must of happened during the hunt. when you left you were acting normal."

        player "i don't remember anything, not even my own name."

        brennan "your name? but we've been saying it all day."

        player "but for some reason, i can't hear it."

        "brennan whispers under his breath"

        brennan "PLACEHOLDER?"

        player "i really am sorry."

        brennan "we will figure this out together, just like old times."

        show brennan happier 

        brennan "you'll be back to your old self in no time!"

        brennan "we just gotta get you back into the groove of things."

        "a part of you was comforted by that fact, but the other part knew that even brennan wasn't sure you would remember."

    else:
        brennan "..."

        brennan "i know your secret, and this isn't it."

        player "???"

        brennan "you aren't PLACEHOLDER."

        player "..."

        brennan "you haven't been, and i know that."

        brennan "your memory has been terrible and i just chalked it up to you being stressed."

        brennan "i kept making excuses for you in my head to rationalize why you were acting you way you were."

        brennan "we shouldn't be adventuring with you anymore."

        player "brennan please i can explain-"

        show brennan upset tears in eyes 
        brennan "stop... talking."

        show brennan wiping away his tears
        brennan "damn it, you even sound like him."

        brennan "listen, we can pretend everything is okay for one more day, but by tommorow you need to disappear."

        player "..."

        brennan "i want you gone. i can't... you can't stay here."

        player "brennan... i'm sorry."

        brennan "i just don't think i can be around you... especially when you look just like him."

        player "brennan, i don't mean any harm i promise. i just want to remember what happened!"

        "you plead, if you were to leave the village all hopes in remembering the past would be gone."

        brennan "fine. whoever you are. because i know..."

        brennan "i know MY PLACEHOLDER, wouldn't forget."

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
    "as you arrive to the cemetary, the graves look all unvisited except one." 

    "the grave is polished, the grass around it well taken care of with fresh flowers planted near."

    "you glance at the headstone to be met with the same writing you could never read."

    "from the headstone you can deduct what your name should look like... but you still can't read it."

    maryanne "sorry we buried you, thought you died."

    "lou hits maryanne on the shoulder."

    lou "sorry, it's just..."

    annie "after we lost contact with you, we thought it was over."

    annie "of course there was never a body to bury but, we just wanted somewhere to visit."

    lou "a place where we could go to."

    brennan "you know..."

    brennan "because you went on the mission, or better known as the hunt."

    "you aren't stupid, you could tell that brennan was spelling things out for you."

    annie "the hunt is stupid. there's too many dangers and they know we didn't stand a chance."

    lou "hey we set PLACEHOLDER with the best chances, statistically it was the highest it would've ever been."

    annie "but maybe if i sent you with more food you wouldn't have come back so much slimmer."

    show annie worried #this is where her like indecisivness leads to delayed action 

    brennan "the hunt was necessary." 

    maryanne "it's a scam. we all know it."

    if trust_level >= 3:
        # brennan will fully explain the hunt
        brennan "the hunt... was controversial but it was us or them."

        brennan "and if we chose them, they would've killed us."

        show brennan telling story and images of history #this similar to like the honor thing in genshin where it starts telling the history of the weapons 

        brennan "we weren't always like this..."

        show village 

        brennan "we didn't need it."

        show adventures finding the very first source of mad honey #brennan doesnt explicitly say mad honey but its shown

        brennan "but once they started, they couldn't live without it."

        brennan "the bees use specific flowers only found on the montune region." #lol made up montune idek what that is 

        brennan "consuming even just a tablespoon leads to godlike powers, all of a sudden you feel stronger, wiser, your reaction time is lightning speed."

        annie "and after that it's anyones guess." 

        maryanne "they say it's for our protection, so that we have a constant supply of food, water, etc. but we all know what that really means."

    
    else: 
        #brennan refuses to explain the hunt. 
        brennan "yeah we SHOULD all know it."

        "brennan stares at you. he has something he wants to say but is holding back."
   
    show brennan upset 
    brennan "it isn't fair. the only reason they chose you is because you were stupid enough to volunteer."

    lou "calm down brennan, we get it."

    show brenna shouting 
    brennan "no you don't!"

    brennan "PLACEHOLDER DIDN'T HAVE TO GO!"

    brennan "HE CHOSE TO!"

    "annie slaps brennan in the face."

    "BAM."

    annie "if he didn't choose to go they would've sent you, or me, or god knows who."

    annie "we all know they don't care about us."

    annie "god brennan, i know you blame yourself but you need to move past it."

    annie "PLACEHOLDER is here now and that's all that matters."

    "you feel the world shift. there's cracks in the sky that appear in your vision. as if the world was telling you otherwise."

    "it seems like the others don't notice the cracks. only visable to you."

    "the group stares silently at the makeshift grave for a moment until lou cuts through the silence"

    lou "let's return home, shall we? it's getting dark now" 

    "lou pats annie reassuringly on her back and they slowly start walking to the direction of the village" #(?)not sure where they live

    "slowly, the rest of the group follows until only you and brennan remain"

    brennan "i..."

    brennan "i'm sorry."

    player "no i understand it must be-"

    brennan "stop talking."

    if trust_level >= 3:
        brennan "it's just... it's all my fault you don't remember."

        brennan "when they asked who wanted to go, none of us wanted to."

        brennan "they were going to choose me."

        brennan "we all knew they were going to."

        brennan "so you volunteered."

        brennan "i should've stopped you before you submitted your name."

        brennan "i should've known you would go behind our backs to do it to."

        brennan "lou would never let you do something that stupid."

    brennan "we tried our best to prepare you."

    brennan "maryanne stopped playing her little games, annie was running around the village gathering anything she could."

    brennan "and i..."

    brennan "...i gave you the stupid honey."

    brennan "i was so angry."

    brennan "so... so angry."

    brennan "i stole. i stole from the higher ups."

    show flashback
    brennan "because we all knew you wouldn't survive. lou was losing his mind, maryanne was trying her hardest to pick up the slack."

    brennan "it's was stupid."

    if trust_level >=3:
        brennan "but maybe thats why you don't remember."

    else:
        brennan "maybe that's why..."

        brennan "you aren't you."

    hide brennan 

    "he starts walking ahead. you walk next to him but don't speak."
    
    "you reach the village as brennan drops you off at your house."

    brennan "you live here by the way."

    if trust_level >= 3:
        show brennan bashful 

        brennan "i didn't know if you would remember."
    
    else:
        show brennan annoyed

        brennan "you wouldn've known if you remembered."

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
    "you quietly tiptoe through the inn, hoping nobody the tiny creaks off the wooden floorboards under your feet"

    "you take one last glance behind you, before opening the door and getting hit in the face with a gust of fresh wind"

    jump forest

label forest:
    "you walk towards the direction of the forest, not sure what you are hoping to find, but hopefully something"

    player "that girl that was here before... I wonder who she was to \"me\""

    unknown_cassia "oh? i guess brennan was right huh?"

    unknown_cassia "thats odd 'cus he usually isn't"

    "you jolt by the touch of someone poking your shoulder and turn around to look over your shoulder"

    player "speak of the devil."

    unknown_cassia "i KNEW it! something was odd about you."

    unknown_cassia "you really aren't PLACEHOLDER are you?"

    player "..."

    unknown_cassia "stop pretending you don't know"

    "the girl uncrumples a scroll and holds it to your face for you to read"

    "the scroll reads..."

    "you still can't read."

    player "i can't read."

    "the girl crumples the scroll back up and tosses it over her shoulder and rolls her eyes"

    unknown_cassia "it says that YOU are YOU. you know?"

    unknown_cassia "some guy gave this to me, didn't trust it at first but now seeing you..."

    unknown_cassia "starting to think it's actually real."

    menu:
        "who are you?":
            jump who_are_you
        "who am i?":
            jump who_am_i

label who_are_you:
    unknown_cassia "number one rule of an adventurer is to NOT give out information for free"

    unknown_cassia "what makes you think i can trust you?"

    menu:
        "i have money":
            jump i_have_money
        "tell the truth":
            jump tell_the_truth

label who_am_i:
    unknown_cassia "YOU? what makes you think i know who you are if YOU don't even know who you are"

    player "i mean, who was \"i\""

    "the girl scrunches her face, annoyed"

    unknown_cassia "now why would i tell you anything?"

    menu:
        "i have money":
            jump i_have_money
        "tell the truth":
            jump tell_the_truth

label tell_the_truth:
    player "i don't remember anything."

    player "i need help."

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

    unknown_cassia "WOAH YOU'RE LOADED"

    "the girl snatches the pouch quicker before you can react" #she could probably run away with the money but also wants to know whats up with mc 

    player "hey-!"

    cassia "i'm cassia nice to meet you by the way i have a 101-100 win lose score against you right now"

    player "what?"

    cassia "come, let's go somewhere more quieter, i have a bounty on my head right now."

    player "!?"

    "you follow cassia through the forest, not sure where you are going but you have a feeling you can trust her."

    jump travelling

label travelling:
    "cassia leads you to night market."

    "although, during the day it stands to be filled with less... obvious illegal activites."

    "cassia sits down in one of the wooden chairs and starts counting the coins in her pouch of money"

    cassia "with this i might be able to finally get a sip of that mad honey kekekekkeke" #HAHAH KEKEKEKEKEKE

    player "answer my question"

    "cassia sighs"

    cassia "alright PLACEHOLDER"

    cassia "mad honey is said to give you the powers that only gods can weild."

    cassia "information is limited, if the general public found out?"

    cassia "the whole system would collapse."

    cassia "what's up with you PLACEHOLDER?"

    player "yeah... i can't hear my own name, it just sounds like muffled and i can't make out anything."

    cassia "so you can't hear your name at all?"

    player "yeah... its like static. i also can't read it either. or i guess read in general. all the writing looks like gibberish." #mc cant read just like me frfr 

    "cassia thinks for a moment, before a smug grin slowly appears on her face."

    cassia "hey PLACEHOLDER PLACEHOLDER PLACEHOLDER PLACEHOLDER PLACEHOLDER PLACEHOLDER PLACEHOLDER PLACEHOLDER PLACEHOLDER PLACEHOLDER PLACEHOLDER PLACEHOLDER PLACEHOLDER PLACEHOLDER PLACEHOLDER PLACEHOLDER"

    "you stare at her, unimpressed"

    cassia "oh~ PLACEHOLDER"

    "you push her away from you." 

    if trust < 3:
        player "i've been meaning to ask"

        menu: 
            "ask about the quest":
                jump discussion
    
    else:
        player "do you happened to know more about... the old me?"

        cassia "hmmm..."

        cassia "well you were really nice, a bit stupid like you are now but, in a more endearing way."

        player "..."

        cassia "you and your friend group were like super close. which is why i found it quite odd when you suddenly stopped hanging out with them as much."

        player "i didn't stop. i just... i was sent on a quest or the hunt, heard of it before?"

        cassia "oh yeah that."

        cassia "the information is all hush hush you know?"

        cassia "i don't really know why but it's all for some mad honey resource."

        player "yeah brennan filled me in."

        cassia "i'm surprised he doesn't resent you or something."

        cassia "especially after hearing what you did back then."

        player "and that was...?"

        cassia "you volunteered behind his back."

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

    cassia "hmmmm...i don't know"

    cassia "you just...disappeared"

    player "...i'm sorry"

    show cassia smile

    cassia "it's okay, i mean, it wasn't you"

    cassia "i think the only people that know about the quest is the ones that sent you on it"

    cassia "...brennan and your party"

    player "yeah thats what i figured...i don't think brennan is going to tell me anytime soon though"

label night_market: 
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

    unknown_brennan "the hunt... was controversial but it was us or them."

    unknown_brennan "and if we chose them, they would've killed us."

    show story scenes 

    unknown_brennan "we weren't always like this..."

    unknown_brennan "we didn't need it."

    unknown_brennan "but once they started, they couldn't live without it."

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

    "you can feel yourself growing angry."

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
    
    show like mystery people here 
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

    menu:
        "answer the door"

        "don't answer the door"
    
    annie "come to the door already, no point in hiding!"

    "you get up and open the door to find annie there."

    player "???"

    annie "brennan wanted me to give you this."

    "she hands you a box."

    player "what is this?"

    annie "don't know, he told me specifically not to open it."

    player "uh... thanks?"

    "annie stands there like she's expecting something."

    menu: 
        "give her money."

            annie "what the heck. i don't want that."

            player "???"

            annie "..."

        "stare back at her."

            annie "..."

            player "..."

    annie "he was right."

    "she turns away and leaves."

    player "does she know? did brennan tell everyone?"

    "you look at the box in your hands. maybe it could provide you with the answers you were seeking."

    menu:
        "open the box."

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

    brennan "PLACEHOLDER come here!"

    "that voice sounded like brennan's except a lot younger."

    og "comming!"

    "your body starts moving without your permission."

    "as you continue to run you see the rest of your friends."

    "they look significantly younger."

    maryanne "my parents said if i did really good on the next evaluation then they'll get me that new game!"

    lou "no fair! ugh my parents said that i can only get books. what if i become a big nerd."

    annie "you already are~"

    "lou starts chasing annie around."

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

    brennan "save your breath, ever since she got that game she's been gone."

    "brennan snatches maryannes game out of her hands."

    maryanne "HEY I WAS PLAYING WITH THAT!"

    annie "hey lesser of the two ann's here look at what i got!"

    "maryanne pauses her chase of brennan to look."

    maryanne "oh neat what even is that?"

    annie "uhh... actually i'm not sure."

    og "looks like a..."

    #looks like one of those rorschach test 
    menu: 
        "looks like a bear.":
            jump bear

        "looks like a late 1800's painting of the esteemed dr louis pierre wilson teaching a class to a group of depressed university students.":
            jump louispierre

label bear: 

label louispierre: