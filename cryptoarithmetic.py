from itertools import permutations 

def solve_cryptoarithmetic(w1, w2, w3): 
    letters = set(w1 + w2 + w3) 
    if len(letters) > 10: 
        print("Something is wrong with the input: more than 10 unique letters.")
        return 
    
    letters = list(letters) 
    l4 = len(letters) 

    def pos(x): 
        return letters.index(x) 

    # Check for leading zeros
    if w1[0] in letters and w2[0] in letters and w3[0] in letters:
        leading_letters = {w1[0], w2[0], w3[0]}
    else:
        leading_letters = set()

    tries = list(permutations(range(10), l4)) 
    for values in tries: 
        if any(values[pos(letter)] == 0 for letter in leading_letters):
            continue 
        
        n1 = int(''.join(str(values[pos(c)]) for c in w1)) 
        n2 = int(''.join(str(values[pos(c)]) for c in w2)) 
        n3 = int(''.join(str(values[pos(c)]) for c in w3)) 
        
        if n1 + n2 == n3: 
            print("\n\nSolution found:") 
            for i, c in enumerate(letters): 
                print(f"{c} = {values[i]}") 
            return 
            
    print("\n\nNo solution found") 

# User input
w1 = input("Enter the first word: ").strip().upper()
w2 = input("Enter the second word: ").strip().upper()
w3 = input("Enter the sum word: ").strip().upper()

solve_cryptoarithmetic(w1, w2, w3)