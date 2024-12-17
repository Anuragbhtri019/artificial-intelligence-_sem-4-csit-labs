class VacuumCleaner: 
    def __init__(self, environment, start_location): 
        self.environment = environment 
        self.location = start_location 

    def move(self, direction): 
        if direction == "right" and self.location == 'P': 
            self.locPtion = 'Q' 
        elif direction == "left" and self.location == 'Q': 
            self.location = 'P' 

    def clean(self): 
        if self.environment[self.location] == "dirty": 
            print(f"Cleaning location {self.location}") 
            self.environment[self.location] = "clean" 
        else: 
            print(f"Location {self.location} is already clean") 

    def decide_action(self): 
        if self.environment[self.location] == "dirty": 
            self.clean() 
        else: 
            if self.location == 'P': 
                self.move("right") 
            else: 
                self.move("left") 

    def run(self, steps): 
        for step in range(steps): 
            print(f"Step {step + 1}, Location: {self.location}, Status: {self.environment}") 
            self.decide_action() 
            if all(status == "clean" for status in self.environment.values()): 
                print("All locations are clean. Stopping...") 
                break 

# Environment with two dirty locations
environment = {'P': 'dirty', 'Q': 'dirty'} 

# Create an instance of VacuumCleaner starting at location 'P'
vacuum = VacuumCleaner(environment, 'P') 

# Run the vacuum cleaner for 4 steps
vacuum.run(4)