% Define animals based on characteristics
animal(dog) :- is_true("is a mammal"), is_true("barks").
animal(cat) :- is_true("is a mammal"), is_true("meows").
animal(eagle) :- is_true("can fly"), is_true("has sharp eyesight").
animal(salmon) :- is_true("can swim"), is_true("is a fish").
animal(frog) :- is_true("can jump"), is_true("is an amphibian").

% Ask user for confirmation
is_true(Q) :-
    format("~s?\n", [Q]),
    read(Response),
    (Response == yes -> true; false).
