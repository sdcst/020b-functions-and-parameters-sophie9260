#!python3

def sum(a,b):
    sum = a+b
    return sum



if __name__ == "__main__":
    print("This is my program")
    x = sum(3,4)
    assert x == 7

    y = sum(11,1.5)
    assert y == 12.5

    assert sum(5,2) == 7
    assert sum(1,2) == 3
    assert sum(5,-32) == -27
    assert sum(5,2.5) == 7.5
    assert round(sum(5.1,2.3),1) == 7.4
    
