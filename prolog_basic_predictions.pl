
% Facts
is_vehicle(car).
is_vehicle(truck).
is_vehicle(bicycle).
is_fuel(gasoline).
is_fuel(electric).

% Rule: Cars and trucks require fuel for operation
requires_fuel(Vehicle) :- is_vehicle(Vehicle), (Vehicle = car; Vehicle = truck).

% Goal: Bicycles do not require fuel for operation
