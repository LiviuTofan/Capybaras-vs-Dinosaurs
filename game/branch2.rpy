label trust_teddy:
    hide suzuki sad
    show suzuki focused at left
    suzuki "Ok, I will trust you, but maybe we need help from the agency?"
    teddy "It is your choice, but I suggest not involving them."
    suzuki "Do you realize we stand no chance alone? We have to get their help. Agent 007!"
    hide teddy2 nervous
    show agent2 capy at right
    agent "What the hell is going on here?! Who is that? Keep your hands raised."
    suzuki "This is Teddy. He wants to help. He knows where the dinosaur king and Yamaha are. I know what you think, but we have to trust him."

    if agencyReputation < 1:
        agent "We cannot do that Suzuki. We can’t allow this after the atrocities done by them."
        scene black
        play music "/audio/gun.mp3"
        centered "{cps=20}Agent 007 shots towards Teddy, while he tries to escape. Teddy gets shot in his leg and leaves a bloody trail behind him{/cps}{w=0.5}{nw}"
        stop music fadeout 1.0
        jump follow_the_blood #branch 1
    else:
        agent "Fine, Suzuki, I do trust you. I hope you do understand the responsibility."
        suzuki "I do, I have trusted in you, now you trust in me."
        jump suzuki_leads #branch 2

label suzuki_leads:
    scene black
    stop music fadeout 1.0
    play music "/audio/cave.mp3"
    centered "{cps=20}Suzuki becomes a leader now, he is growing in the eyes of the agent, being capable of commanding a squad and finding a common language with the enemy.{/cps}{w=0.5}{nw}"
    
    scene cave door
    "Teddy leads them inside a cave underground, where he shows them the room where the dinosaur boss resides and the room where capybaras are being kept."
    show agent2 capy at right
    agent "WHAT HAVE YOU DONE TO THEM?"
    show teddy simple at left
    teddy "Believe me, I have done nothing and it was extremely difficult to make the superiors wait. I convinced them to not touch them for the time being."
    agent "Now what is the plan?"
    teddy "It will be an ambush. You draw the attention of the dinosaur king, while me and Suzuki are attacking from above. We strike him down and we win. There are guards hidden in that room, so be prepared and armed, while we ambush on him."
    jump teddy_and_suzuki #branch 3