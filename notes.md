## Intro

## The Rules

introduce them

the get out of jail free card

I decided to try them out in a project I'll describe to you now

## Example Time

show tomsplanner screenshot

show tomsplanner json export in sublime text - big and long

show detail of time period - startmoment and finishmoment

So I have the time period, the type and the row (= person)

### versions/1/

Notes: if you want the code read, just show a snippet, but if just showing the "shape" of the code, then can show longer section, but tell people not to try to parse it

At one point in development I am using dicts a lot, which means a lot of my
logic is in if/else statements as I move around the code.

### versions/2/

Here we have split Activity into it's own shallow class heirarchy.

#### inheritance

- Django CBV
    - update view has 9 parent/mixin classes! [update view on ccbv](https://ccbv.co.uk/projects/Django/1.8/django.views.generic.edit/UpdateView/)
    - full heirarchy? https://i.imgur.com/uuS3Zy5.png
    - be clear this is ancestry, not the complete map
    - shallow/narrow heirarchy

- open/closed
    - open for extension, closed for modification
    - if you don't have to edit the working code, it won't break!
    - `super()` vs `extra_init()`
        - hands up who has copied a call with `super()` and forgotten to edit the
          class, leading to some calls being missed out
        - add code example of `super()` - Activity without `extra_init()`
        - better example if `Activity.__init__()` actually did something itself!
        - add "the wrong parent" to the slide, make it a second slide
        - doesn't work so well with even 2 levels of parents ...

## Example time 2

halfdays refactor

less ifs (apart from `__lte__()` )

end up with reusable classes


maybe concentrate on the new `xhalfdays()` method iterator


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

Refactoring: "make the change easy (that might be hard) then make the easy change" Kent Beck

## END OF TALK

What did I learn from trying these rules out?

Kent Beck rules

...




NOTES

- check if things will go off slides on 1024x768 ...
    - UpdateView diagram
    - code samples
    ...
- preformat and prepare code samples - not text editor



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
