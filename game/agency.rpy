label discussion:
    stop music fadeout 1.0
    play music "/audio/answer.mp3" volume 3.0
    scene capybara agency
    with fade
    show agent capy at right
    stop music fadeout 1.0
    agent "Suzuki, this is the Capybara agency. We know about Yamaha's abduction. It's time for you to join us and learn the truth about the dinosaurs."

    scene bg lake
    show suzuki phone at left
    suzuki "The truth? What's going on? Tell me!"

    play music "/audio/end call.mp3"
    with Shake((0, 0, 0, 0), 2.0, dist=15)
    scene black
    pause 0.1
    stop music fadeout 1.0

    scene capybara agency
    show agent2 capy at right
    agent "There's more to this world than you know, Suzuki. The dinosaurs have a hidden agenda, and Yamaha is in grave danger. You must become the hero Capybara City needs."

    show suzuki nervous at left
    suzuki "Why would I believe you?"
    agent "You have no other option"
    agent "The dinosaurs are desperate for resources. They believe reclaiming the world is the only way to survive. Your love for Yamaha puts you at the center of this struggle, Suzuki. You must save her and prevent a catastrophic conflict."
    suzuki "What is all this stuff about dinosaurs? I don’t care about them, as soon as I get Yamaha back. Yamaha… My beloved Yamaha..."
    agent "Suzuki, here’s the deal. We know your grief and your anger, we know that you are impatient and do not understand why we are wasting your time here. But listen close if you want to see Yamaha again."
    agent "Long time ago, our world was somehow different, that is what our researchers and intel say. To cut unnecessary details off, there are dinosaurs living under the surface of the Earth, something happened long ago and they remained there."
    
    menu:
        "Ok, so what does it tell us?":
            $ agencyReputation += 1
            suzuki "Ok, so what does it tell us?"
            agent "That they somehow got out, we do not really know the reasons, but some of our scientists say that their appearance may be related to a downfall in their civilization. We have been told of other cases of capybara kidnaps, but they all had to remain hidden to avoid panic." 
        "Nice bedtime story, but where is Yamaha?":
            $ agencyReputation -= 1
            suzuki "Nice bedtime story, but where is Yamaha?"
            agent "Suzuki, this will not help, please try to focus and you will find your Yamaha!"
    
    agent "Going on, we want to find the reason for this and get rid of it. We do not know the scale of the problem, that is yet to be found. That is yet to be found by you."
    scene black
    with dissolve
    centered "{cps=20}Suzuki and the agents headed to the place where Yamaha was kidnapped. They started looking around for clues.{/cps}{w=0.5}{nw}"
    centered "{cps=20}Suzuki finds a heap of scales and decides to show them to the agents.{/cps}{w=0.5}{nw}"

    jump clues

label clues:
    play music "/audio/lake.mp3" volume 2
    scene bg lake3
    pause 1
    show suzuki focused at left
    suzuki "Come here! Look what I found!"
    show agent2 capy at right
    agent "Great job, we’ll search out the zone and will take these scales to our labs to identify their provenience."
    suzuki "And what do I do now? Where is Yamaha? How does this help?"
    agent "Patience, Suzuki, patience. She should not be in danger."
    menu:
        "How can you be so sure?! How can you know anything like that?!":
            suzuki "How can you be so sure?! How can you know anything like that?!"
            agent "Please, do not lose your temper. We want to find her as much as you do. Usually, the capybaras reported being kidnapped appear nearby the place they were last seen. However, they are very tired and for some reason they are very weakened. It seems like they try to torture them to obtain information."

            menu:
                "Great, now I know she may be tortured, really saved the day!":
                    $ agencyReputation -= 1
                    suzuki "Great, now I know she may be tortured, really saved the day!"

                "Ok, but how do we save her then? What does it mean?":
                    $ agencyReputation += 1
                    suzuki "Ok, but how do we save her then? What does it mean?"
                    agent "This means that as soon as we find her, the better state she will be in."
        "I really hope so…":
            suzuki "I really hope so…"
            agent "Don’t worry son, it’ll be fine."
    agent "Ok, Suzuki, you go north and search for something more. Maybe you will find some other clues."
    
    if lookedForFootsteps:
        jump cigarette1
    else:
        jump cigarette2



label cigarette1:
    scene bg lake3
    menu:
        "Go for the footsteps":
            scene bg steps
            show suzuki sad at left
            suzuki "Here it all happened. Maybe if we did not go to the lake that day… Please, Yamaha, keep strong."
            
            menu:
                "Go back":
                    call cigarette1

        "Go away and light up a cigarette":
            jump first_meet

label cigarette2:
        suzuki "What are these tracks? Maybe I should follow them?"
        scene black
        "{cps=20}Suzuki follows the tracks and the tracks fade into the high grass.{/cps}{w=0.5}{nw}"
        scene bg steps
        "{cps=20}The footsteps get into high grass and disappear, Suzuki cannot track them anymore{/cps}{w=0.5}{nw}"
        
        call cigarette1