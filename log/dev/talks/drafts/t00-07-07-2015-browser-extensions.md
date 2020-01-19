# Browser extensions: API, product environment and feature flow

[video](https://www.youtube.com/watch?v=Tm4eZkNLzjE&t=6160)

## whoami

...

## whereis - what the market is about: target platforms

* GC, Opera
* FF
  * old school (XUL)           <- low-level API + XML
  * restartless                <- plain old JS, XUL capabilities accessible
  * add-ons (SDK)              <- simplicity intended, odd debug, 2-level API
* IE (oh yeah)
  * DLLs, anyone?
  * hidden windows
  * omg, registry              <- glues things together
  * you'll need an installer   <- wix, probably
  * 20ms startup limit         <- no chances for C# :/
  * still enough motivation?

## whereis - "take me to store": first impression

(Chrome Store overview <- screenshot)

## whereis - "take me to store": are you sure? permissions!

(Chrome Store confirmation <- screenshot)

## whereis - "take me to store": finally

(Extension added <- screenshot)

## it all starts with a brilliant idea

* drawings, sketches, all kinds of schemes
* orchestrate your creativity

## the env one could live in: roles

("Річард з гір" <- meme)

## the env one could live in: feature flow

* crazy idea
* user story
* elaboration/investigation
* implementation               <- here we code, believe it or not
* maintenance
* deprecation/reincarnation

## the env one could live in: how to even test

* standalone (dev)
  * unit                       <- don't let those buzzwords (TDD/BDD) ruin your architecture
  * functional                 <- it's pure fun, having DDD in hand
  * integration                <- modules, "we are all united"
* complex (QA)
  * UI                         <- yes, Selenium/Webdriver (to click over all the controls)
  * integration                <- products, there are always some
  * regression                 <- "son, I am dissapoint" meme
* complected (pm+)
  * UX                         <- "live or let die"
  * A/B                        <- measure the impact, fight falsy assumptions
  * long-term impact           <- manage feature conflicts, measure retention

## the env one could live in: and deploy

* docs                         <- release pages + howto
* CI, DTAP                     <- acceptance -> beta -> prod
  * stores, again              <- https://chrome.google.com/webstore/developer/dashboard
  * or landing page?
  * review process (by vendors)

## does the scrum fit?

* if you say so
* artifacts                    <- traceability
* integration challenges       <- scalability

## show me some code

* oh noes, let's mention conventions first
  * how to derive common parts
* does it make sense to open-source?
* modularity
  * don't let it ruin your architecture
* refactor all the things
  * hidden costs               <- don't simply spam the backlog
  * FF electrolysis epicness

## inventory: debug, context (where is my beloved "this"?)

* GC  <- :)
* FF  <- :|
* IE  <- :/

(GC background page)

## inventory: setup

* WMs                              <- yes, testing, again
* build process
  * gluing common logic with API specifics
  * packaging                      <- `*.crx`, `*.xpi`, `*.msi`
  * grunt/gulp/Makefile/whatever   <- absolutely no fun there

## inventory: browser profiles, folder structure

(Extension in GC profile <- screenshot)

http://www.chromium.org/user-experience/user-data-directory

## the power of community

* public issue trackers
* MDN
* your own cozy knowledge base
* wait, don't we have StackOverflow?
* stores, again

(Chrome store support <- screenshot)

## API and what to care about: vox populi

* permissions, over and over   <- forbidden fruit
* single purpose policy        <- ban, he-he
* any other sort of of policy  <- world is a cruel place

## API and what to care about: background + content

* js sandboxed                 <- not really
* though DOM is accessible     <- and observable
* messaging
  * custom pub/sub
  * you'll have to track your callbacks, man

## API and what to care about: live cycle

* install/uninstall            <- user settings recovery
* startup/shutdown             <- app state recovery
* migrations                   <- fight the legacy
* garbage collector            <- don't ignore this guy

## API and what to care about: caniuse

* HTTP request flow            <- interception, headers injection
* offline mode                 <- FS, storage
* caching
* i18n
* tracking/reporting           <- Mixpanel and such
* logging
* frameworks?
  * say it, say it again
  * decent architecture instead

## API and what to care about: did someone say UX?

* persistent                       <- window-based
  * an icon
  * a popup vs. built-in html pages
* short-term                       <- tab-based
  * third-party DOM manipulation
  * an iframe                      <- seriously

## so what?

(Metallica's "so what?!" <- meme)

the whole hassle is about competence and comprehension

