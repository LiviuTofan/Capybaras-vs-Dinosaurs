define suzuki = Character("Suzuki")
define phoneCall = Character("Phone Call")
define yamaha = Character("Yamaha")
define teddy = Character("Teddy")
define boss = Character("Boss")
define agent = Character("Agent 007")

define roses = 0
# start with scenario
# trebuie de scos fundalul alb de pe imagini, png sa fie
# ar fi de dorit de rotit ca suzuki sa priveasca inspre dreapta, tipa se uite spre yamaha, si ea spre el
# in drept am pus sunete care ar trebui adaugate la caracter
# de adaugat o poza unde suzuki sta cu o floare in mana, tipa i-o da lu yamaha ca loop

label start:
    call intro
    call home
    call first_meet
