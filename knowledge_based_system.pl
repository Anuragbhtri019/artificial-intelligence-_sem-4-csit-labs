% Facts
employee(alice).
employee(bob).
employee(charlie).
employee(david).
employee(eve).
employee(frank).

manager(alice, bob).       % Alice is Bob's manager
manager(alice, charlie).   % Alice is Charlie's manager
manager(bob, david).       % Bob is David's manager
manager(bob, eve).         % Bob is Eve's manager
manager(charlie, frank).   % Charlie is Frank's manager

% Rules
subordinate(X, Y) :- manager(Y, X).  % X is a subordinate of Y if Y is X's manager
colleague(X, Y) :- manager(Z, X), manager(Z, Y), X \= Y.  % X and Y are colleagues if they share the same manager
top_manager(X) :- \+ manager(_, X).  % X is a top manager if no one reports to X

% Goal
%Find  all employees under a specific manager.
under_manager(Manager, Subordinate) :- manager(Manager, Subordinate).
