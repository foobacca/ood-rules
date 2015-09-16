## Intro

## The Rules

introduce them

the get out of jail free card

## Example Time

show tomsplanner screenshot
show tomsplanner json export
show detail of time period

So I have the time period, the type and the row (= person)

### versions/1/

At one point in development I am using dicts a lot, which means a lot of my
logic is in if/else statements as I move around the code.

### versions/2/

Here we have split Activity into it's own shallow class heirarchy.

#### inheritance

- open/closed
    - open for extension, closed for modification
    - if you don't have to edit the working code, it won't break!
- Django CBV
    - update view has 9 parent/mixin classes! [update view on ccbv](https://ccbv.co.uk/projects/Django/1.8/django.views.generic.edit/UpdateView/)
- `super()` vs `extra_init()`

- shallow/narrow heirarchy




## Example time 2

half days refactor




shell script to do:
    git checkout commit
    vim filename +line_no


Code to show:

    calendar_data.py @ 6b1bd43088de8d893769bd2f3be6749dac96ca4d
    - lots of if, for loops, long CSV writer

    calendar_data.py @ 750f0a0fe2fcca1bdebcfaee3ef64bb6811df584
    - activity classes in shallow inheritance heirarchy


## ALSO

- refactor the utils class

Refactoring: "make the change easy (that might be hard) then make the easy change" Martin Fowler

## END OF TALK

Other stuff for talk?


### testing

- only test public methods
    - convention for private, leading underscore
- small POPO have **fast** tests
- easier to write comprehensive unit tests for small classes
- mocks - see POODR



### other possibilities

some duplication is less bad than the wrong abstraction

if/elif/else (case) statement vs config

why have rules?


### Build example tomsplanner

- people - Clara Oswald, Donna Noble, Rose Tyler ...
- projects - Daleks, Cybermen, Weeping Angels, ...
