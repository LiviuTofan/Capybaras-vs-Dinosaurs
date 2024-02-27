label home:
    scene black
    centered "{cps=7}{b}Let's start the adventure...{/b}{/cps}{w=0.5}{nw}"
    stop music fadeout 1.0

    scene bg home

    call give_flower

    play music "/audio/lake.mp3" volume 2
    show suzuki happy at left 
    suzuki "Yamaha, the day is as perfect as your smile. How about we escape to the lake?"

    show yamaha happy at right
    yamaha "Suzuki, you always know how to make my heart flutter. The lake sounds like a wonderful idea."

    jump way_to_lake


label way_to_lake:
    scene bg way
    call give_flower

    jump cave

label cave:
    play music "/audio/cave.mp3" volume 3.0
    scene black
    centered "{cps=8}{b}Somewhere far away, beneath the ground...{/b}{/cps}{w=0.5}{nw}"
    with dissolve

    scene dinosaurs cave
    with dissolve

    show teddy simple at left
    teddy "For years, we've been confined here, in darkness and dust. I've had enough! You do as you please, but I'm starting to dig a way towards the light."

    show boss simple at right
    boss "Do as you wish, but there will be no light anymore, the meteorite has destroyed everything."

    scene dinosaur dig
    with dissolve
    "{cps=20}Boss, see what I see? Finally, sunbeams are entering the cave, I've found the way.{/cps}{w=0.5}{nw}"
    
    jump lake

label lake:
    stop music fadeout 1.0
    play music "/audio/lake.mp3" volume 2
    scene bg lake
    show suzuki happy at left
    with dissolve
    suzuki "Today feels different, like the universe is conspiring to make our time at the lake even more special."

    show yamaha happy at right
    with dissolve
    yamaha "Here, by the lake, with you... it feels like time stands still. Each shared moment becomes a cherished note in the symphony of our hearts"
    stop music fadeout 1.0

    call give_flower

    play music "/audio/dino.mp3"
    scene bg lake2
    "{cps=20}Suddenly, an inexplicable darkness draped over the idyllic scene, casting a shadow on their romantic escapade.{/cps}{w=0.5}{nw}"

    show suzuki poker at left
    with dissolve
    suzuki "Yamaha, something's not right. Do you feel that?"
    stop music fadeout 1.0
    play music "/audio/shake.mp3" volume 4.0
    with Shake((0, 0, 0, 0), 2.0, dist=30)

    scene bg lake
    stop music fadeout 1.0
    play music "/audio/sad.mp3"
    show suzuki sad at left
    suzuki "Yamaha! No, this can't be happening!"
    "{cps=20}The laughter that once echoed by the lake transformed into desperate cries. Suzuki was left alone with the echoes of their moments and a broken heart.{/cps}{w=0.5}{nw}"
    suzuki "I won't let anything keep us apart, Yamaha. Whatever it takes, I'll bring you back!"
    "{cps=20}Suzuki starts looking around for Yamaha or signs of her.{/cps}{w=0.5}{nw}"
    call call_or_steps


label call_or_steps:
    scene bg lake
    show suzuki sad at left
    with dissolve
    menu:
        "Follow the footsteps":
            $ lookedForFootsteps = True
            stop music fadeout 1.0
            play music "/audio/lake.mp3" volume 2.0
            scene bg steps
            "{cps=20}The footsteps get into high grass and disappear, Suzuki cannot track them anymore{/cps}{w=0.5}{nw}"
            menu:
                "Go back":
                    call call_or_steps
        "Try to call Yamaha":
            show suzuki sad at center
            suzuki "Yamaha! Where are you?{w=0.5}{nw}"
            scene bg lake
            show suzuki phone3 at center
            play music "/audio/iphone.mp3"
            show suzuki phone3 at center
            pause 2.0
            call zvanok

label zvanok:
    scene bg lake
    show phoneCall

    menu:
        "Answer":
            jump discussion
