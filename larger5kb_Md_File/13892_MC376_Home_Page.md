#  MC376: Cryptography

#  Spring, 2001

* * *

This syllabus is available on-line at
_http://www.cs.bc.edu/~straubin/mc376/376.html._

##  Contents

  * Instructor
  * Class Meetings
  * Alice and Bob...
  * Required Background
  * Textbook
  * Required Work
  * Handouts
  * Grading

* * *

##  Instructor

[Howard Straubing](http://www.cs.bc.edu/~straubin)

460E Fulton

Telephone: 552-3977

Office Hours:   Monday and Wednesday 1:30-4:30, or by appointment

[e-mail: straubin@cs.bc.edu](mailto:straubin@cs.bc.edu)

  

* * *

##  Class Meetings

The class meets Tuesdays and Thursdays at noon in Fulton 453.  

* * *

  
  


##  Alice and Bob....

Contemporary books on cryptography always contain a standard list of _dramatis
personae,_ and two of the three players are always called Alice and Bob.
Alice wants to send a message to Bob over a computer network.  A love letter
perhaps.  Or maybe Bob is Alice's bank and she wants to transfer funds from
her account to a third party.  Or Bob is an on-line merchant and Alice is
sending him her credit card number.

Can Alice be sure that no one but Bob will read her love letter?  Can Bob be
sure that the love letter is really from Alice? How can Alice's bank be
certain that the request for a fund transfer really originates with Alice, or
Alice sleep soundly, secure in the knowledge that no one will be able to
tamper with the credit card number that she has just sent through cyberspace?  


##  ...and Marvin

Cryptography is the study of  secure communication in the presence of _bad
guys_.   The bad guys are very very smart and very very wicked, but still
manage to have lots of smart friends who are just as bad as they are and who
have lots of fast computers. The bad guys are eager to chuckle over your
private correspondence, to send instructions to your bank to transfer funds
from your account into theirs, to find out your credit card number and use it
to buy lavish presents for their nasty friends who allowed them use the fast
computers.  There is no solid agreement in the literature about what to call
the archetypal Bad Guy.  I've seen "Eve" and "Oscar"; I thought "Caligula"
might be good (so that the characters are now A, B and C), but one article I
read called him "Marvin", which somehow seemed right to me.  I once knew a
Marvin.  I hope no one in the class is named Marvin.

To protect their communications, Alice and Bob decide to _encrypt_ their
messages---to translate them into apparent gibberish by using a secret code.
The intended recipient of the message must possess a "key" which enables him
to decrypt the gibberish and restore the original message. Marvin, lacking
this knowledge, can listen in all he pleases; he will only receive the
gibberish and be unable to decipher it. In this course we will study what
makes a good (or a bad) cryptographic system, and see many examples, both
ancient and modern, of both.

Of course, all this depends on your point of view.  Maybe Alice and Bob are
the wicked ones---commanders of the enemy army, interantional drug
traffickers, this sort of thing.  Now Marvin, who labors alongside his
patriotic friends with their banks of fast computers to decrypt Alice and
Bob's sinister communications, is not a bad guy---he's a _cryptanalyst_.

Until the 1970's, all cryptographic systems suffered from one awkward defect
---Alice and Bob must share knowledge of the secret key in order to encrypt
and decrypt messages. That means one of them has got to send the key to the
other.  But how are they to to do this?  Remember, Marvin is listening in on
the line, and if he intercepts the key, he will be able to decrypt the
remaining messages.  Beginning about twenty-five years ago, researchers
discovered (a) a method whereby Alice and Bob could share a secret key without
either of them ever having to transmit the key, and without involving a third
party; and (b) a method whereby the algorithm for encrypting a message can be
made publicly available by Bob, but only Bob will be able to decrypt messages.
If you think hard enough about it, you'll be able to convince yourself that
both these things are impossible.  You have to think harder!  The invention of
such "public-key" cryptosystems revolutionized the study of cryptography.

We will begin this course with a look at some classical cryptographic systems
---systems that were in use before the advent of computers, then study
symmetric (= "conventional") cryptostystems in current use: DES and its
successors.  After a survey of the requisite we will study public-key
cryptography, including key exchange methods, digital signatures, hash
functions and authentication schemes.  We'll finish the course with a closer
look at PGP, a real-world system that incorporates both public-key and
conventional methods.

For those inclined to nit-picking over fine points of English:  _cryptography_
is the activity of creating and using secret ciphers, _cryptanalysis_ is the
activity of breaking these systems, and _cryptology_ is the science that
studies both these activities.   Which means that this course should probably
be called Cryptology.  I am inclined to nit-picking myself, so it irks me to
confess that  I was not aware of this delicate distinction until about a week
before the start of classes.  I get the impression that "cryptography" is
emerging, in technical writing on the subject, as the term for the general
study, while "cryptology" is fading from use.  

* * *

  
  


##  Required Background

Programming skills:  CS1 is an absolute necessity and CS2 an almost-absolute
one.  Students who are currently taking CS2 and are really, really sharp
programmers, can also take this course.  It's the skill and experience I'm
after, rather than anything specific that they teach you in CS2.

Math:  Oh yeah, there's a bunch of math in this course.  Some of it is the
standard mathematical notation and terminology involving functions, some
concerns the asymptotic running time of algorithms. Much of it involves number
theory, some of which (Euclid's algorithm for computing gcd's for example)
should look familiar.  Discrete Mathematics is therefore an essential
prerequisite.  

* * *

  

##  Textbook

The textbook for this course is _Cryptography and Network Security---
Principles and Practice,_ by William Stallings, a gentleman who is, to all
appearances, a one-man textbook-writing machine.   All books on cryptography
promise some mix of theory and practice.  This one is rather less theoretical
in its emphasis than most of the rest of the lot---students seem to appreciate
that, although I have mixed feelings about it.  We will cover Parts I and II,
devoted, respectively, to conventional and public-key cryptosystems, and a bit
of Chapter III concerning PGP. ( There is also a fair amount of material in
the book about network security issues that are not directly related to
cryptography; we will not treat this material in the course.)

Other books I like:

_Cryptography:   Theory and Practice _(there we go again!) by Douglas Stinson  
_A Course in Number Theory and Cryptography,_ by Neal Koblitz  
_Decrypted Secrets:   Methods and Maxims of Cryptology,_ by F. L. Bauer  
_Handbook of Applied Cryptography_ by Menezes _,_ van Oorschot and Vanstone.  


The last is available in its more than seven hundred page entirety on the web
at
[http://www.cacr.math.uwaterloo.ca/hac/](http://www.cacr.math.uwaterloo.ca/hac)

There is a large assortment of other Web-based resources devoted to
cryptography, including pages for cryptography courses taught at other
universites, pages maintained by the RSA Security corporation (which includes
the detailed technical standards for public-key encryption), pages devoted to
PGP, etc.  By all means, surf and explore these sites.

This is an advanced Computer Science course, and as such we concentrate on the
technical aspects of the subject.  But one can hardly ignore the fact that
there is an important political, legal and social face to technical
developments in cryptography, touching on issues of privacy, national
security, and intellectual property rights.  If you watch the newspapers
closely, you will be almost certain, in any given week, to see an article that
concerns some aspect of cryptography.  I encourage you to read these as you
find them, and to call them to the class's attention.   In this connection,
here are some books aimed at a popular audience, devoted both to the history
of the subject and to contemporary issues:

_The Codebreakers,_ by David Kahn  
_The Code Book,_ by Simon Singh  
_Crypto,_ by Steven Levy

The first is quite dated, but loaded with intriguing detail about what it does
cover.  The second, published last year, takes account of very recent
developments. The last, published in 2001 (!) is about the conflict between
academic researchers, hackers and business people on one side, and government
intelligence agencies on the other, over public access to secure cryptographic
methods.  (An excerpt appeared last week in _Newsweek_.)

* * *

  

##  Required Work

###  Homework

 Weekly homework assignments will consist of pencil-and-paper exercises and
programming problems.  For the programs, you may write in either C or Java.
(All my class examples will be in C.) I will ask you to electronically submit
the source code for any programs that you write for this course.  The homework
assignments will all be posted below.

[Assignment 1](hw1.html)

[Assignment 2 (with solutions)](hw2/hw2.html)

[Assignment 3](hw3.html)

[Assignment 3 Solutions](hw3solutions.ps) (Postscript)[](hw4solutions.html)

[Assignment 4 (with solutions)](hw4solutions.html)

[Assignment 5](hw5.html)

[Assignment 6](hw6.html)  

* * *

###  Exams

There will two in-class tests, and a final exam during the usually scheduled
time for courses in this time slot.

* * *

  


##

##  Handouts

Lecture Notes 1: ETAOIN SHRDLU [(Postscript)
](cryptonotes1.ps)[(pdf)](cryptonotes1.pdf)

Lecture Notes 2:  Block Ciphers  [(Postscript)](cryptonotes1.ps)
[(pdf)](cryptonotes2.pdf)

Lecture Notes 3:  Overview of Public-Key Cryptography
[(Postscript)](cryptonotes3.ps) [(pdf)](cryptonotes3.pdf)

Lecture Notes 4:  Outline of Number Theory [(Postscript)](cryptonotes4.ps)
[(pdf)](cryptonotes4.pdf)

Lecture Notes 5: RSA [(Postscript)](cryptonotes5.ps) [(pdf)](cryptonotes5.pdf)

Lecture notes 6:  Diffie-Hellman and Related Methods
[(Postscript)](cryptonotes6.ps) [(pdf)](cryptonotes6.pdf)

Lecture Notes 7: Hash functions [(Postscript)](cryptonotes7.ps)
[(pdf)](cryptonotes7.pdf)

Lecture Notes 8: Digital Signature Algorithm [(Postscript)](cryptonotes8.ps)
[(pdf)](cryptonotes8.pdf)

Lecture Notes 9: Digital Cash [(Postscript)](cryptonotes9.ps)
[(pdf)](cryptonotes9.pdf)

[An Excel spreadsheet that helps decrypt the Caesar cipher](caesarcipher.xls)

[A C program that performs encryption using Caesar cipher](shift_encrypt.c)

[A C program that uses a statistical method for determining the key of a
Caesar-encrypted text](shift_decrypt2.c)

[A C routine for modular exponentiation](modexp.c)

[A C program that hunts for primes](testprime.c)  

* * *

  

##  Grades

 To be eligible for a passing grade in the course you must satisfactorily
complete a minimum of 60% of the weekly homework assignments, handed in before
the solutions are posted. Your course grade will then be computed from the
scores on homework, the in-class midterm, and the final exam.  The final exam
will account for about one-third of the grade, the in-class tests for one-
third, and the homework for one-third.

