
define suzuki = Character("Suzuki")
define yamaha = Character("Yamaha")
# start with scenario
# trebuie de scos fundalul alb de pe imagini, png sa fie
# ar fi de dorit de rotit ca suzuki sa priveasca inspre dreapta, tipa se uite spre yamaha, si ea spre el
# in drept am pus sunete care ar trebui adaugate la caracter
# de adaugat o poza unde suzuki sta cu o floare in mana, tipa i-o da lu yamaha ca loop

label start:
    scene bg home
    "Welcome to the game!"

    show happy suzuki # smiling, invitingly
    with dissolve
    suzuki "Yamaha, the day is as perfect as your smile. How about we escape to the lake? Its waters mirror the warmth I feel whenever you're near"

    show happy yamaha # giggling
    with dissolve
    yamaha "Suzuki, you always know how to make my heart flutter. The lake sounds like a wonderful idea"

    jump way_to_lake


label way_to_lake:
    scene bg way

    show happy suzuki # aici trebuie cu floarea
    with dissolve
    suzuki "Yamaha, this flower is for you, a delicate echo of the beauty you bring into my world"

    show shy yamaha
    with dissolve
    "Suzuki, your words and this beautiful flower create a symphony of warmth in my heart. I cherish the beauty you bring into my world, just like this delicate gift."
 
    jump lake

label lake:
    scene bg lake

    show happy suzuki
    with dissolve
    suzuki "Today feels different, like the universe is conspiring to make our time at the lake even more special."

    show happy yamaha
    with dissolve
    yamaha "Here, by the lake, with you... it feels like time stands still. Our laughter becomes the music, and each shared moment becomes a cherished note in the symphony of our hearts"

    return