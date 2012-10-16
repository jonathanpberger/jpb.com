# Hello

---
# Spike Driven Design

> Jonathan Berger, Pivotal Labs, October 2012

> for the Agile Experience Design Co-Meetup 

> with the New York Compass and Sass Meetup

---
The plan:
# ~15 minutes

---

# What
### is Spike Driven Design?

---

### TL;DR
## Spike-Driven Development

- • **Design in Rails** with throw-away code,
- • **Screenshoot** working software for mocks,
- • **Cherry-pick small changes** and contribute them back,
- • **Devs can harvest code** when they go through and TDD the stories.


---

# The Problem

---

### Adobe-app-based design 
## Good for...
- • Designing before any software is built, 
- • Quickly iterating on user flows, 
- • Experimenting with new high-level concepts. 

---

### Adobe-app-based design 
## Terrible because...
- • Once working software exists, mockups have to play catchup with reality
- • Does little to aid in designing interactions

---

### Designing in the browser 
## Good for...
- • Working out low-level tactics, 
- • Quickly iterating on interface and small interactions, 
- • ~$0 set-up cost

---

### Designing in the browser 
## Terrible because...
- • The toolset and techniques are immature, 
- • Saving your work is difficult,
- • High learning curve, and
- • The tools are tantalizingly close to the real app on the front end, entirely missing on the back end.

---

### Enter
# Spike Driven Design

---

## Spike Driven Design

- • **Design in Rails** itself, using mostly SASS and HAML and little bits of Ruby.
- • No tests; this is **throw-away code**.
- • Move fast, **focus on the UX** and visual design problems.
- • Design using the **actual medium** the user will end up with: working software.

---

### Interlude:
# What's a spike?

- • An Agile "spike" is a **short investigation** into a technique or a problem. 
- • By nature it's explicitly exploratory and limited, and **the goal is learning**.
- • After a spike is completed, the **code *must* be thrown away**. 

---

# HOW
### Do I SDD?

- • Branch the project, 
- • Gleefully and recklessly hack around,
- • Write fake methods if needed,

---
## How to SDD
- • Write comments like `# TODO: make this real`, 
- • Quick fixes and polish, while I'm in context,
- • As I work, I'll play around with the interaction,

---
## How to SDD
- • **Check in regularly** w/ the PM & Devs,
- • **Write stories in Tracker** and take screenshots of the SDD site and attach them as mock ups,
- • I'll also **create an epic** called "SDD", with a note mentioning where the branch lives and what I've done in it.

---

## How to SDD

- • Go back through my work and break changes down into **small, atomic commits**
- • I hop onto the master branch
- • `git cherrypick` the styling commits

---

# **BOOM!** 
## Free style tweaks and polish!

---
## Phase Two

- • Devs get to the SDD'd stories in the backlog (which ideally is within a few days). 
- • There's a comment pointing them to the branch, 
- • which they can **check out as a renamed repo** and then **run on another port**:

---

`git clone git@github.com:jonathanpberger/hamazon.git hamazon-sdd-order_history`

`cd hamazon-sdd-order_history`

... (bundle, set up db's, etc)

`rails server -p5555`

---
    
## During development
- • Run the real app on port 3000 and do everything normally, 
- • Living, functional mock-ups exist for reference on port 5555. 
- • They can take a look at the code for ideas on things like structuring the DOM, and can even
- • Harvest things like SASS and assets from the branch. 

---

### This means that a lot of the work from the design phase can go directly into the finished project, without duplication of effort, and without sacrificing quality.

---

# When / Where?
So what sorts of projects and teams are good candidates for SDD? 

- • We've established the basic design of the app ,
- • We're building a fair number of small or medium-sized features or feature tracks, 
- • and it's important that we make sure our additions work well within the existing app and user flows. 

---
## Bonus
- • SDD stories pull me into the pair rotation in a non-time-sensitive manner, which helps smooth out rough spots in the rotation if someone has a doctors appointment or is interviewing a candidate. 

---
## TL;DR
### SDD seems to work well on projects that're past their initial design phase, and have small- to medium-sized teams with a technical designer.

---

## Problems w/ SDD

- • Because of the technical requirements, there's a **high learning curve** for the designer. 
- • **It's a little shady** to push real work into comments saying "make this real". 
- • **Sub-production-quality code** may leak in. 
- • The SDD branch **gets stale quickly**.

---

## Conclusion
Despite these shortcomings, SDD has proven to be an effective technique for our team. We look forward to continuing to explore this way of working, and especially to hearing if it works for others.

---

## Find me at
## jonathanpberger@
## pivotallabs.com, gmail.com, twitter, forrst, flickr, etc...

# Thanks!
## Any questions?

