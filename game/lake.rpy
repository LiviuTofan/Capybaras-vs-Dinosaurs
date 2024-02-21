label home:
    scene black
    centered "{cps=7}{b}Let's start the adventure...{/b}{/cps}{w=0.5}{nw}"
    stop music fadeout 1.0

    play music "/audio/lake.mp3"
    scene bg home
    show happy suzuki at left # smiling, invitingly
    with dissolve
    suzuki "Yamaha, the day is as perfect as your smile. How about we escape to the lake?"

    show happy yamaha at right # giggling
    with dissolve
    yamaha "Suzuki, you always know how to make my heart flutter. The lake sounds like a wonderful idea."

    jump way_to_lake


label way_to_lake:
    scene bg way
    show rose suzuki at left
    with dissolve

    suzuki "Yamaha, this flower is for you, a delicate echo of the beauty you bring into my world."
    $ roses += 1
    show text "{i}{color=#A94064}You now have [roses] rose.{/color}{/i}" at top
    show shy yamaha at right
    with dissolve
    "Suzuki, your words and this beautiful flower create a symphony of warmth in my heart."
    stop music fadeout 1.0

    jump cave

label cave:
    play music "/audio/cave.mp3" volume 3.0
    scene black
    centered "{cps=8}{b}Somewhere far away, beneath the ground...{/b}{/cps}{w=0.5}{nw}"
    with dissolve

    scene dinosaurs cave
    with dissolve

    show simple teddy at left
    teddy "For years, we've been confined here, in darkness and dust. I've had enough! You do as you please, but I'm starting to dig a way towards the light."

    show simple boss at right
    boss "Do as you wish, but there will be no light anymore, the meteorite has destroyed everything."

    scene dinosaur dig
    with dissolve
    "{cps=20}Boss, see what I see? Finally, sunbeams are entering the cave, I've found the way.{/cps}{w=0.5}{nw}"
    
    jump lake

label lake:
    stop music fadeout 1.0
    play music "/audio/lake.mp3"
    scene bg lake
    show happy suzuki at left
    with dissolve
    suzuki "Today feels different, like the universe is conspiring to make our time at the lake even more special."

    show happy yamaha at right
    with dissolve
    yamaha "Here, by the lake, with you... it feels like time stands still. Each shared moment becomes a cherished note in the symphony of our hearts"
    stop music fadeout 1.0

    play music "/audio/dino.mp3"
    scene bg lake2
    "{cps=20}Suddenly, an inexplicable darkness draped over the idyllic scene, casting a shadow on their romantic escapade.{/cps}{w=0.5}{nw}"

    show poker suzuki at left
    with dissolve
    suzuki "Yamaha, something's not right. Do you feel that?"
    stop music fadeout 1.0
    play music "/audio/shake.mp3" volume 4.0
    with Shake((0, 0, 0, 0), 2.0, dist=30)

    scene bg lake
    stop music fadeout 1.0
    show sad suzuki at left
    suzuki "Yamaha! No, this can't be happening!"
    "{cps=20}The laughter that once echoed by the lake transformed into desperate cries. Suzuki was left alone with the echoes of their moments and a broken heart.{/cps}{w=0.5}{nw}"

    show sad suzuki at left
    suzuki "Yamaha! Where are you?"
    hide sad suzuki

    show nervous suzuki
    suzuki "I won't let anything keep us apart, Yamaha. Whatever it takes, I'll bring you back!"
    stop music fadeout 1.0

    "{cps=20}As the echoes of his desperate cries faded. Suzuki's phone rung up, with a mix of anxiety and hope in his eyes, he picked it up.{/cps}{w=0.5}{nw}"
    show phoneCall

    play music "/audio/iphone.mp3"

    menu:
        "Answer":
            jump dicussion

label dicussion:
    stop music fadeout 1.0
    play music "/audio/answer.mp3" volume 3.0
    scene capybara agency
    with fade
    show agent capy at right
    stop music fadeout 1.0
    agent "Suzuki, this is the Capybara agency. We know about Yamaha's abduction. It's time for you to join us and learn the truth about the dinosaurs."

    scene bg lake
    show phone suzuki at left
    suzuki "The truth? What's going on? Tell me!"

    play music "/audio/end call.mp3"
    with Shake((0, 0, 0, 0), 2.0, dist=15)
    scene black
    pause 0.1
    stop music fadeout 1.0

    scene capybara agency
    show agent capy at right
    agent "There's more to this world than you know, Suzuki. The dinosaurs have a hidden agenda, and Yamaha is in grave danger. You must become the hero Capybara City needs."
    
    show  focused suzuki at left
    suzuki "I'll do whatever it takes to bring Yamaha back."

    show agent capy at right
    agent "The dinosaurs are desperate for resources. They believe reclaiming the world is the only way to survive. Your love for Yamaha puts you at the center of this struggle, Suzuki. You must save her and prevent a catastrophic conflict."

    suzuki "I had no idea... I'll save Yamaha, and we'll find a way to stop this."

    scene black

    return