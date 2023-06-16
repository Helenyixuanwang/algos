# 2126. Destroying Asteroids

# You are given an integer array asteroids and an integer mass representing the mass of a planet. The planet will collide with the asteroids one by one - you can choose the order. If the mass of the planet is less than the mass of an asteroid, the planet is destroyed. Otherwise, the planet gains the mass of the asteroid. Can you destroy all the asteroids?

# Another thing to note is that in many greedy problems, you will be sorting the input at the start. Again, this is because we want to greedily choose the max/min elements in many problems, and sorting the input makes this convenient.

def asteroidsDestroyed(mass, asteroids) -> bool:
        asteroids.sort()
        for asteroid in asteroids:
            if asteroid > mass:
                return False
            mass += asteroid
        
        return True