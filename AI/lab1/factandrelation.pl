% Facts
cat(tom).
hair(tom, black).
lazy(pratyusha).
dances(lili).
searching_for_food(tom).
free(ryan).
loves(kunal, pasta).
loves(nawaz, games).
loves(jack, cricket).
loves(bill, cricket).

school_closed.

% Relations
happy(lili) :- dances(lili).
hungry(tom) :- searching_for_food(tom).

friends(jack, bill) :- loves(jack, cricket), loves(bill, cricket).
go_to_play(ryan) :- free(ryan), school_closed.
