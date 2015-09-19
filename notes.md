## Intro

Hello, me

I'm talking about Object Oriented Design and some rules I came across that seemed
like they would be useful AND they would be a challenge to follow.  So this talk
is about:

* the rules
* some code I refactored to get them to follow the rules
* techniques and guidelines that work well with the rules
* my reflections on following the rules

## The Rules

* These rules come from Sandi Metz - a wise woman in the Ruby world.
* Watch her talks, read her book - she's great
* rules are arbitrary, but following them is likely to lead to you to write better OO code

The rules

Are they a straight jacket?  Do you need to break free?

Meta rule

## Example Time

I decided to try them out in a project I'll describe to you now (and I'm not claiming that I've got to an ideal end point, but I am claiming I have improved the code)

Where I work, we work on lots of small projects, so we need to plan people's time

### Planning Work

show tomsplanner screenshot - this is what it looks like

show tomsplanner json export - big and long and nested

show detail of time period - startmoment and finishmoment

So I have the time period, the type and the row (= person)

- talk about data structure I'm aiming for

### versions/1/

* Here is some of the code at one point in this project - this is all one class
* you can do a "squint test" - look for mix of colours, shape etc - strings, logic etc mixed up

* At one point in development I am using dicts a lot, which means 
    * a lot of my logic is in if/else statements as I move around the code.
    * the code has to reach into the dict to make strings for keys

So let's make some improvements

### ood can do it

### versions/2/

* Here we have split Activity into it's own shallow class heirarchy instead of using dicts, to encapsulate the internals.
* We can now call the `__unicode__()` method to get a string as a key, and can create Activity objects with just the parameters required.

(I'll come back to `extra_init()` )

### inheritance

- you first discover inheritance, you love it

### in the ood for love

Then you get into trouble as you create huge heirarchies and some people run away screaming.

* I would advise to keep your heirarchy **shallow** and **narrow**.
* Consider composition instead of inheritance.

## Django CBV

- update view has 9 parent/mixin classes! [update view on ccbv](https://ccbv.co.uk/projects/Django/1.8/django.views.generic.edit/UpdateView/)
- full heirarchy? https://i.imgur.com/uuS3Zy5.png
- be clear this is ancestry, not the complete map
- shallow/narrow heirarchy

## open/closed

- open for extension, closed for modification
- if you don't have to edit the working code, it won't break!

### `super()` vs `extra_init()`

- hands up who has copied a call with `super()` and forgotten to edit the class?
- add code example of `super()` - Activity without `extra_init()`
- better example if `Activity.__init__()` actually did something itself!
- add "the wrong parent" to the slide, make it a second slide
- doesn't work so well with even 2 levels of parents ...

## Example time 2

* slide 1: Here is a utility function that generates a list of strings, 2/day
    * longer explaining the output strings, input/output
* slide 1: set up code on first slide
* slide 2: yields, if, while

refactor

* HalfDay class that increments itself, can be compared and generates a string
* HalfDayIterator.xhalfdays is now trivial

end up with reusable classes

## What I learnt

What I learnt found

- easy to test
- reusable


Refactoring: "make the change easy (that might be hard) then make the easy change" Kent Beck

And now your brain might have melted from all this ood stuff

## pasta ood

## Recap

Trying to follow these rules will

- give you small, reusable classes, than can be fully unit tested well and with quick tests
- help you write classes that are open/closed

## END OF TALK

What did I learn from trying these rules out?

I like it and will continue to try to write my code this way.

If you want to learn more, look up Sandi Metz, watch her talks online, read her book





NOTES

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
