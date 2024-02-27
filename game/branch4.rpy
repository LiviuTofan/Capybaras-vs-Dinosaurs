label ask_agent_for_help:
    agent "Fine, we will help you. Half the squad waits here, the other half goes with me."

    scene black
    centered "{cps=20}They follow the bloody path and find the wounded Teddy. Agent 007 warns to shoot him."

    scene cave door
    show agent2 capy at left
    agent "Stand still! Do not attempt anything stupid. We are representatives of the Capybara Agency against Dinosaur Invasion."
    show teddy simple at right
    teddy "Please, I don’t want to hurt anyone. I want to establish peace. I recognize that I have led a capture expedition, but none of the capybaras were hurt. You can look through the lock and see that they are well."
    agent "And why shouldn’t I end you here and free them?"
    teddy "The room is guarded and will take orders only from the king. I do have a plan, I want to take the throne, I just need allies I can trust. I have a plan, we can ambush him. I need you to draw his attention."
    agent "Are you kidding me? What kind of games are that?"
    show suzuki nervous at left
    suzuki "I have to make a decision quickly."

    menu:
        "Shoot Teddy":
            jump cave_end

        "Convince Agent 007":
            suzuki "Trust him. He can help us."
            agent "Suzuki, this is madness!"
            suzuki " It’s the only way we can save Yamaha and turn the tables for us."
            agent "Fine. But the first trick and you both get shot."
            scene black
            "{cps=20}The agents are heading the other way, as instructed by Teddy.{/cps}{w=0.5}{nw}"
            jump teddy_and_suzuki
