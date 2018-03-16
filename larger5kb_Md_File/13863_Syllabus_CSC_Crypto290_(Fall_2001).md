![](http://www.cs.rochester.edu/u/www/images/urcslogo.gif)

#  Approximate Syllabus  
CSC290: Cryptology 2001

![---](http://www.cs.rochester.edu/u/brown/images/line.minirainbow.gif)

> Thus, a short introductory course in cryptography could simply proceed
straight through the text and stop when time ran out. In some sense this is
the most natural use of this material.

>

> \-- Paul Garrett

![---](http://www.cs.rochester.edu/u/brown/images/line.minirainbow.gif)

##  Administrategy and Administrivia

**![](http://www.cs.rochester.edu/u/brown/images/carrot.gif) Here is [ The
290A: Cryptology 2001 Home Page
](http://www.cs.rochester.edu/u/brown/Crypto/Crypto.html) for this course.

![](http://www.cs.rochester.edu/u/brown/images/carrot.gif) And here is a [
link to (a subset of the) text
Errata!](http://www.math.umn.edu/~garrett/crypto/Errata.html)

**

It's unclear how quickly we'll get through this material, so the dates and to
some extent the contents are approximate. guess at where we'll be. The
material falls into a handful of related topics or modules, which are grouped
together below along with reading and assignment information.

We're part of a pilot study for a course tools product called [ WebCT
](http://www.courses.rochester.edu/webct) about which you'll be hearing more.
We'll be using WebCT discussion groups and WebCT assignment drop box
functionality, as well as possibly WebCT mail.

#  Assignments

##  \--What and Where

The **assignments** come in four flavors: Cryptanalytic, Programming, Textbook
(names: T1, T2,....), and Term Project, and are labelled as such in the course
description below.

**![](http://www.cs.rochester.edu/u/brown/images/carrot.gif) Here are [ the
assignment descriptions
](http://www.cs.rochester.edu/u/brown/Crypto/assts/exercises.html)
corresponding to the names below. **

**![](http://www.cs.rochester.edu/u/brown/images/carrot.gif) Here are some [
project ideas ](http://www.cs.rochester.edu/u/brown/Crypto/assts/projs.html).
**

##  \-- When and How

All Programming, Cryptanalysis, and Term Project assignments must be handed in
(in PDF format) through webCT as well as in hardcopy to me. (For Cryptanalysis
assignments, hand in all your scratch paper, intermediate results, the entire
paper trail of your solution.) The due dates for all webCT assignments appear
with them on webCT, and that is the only place they appear. The due dates for
Textbook exercises appear in this section, and that is the only place they
appear.

**Important: you can't hand webCT assignments twice, nor hand them in late.**
Every assignment is available for work starting now, but the course
description below suggests "hand-out" dates after which you can consider the
assignment to be current. Here is a list of the assignments and due dates.

**Cryptanalytic: see webCT assignment for due date.**

  1. Aristocrat Cryptogram 
  2. Rotating Grille 
  3. Autokey 
  4. Hill 
  5. Mystery I or Mystery II or Singh's Crypto Challenge Problems (initial and final results, two assts).  
**Programming: see webCT assignment for due date.**

  1. Substitution Attack Tools 
  2. Vigenere, Kasiski, Friedman 
  3. Public Key 
  4. Unix Dictionary Attack 
**Term Project: see webCT assignment for due date.**

  1. Proposal 
  2. Final Submission 
**Textbook: Due at Start of Class on Dates Shown HERE.**

  1. T1: Sept. 11 
  2. T2: Sept. 18 
  3. T3: Sept. 25 
  4. T4: Oct. 2 
  5. T5: Oct. 9 
  6. T5A: Oct. 16 
  7. T6: Oct. 23 
  8. T7: Oct. 30 
  9. T8: Nov. 6 
  10. T9: Not offered this year, sorry. 
  11. T10: Nov. 29 
  12. T11: TBD 
  13. T12: TBD 

Here is another view of [ What's Due When. ](Schedule.txt) It is a snapshot of
early thinking, unofficial, and NOT to be used for your scheduling!.

#  Course Description

**Key:**  
R: To Read Before this week (Chapters are from Text)  
A: Assigned for your attention and for you to begin work  
D: Due (hand in after w/e)  

The "lecture notes" are just that, mostly notes taken straight from the
textbook with no added value, probably the reverse. The exception are the
notes on protocols (Module 7), which are cribbed from a different book, namely
Schneier.

##  \-- Module 1: Simple Ciphers

Content:Course Plan, webCT, Projects, Homework, Readings, Materials. H.W.
rules; all your work! First several weeks are just a review of stuff you
should have had before, prob. combinatorix, etc. History (not much) trad. en-
and de-cipher. outline of substitution vs. permutation ideas. Shift ciphers,
reduction/division, one-time pad, affine cipher. Rotating grill, columnar
transposition, other classic ciphers.

Exercises involve decrypting simple substitution and rotating grille ciphers.

**Week 1:**

R: Gaines handout, Chapter 1, All Appendices [ Introductory Notes
](http://www.cs.rochester.edu/u/brown/Crypto/lectures/1.txt), [ Classical
Cipher Notes ](http://www.cs.rochester.edu/u/brown/Crypto/lectures/2.txt), [
Chapter 1 Notes ](http://www.cs.rochester.edu/u/brown/Crypto/lectures/4.pdf),
webCT information, AND get familiar with the layout and content of the course
web pages.

A: Cryptanalytic: Aristocrat Cryptograms and Rotating Grille, T1. Long-Term
Cipher (Mystery Cipher Initial Asst).

D: nothing

##  \-- Module 2: Substitutions and Transpositions

Content: More on substitution ciphers, probability, statistics of English,
affine cipher attack. Substitutions as permutations, shuffles, block
interleavers, basic combinatorics.

The programming exercise is to produce statistical and other tools to attack
substitution cryptograms.

**Week 2:**

R: Chapter 2 [ Substitution Notes
](http://www.cs.rochester.edu/u/brown/Crypto/lectures/subst.txt). [ Chapter 2
Notes ](http://www.cs.rochester.edu/u/brown/Crypto/lectures/Ch2.pdf),

A: Programming: Substitution Attack Tools, T2

D: Cryptanalytic: Aristocrat Cryptograms and Rotating Grille, T1.

**Week 3:**

R: Chapter 3, [ Chapter 3 Notes
](http://www.cs.rochester.edu/u/brown/Crypto/lectures/6.pdf),

A: T3,(Mystery Code).

D: T2

## \-- Module 3: Polyalphabetics and Modern Symmetric Ciphers

Content: The Vigenere and related polyalphabetic ciphers, with statistical
attacks of Kasiski and Friedman. Mathematical ideas of LCM and GCD. The goals
of a symmetric cipher system and the Data Encryption Standard.

The programming exercise is to develop tools to extract the keylength of, to
decrypt, and to find the key of Vigenere ciphers.

**Week 4:**

R: Chapter 4, 6 (5 is optional), [ lecture notes Chapter 6
](http://www.cs.rochester.edu/u/brown/Crypto/lectures/Ch6.pdf), and [Baby DES
](http://www.cs.rochester.edu/u/brown/Crypto/lectures/BabyDES1.pdf), and [
Attacking DES
](http://www.cs.rochester.edu/u/brown/Crypto/lectures/DESAttack.pdf), (both
stolen from Ed Shaefer of Sta. Clara: nice notes but watch for misprints. E.g.
are those S-boxes right?).

A: Programming: Vigenere, Kasiski, Friedman; Cryptanalytic: The Autokey
cipher; Textbook: T4.

D: Programming: Substitution ciphers and attacks, T3

##  \-- Module 4: Number Theory and Hill Cipher

> Cryptography is a mixture of mathematics and muddle, and without the muddle
the mathematics can be used against you.

>

> Ian Cassells

The main non-text exercise is to solve some Hill's ciphers.

**Week 5:**

R: Chapter 7 , [ Chapter 7 notes (nothing new)
](http://www.cs.rochester.edu/u/brown/Crypto/lectures/Ch7.pdf)

A: (Mystery Code!), T5

D: T4

**Week 6:**

R: Chapter 7 and 8

A: T5A, Cryptanalytic: Hill's Cipher

D: Programming: Vigenere, Kasiski, Friedman; T5

##  \-- Module 5: Public Key, RSA, El Gamal, Elliptic Curves

Content: Public key ciphers are a recent invention based on what complexity
theory now believes to be one-way functions with trap doors. We review
complexity notion ("Big Oh"), revisit worst- versus average-case complexity,
look into Kolmogorov complexity, probabilistic algorithms, linear and feasible
(subexponential) algorithms.

This module gives a quick overview of the idea behind public key ciphers, and
then outlines the algorithms behind RSA, Diffie-Hellman, ElGamal, Knapsack,
NTRU, Arithmetica algorithms, lightly touches on quantum cryptography and
political economy.

The programming exercise is to implement and use an RSA public key encryption
scheme. A bonus: we also use an ordered codebook on this exercise. At about
this time you should be pursuing ideas for the term project and proparing to
write your project proposal.

An excellent treatment of the history of PK and Crypto in general since 1970
is _Crypto_ , by Steven Levy. I extracted three summary diagrams from it.
First, a [ General timeline ](/u/brown/Crypto/lectures/TimeLine.pdf) and
partial flow diagram of people, organizations, and products and products.
Next, a [ diagram of conflicts, ](/u/brown/Crypto/lectures/NSATimeLine.pdf)
mainly attempts by NSA to squelch crypto progress. Last, What was going on in
[ British Crypto ](/u/brown/Crypto/lectures/UKTimeLine.pdf) at the time.

**Week 7:**

R: Chapter 9, 10,

A: Find Project Topic, (Mystery?), T6, Programming: RSA Public Key Exercise.

D: T5A

##  \-- Module 6: Primes and Factors

> The problem of distinguishing prime numbers from composite numbers and of
resolving the latter into their prime factors is known to be one of the most
important and useful in arithmetic... The dignity of the science itself seems
to require that every possible means be explored for the solution of a problem
so elegant and celebrated.

>

> K.F Gauss (1777 - 1855)

> The following numbers are all prime...  
>  31; 331; 3,331; 33,331; 333,331; 3,333,331; and 33,333,331.  
>  However, 333,333,331 = 17 * 19,607,843. Darn...

Content: Primes and pseudo primes, Fermat pseudoprimes, non-prime
pseudoprimes, Euler pseudoprimes, the Solovay-Strassen test, Strong
pseudoprimes, the Miller-Rabin test. Factorization algorithms (Rho, p-1,
sieves). Modern factorization attacks (Quadratic sieve, Gaussian elimination,
random squares factoring...).

**Week 8: Oct 23, 25**

R: Chapters 11, 12

A: T7

D: T6, Cryptanalytic: Hill's Cipher.

**Week 9: Oct 30, Nov 1**

R: Chapters 16, 24

A: T8

D: T7

##  \-- Module 7: Protocols

Content: A Protocol is sequence of steps by two or more people to accomplish a
task. It's a multi-agent algorithm if you will. Examples are buying groceries,
using a trusted third party as an intermediary when I give you a check for a
product and you want to be sure my check is OK and I want to make sure I get
my product from you. We learn about protocol basics and move on to key
exchange, digital signatures, authentication, bit commitment, digital
cash...etc.

Exercises not all clear yet but we at least will use a dictionary attack on
some rather naive UNIX passwords.

**Week 10: Nov 6, 8**

R: R: (Chapter 18 + Stinson 6-13, maybe more!). [ Protocol Building Block
Notes ](http://www.cs.rochester.edu/u/brown/Crypto/lectures/prot1.pdf), AND...
[ Protocol Building Block Overheads
](http://www.cs.rochester.edu/u/brown/Crypto/lectures/ProtocolBldgBlox.html),

[ Basic Protocol Notes
](http://www.cs.rochester.edu/u/brown/Crypto/lectures/prot2.pdf), AND... [
Basic Protocol Overheads
](http://www.cs.rochester.edu/u/brown/Crypto/lectures/basicprot.html),

A: Programming: Unix Dictionary Attack; T8

D: Programming:T7, Decryption: Long-Term Cipher (Mystery preliminary work),
Project Proposal.

**Week 11: Nov. 13,15**

R: [ Intermediate Protocol Notes
](http://www.cs.rochester.edu/u/brown/Crypto/lectures/prot3.pdf),

[ Advanced and Esoteric Protocol Notes
](http://www.cs.rochester.edu/u/brown/Crypto/lectures/prot4.pdf),

A:

D: Programming: Public Key Encryption

##  \-- Module 8: Random Numbers

**Week 12: Nov. 20, 22**

R: Ch. 21

A: T10

D: Nothing

**Week 13: Nov. 27, 29**

R:

A:

D: T10, Programming: UNIX password hacking with the dictionary attack.

**Week 14: Dec. 4, 6**

R:

A:

D: Mystery Cipher!, Term Project Presentations and Writeups.

![---](http://www.cs.rochester.edu/u/brown/images/line.minirainbow.gif) _This
page is maintained by[CB.](http://www.cs.rochester.edu/u/brown)_

_Last update: 24.8.01._

* * *

