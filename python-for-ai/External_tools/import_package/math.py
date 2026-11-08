import math
#basic function

math.sqrt(16)
math.pow(3,4)
math.gcd(6,3)
math.factorial(5)

#rounding

math.ceil(4.4)
math.trunc(4.6)
math.floor(-4.2)   # -5 (goes down)
math.trunc(-4.2)   # -4 (just removes .2)
math.ceil(-4.2)    # -4 (goes up)

#constant

math.pi   # 3.14159...
math.e    # 2.71828...
math.inf  # infinity
math.nan  # not a number

#Logarithms and exponents

math.log(100, 10)  # 2.0
math.log10(1000)   # 3.0
math.log2(8)       # 3.0
math.exp(2)        # e squared

#Trigonometry (angles in radians)
math.cos(0)            # 1.0
math.tan(math.pi / 4)  # ~1.0
math.radians(180)      # 3.14159... (degrees → radians)
math.degrees(math.pi)  # 180.0 (radians → degrees)
math.sin(math.pi / 2)  # 1.0
math.cos(0)            # 1.0
math.tan(math.pi / 4)  # ~1.0
math.radians(180)      # 3.14159... (degrees → radians)
math.degrees(math.pi)  # 180.0 (radians → degrees)

#Other useful ones

math.hypot(3, 4)       # 5.0 (distance/hypotenuse)
math.dist([0, 0], [3, 4])  # 5.0 (distance between points)
math.comb(5, 2)        # 10 (combinations)
math.perm(5, 2)        # 20 (permutations)
math.isclose(0.1 + 0.2, 0.3)  # True (safe float compare)

