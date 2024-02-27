label suzuki_call_agent:
    show suzuki phone at left
    suzuki "Agent 007! Come here! Fast, I have caught it."
    scene capybara agency
    show agent capy at right
    agent "What do you mean Suzuki?"
    scene bg city
    show suzuki phone at left
    suzuki "A DINOSAUR!"
    
    scene black
    centered "{cps=20}Agents rush to the place. While Teddy tries to run away, Suzuki tries to catch him, but only scratches him, letting Teddy to make blood marks on the earth.{/cps}{w=0.5}{nw}"
    show agent2 capy at right
    scene bg city
    show agent2 capy at right
    agent "Suzuki! What is happening?"
    show suzuki focused at left
    suzuki "Hurry up, we have to find him! Follow the blood trail on the earth."

    scene blood way
    pause 1.5
    scene black
    centered "{cps=20}They both run until they find a hole in the ground, where the blood trail leads.{/cps}{w=0.5}{nw}"
    scene cave entry
    pause 1.5
    scene black
    centered "{cps=20}They decide to follow it inside the cave and find themselves at a crossroad.{/cps}{w=0.5}{nw}"
    scene cave interior
    pause 1.5
    show agent2 capy at right
    agent "So? What do you think? The trail leads on one side, but who knows what is on the other? Who was that at all?"
    show suzuki nervous at left
    suzuki "That was the dinosaur that caught Yamaha. We have to find him."
    agent "The choice is yours."

    if agencyReputation >= 1:
        jump suzuki_choose1
    else:
        jump suzuki_choose2


label suzuki_choose1:
    menu:
        "Continue with Capybara Agency":
            suzuki "Please, I have helped you so far, let’s grab that dinosaur, he knows where Yamaha is."
            jump cave_end

        "Go separately to find Teddy.":
            jump da #branch3


label suzuki_choose2:
    menu:
        "Go with the agent and abandon the pursuit.":
            jump da #branch2

        "Go separately to find Teddy.":
            jump da #branch3


label cave_end:
    scene black
    "{cps=20}They follow the path until they find themselves inside a large room with a big door."
    scene cave door
    #zvuk de fbi open the door
    pause 2.0
    scene black
    "{cps=20}The other agents follow from behind. They breach the door and find the dinosaur king."
    
    scene cave boss
    show agent2 capy at right
    agent "Keep your hands raised! It’s over! "
    show boss2 nervous at left
    boss "And what if I do not?"
    
    scene cave boss2
    show agent2 capy at right
    agent "We’ll shoot you dead, there is enough witness against you! Yow will not escape! "
    show boss2 nervous at left
    boss "Do as you wish. It is my fault that I have trusted that brainless lizards do the important work. I have to pay for my mistakes now. I will not even try to resist."
    agent "Perfectly, so you’re coming with us! Put the cuffs on him, guys."
    "The capybara agents approach to cuff Rex, with multiple guns pointed at him. In that same moment, a swarm of pterodactyls and dinosaurs ambush the capybara agents as if following a secret order from their King."
    scene cave boss3
    pause 2.0
    "Suzuki rushes to the exit, in an attempt to find Yamaha and gather allies."

    scene cave interior
    "He returns to the track where they decided to go the other way, with dinosaurs following his steps."
    show suzuki focused at left
    suzuki "That dinosaur must have been here, the path is still marked by his blood. I have to find him. "
    "Suzuki’s resolve is getting stronger as he heads on the path that the wounded dinosaur left."
    scene black
    "{cps=20}But he didn't expact that...{/cps}{w=0.5}{nw}"

    scene caged capybaras
    pause 1.5
    "Suzuki sees his beloved Yamaha dead in a cage, with Teddy lying on the floor, full of wounds, with keys to the cage in his hands, as if he wanted to free Yamaha to prove his intentions to Suzuki."
    show suzuki sad at left
    suzuki "How? Why? Where have I failed? It all was for nothing. Yamaha, the agents, even this dinosaur were killed. What remains for me?"

    scene black
    "{cps=20}With these words, a dinosaur strikes behind Suzuki, leaving him dead next to Yamaha’s body."
    scene dead
    suzuki "At least we are together. See you soon, Yamaha."
    "These were his last words as the image in front of him started to fade away."

    scene black
    "{cps=20}That day, the dinosaur king got rid of the capybara agency, that was his biggest threat, allowing him an attack over the capybara town. Soon, they invaded the whole world, bringing destruction and desolation to everything.{/cps}{w=0.5}{nw}"
    scene dinsaurs power
    pause 1.5
    scene black
    centered "{cps=20}Finita La Commedia{/cps}"