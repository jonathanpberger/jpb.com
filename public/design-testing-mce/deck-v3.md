class: center middle

# Hi :-)

---

# Towards a Theory and Methodology of Test‑Driven Design
Jonathan Berger, 2015

Mobile Central Europe, Warsaw

---

## Who Am I?

- @jonathanpberger
- ~30 agile projects since 2008
- design, code, pm
- interested in agile practice for design

---
name: who-are-you

## Who are you?
Show of hands:

--

- Designer? 

--

- Developer?



??? 

What else?

---

## What it says on the tin

> Years ago, Developers had problems and devised Agile techniques to address them. Today, Designers face similar problems. Can we adopt similar techniques? In this talk, we’ll explore what automated testing might look like for design. What would it look like to have a more defined definition of “done” for design? What if designers could refactor with impunity? We’ll explore testing possibilities for Visual design, User Experience design, and front-end engineering, and try to build a testing pyramid for design.

---

.small[# The Plan]

## I. Origin Story
- Finding Agile, The (Dev) Problems it solves, Why that doesn't map 1:1 for design

## II. What's out there today
- Getting Technical, Review of Current tools and thinking, What's Missing

# III. Possible Solutions 
- straw man Pyramid, CI, CTA

---

class: center, middle, inverse

# Origin Story

---

## Finding Agile

---

I discovered Agile by accident. 

???

I was a self-taught designer who’d travelled to Florida to hand off a project to the development team. 
My partner and I had spent the summer building this perfect product, and I was completely in love with it. 

---

there was a problem

???
But there was a problem: I knew that when those dummy developers got their hands on it, they’d ruin the thing. 
So I did the only thing I could: I went down there (in a very hostile frame of mind) to defend my baby.

---

That’s when everything changed.

---

Smart, friendly, wonderful people, working in pairs with a sane process. 

???

Those “dummy developers” weren’t dummies at all. 
They were amazing. 
This wasn’t an exception. 
I didn’t luck out and meet the one rockstar or the lone unicorn. 

---

This Worked

???

this was a world where there was a system that worked to help people build strong web apps in a sane, sustainable way. 

---

The same problems that haunted designers were solved!

???
- sustainable pace
- definition of done
- 

The process held the promise that all those late nights, all the stress, all that constant re-invention of the design-wheel could be replaced with a systematic, repeatable, tractable practice for design. 

---

I wanted this

???

I returned to New York determined never to go back to the old way. 
I wanted to bring these things to design. 
I wanted to figure out how to do Pairing and Testing. 

---

How could this apply to Design?

???

Maybe it wouldn’t be exactly the same for design as for development, but the benefits of these techniques were missing in design—and I wanted them.

---


### Problems it solves for Dev
### Why that doesn't map 1:1 for design


## Getting Technical

---

I started as 
### a self-taught designer

---
I worked on [Spot.Us](http://spot.us) and
### found Agile and fell in love. 

---
### I wanted to bring Agile to design.

---
I found Pivotal, and 
### they needed an Agile designer

---
###Sweet! 
I started working with 2 pairs of developers.

---
They would type code
### I would use Adobe for mocks

---
Learning ###1
### In-browser Mockups
with basic CSS, HTML, and a templating framework (Erb)

---
Learning ###2
### TDD and Story Writing
using Cucumber. This helped my UX and UI practice **enormously**.

---
Learning ###3
### Basic Tools
Setting up an environment, Bundler, Rake, etc., let me run locally. 

---
Learning ###4
### Git
So I could contribute small fixes, mostly copy and CSS. 

---
### But
I was breaking a lot of tests

---
Learning ###5
### Rspec and Capybara
So I run tests and make some fixes.

---
Now I could commit code
### **without** breaking the build
:-)

---
Learning ###6
### JQuery and the DOM
So I could make better in-browser mocks and make more changes

---
Learning ###7
### More Ruby, which led to ORMs and REST and HTTP verbs.
That's a mouthful.

---
Learning ###8
### By now, I was doing development regularly
and starting to bring my Design practice back to it. Personas in cuke!

---
Learning ###&infin;
### Still learning every day


---
## What it looks like in practice: Hamazon


# What's out there today
## Review of Things in Jars presentation, CSSTe.st
## Brad Frost / Atomic Design?
## What's Missing

# Solution: straw man Pyramid

# CTA
