label first_meet:
    scene black
    pause 1.0

    scene bg city
    show suzuki smoke at left
    with dissolve
    suzuki "I am so sorry, Yamaha, I will find you."

    "{cps=20}Suddenly, a strange sound was heard from the shades of the trees."
    show teddy2 simple at right
    with dissolve
    teddy "Suzuki! I know you!"
    hide suzuki smoke
    show suzuki nervous at left
    suzuki "Stay where you are! I will call the agents right now!"
    teddy "Please wait, I can explain. I know where Yamaha is, I know what you want, just trust me."
    suzuki "Why should I?"
    teddy "Because I want to change things. The dinosaur boss is a horrific dictator that exploits us. The dinosaur civilization is at its downfall. We share the same pain, that’s why you have to trust me."
    "{cps=20}Suzuki, though hesitant, sensed a genuine sincerity in Teddy's words. The alliance formed in that unlikely encounter held the promise of an uncharted friendship.{/cps}{w=0.5}{nw}"

    menu:
        "Call Agents":
            hide suzuki nervous
            jump suzuki_call_agent

        "Listen to the Dinosaur":
            suzuki "Ok, speak fast, otherwise I will call them."
            jump discussion_suzuki_teddy


label discussion_suzuki_teddy:
    teddy "Long time we were living under the rule of the dinosaur boss, he abused his power for a long time and our kind was suffering. I want to change that, the dinosaurs deserve better."
    teddy "He believes that there is place for only one dominant species in our world, so it is either us or you. But I can’t buy that. After he abducted my close ones, I tried to disguise around him and find allies that would help me."

    show suzuki nervous at left
    suzuki "And what has that to do with me? Where is Yamaha?!"
    teddy " I know where she is, I can help you! Let me finish, please."
    suzuki "Go on…"
    teddy "I finally rose up to be sent to capture capybaras. They do really horrific stuff with them during interrogations."
    teddy "I saw you two wandering around the lake, and I knew that you were the right one. Yamaha is sound and safe. I just need your help."

    menu:
        "Do you realize how many times I have heard that already?":
            suzuki "Do you realize how many times I have heard that already?"
            teddy "I do, but I am the only one that can help you find Yamaha and help her."

        "So where is she?":
            show suzuki sad at left
            suzuki "So where is she?"
            teddy "I need your word that you will help me. But this has to be done without the agency. They will want to destroy our species. What we really want is peace."

    teddy "After we finish with the dinosaur king, I will lead the opposition and we will come with a peace treaty to the capybaras. The violence and abuse will not lead to anything good."

    menu:
        "Call the agents":
            jump suzuki_call_agent #branch1

        "Trust teddy":
            jump trustteddy

label trustteddy:
    "yes"