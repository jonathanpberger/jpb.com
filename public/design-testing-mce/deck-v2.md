# Intro

## who: hi, I'm jon

### origin story
- designer
- discovered agile
- want to bring it to design

## who're you?


# what problems does agile solve for dev?
	waterfall
	building the wrong thing
	not knowing if it still all works
	not being human-centered

# what solutions does agile offer?
	sus'l pace
	better work methods
	values that focus on the right things

# how does it work for Dev?
##Every Day
###Pairing
###TDD
###CI
##Every Week
###Standups
###Retros
###IPMs => storywriting
###release planning => Big Design Refactor

# how might design work analogously?
## ontological design => what works for OO programming should work for Product Design
## testing" in design == user testing. why automated testing is different and important

##Every Day
###Pairing- working on it
###TDD- this talk
###CI- next talk
##Every Week
###Standups- doing it!
###Retros- doing it!
###IPMs => storywriting: working on it / this talk
###release planning => Big Design Refactor

--

# who: back to my story
## came to Piv

## what: learned dev, PM

## how does TDD work for Dev?
	TDD hamazon story

--


# who: designers
## what: tdd for design
## how:
###	break it down into the design pyramid
	- inventory what's low-hanging and what's not
	- hook into CI / notion of "healthy product"

# next: conclusion
## recap
## CTA

---

Atomic Design, series of Jars, they're all missing something: they're trying to cargo-cult the form of classification and development concerns without first addressing what the differences are between design and dev.

What are those differences?

##Every Day

Test-Driven Development depends on 
	- red: testing languages 
		- RSPEC: assert at the functional unit level, e.g. "calculate_ny_sales_tax.should == price * 1.10". What's the design equivalent of function?
		- Cucumber: describe a happy path. How do we do this in design? With user flows
	- green: running automated tests
	- refactor: testing, abstraction, modularity, SOLID
	
Pairing: works, though it would be nice to have ping-pong. Ping-pong is blocked on being able to write a red test and check it goes green. How could this work?
	- FE: if we're testing the implementation of the mockup, we could use Wraith or CSS Critic.
	- IA: IA is done when the user can intuit how to navigate, and new concerns don't fundementally break the system
	- UI: UI is "done" when it's a reusable/extendable system that's grokkable. We can test this by 1) testing extendability, and 2) testing grokkability
	- UxD: UxD is "done" when the user feels joy after using the product. We can test this by 1) qualitative research and 2) usage metrics.
	- VxD is done when 1) it's not a roadblock, 2) users are pleased by the look,
CI:
##Every Week
###Standups- doing it!
###Retros- doing it!
###IPMs => storywriting: working on it / this talk
###release planning => Big Design Refactor

