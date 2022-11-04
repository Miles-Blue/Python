def set_operations():
    softball = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])
    basketball = set(['Eva', 'Carmen', 'Alicia', 'Sarah'])
    both = softball.intersection(basketball)
    either = softball.union(basketball)
    not_b_ball = softball.difference(basketball)
    not_softball = basketball.difference(softball)
    one_sport = softball.symmetric_difference(basketball)
    
    print("\nThe following students are on the softball team:")
    for name in softball:
        print(name)
    
    print("\nThe following students are on the basketball team:")
    for name in basketball:
        print(name)
    
    print("\nThe following students play both softball AND basketball:")
    for name in both:
        print(name)
    
    print("\nThe following students play either softball OR basketball:")
    for name in either:
        print(name)
    
    print("\nThe following sutdents play softball, BUT NOT basketball:")
    for name in not_b_ball:
        print(name)
    
    print("\nThe following students play basketball, BUT NOT softball:")
    for name in not_softball:
        print(name)
        
    print("\nThe following students play one sport, but not both:")
    for name in one_sport:
        print(name)

set_operations()
    
    