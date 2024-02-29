label suzuki_call_agent:
    stop music fadeout 1.0
    play music "/audio/suspans.mp3" volume 0.5
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
    scene bg city
    show agent2 capy at right
    stop music fadeout 1.0
    play music "/audio/lake.mp3" volume 2
    agent "Suzuki! What is happening?"
    jump follow_the_blood

label follow_the_blood:
    scene bg city
    show agent2 capy at right
    show suzuki focused at left
    suzuki "Hurry up, we have to find him! Follow the blood trail on the earth."

    scene blood way
    pause 1.5
    scene black
    stop music fadeout 1.0
    play music "/audio/cave.mp3" volume 3.0
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

    if agencyReputation >= 1: # aici sa fie 1
        jump suzuki_choose1
    else:
        jump suzuki_choose2


label suzuki_choose1:
    menu:
        "Continue with Capybara Agency":
            suzuki "Please, I have helped you so far, let’s grab that dinosaur, he knows where Yamaha is."
            jump cave_end # this branch where capybaras lost

        "Ask the agency for help":
            jump ask_agent_for_help

        "Go separately to find Teddy.":
            jump with_teddy #branch 3


label suzuki_choose2:
    menu:
        "Continue with Capybara Agency":
                suzuki "Please, I have helped you so far, let’s grab that dinosaur, he knows where Yamaha is."
                jump cave_end # this branch where capybaras lost

        "Go separately to find Teddy.":
            jump with_teddy #branch 3


label cave_end:
    scene black
    centered "{cps=20}They follow the path until they find themselves inside a large room with a big door.{/cps}{w=0.5}{nw}"
    scene cave door
    pause 1.5

    play music "/audio/fbi.mp3" volume 0.3
    "{cps=20}The other agents follow from behind. They breach the door and find the dinosaur boss.{/cps}{w=0.5}{nw}"
    stop music fadeout 1.0

    scene cave boss
    play music "/audio/cave.mp3" volume 3.0
    pause 1.5
    show agent2 capy at right
    agent "Keep your hands raised! It’s over! "
    show boss2 nervous at left
    boss "And what if I do not?"
    
    scene cave boss2
    agent "We will shoot you dead, there is enough witness against you! Yow will not escape! "
    boss "Do as you wish. It is my fault that I have trusted that brainless lizards do the important work. I have to pay for my mistakes now. I will not even try to resist."
    agent "Perfectly, so you are coming with us! Put the cuffs on him, guys."
    "The capybara agents approach to cuff Rex, with multiple guns pointed at him. In that same moment, a swarm of pterodactyls and dinosaurs ambush the capybara agents as if following a secret order from their King."
    play music "/audio/shake.mp3" volume 4.0
    with Shake((0, 0, 0, 0), 2.0, dist=30)

    stop music fadeout 1.0
    scene cave boss3
    play music "/audio/cave.mp3" volume 3.0
    pause 2.0
    "Suzuki rushes to the exit, in an attempt to find Yamaha and gather allies."

    scene cave interior
    "He returns to the track where they decided to go the other way, with dinosaurs following his steps."
    show suzuki focused at left
    suzuki "That dinosaur must have been here, the path is still marked by his blood. I have to find him."
    "Suzuki’s resolve is getting stronger as he heads on the path that the wounded dinosaur left."
    stop music fadeout 1.0

    play music "/audio/sad.mp3"  volume 0.5
    scene black
    centered "{cps=20}But he didn't expact that...{/cps}{w=0.5}{nw}"

    scene caged capybaras
    pause 2.0
    "Suzuki sees his beloved Yamaha dead in a cage, with Teddy lying on the floor, full of wounds, with keys to the cage in his hands, as if he wanted to free Yamaha to prove his intentions to Suzuki."
    show suzuki2 sad at right
    suzuki "How? Why? Where have I failed? It all was for nothing. Yamaha, the agents, even this dinosaur were killed. What remains for me?"

    scene black
    centered "{cps=20}With these words, a dinosaur strikes behind Suzuki, leaving him dead next to Yamaha’s body."
    scene dead
    pause 2.5
    suzuki "At least we are together. See you soon, Yamaha."
    "These were his last words as the image in front of him started to fade away."

    scene black
    centered "{cps=20}That day, the dinosaur king got rid of the capybara agency, that was his biggest threat, allowing him an attack over the capybara town. Soon, they invaded the whole world, bringing destruction and desolation to everything.{/cps}{w=0.5}{nw}"
    scene dinosaurs power
    pause 2.0
    scene black
    centered "{cps=20}Finita La Commedia...{/cps}"

    jump home