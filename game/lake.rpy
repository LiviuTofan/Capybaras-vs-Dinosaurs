label home:
    scene black
    centered "{cps=7}{b}Let's start the adventure...{/b}{/cps}{w=0.5}{nw}"

    scene bg home
    show happy suzuki at left # smiling, invitingly
    with dissolve
    suzuki "Yamaha, the day is as perfect as your smile. How about we escape to the lake? Its waters mirror the warmth I feel whenever you're near."

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
    "You now have [roses] roses"

    show shy yamaha at right
    with dissolve
    "Suzuki, your words and this beautiful flower create a symphony of warmth in my heart. I cherish the beauty you bring into my world, just like this delicate gift."
 
    jump cave

label cave:
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
    scene bg lake
    show happy suzuki at left
    with dissolve
    suzuki "Today feels different, like the universe is conspiring to make our time at the lake even more special."

    show happy yamaha at right
    with dissolve
    yamaha "Here, by the lake, with you... it feels like time stands still. Our laughter becomes the music, and each shared moment becomes a cherished note in the symphony of our hearts"

    scene bg lake2
    "{cps=20}Suddenly, an inexplicable darkness draped over the idyllic scene, casting a shadow on their romantic escapade.{/cps}{w=0.5}{nw}"

    show poker suzuki at left
    with dissolve
    suzuki "Yamaha, something's not right. Do you feel that?"
    with Shake((0, 0, 0, 0), 2.0, dist=30)

    scene bg lake
    show sad suzuki at left
    suzuki "Yamaha! No, this can't be happening!"
    "{cps=20}The laughter that once echoed by the lake transformed into desperate cries. Suzuki, left alone with the echoes of their moments, felt a surge of determination and fear intertwining in his heart.{/cps}{w=0.5}{nw}"

    show sad suzuki at left
    suzuki "Yamaha! Where are you?"
    hide sad suzuki

    show nervous suzuki
    suzuki "I won't let anything keep us apart, Yamaha. Whatever it takes, I'll bring you back to the serenity of our lake."

    "{cps=20}As the echoes of his desperate cries faded, a mysterious communication device, adorned with the symbol of the Capybara agency, buzzed to life. Suzuki, a mix of anxiety and hope in his eyes, picked it up.{/cps}{w=0.5}{nw}"
    show phoneCall

    menu:
        "Answer":
            jump dicussion

label dicussion:
    scene capybara agency
    with fade
    show agent capy at right
    agent "Suzuki, this is the Capybara agency. We know about Yamaha's abduction. It's time for you to join us and learn the truth about the dinosaurs."

    scene bg lake
    show poker suzuki at left
    suzuki "The truth? What's going on? Tell me!"

    with Shake((0, 0, 0, 0), 2.0, dist=15)
    scene black
    pause 0.1

    scene capybara agency
    show agent capy at right
    agent "There's more to this world than you know, Suzuki. The dinosaurs have a hidden agenda, and Yamaha is in grave danger. You must become the hero Capybara City needs."
    
    show  focused suzuki at left
    suzuki "I'll do whatever it takes to bring Yamaha back. Tell me what I need to know."

    show agent capy at right
    agent "The dinosaurs are desperate for resources. They believe reclaiming the world is the only way to survive. Your love for Yamaha puts you at the center of this struggle, Suzuki. You must save her and prevent a catastrophic conflict."

    suzuki "I had no idea... I'll save Yamaha, and we'll find a way to stop this. I won't let their desperation lead to destruction."

    scene black

    centered "{cps=20}As Suzuki gained insight into the hidden conflict, his resolve solidified. The lake, once a symbol of romance, now mirrored the ripples of change about to unfold. Suzuki, armed with newfound knowledge and determination, set out on a journey to save Yamaha and uncover the truth that lay beyond the serene surface of Capybara City.{/cps}{w=0.5}{nw}"

    centered "{cps=20}As Suzuki embarked on his quest to save Yamaha, the path led him to a part of Capybara City less frequented. Amidst the shadows and foliage, he encountered Teddy, a dinosaur with an unexpected sincerity in his eyes.{/cps}{w=0.5}{nw}"


    return