import random
from time import sleep
import sys

#This function serves as the game pathing
def main():
    
    data = {'room':1,'tracker':0,'matcherHint':0,'player':['name',0,0],'inv': {}, 'person':'', 'weapon':'','lives': 3,'dead':False, 'skip':False, 'body':False}
    # tracker = Number of room movements
    # room = Which room are you in
    # matcherHint = Tells player about matcher
    # player = [name, money, deaths]
    # person = Who is the murderer
    # weapon = Which weapon was used
    # lives = Number of lives
    # dead = boolean check
    # body = body check

    while True:
        data['dead'] = False #Sets dead boolean back to false, after death occurs
        
        if data['player'][2] == 0: #calls introduction. Bypasses if death occurs
            intro(data)
            
        answer(data) #Generated a random murderer and weapon

        #print(data['person']) #Debug Tool
        #print(data['weapon'])
    
        while True:
            if data['dead'] == True:
                room(data)
                break
            if data['tracker'] == 0:
                living(data)            
            else:           
                options(data)
                
#This function serves as the introduction
def intro(data):
    while True:
        name = input('What is your name?\n') #Allows player to name their character
        if name == '':
            continue
        else:
            data['player'][0] = name
            break
    print('NOTE: If you see an ellipsis (...), press enter to continue')
    skip = input('...')
    if matcher([skip,'skip']): #Debug tool
        data['skip'] = True
        return
    else:
        pass
    print('"Sorry I can’t be there with you tonight, Detective',data['player'][0],'. \
But the crime unit is already at the scene waiting for your arrival.”')
    input('...')
    print('You hang up the phone.')
    input('...')
    print('Up ahead, you see the famed mansion owned by Mr. Leung.')
    input('...')
    print('You’d think that the billionaire would be immune to petty crimes, but things happen they say.')
    input('...')
    print('“Glad you can make it, Detective', data['player'][0],'. I’m Chief Williams. There’s been a homicide. Mr. Leung has been murdered. \
Apparently he was supposed to have guests over tonight and they found him dead on arrival. They’re waiting inside.”\n')
    sleep(2)
    print('The Mansion Murder\n')
    sleep(2)
    print('By Nicholas Leung')
    print('A Cisc 121 Assignment')
    input('...')
    

#This function serves as the opening room
def living(data):

    if data['tracker'] == 0:
        print('You are in the living room. In front of you lies the corpse of Mr. Leung. \
The suspects, Vincent, Howard, and Chester, are all in the room, seemingly minding their own business. Despite the beautifully decorated room, a somber \
atmosphere fills in the air.')
        input('...')
        print('"Here are the three guests that Mr. Leung invited tonight. You can ask them questions or gather evidence around the house, \
but I would definitely examine the body first."')
        input('...')
        print('"When you\'ve figured it out or if you need some help, come see me and we\'ll get take care of business"')
        input('...')
        data['tracker'] += 1
       
    if data['matcherHint'] == 0:
        print('NOTE: You can type "help" to get a full list of commands and "options" to display the options that are available to you.')
        input('...')
        print('NOTE: No need to type in the whole word, as long as your input is a substring of the input.')
        input('...')
        data['matcherHint'] = 1

    options(data)

#This function holds the game's option tree
def options(data):
    room(data)
    print('> Look around.')
    print('> Examine.')
    if data['room'] == 1: #Only available if they are in the living room       
        print('> Approach.')
    print('> Leave the room\n')

    while True:
        userInput = input('What do you do?\n')
        if matcher([userInput,'look around']): #Allows player to look around the room
            look(data)
        elif matcher([userInput,'examine']): #Allows player to interact with objects
            examine(data)
        elif matcher([userInput,'approach']) and data['room'] == 1: #Allows player to interact with people
            dialogue(data)
            if data['dead'] == True:
                return
            else:
                continue
            
        elif matcher([userInput,'leave the room']): #Allows the player to change rooms
            if data['skip'] == False and data['body'] == False: #Only allows players to explore if they have examined the body
                print('\nYou should examine the body before you look around the mansion.') 
                input('...')
            else:
                move(data)
                return
        elif matcher([userInput,'inventory']): #Displays your inventory and the amount of each item you have
            if len(data['inv']) == 0:
                print('You have nothing on you.')

            else:
                print('You have on you:')
                for x in data['inv']:
                    print(x,'x',data['inv'][x] )
            print()
        elif matcher([userInput,'options']): #Displays what options you have available to you
            print('> Look around.')
            print('> Examine.')
            if data['room'] == 1:        
                print('> Approach.')
            print('> Leave the room\n')
        elif matcher([userInput,'room']): #Displays what room you currently are in
            room(data)                
        elif matcher([userInput,'map']): #Displays a map of the mansion
            map(data)
        elif matcher([userInput,'lives']): #Displays the number of lives you have left
            print('You have', data['lives'],'lives left.\n')
        elif matcher([userInput,'money']): #Displays the amount of money you have
            print('You have', data['player'][1], 'dollars.\n')
        elif matcher([userInput,'visited']): #Displays the number of rooms you have visited
            print('You have visited:',data['tracker'],'rooms so far.\n')
        elif matcher([userInput,'help']): #Provides help
            help(data)
        elif matcher([userInput,'name']): #Displays player name
            print('And his name is',data['player'][0],'!!!\n')
        elif matcher([userInput,'deaths']): #Displays number of deaths
            print('You have died',data['player'][2],'times.\n') 
        else:
            print('NOTE: You can type "help" for input guidance.\n')

#This function executes when the player wants to look around            
def look(data):
    print('You look around the room.\n')
    if data['room'] == 1:
        print('The living room is impressively well furnished. In front of you are the guests, who are currently seated on a leather [couch]. \
Combined with the [table] in front, these pieces of furniture shout "perfection". \
On the far side of the room, Chief Williams is staring into a [fireplace]. The dim, flickering light creates dancing shadows around the room. \
If not for the [corpse] in the middle of the room, tonight\'s gathering would have \
probably been quite lovely.\n')
        return
    if data['room'] == 2:
        print('Your footsteps echo throughout the main hall for each step you take on the glistening marble floor. \
The light in the [closet], where you previously put your [coat], is on. Next to the [door] sits a collection of [umbrellas].\n')
        return
    if data['room'] == 3:
        print('A surprisingly simple bedroom for someone who owned such a grand house. Occupying most of the room is the king size [bed], \
adorned with a small [side table]. Otherwise, the room is rather empty.\n')
        return
    if data['room'] == 4:
        print('The study is probably the most lived-in place in the mansion. Like any big CEO, Mr. Leung had a huge [desk] littered with papers \
stacked up to the ceiling and a [chair] akin to a throne. Behind the [desk] is a wall lined with enough [books] to entertain for a lifetime.\n')
        return
    if data['room'] == 5:
        print('Despite how busy Mr. Leung must have been, it seems that he always had time for his hobby as a chef. A [counter] fills the \
space in the centre of the room, while a [stove] occupies the entirety of the far side of the wall.\n')
        return

#This function serves as the movement between rooms    
def move(data):

    room(data)
    if data['tracker'] == 1 and 'map' not in data['inv']: #Provides a hint to map
        print('\nIf you help with directions, a [map] is sitting on the [table].')
        input('...')
    if data['room'] in [1,2,5]: #Prints available movement options
        print('> North')
    if data['room'] in [2,4]:
        print('> East')
    if data['room'] in [3,5]:
        print('> West')
    if data['room'] in [2,3,4]:
        print('> South')
    if 'map' in data['inv']:
        print('> Map')
    print('Back\n')

    while True: #Movement between rooms
        userDir = input('Which direction?\n')
            
        if matcher([userDir,'north']) and data['room'] in [1,2,5]:
            print('You head North.')
            if data['room'] == 1:
                data['room'] = 2
            elif data['room'] == 2:
                data['room'] = 4
            elif data['room'] == 5:
                data['room'] = 3
            data['tracker'] += 1
            break

        elif matcher([userDir,'east']) and data['room'] in [2,4]:
            print('You head East.')
            if data['room'] == 2:
                data['room'] = 5
            elif data['room'] == 4:
                data['room'] = 3
            data['tracker'] += 1
            break
        
        elif matcher([userDir,'west']) and data['room'] in [3,5]:
            print('You head West.')
            if data['room'] == 3:
                data['room'] = 4
            elif data['room'] == 5:
                data['room'] = 2
            data['tracker'] += 1
            break
        
        elif matcher([userDir,'south']) and data['room'] in [2,3,4]:
            print('You head South.')
            if data['room'] == 2:
                data['room'] = 1
            elif data['room'] == 3:
                data['room'] = 5
            elif data['room'] == 4:
                data['room'] = 2
            data['tracker'] += 1
            break

        elif matcher([userDir,'map']):
            map(data)
        
        elif matcher([userDir,'back']):
            break
        
#Allows players to examine objects of interest        
def examine(data): 
    while True:
        userInput = input('What do you want to examine?\n')
        if data['room'] == 1: #Objects in Living Room
            if matcher([userInput,'back']):
                return
            elif matcher([userInput,'map']):
                print('You examine the map.')
                input('...')
                print('A convienently placed map of the Leung Mansion.')
                pickup([data,'map'])
                print('\nNOTE: You can now use the map by typing "map".\n')
                return
            elif matcher([userInput,'table']):
                print('You examine the table.')
                input('...')
                print('A hardy table fit for a king and his knights, except for the fact that it\'s not round.')
                input('...')
                print('There is a [map] on the table.\n')
            elif matcher([userInput,'couch']):
                print('You examine the couch.')
                input('...')
                print('A excellent piece to any comfy living room.')
                input('...')
                print('You find a $1 coin under the cushion.\n')
                data['player'][1] += 1
            elif matcher([userInput,'fireplace']):
                print('You examine the fireplace.')
                input('...')
                print('A cozy fire fills the room with a warm glow and the crackling of the wood delivers a satsfying sound.')
            elif matcher([userInput,'body']) or matcher([userInput,'corpse']):
                print('You examine the body.')
                input('...')
                print('Despite being dead, Mr. Leung looks like he\'s sleeping peacefully.')
                input('...')
                if data['weapon'] in ['gun','knife']:
                    print('After close examination, you source an entry wound in the chest.\n')
                    input('...')
                    if data['weapon'] == 'gun':
                        print('It\'s a small hole.')
                    elif data['weapon'] == 'knife':
                        print('It\'s a big hole.')
                if data['weapon'] in ['pillow','tablet']:
                    print('After close examination, you determined the cause of death to be asphyxiation.\n')
                    input('...')
                    if data['weapon'] == 'pillow':
                        print('You find a tiny feather on the body,')
                    elif data['weapon'] == 'tablet':
                        print('He\'s foaming in the mouth.')
                elif data['weapon'] in ['frying pan','umbrella']:
                    print('After close examination, Mr. Leung appears to have suffered blunt force trauma.\n')
                    input('...')
                    if data['weapon'] == 'frying pan':
                        print('There\'s a noticeable dent in his skull.')
                    elif data['weapon'] == 'umbrella':
                        print('You find some splinters in his skull.')
                data['body'] = True
                return
            
            else:
                print('NOTE: You can back out of any input by typing "back"\n')
                
        elif data['room'] == 2: #Objects in Main Hall
            if matcher([userInput,'back']):
                return
            elif matcher([userInput,'umbrellas']):
                print('You examine the umbrellas.')
                input('...')
                print('Brightly colored umbrellas for those wet days.')
                if data['weapon'] in ['frying pan','umbrella']:
                    input('...')
                    print('Could this be what caused Mr. Leung\'s blunt force trauma?')
                pickup([data,'umbrella'])
                return
                
            elif matcher([userInput,'closet']):
                print('You examine the closet.')
                input('...')
                print('A variety of [coats] and empty [hangers] line the closet. You can spot your coat along with those of the other guests.')
            elif matcher([userInput,'hangers']):
                print('It hangs coats, not people.')
                pickup([data,'hanger'])
                return
            elif matcher([userInput,'coats']):
                print('You examine the coats.')
                input('...')
                print('Keeps you warm outside. Best leave them where they belong.')
            elif matcher([userInput,'door']):
                print('You examine the door.')
                input('...')
                print('You can\'t leave now. You have a job to do.')
            elif matcher([userInput,'back']):
                return
            
        elif data['room'] == 3: #Objects in Bedroom
            if matcher([userInput,'back']):
                return
            elif matcher([userInput,'bed']):
                print('You examine the bed.')
                input('...')
                print('A comfy fortress armed with a surplus of [pillows].')
            elif matcher([userInput,'pillows']):
                print('You examine the pillows.')
                input('...')
                print('The softest and most unsuspecting of weapons.')
                if data['weapon'] in ['pillow','tablet']:
                    input('...')
                    print('Could this be what caused Mr. Leung\'s asphyxia?')
                pickup([data,'pillow'])
                return
            elif matcher([userInput,'side table']):
                print('You examine the side table.')
                input('...')
                print('A mahogany side table. There is a [bottle] containing [tablets] on the table.')
            elif matcher([userInput,'tablet']) or matcher([userInput,'bottle']):
                print('You examine the tablets.')
                input('...')
                print('Prescription drugs for some complex condition called "Meme Overdose".\
The instructions read: "Take one whenever you feel salty.')
                if data['weapon'] in ['pillow','tablet']:
                    input('...')
                    print('Could this be what caused Mr. Leung\'s asphyxia?')
                pickup([data,'tablet'])
                return
            
        elif data['room'] == 4: #Objects in Study
            if matcher([userInput,'back']):
                return
            elif matcher([userInput,'desk']):
                print('You examine the desk.')
                input('...')
                print('A beautiful mahogany desk, outfitted with [drawers] and a leather swivel [chair].')
            elif matcher([userInput,'chair']):
                print('You examine the chair.')
                input('...')
                print('You sit in the chair. It feels comfy and expensive.')
            elif matcher([userInput,'drawers']):
                print('You examine the drawers.')
                input('...')
                if data['weapon'] in ['knife','gun']:
                    print('You see that one of the drawers has been left ajar. You open it to find a Beretta M9 and couple 9mm bullets. \
The gun appears to be empty.')
                    input('...')
                    print('Could a gun be the source of the entry wound?')
                else:
                    print('You rummage through the drawers to find a Beretta M9 and a handful of bullets. \
The gun is still loaded.')
            elif matcher([userInput,'gun']):
                print('You examine the gun.')
                input('...')
                print('It\'s well balanced in the hand.')
                pickup([data,'gun']) 
                return
            elif matcher([userInput,'bullets']):
                print('You examine the bullets.')
                input('...')
                print('Small but deadly.')
                pickup([data,'bullet']) 
                return
            elif matcher([userInput,'books']):
                print('You examine the books.')
                input('...')
                print('Colorful books occupy the shelves.')
                pickup([data,'book']) 
                return
        elif data['room'] == 5:
            if matcher([userInput,'counter']):
                print('You examine the counter.')
                input('...')
                print('A marble counter that so clean you can see your reflection. \
A [knife] block filled with assorted knives sits in the middle of the counter.')
            elif matcher([userInput,'knife']):
                if data['weapon'] in ['knife','gun']:
                    print('One of the knives is missing.')
                    input('...')
                    print('Perhaps the entry wound was caused by a knife?')
                else:
                    print('So many knives to choose from. There\'s a kind of [knife] for everything.')
                pickup([data,'knife'])
                return
            elif matcher([userInput,'stove']):
                print('You examine the stove.')
                input('...')
                print('A stack of [frying pans] are sitting on the stovetop.')
                if data['weapon'] in ['frying pan','umbrella']:
                    input('...')
                    print('Maybe a frying pan killed Mr. Leung?')
                    input('...')
                pickup([data,'frying pan'])
                return
            elif matcher([userInput,'back']):
                return
            
#This function serves as the dialogue tree
def dialogue(data):
    print('\nApproach:\n> Chester\n> Howard\n> Vincent\n> Williams\n Back\n')
    while True:
        talk = input('Who do you want to approach?\n')
        if matcher([talk,'chester']): #Approach Chester
            print('You ask Chester what happened.')
            input('...')
            if data['person'] == 'Howard':
                print('"I came here with Vincent when we arrived at the scene and found the body. We called the cops as soon as \
we saw him lying there. Howard apparently running late so we gave him a call. Turns out he wasn’t even going to come, \
had we not called him."')
            if data['person'] == 'Vincent':
                print('"When I got here, the door was unlocked. Vincent and Howard were already here, but arrived too \
late to save him. Vincent looked like he saw Leung’s ghost because how pale he was."')
            if data['person'] == 'Chester':
                print('"The cops were already outside when I got here. They brought me in here and only then did I found \
out that someone killed Leung. Whoever wanted Leung dead must have wanted his money."')
            input('...')
            return
        elif matcher([talk,'howard']): #Approach Howard
            print('You ask Howard what happened.')
            input('...')
            if data['person'] == 'Howard':
                print('"Leung invited me over to the place, but I already had an arrangement. When they found him \
dead, they called me over. It’s unfortunate, but what do I have to do with this?"')
            if data['person'] == 'Vincent':
                print('"When I got here, Vincent was already here. He was looking really panicky. \
He was like: “Oh! Howard, it’s just you.” Or something like that. You’d think he might have killed him."')
            if data['person'] == 'Chester':
                print('"I got here a bit early but there was no answer at the door. I first noticed something was wrong \
when the door was unlocked. When I saw him like this, I called the cops. Vincent came a bit later and we waited together. You \
don’t know how stressful it is babysitting a dead body. Anyways, Chester showed up afterwards. What was weird was that he didn’t \
seem to react much at all."')
            input('...')
            return
        elif matcher([talk,'vincent']): #Approach Vincent
            print('You ask Vincent what happened.')
            input('...')
            if data['person'] == 'Howard':
                print('"Chester and I came together when we found him dead. We called the cops, but they took a long time. \
We also called Howard and he came really quickly, which is odd since he said that he had something to do tonight that’s quite a \
distance from here."')
            if data['person'] == 'Vincent':
                print('"I was the first one to come. Leung was fine when I got here, but he started choking. \
Next thing you know, he’s dead!"')
            if data['person'] == 'Chester':
                print('"I got here by myself and Howard had already arrived. He seemed glad \
to see I came, since a dead guy doesn’t keep great company. I tried to get a hold of Chester, but he wasn’t picking up the phone."')
            input('...')
            return
        elif matcher([talk,'williams']): #Approach Chief Williams
            print('"Have you figured it all out yet? Or do you need more time?"')
            input('...')
            print('1. "I think I know who did it and how."')
            print('2. "I need a bit of help."')
            print('3. "Any thoughts?"')
            print('Back\n')
            while True:
                userInput = input('What do you want to say?\n')
                if userInput == '1': #Making the decision
                    
                    while True:
                        gate = 0
                        while gate == 0:
                            killer = 'blank'
                            person = input('Who is the murderer?\n') #Identifying the murderer
                            if matcher([person,'chester']):
                                killer = 'Chester'
                                break
                            elif matcher([person,'howard']):
                                killer = 'Howard'
                                break
                            elif matcher([person,'vincent']):
                                killer = 'Vincent'
                                break
                            elif matcher([person,'williams']):
                                break
                            elif matcher([person,'back']):
                                gate = 2
                            else:
                                gate = 1

                        if gate == 1:
                            continue
                        elif gate == 2:
                            break
                    
                        while gate == 0:
                            tool = 'blank'
                            weapon = input('What was the murder weapon?\n') #Identifying the weapon
                            if matcher([weapon,'knife']):
                                tool = 'knife'
                                break
                            elif matcher([weapon,'gun']):
                                tool = 'gun'
                                break
                            elif matcher([weapon,'pillow']):
                                tool = 'pillow'
                                break
                            elif matcher([weapon,'frying pan']):
                                tool = 'frying pan'
                                break
                            elif matcher([weapon,'tablet']):
                                tool = 'tablet'
                                break
                            elif matcher([weapon,'umbrella']):
                                tool = 'umbrella'
                                break
                            elif matcher([weapon,'back']):
                                gate = 2
                            
                        if gate == 2:
                            break

                        print('"Thanks for your hard work, Detective. I\'ll take it from here."')
                        print(killer,'was arrested.\n')

                        if killer == data['person'] and tool == data['weapon']: #Correct answer
                            print('You have successfully identified the murderer and the weapon.')
                            input('...')
                            print('Congratulations!')
                            sys.exit()
                        elif killer != data['person']: #Wrong person identified
                            print('Despite your best efforts to identify the murderer,',killer,'was not the murderer. As you have convicted \
the wrong person, the real murderer,',data['person'],', kills you.\n')
                            death(data) #Death Condition
                            return
                        elif tool != data['weapon']: #Wrong weapon identified
                            print('While you have successfully identified the murderer, he was acquitted of all charges as the \
weapon did not match the evidence received from the autopsy. In an act of revenge,',data['person'],'kills you with the same weapon \
he used on Mr. Leung: a', data['weapon'],'.\n')
                            death(data) #Death Condition
                            return
                        
                    
                elif userInput == '2':
                    print('"If you haven\'t already done so, go examine the body to find out the cause of death."')
                    input('...')
                    print('"Try talking to the suspects to figure out what really happened.\
 You can also go look around the place to find clues."')

                elif userInput == '3':
                    print('"If I were you, I\'d look for things that doesn\'t feel right, because I know that Mr. Leung was a \
stickler for keeping things tidy."')
                elif matcher([userInput,'back']):
                    break
            return
        elif matcher([talk,'back']):
            return
        
#Allows for evaluation of player's input    
def matcher(match): 
    strand = match[0]
    string = match[1]
    if len(strand) < 1:
        return False
    if strand.lower() == string[:len(strand)]:
        return True
    return False

#Pick up function and adding items to the inventory
def pickup(obj): 
    data = obj[0]
    name = obj[1]
    while True:
        add = input('Pick it up?\n')
        if matcher([add,'yes']):
            if name in data['inv']:
                data['inv'][name] += 1
            else:
                data['inv'][name] = 1
            print('You picked up one',name)
            return
        elif matcher([add,'no']):
            return
        
#Provides players with a visual of the mansion's map
def map(data):
    if 'map' in data['inv']: 
        print('\n[Study]  -  [Bedroom]')
        print('  |             |')
        print('[Hall]   -  [Kitchen]')
        print('  |')
        print('[Liv. Rm.]\n')
        return
    else:
        print('You don\'t have a map on you.\n')
        return
    
#This function displays which room the player is in
def room(data): 
    if data['room'] == 1:
        print('You are in the [Living Room].\n')
    elif data['room'] == 2:
        print('You are in the [Main Hall].\n')
    elif data['room'] == 3:
        print('You are in the [Bedroom].\n')
    elif data['room'] == 4:
        print('You are in the [Study].\n')
    elif data['room'] == 5:
        print('You are in the [Kitchen]\n.')
    return

#This function provides assistance to players
def help(data):
    print('\nNOTE: Object of interest are denoted as: [Object]. You can further examine these objects, which may reveal more \
objects of interest.\n')
    print('List of commands: [help, name, deaths, room, lives, money, inventory, visited, options]\n')
    
#This function randomizes a murderer and a weapon    
def answer(data): 
    person = random.randint(1,3)
    if person == 1:
        data['person'] = 'Chester'
    elif person == 2:
        data['person'] = 'Howard'
    elif person == 3:
        data['person'] = 'Vincent'

    weapon = random.randint(1,6)
    if weapon == 1:
        data['weapon'] = 'knife'
    elif weapon == 2:
        data['weapon'] = 'gun'
    elif weapon == 3:
        data['weapon'] = 'pillow'
    elif weapon == 4:
        data['weapon'] = 'frying pan'
    elif weapon == 5:
        data['weapon'] = 'tablet'
    elif weapon == 6:
        data['weapon'] = 'umbrella'

#This function executes the player's death
def death(data):
    data['room'] = 1 #Sent back to the living room
    data['player'][2] += 1 #Adds 1 to death count
    data['inv'] = {} #Empties inventory
    data['lives'] -= 1 #Removes a life
    data['dead'] = True

    print('You Died.')
    input('...')
    print('Your inventory and money has been reset.')
    input('...')
    print('The murderer and the weapon has now been changed.')
    input('...')

    if data['lives'] == 0: #Game over
        print('You have no more lives.')
        input('...')
        print('Game Over.')
        sys.exit()
    else:
        print('You have',data['lives'],'lives left.\n')
    
main()

    
