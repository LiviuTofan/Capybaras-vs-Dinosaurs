label intro:
    play music "/audio/cinema.mp3" volume 0.5
    scene black
    with dissolve

    centered "{cps=7}{b}Long time ago, when the earth was flat...{/b}{/cps}{w=0.5}{nw}"
    with dissolve


    scene black
    centered "{cps=15}{b}Above the ground, the earth was inhabited by capybaras, while bellow it, dinosaurs roamed. They were peacefully coexisting, without knowing about the existence of each other.{/b}{/cps}{w=0.5}{nw}"
    with dissolve

    scene flat2 earth
    with fade
    $ renpy.pause(delay=2)
    
    scene black
    centered "{cps=10}{b}One day, a meteorite struck the Earth.{/b}{/cps}{w=0.5}{nw}"
    with dissolve

    scene flat earth
    with fade
    $ renpy.pause(delay=2)

    scene black
    centered "{cps=15}{b}As a result, the Earth transformed into a sphere, with capybaras remaining above, and dinosaurs dwelling in the depths of the ground.{/b}{/cps}{w=0.5}{nw}"
    with dissolve

    scene sphere earth
    with fade
    $ renpy.pause(delay=2)

    return