label with_teddy:
    scene cave interior
    show suzuki focused at left
    suzuki "Agent 007, I must go the other way. That dinosaur had information about Yamaha’s location. I must find him and rescue her."
    show agent2 capy at right
    agent "Do as you wish, son, but we will not be able to help you. We have to find their leader."
    suzuki "Hey, listen! I helped you, you have said that you would help me too, what’s the matter now?"
    agent " You did find the way to your girlfriend, now you can choose to go and find her by yourself, or help us do our task till the end and then we will find her together."

    menu:
        "Go back and choose another option":
            if agencyReputation >= 1: # aici sa fie 1
                jump suzuki_choose1
            else:
                jump suzuki_choose2

        "Go without the agents":
            suzuki "I will find her myself. Thank you for nothing."
            jump with_teddy2


label with_teddy2:
    scene black
    centered "{cps=20}Suzuki heads on the path of the dinosaur he wounded, until he meets a huge door.{/cps}{w=0.5}{nw}"
    scene cave door
    "{cps=20}Teddy ambushes him from behind and captures him, trying to convince him once more.{/cps}{w=0.5}{nw}"
    show teddy2 simple at right
    teddy "Suzuki, please! Think one more time, Yamaha is right behind that door, but the room is guarded, we can’t get her if we rush inside like that. Help me and I will help you."
    suzuki "How can I be so sure about it? What if you are tricking me?"
    show teddy keys at right
    teddy "Here are the keys to her cage and other capybara’s cages. I swear on my word that they have not been injured, you can look through the lock, she is fine. It was my order to do nothing to them, and you can’t imagine how hard it was to get approval."
    suzuki "So what now?"
    show teddy2 simple at right
    teddy "Where are the agents?"
    suzuki "We split paths, I went for you, they went in another direction."
    teddy "Then we must hurry, they must have arrived at the dinosaur boss's room. They will surely be killed, the room has a big system of tunnels with guards inside them."
    suzuki "Lead then now"
    
    jump teddy_and_suzuki


label teddy_and_suzuki:
    scene cave interior
    "{cps=20}Teddy and Suzuki head through a shortcut till they arrive right above the dinosaur boss’s throne.{/cps}{w=0.5}{nw}"
    scene cave hole
    show suzuki focused at left
    show teddy2 simple at right
    pause 1.5

    scene caave boss2
    pause 1.0
    show agent2 capy at left
    agent "Put your hands up! You are arrested for all the crimes you have committed!"
    show boss2 nervous at right
    boss "Oh, so bad for me! I must pay for my sins then. Go ahead and cuff me. "
    agent "Grab him, guys!"

    scene cave hole
    show suzuki focused at left
    show teddy2 simple at right
    menu:
        "Tell them about the trap":
            suzuki "Wait! This is a trap!"
            teddy "What have you done? You blew up our cover!"

        "Wait":
            suzuki "What do we do? He will kill them!"
            teddy "Don’t worry, wait for the moment, trust me."
    
    scene black
    "{cps=20}Teddy jumps from above on the dinosaur boss, immobilizing him. Agent Milton stays in shock and aims his gun at each of them.{/cps}{w=0.5}{nw}"
    
    scene cave boss2
    show suzuki focused at left
    suzuki "Agent 007! Now! Capture him, this dinosaur is helping us!"
    "Meanwhile, guards started to swarm the room, and the agents are fighting them while Teddy and the boss are trying to stop each other."
    
    scene cave boss3
    suzuki "I will do this myself… For you, Yamaha. Agent Milton, throw me something!"
    "Agent 007 throws Suzuki a huge rope, which he uses to tie down the dinosaur boss with the help of Teddy, while the agents are fighting the other guards"
    show teddy nervou at right
    teddy "Stop right now! As the boss has fallen, through our laws I am the one to inherit his power. All guards are ordered to retreat."
    show agent2 capy at left
    agent "Now you raise your hands and stand still! We have lots to discuss."
    teddy "There is no need. I ask for a peace treaty from you. Our previous ruler has been tyrannical, putting his desires above the desires of his people. We got rid of him. Now, I can give you my word, that the dinosaurs will not bother capybaras anymore."
    agent "Ok, I trust you, you saved our lives when you could have easily killed us. We will ensure that peace is maintained."
    show suzuki nervous at right
    suzuki "That is very great, but I have done all that to get Yamaha."
    show teddy2 simple at left
    teddy "Follow me."

    scene black
    "{cps=20}Teddy leads Suzuki back to the room and orders the guards to stand still and free all capybaras. They were released and told what had happened.{/cps}{w=0.5}{nw}"
    
    scene find yamaha
    show yamaha shy at left
    yamaha "Suzuki! You are my hero! I feared I would never see you again."
    show suzuki shy at right
    suzuki "Yamaha, I love you so much, I will never let you alone again."
    show teddy2 simple at left
    teddy "Thank you, Suzuki. You are now a symbol of peace and love for both our nations. You have become a hero."

    scene black
    centered "{cps=20}Suzuki and Yamaha get married soon after, and Suzuki takes a core position in the new Capybara Ministry of International Integration, building a good relationship between dinosaurs and capybaras alongside Teddy.{/cps}{w=0.5}{nw}"
