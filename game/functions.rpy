init:

    python:
    
        import math

        class Shaker(object):
        
            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }
        
            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child
                
            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.                
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor
                
                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)
        
        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)
        
            return renpy.display.layout.Motion(move,
                        time,
                        child,
                        add_sizes=True,
                        **properties)

        Shake = renpy.curry(_Shake)

# Phone Calling
image phoneCall:
    "suzuki phone1" with Dissolve(0.1)
    pause 0.1
    "suzuki phone2" with Dissolve(0.1)
    pause 0.1
    repeat

# Give flower to Yamaha loop
label give_flower:
    $ flowers += 1
    stop music fadeout 1.0
    menu:
        "Give a {color=#A94064}Rose{/color}":
            show text "{i}{color=#A94064}You now have [flowers] flowers.{/color}{/i}" at top
            play music "/audio/romantic.mp3"
            $ love += 1
            show suzuki rose at left
            with dissolve
            suzuki "Yamaha, this rose is for you, a delicate echo of the beauty you bring into my world."
            show yamaha shy at right
            with dissolve
            yamaha "Suzuki, your words and this beautiful flower create a symphony of warmth in my heart."
            stop music fadeout 1.0
            hide suzuki rose

        "Give a {color=#FFDF00}Tulip{/color}":
            show text "{i}{color=#A94064}You now have [flowers] flowers.{/color}{/i}" at top
            play music "/audio/broken.mp3" volume 0.5
            $ love -= 1
            show suzuki tulip at left
            with dissolve
            suzuki "Yamaha, this tulip is for you, a delicate echo of the beauty you bring into my world."
            show yamaha nervous at right
            with dissolve
            yamaha "Suzuki, you disappointed me, how could you forget that I'm allergic to tulips?..."
            stop music fadeout 1.0
            hide tulip suzuki