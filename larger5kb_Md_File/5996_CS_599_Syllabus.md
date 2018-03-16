# CS 599  
Formal Methods in Software Architectures

Fall Semester, 2000  
Location: WPH 106  
Time: Th 2:00 - 4:50 pm  
Class number: 048-33637D  
Prerequisite: [CS 612](http://sunset.usc.edu/classes/cs612_2000/index.html) or
instructor's consent

* * *

Instructor | Overview | Readings | Assignments | Schedule

* * *

# Instructor

  * [Nenad Medvidovic](http://sunset.usc.edu/~neno/)
  * Electronic Mail: [neno@usc.edu](mailto:neno@usc.edu)
  * Office: SAL 338
  * Office Phone: (213) 740-5579
  * Office Hours: Th 1:00 - 2:00 pm and by appointment

* * *

# Overview

Software architectures have gained a lot of popularity in the academic and
commercial worlds during the last decade.  Numerous potential benefits have
been attributed to architectures: ability to readily ensure system properties;
improved support for software reuse; development of reliable, distributed,
large-scale systems on time and within budget; and so forth.  In order to
ensure these benefits, researchers have developed a set of modeling notations
that allow architects to precisely specify the structure, behavior, and
properties of the critical aspects of a system.  The precision of
architectural models stems directly from each notation's underlying semantics,
which is, in turn, based on a formal specification method (e.g., communicating
sequential processes, ¦° calculus, finite state machines, temporal logic).

This course will expose students to formal specification methods, with a
particular focus on those used in software architectures. A secondary focus of
the class will be on the many software development activities, including
architecture, that benefit from the use of formal methods. Several categories
of formal methods will be studied, including algebraic, axiomatic, model-
based, state-based, and temporal.  Specific modeling formalisms within each
category will be highlighted and their applicability to software architectures
assessed.  Students will study different types of formal specification
languages and utilize specific languages to describe software systems.
Students will demonstrate their understanding of the covered material through
class presentations.  Additionally, students will be required to complete a
course project that will investigate the application of a formal method on a
specific, architecturally relevant problem.

At the end of the course, students should be conversant with the primary
current approaches to formal methods and their use in software engineering.
Students should be familiar with the "canonical" examples typically used in
research papers (e.g., gas station, elevator, cruise control, alarm clock).
Students should also be aware of the major open problems in the use of formal
methods in software engineering and software architectures, such that research
within this domain would be a natural follow-on to this course.

Course requirements are

[1]   reading relevant papers on formal methods,

[2]   a presentation of the details of one and a modeling exercise involving
another formal method,

[3]   participation in class discussions, and

[4]   a semester project.

* * *

# Readings

  * There is no textbook for the course.
  * Several papers (see the Schedule) will be used as the basis of the course.  Copies of these papers will be available for purchase from the Department office (SAL300). Furthermore, students tasked with presenting a particular topic will be required to locate additional relevant papers as needed.
  * To aid your note taking, I will also make the lecture slides available on-line. Students in charge of a given presentation will be required to mail their slides to [me](mailto:neno@usc.edu) by noon of the day of the presentation. Students will be able to download the slides by going to the appropriate _Discussion Topic_ in the  Schedule.

* * *

# Assignments

#### Name

|

#### Description

|

#### Weight  
  
---|---|---  
  
Presentations

|

Each student will be required to collaborate with one or two classmates and
present the details of one category of formal methods.

|

25%  
  
Examples

|

Each student will be require to collaborate with one or two classmates and
model two example systems in a specific formal method (e.g., Statecharts or
OBJ). The two examples are [cruise
control](http://sunset.usc.edu/classes/cs599_2000/CruiseControl.pdf) and [gas
station](http://sunset.usc.edu/classes/cs599_2000/GasStation.pdf).

|

25%  
  
Class participation

|

Students are expected to prepare for each class (by reading papers) and
actively participate in the discussions of the topics for which they are not
presenters.

|

25%  
  
Class project

|

Eight groups of two students will use a single formal approach to provide an
in-depth model of NeoChiron and, based on the primitives provided by
NeoChiron, the C2 architectural style. NeoChiron has been referred to as the
"assembly language" or architectural modeling and composition. The C2 style
has a set of higher-order architectural primitives that should be expressible
by an architectural "assembly language." The students are required to select a
formal method for which modeling and analysis tool support exists; each group
is expected to analyze their model and demonstrate its properties. Given that
different formal methods' strengths and tool support vary, the demonstrated
properties are also likely to be different across projects. Ultimately, the
exercise will allow a comparison of the suitability of the various formal
modeling techniques for the needs of software architectures and, potentially,
the ability to combine them in a single specification. The details of the
project are discussed and supporting materials provided in Week 4.



In addition to the 30-minute presentations of each project's results,
scheduled in class in weeks 14 and 15 of the semester, each group is also
required to submit a detailed written report by December 11.

|

25%  
  
* * *

# Schedule (Subject to Change)

**_Week_**

|

**_Date_**

|

**_Discussion Topic_**

|

**_Readings_**

|

**_Presenters_**  
  
---|---|---|---|---  
  
1

|

Aug 31

|

  * Course Introduction
  * Overview of Software Architectures ([PDF](http://sunset.usc.edu/classes/cs599_2000/August31.pdf))

|



|

  * Medvidovic

  
  
2

|

Sep 7

|

  * Introduction to Formal Methods ([PDF](http://sunset.usc.edu/classes/cs599_2000/September7.pdf))
  * Overview of Formal Methods in Software Architectures ([PDF](http://sunset.usc.edu/classes/cs599_2000/September7b.pdf))

|

  * A. Hall. **Seven Myths of Formal Methods.** _IEEE Software_ , 7(5):11-19, September 1990.
  * R. A. Kemmerer. **Integrating Formal Methods into the Development Process.** _IEEE Software_ , 7(5):37-50, September 1990.
  * J. M. Wing. **A Specifier 's Introduction to Formal Methods.** _IEEE Computer_ , 23(9):8-24, September 1990.
  * N. Medvidovic and R. N. Taylor. **A Classification and Comparison Framework for Software Architecture Description Languages.** _IEEE Transactions on Software Engineering_ , 26(1):70-93, January 2000.

|

  * Medvidovic

  
  
3

|

Sep 14

|

DARPA meeting - No Class  
  
4

|

Sep 21

|

  * Course Project Discussion ([PowerPoint](http://sunset.usc.edu/classes/cs599_2000/September21a.ppt))

|

  * R. N. Taylor et al. **[A Component- and Message-Based Architectural Style for GUI Software.](http://sunset.usc.edu/classes/cs599_2000/C2-TSE.pdf)** _IEEE Transactions on Software Engineering_ , 22(6):390-406,  June 1996.
  * N. R. Mehta et al. **[Towards a Taxonomy of Software Connectors.](http://sunset.usc.edu/classes/cs599_2000/Conn-ICSE2000.pdf)** _22 nd International Conference on Software Engineering_, Limerick, Ireland, June 2000.
  * N. Medvidovic. **[Formal Definition of the Chiron-2 Software Architectural Style.](http://sunset.usc.edu/classes/cs599_2000/C2inZ.pdf)** Technical Report UCI-ICS-95-24, Department of Information and Computer Science, University of California Irvine, April 1996.

|

  * Mehta and Medvidovic

  
  
  * State-Transition Specification ([PowerPoint](http://sunset.usc.edu/classes/cs599_2000/September21b.ppt))

|

  * D. Harel. **Statecharts: A Visual Formalism for Complex Systems.** _Science of Computer Programming_ , 8(1987):231-274, 1987.
  * J. M. Atlee and J. Gannon. **State-Based Model Checking of Event-Driven System Requirements.** _IEEE Transactions on Software Engineering_ , 19(1):24-40, January 1993.
  * B. Auernheimer and R. A. Kemmerer. **ASLAN User 's Manual. __** Technical Report TRCS84-10, University of California, Santa Barbara, April 1992.
  * B. Selic. **Turning Clockwise: Using UML in the Real-Time Domain.** _Communications of the_ ACM, 42(10):46-54, October 1999.

|

  * Bhachech
  * Dincel
  * Mehta

  
  
5

|

Sep 28

|

  * State-Transition Example ([PowerPoint](http://sunset.usc.edu/classes/cs599_2000/September28a.ppt))

|



|

  * Gao
  * Rakic
  * Roshandel

  
  
  * Axiomatic Specification ([PDF](http://sunset.usc.edu/classes/cs599_2000/September28b.pdf))

|

  * C. A. R. Hoare. **An Axiomatic Basis for Computer Programming.** _Communications of the ACM_ , 12(10):576-583, October 1969.
  * D. C. Luckham and F. W. von Henke. **An Overview of Anna, A Specification Language for Ada.**   _IEEE Software_ , 2(2):9-23, March 1985.
  * N. Medvidovic, D. S. Rosenblum, and R. N. Taylor. **Heterogeneous Typing for Software Architectures.** Submitted to _ACM Transactions on Software Engineering and Methodology_ , 1999.

|

  * Al Said
  * Apcar
  * Jerejian

  
  
6

|

Oct 5

|

  * Axiomatic Example ([PowerPoint](http://sunset.usc.edu/classes/cs599_2000/October5a.ppt))

|



|

  * Dincel
  * Rampurwala

  
  
  * Abstract Model Specification ([PowerPoint](http://sunset.usc.edu/classes/cs599_2000/October5b.ppt))

|

  * J. M. Spivey. **The Z Notation: A Reference Manual.** Oriel College, Oxford, England, 1998. 
  * D. Jackson. **Alloy: A Lightweight Object Modeling Notation.** Technical Report, Laboratory of Computer Science, Massachusetts Institute of Technology, July 2000.
  * P. Inverardi and A. L. Wolf. **Formal Specification and Analysis of Software Architectures Using the Chemical Abstract Machine Model.** _IEEE Transactions on Software Engineering_ , 21(4):373-386, April 1995.
  * G. Abowd, R. Allen, and D. Garlan. **Formalizing Style to Understand Descriptions of Software Architecture.** _ACM Transactions on Software Engineering and Methodology_ , October 1995.

|

  * T. Garg
  * Nagaraj

  
  
7

|

Oct 12

|

  * Abstract Model Example ([PowerPoint](http://sunset.usc.edu/classes/cs599_2000/October12a.ppt))

|



|

  * Mehta
  * Patel
  * Viswanathan

  
  
  * Algebraic Specification ([PowerPoint](http://sunset.usc.edu/classes/cs599_2000/October12b.ppt))

|

  * J. A. Goguen and T. Winkler. **Introducing OBJ3.** Technical Report, SRI-CSL-88-9, SRI International, August 1988.
  * J. V. Guttag, J. J. Horning, and J. M. Wing. **The LARCH Family of Specification Languages.** _IEEE Software_ , 2(5):24-36, September 1985. ****
  * W. Tracz. **Parameterized Programming in LILEANNA.** _ACM/SIGAPP Symposium on Applied Computing: States of the Art and Practice_ , Indianapolis, IN, February 1993.

|

  * Rakic
  * Roshandel

  
  
8

|

Oct 19

|

  * Algebraic Example ([PowerPoint](http://sunset.usc.edu/classes/cs599_2000/October19b.ppt))

|



|

  * T. Garg
  * Nagaraj

  
  
  * Temporal Specification ([PowerPoint](http://sunset.usc.edu/classes/cs599_2000/October19a.ppt))

|

  * L. Lamport. **What Good Is Temporal Logic?** _9 th_ _ World Computer Congress_ _, 657-668, Paris, France_ , IFIP, North Holland, 1992. __
  * L. A. Dillon, G. Kutty, L. E. Moser, P. M. Melliar-Smith. **Graphical Specifications for Concurrent Software Systems.** _14 th International Conference on Software Engineering_, 214-224, May 1992.
  * D. C. Luckham, J. J. Kenney, L. M. Augustin, J. Vera, D. Bryan, and W. Mann. **Specification and Analysis of System Architecture Using Rapide.** _IEEE Transactions on Software Engineering_ , 21(4):336-355, April 1995.

|

  * Patel
  * Viswanathan

  
  
9

|

Oct 26

|

  * Temporal Example ([PowerPoint](http://sunset.usc.edu/classes/cs599_2000/October26b.ppt))

|



|

  * Al Said
  * Bhachech
  * A. Garg

  
  
  * Concurrency Specifications ([PowerPoint](http://sunset.usc.edu/classes/cs599_2000/October26a.ppt))

|

  * U.A. Buy and R. Moll. **A Specification-Based Approach to Concurrency Analysis.** _Journal of Automated Software Engineering_ , 2(2):265-309, 1995.
  * G. Naumovich, G. S. Avrunin, L. A. Clarke, and L. J. Osterweil. **Applying Static Analysis to Software Architectures.** _6 th European Software Engineering Conference together with 5th ACM SIGSOFT Symposium on the Foundations of Software Engineering_, 77-93, Zurich, Switzerland, September 1997.
  * R. Allen and D. Garlan. **A Formal Basis for Architectural Connection.** _ACM Transactions on Software Engineering and Methodology_ , 6(3):213-249, July 1997.

|

  * A. Garg
  * Rampurwala

  
  
10

|

Nov 2

|

  * Concurrency Example ([PowerPoint](http://sunset.usc.edu/classes/cs599_2000/November2a.ppt))

|



|

  * Apcar
  * Chiu
  * Jerejian

  
  
  * Formal Verification ([PowerPoint](http://sunset.usc.edu/classes/cs599_2000/November2b.ppt))

|

  * S. Igarashi, R. L. London, and D. C. Luckham. **Automatic Program Verification I: A Logical Basis and Its Implementation.** _Acta Informatica_ , 4:145-182, 1975.
  * S. L. Hantler and J. C. King. **An Introduction to Proving the Correctness of Programs.** _ACM Computing Surveys_ , 8(3):331-353, September 1976.
  * R. A. DeMillo, R. J. Lipton, and A. J. Perlis. **Social Processes and Proofs of Theorems and Programs.** _Communications of the ACM_ , 22(5):271-280, May 1979.
  * M. Moriconi, X. Qian, and R. A. Riemenschneider. **Correct Architecture Refinement.** _IEEE Transactions on Software Engineering_ , 21(4):356-372, April 1995.

|

  * Chiu
  * Gao

  
  
11

|

Nov 9

|

FSE 2000 - No Class  
  
12

|

Nov 16

|

  * Multi-Paradigm Modeling ([PowerPoint](http://sunset.usc.edu/classes/cs599_2000/November16.ppt))

|

  * A. Finkelstein, D. Gabbay, A. Hunter, J. Kramer, and B. Nuseibeh. **Inconsistency Handling in Multiperspective Specifications.** _IEEE Transactions on Software Engineering_ , 20(8):569-578, August 1994.
  * P. Zave and M. Jackson. **Where Do Operations Come From? A Multiparadigm Specification Technique.** _IEEE Transactions on Software Engineering_ , 22(7):508-528, July 1996.
  * L. Blair and G. Blair. **Composition in Multi-Paradigm Specification Techniques.** _3 rd International Conference on Formal Methods for Open Object-Based Distributed Systems_, Florence, Italy, February 15-18, 1999.
  * P. Tarr, H. Ossher, W. Harrison, and S. M. Sutton, Jr. **_N_ Degrees of Separation: Multi-Dimensional Separation of Concerns.** _21 st International Conference on Software Engineering_, 107-119, Los Angeles, CA, May 1999.

|

  * Medvidovic

  
  
13

|

Nov 23

|

Thanksgiving Day - No Class  
  
14

|

Nov 30

|

  * Project presentations and discussions

|



|

  
  
15

|

Dec 7

|

  * Project presentations and discussions

|



|

  
  


|

Dec 11

|

  * Final project write-ups due

|



|

  
  
* * *

Last updated:  11/16/00

