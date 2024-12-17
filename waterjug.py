def water_jug_problem():
    # Capacities of the jugs
    jug_a_capacity = 4   
    jug_b_capacity = 3  
    target = 2   # The target amount of water to measure
    current_a = 0  # Current amount in jug A
    current_b = 0  # Current amount in jug B
    actions = []  # List to store the sequence of actions

    # Function to perform an action and update the state
    def perform_action(action):
        nonlocal current_a, current_b
        actions.append(action)
        
        if action == "fill_a":
            current_a = jug_a_capacity  # Fill jug A to its capacity
        elif action == "fill_b":
            current_b = jug_b_capacity  # Fill jug B to its capacity
        elif action == "empty_a":
            current_a = 0  # Empty jug A
        elif action == "empty_b":
            current_b = 0  # Empty jug B
        elif action == "pour_a_to_b":
            to_pour = min(current_a, jug_b_capacity - current_b)  # Calculate how much to pour from A to B
            current_a -= to_pour
            current_b += to_pour
        elif action == "pour_b_to_a":
            to_pour = min(current_b, jug_a_capacity - current_a)  # Calculate how much to pour from B to A
            current_b -= to_pour
            current_a += to_pour

    # Main loop to reach the target amount in either jug
    while current_a != target and current_b != target:
        if current_a == 0:
            perform_action("fill_a")  # Fill jug A if it's empty
        elif current_b == jug_b_capacity:
            perform_action("empty_b")  # Empty jug B if it's full
        elif current_a > 0 and current_b < jug_b_capacity:
            perform_action("pour_a_to_b")  # Pour from A to B
        else:
            perform_action("pour_b_to_a")  # Pour from B to A

    # If jug A has not reached the target, continue to fill or pour
    while current_a != target:
        if current_a == 0:
            perform_action("fill_a")
        else:
            perform_action("pour_a_to_b")

    # If jug B has not reached the target, continue to fill or pour
    while current_b != target:
        if current_b == jug_b_capacity:
            perform_action("empty_b")
        else:
            perform_action("pour_a_to_b")

    # Print the sequence of actions taken
    print("Sequence of actions:")
    for action in actions:
        print(action)

# Run the water jug problem
water_jug_problem()