# Announcements (Unix Tools, spring 2001)

Most recent announcement (bottom of page)

I will refer to your texts "Unix Primer Plus" as primer, and "Unix for
Programmers and Users" as glass.

Tues, jan 16 2001 (Lec 01): First class. Introductory and administrative
stuff. Your grader Tao Ling said hi to you. We took a quick look at some of
the capabilites of Unix. There is a problem with acf5 (as you all know), and I
will explain this, as well as I understand it, next class. Apparently, we will
all be using i5 (not is5) soon, according to the ITS, but for now, (almost) no
one can run anything on acf5. You should all click on the link about the [mail
list](mail_list.htm), and subscribe immediately, please. There was a problem
with the mail list earlier, but the system folks seem to have fixed it up. I
will assign homework next class (very simple) that will not require the use of
acf5, which is just as well, because we won't have access to acf5 by then,
anyway.

Thurs, jan 18 2001 (Lec 02): We discussed why learning Unix can be useful. One
major reason is that many, if not most, web servers run Unix. We talked about
the file/directory structure of a Unix system. We discussed showing your
current directory with pwd (see glass chap. 2 and primer chap. 7). We talked
about changing directories with cd (primer chap. 7, glass chap. 2). In glass
chap. 2 you will also find coverage of the concepts of absolute and relative
pathnames. We glanced at getting on-line help with with man (primer chap. 3,
glass chap. 2). We discussed the ls command (see primer chap. 4 and glass
chap. 2), including some of its options, including the -a option to show "dot
files". We glanced at the .login and .cshrc files, and showed how to add
commands to the .login file. We discussed filename completion, and discovered
that the variable filec needs to be set to enable this feature. We put the
command set filec inside my .login file so that filename completion would be
enabled every time I login. We discussed the use of the * wildcard (primer
chap. 7, glass chap. 3), and I confused myself and the class with a couple
examples using this feature, which I will clarify next class. Please note that
if you choose to skip lecture, you risk missing material that may not be
covered, or covered in depth, or covered well, in your text(s).

Please note that homework #1 has been posted! There is a new
[homework](homework.htm) link on the main class page. As I get feedback from
you (from your homework #1's), this will help me tighten up the syllabus and
plan of action for the course.

Please note that there is a new link on the main page (more on student
civility), called [student civility 2](student_civility2.htm). Kindly read
this, thanks.

If you want to ask me something after class, please wait outside the
classroom, so I can ready the room for the next instructor, and then will be
out in the hallway ASAP.

Please note that you all now *should* have accounts on i5.nyu.edu. Login name
is netID, initial password is first 5 digits of SSN (I also e-mailed this info
to class list).

Tues, jan 23 2001 (Lec 03): One thing I forgot to do today was talk a bit more
about wildcards, and about the problem I had at the end of class two lectures
ago, when I tried ls *. I will talk about this (and how to recursively list
the contents of all directories) briefly at the beginning of next class. Today
we quickly walked through some file manipulation basics. We looked at the use
of cat to create simple text files (Glass, p. 26, Primer p. 72). This involved
the concept of redirecting standard input and output. We also saw how to use
cat to simply show a file's contents on the screen. We looked at how to copy a
file with cp, rename a file with mv, and delete a file with rm. Recall the use
of the -i option to prompt before overwriting a file. We created one or two
simple aliases. We will see how to put aliases (and other stuff) in your
.login and .cshrc startup files. We discussed some uses of more. Recall that
when at the "more prompt", you can type ?, and you have tons of options that
you can perform at that point. We looked at some examples of creating
pipelines with the use of pipes. Pipes use the | symbol (on the same key as
the backslash). In this context, we used sort and who and wc. I don't recall
every command we looked at today, but you can find coverage of all the simple
stuff we did today in the early chapters of your texts. And you can always use
the man command to get info on a command. I will work on a more precise
syllabus over the next few days (including chapter references in your texts),
though it is hard to stick to these things 100%. If you just joined the class,
be sure to do [homework](homework.htm) #1 immediately, please. You new folks
will also need accounts on i5.nyu.edu; I'll have to find out how this works
and get back to you... In the meantime, you can try logging on with your netID
and first 5 digits of SSN (this may not work yet for you new folks; don't
panic and flood me with mail, please). Next class, I will give you some fun
homework to do.

Thurs, jan 25 2001 (Lec 04): Today we really had some fun. We talked some more
about wildcards, including *, ?, and [..]. These things are powerful and
useful, especially if you adopt and stick to file-naming conventions. You can
read all about wildcards in both of your texts. We then talked a good deal
about file (and directory) permissions. We saw how to change permissions using
chmod. I personally prefer to use the octal number form of the chmod utility,
but you should be aware of another method (using letters, etc). This stuff is
fully described in both of your texts. At the end of class, I did a really
(really!) quick tiny example of a C-shell script. Be sure to read Glass chap.
3, which talks about common functionality of all shells (including passing
command-line arguments to scripts). You should read all of Glass chap. 3, as
we will cover most of that material in the classes to come. Also read Glass
chap. 6, which talks about C-shell specific stuff.

Homework #2 has been posted on our web page, under the
[homework](homework.htm) link. Please check it out for details! I will update
this announcements page again tomorrow (Sat).

jan 27 2001: I am reading your e-mails, and working on a revised syllabus. I
will do my best to stick to it, but changes, falling behind, etc., are hard to
avoid. It will not leave behind people with little or no Unix background,
because there are no Unix pre-reqs. But I expect the pace will pick up a bit.

jan 27 2001: I have posted an [addendum to the hwk #2
writeup](hwk02_addendum.htm), which is found under the
[homework](homework.htm) link. This includes crucial info about exactly how to
submit your homework, and exactly (time of day) when it is due, and other
useful info. You are totally responsible for the material there, so be sure to
read it!

Tues, jan 30 2001 (Lec 05): Today we talked a good deal more about various
command-line "tricks". We discussed list variables (Actually, you can think of
a "simple" variable as a list variable of length 1. In that sense, *all*
variables are list variables). List variables can be indexed sort of like
arrays (but starting with index 1, not 0). We discussed the use of the
backslash (\) character to escape a character with special meaning. For
example

% echo \\*

will just print a star, instead of a list of your files. We also discussed
quoting, and the differences between single quotes and double quotes. We
looked at command substitution, which uses the backtick (`) character. See the
brand new [programs from lecture](programs.htm) link on the main page for an
example of a simple script that uses command substitution. I showed you a
handy use of the mailx mail program for quick-and-dirty emails. Actually, the
mailx program is *extremely* useful for automating emails from within a
script. Let's see... we talked about the path that Unix uses to search for
programs that you want executed. It is common and useful to change your path
to customize it for your own purposes. We also discussed some C-shell history
tidbits, which are useful for quick re-execution of previously issued
commands. We also started on the large and complex topic of processes, which
will require somewhat more attention. We saw that from your login shell, you
can invoke a sub-shell interactively, for example by typing

% sh

you invoke a Bourne shell and your login shell just chills til you exit the
sub-shell. The login shell (in this case) is the parent shell, and the sub-
shell is the child shell. When you execute a script, that script is executed
by a sub-shell (the one specified in the very first line of the script, called
the "shebang line"). We took a small foray into the world of background
processing, which we will, of course, talk about more. In this context, we
will discuss some simple uses of the extremely complex and unbelievably
powerful find utility.

I also wrote and showed you a simple script (see the [programs](programs.htm)
link) that counts and echoes command-line arguments. Recall you must use @
(not set) for arithmetic in the C-shell.

In the meantime, peruse all these topics in Glass, chaps. 3 and 6 (mostly),
and you can also find pretty good coverage in the Primer book. Don't worry,
that book will come in useful, you'll see :) Please recall that you have
[homework #2](hwk02.htm) (calculator script) due this Friday. For homework
help, please write to Alexander (email address found under [course
info](outline_v22_sp01.htm) link.) or the class list, but not to me. (I do
read mail sent to the list.) This is a reflection of the way the department
structures the course. Note: you may also find it useful to read up on so-
called here documents, covered both in Glass and the Primer. _Here documents_
may come in handy for hwk #2, though are not required. Enough for now... peace
out...

Thurs, feb 01 2001 (Lec 06): Today I missed class due to a personal emergency.

Tues, feb 06 2001 (Lec 07): Today we talked a good deal about job control in
the C shell. We looked at the jobs command, and various ways of putting jobs
in the foreground, background, stopping them, resuming them, etc. We saw how
to direct standard output and standard error to the same file, and how to
direct them separately with a clumsy "trick". We saw one use of the find
command: to locate a file within a directory "branch". We also learned how to
create parameterized aliases (very useful!). The entire transcript of the
class session is posted under the [programs](programs.htm) from lecture link
on the main page. Recall that the late date for hwk #2 (the calculator script)
is Friday, feb 9.

Thurs, feb 08 2001 (Lec 08): Today we talked more about job control, and saw
that background jobs continue even when you log out, but lose their control
terminal. We looked at some uses of grep, and had an intro to limited regular
expressions. We also some of the options that can be used with grep. Note that
grep supports escaped angle brackets to find stand-alone words, eg "hi there"
but not "him" (for "hi"). For example:

**_% grep '\ <hi\>' filename_** ...finds "hi" only as a word.

I'm not sure how to get grep to deal with the tab character, but I will
investigate this. We will learn more about grep, sed, awk, find, and others,
and see how these can be used to create highly flexible, powerful commands and
scripts. Perl has outstanding regular expression support, and text-handling
facilites in general, and we will see some exciting uses of Perl in this
capacity. Note the entire [transcript](feb0801.log) of today's class session
is posted under the [programs](programs.htm) from lecture link on the main
page. I stronly urge you to read the relevant sections of your texts, as this
will help solidify your understanding of these new, confusing-at-first
concepts.

Recall that the late date for [hwk #2](hwk02.htm) (the calculator script) is
Friday, feb 9. Next week I will give some exciting, highly challenging new
homework.

Sun, feb 11 2001: I posted my [hwk #2 (calculator script) solution](calc)
under the [homework](homework.htm) link on the main page. I updated the
[syllabus](syll_v22_sp01.htm) for weeks 5 - 7 (please check it out!), and I am
working on midterm exam review guidelines.

Tues, feb 13 2001 (Lec 09): Today we talked a good deal more about grep and
limited regular expressions. We did not yet get to egrep, which uses extended
regular expressions, or Perl, whose regular expression capabilites are even
_more_ extended.

Suppose you want to find the literal string _`date`_ in a file. Think about
the difference between

% _grep '`date`' filename_

and

% _grep "`date`" filename_

This should help illustrate why we (almost always) use  single quotes when
delimiting a regular expression typed at the shell prompt.

Also think about how to write a single grep command to find all lines in a
file that contain one or more repetetions of a single character. Joe came up
with it perfectly, and I'm sure you all can, too. Just to get your creative
juices flowing: You will need to "remember" the very first character on the
line, and then determine whether all subsequent characters on that line are
that same "remembered" character.

I started to show you the use of my limited _ts_ C-shell script ( _ts_ stands
for _text search_ based on a Norton Utility I used as a youngster). There was
a problem when I used  *, but that's not a problem with * per se. I'll say
more about this in the formal write-up.

I will formally assign new homework tomorrow (Thurs). I am working on a
summary of what to study for the midterm, but in the meantime you can get a
good idea from the stuff posted on this announcements page.

Please check out [Student Civility](student_civility.htm), [Student
Civility2](student_civility2.htm), and [e-mail
guidelines](email_guidelines.htm) (all these links are on the main page).

Please note that as usual, today's entire class [transcript](feb1301.txt) is
posted under the [programs](programs.htm) link.

Thurs, feb 15 2001 (Lec 10): Today we had our must fun (and productive) class
yet. The entire class [transcript](feb1501.txt), is as usual, posted under the
[programs from lecture](programs.htm) link on the main page. We discussed
egrep, and looked at its extended regular expression capabilites. A possible
exam question might ask something about obtaining the effect of an extended
regular expressions metacharacter (e.g. +, or ?) by using limited regular
expressions (what you have with _grep_ as opposed to _egrep_ ). We then looked
at how to set up your i5 account to do CGI-Perl stuff, and looked at an
example of a web page with a form. The form's input is then sent to the server
( _i5.nyu.edu_ , in this case) by clicking the _send data_ or _submit_ button.
Then your  perl script (ending with the _.cgi_ extension) checks for a valid
zip code using regular expression matching. These files
([using.html](using.html), [using.cgi](using.cgi),
[subparseform.lib](subparseform.lib)) are posted under [programs from
lecture](programs.htm). Detailed instructions on how to set up your  i5 web
page and CGI stuff can be found at <http://i5.nyu.edu>. You must follow these
instructions to a T, or this whole thing will not work. **_Note_** : when you
copy _using.html_ to your own public_html directory, you will see a line
inside that file containing my userID, _dqb3240_. Be sure to change the
dqb3240 to your own userID. Make sure all directories and files have right
permissions.

Fri, feb 16 2001: Just added new link to main page for [midterm
review](mid_review.htm). Check it out!

Sat, feb 17, 2001: Please check out the write-up for [hwk #3](hwk03.htm) (the
text search ts script) on the [homework](homework.htm) page.

Sat, feb 17, 2001: Just added another new link on main page for [midterm
review 2](mid_review2.htm). Check it out! Please understand that these
"midterm review" postings only reflect what we have covered so far ( _through
Thurs feb 15_ ). There we be additional material not posted on these lists
that you will be responsible for on the midterm.

Mon, feb 19, 2001: Happy Presidents (President's?) (Presidents'?) Day! I just
added a tiny addendum to the [midterm review 2](mid_review2.htm) guidelines
(from the Glass text).

Tues, feb 20 2001 (Lec 11): Today we looked more at regular expressions in
Perl (entering data into a web page, and using the CGI protocol). We worked
through an example of validating a zip code, and building in some flexibility
to make data entry easier and more intuitive for the "naive user" like my
grandmother. You should think about how we might handle this to validate a
phone number (area code required or optional? optional parens around an
optional area code? required or optional dashes and spaces? how many? etc.
etc.).

We also had a brief introduction to sed. We will, of course, talk more about
sed. I will assign you an addendum to hwk #3 (the _ts_ text search script) to
force you to get some practice with sed. That addendum will be considered a
part of hwk #3, and will be due on the same due date as hwk #3, and will be
submitted with hwk #3, as a separate attachement. This addendum will _not be
any big deal_ , trust me! Stay tuned for details on this addendum.

Be sure to get Perl-CGI up and running on your i5 accounts. This will be
necessary for you to get practice doing this stuff; you will really need to
know how to do this, both for this course, and in future courses and "real
world" situations. The Perl-CGI stuff is not covered in either of your texts,
but I have given you plenty to go on, and you can find the whole scoop at
<http://i5.nyu.edu>.

The readings for sed are Primer, chap. 10, and Glass, chap. 7 (p. 253 - 257).
See, now you know what sections of the book to read :)

Please note that today's class [transcipt](feb2001.txt) is posted, as usual,
under the [programs from lecture](programs.htm) link on the main page. So is
[zip.html](zip.html) and [zip.cgi](zip.cgi). Check it out!

Thurs, feb 22, 2001: Please note that I added a [new
link](perl_class_shorthands.htm) on the main page listing the Perl class
shorthands I showed you last class. Also, please note that due to overwhelming
lack of interest, tomorrow's (Fri feb 23) make-up class has been cancelled.

Thurs, feb 22 2001 (Lec 12): Today we briefly reviewed the zip code validation
example from Perl, which I have posted on the web site as zip.html, and
zip.cgi (posted last lecture). I suggest you peruse and perhaps play with
these. Note that the use of $1, $2, etc., could be improved inside zip.cgi.
Even though we didn't exactly learn much Perl yet, you should think about
this. Recall how each item "remembered" by a pair of parens is referred to (in
Perl) as $1, $2, etc. (similar to \1, \2, etc. in grep, sed).

Today we looked at a bunch of sed stuff. Recall that sed is "non-destructive",
meaning it only writes its changes to standard output by default. I sincerely
apologize for my mistakes, confusion, and wasted time trying to use the _i_
flag with sed to ignore case, which doesn't exist in sed (it does in Perl,
however).

In sed, the following is the correct way to find all lines containing an _a_ ,
and change the _first_ _a_ in all such lines to a _b_.

% sed 's/a/b/' filename

In this next example, I changed _all_ _a_ 's to _b_ 's. Note the _g_ flag. I
posted [sed_story.txt](sed_story.txt) on the [programs](programs.htm) link for
you to play around with this:

% sed 's/a/b/g' filename

I then wasted your time, (and you have my  sincerest apologies) trying to get
sed to ignore case by doing the following: The intent here is replace the
first _a_ of either case (if any) on each line with a _Q_. Only problem is, no
such flag as _i_ (to ignore case) in sed! (Of course, there are ways around
this, but it's much easier (shock!) in Perl.) So the following is  illegal in
sed:

% sed 's/a/Q/i' filename

Perl, however, lets me do this. Note the use of the _i_ flag:

if ($var =~ /daniel/i)... ... matches Daniel, daniel, dAnIeL, etc. I posted
[alt.perl](alt.perl) to demo this _i_ flag.

grep (and egrep), of course, have a _-i_ option to ignore-case.

Also, be careful with the following; although it is perfectly legal to write
something like:

% sed 's/^hey/hoo/' *.txt

...all output will dumped in one continuous "stream" to standard output. This
is probably not what you want. To do something more useful, you will probably
want a simple script to loop through your _*.txt_ files (possibly with
_foreach_ ), and handle each *.txt file separately.

I will show use you how (or point you in the right direction :) to use find
combined with sed to recursively do stuff like: find all _*.java_ files in and
below your home directory, changing all occurrences of _system.out_ to
_System.out_.

To clarify some other sed matters I messed up in class, here are some
examples:

% sed 'd' filename ...deletes _all_ lines, since no range is given  
% sed '3d' filename ... deletes only the 3rd line (counting starts at 1)  
% sed '/e/d' filename ...deletes _all_ lines containing _e_

Your midterm exam is this coming Thursday, March 1, 2001.

Tues, feb 27 2001: Please note the error that a sharp student pointed out in
your Glass text, on p. 81: The result of the command:

% _echo hi \ > file_

is to print the string _hi > file_ literally to standard output, _not_ to
create a file called _file_.

Tues, feb 27 2001 (Lec 13): Today we reviewed for the midterm exam, which is
this Thursday, March 1st, usual room and time. The exam is open-book; you may
bring any books and notes. But you may not exchange any materials whatsoever
with your classmates! I showed you an interesting, useful (?) C-shell script
called [mail_list.csh](mail_list.csh), which of course is posted under the
[programs](programs.htm) link on the main page. I also, as always, posted
[today's transcipt](feb2701.txt) under the [programs](programs.htm) link.
Also, more or less by popular demand, I will squeeze in an emacs lecture
"soon". Error correction: please note that a student (Vito?) asked whether
egrep supports the _\ <_ and _\ >_ metacharacters, and I said I think so. But
Vito's right, egrep _does not support_ these particular reg exp metacharacters
(but grep does).

Thurs, mar 01 2001 (Lec 14): Today was our midterm exam. I will post solutions
shortly.

Tues, mar 06 2001 (Lec 15): Today we had an intro to awk, but we used the
newer version called nawk, which is upward-compatible with awk. I have posted
two files under the [programs](programs.htm) link. One,
[awk_stuff.txt](awk_stuff.txt), is a plain text file I prepared before class,
chock full of awk examples, annotated liberally with useful comments. I
strongly urge you to read through these examples, and try them out! The other
file I posted, [mar0601.txt](mar0601.txt), is the usual telnet capture of
today's session. I am working on grading the exams, and will post them on
Tao's site just as soon as I can (at that time, I will e-mail the list to let
you know). Til then, please sight tight. I am considering assigning new
homework tomorrow (Thurs, march 8), but may defer that til after break.

Thurs, mar 08 2001 (Lec 16): Today we looked at a couple more awk examples,
posted under the [programs](programs.htm) link. I strongly urge you to look at
these, and get them to your account to run them. We also looked at some uses
of the find command, though there just wasn't enough time to go through all of
find's uses. Therefore, you should look at the examples in both of your texts,
and try them out. Finding files by last modification time is particularly
useful (as far as the stuff we didn't get to in lecture). I also posted (under
the [programs](programs.htm) link) a file called
[find_stuff.txt](find_stuff.txt), which contains a bunch of examples with
clear explanations, that I had prepared before-hand. Please look thru this
file! All reading is listed under the [syllabus](syll_v22_sp01.htm) link.

I will assign homework later today (Sat), and will write you when it's ready.
Don't worry! There will be time to start after break (but not too long after
break).

I will mail the list when your exams are graded! Please don't write asking me
when, thanks!

Fri, mar 16, 2001: Please note that I have posted the "formal"
[hwk04](hwk04.htm) writeup under the [homework](homework.htm) link. Please
check it out!

Tue, mar 13, 2001 SPRING BREAK!

Thu, mar 15, 2001 SPRING BREAK!

Tues, mar 20 2001 (Lec 17): Class covered by Toto Paxia.

Thurs, mar 22 2001 (Lec 18): Class covered by Marc Walmdan.

Tues, mar 27 2001 (Lec 19): No class coverage :(

Thurs, mar 29 2001 (Lec 20): Class covered by David Mazieres.

Tues, apr 03 2001 (Lec 21):Today was my first day back after a two-week
absence due to illness. We talked about Perl basics today ( _scalars_ ,
_arrays_ , _hashes_ ), and looked at some sample programs, which are posted,
as usual, under the [programs from lecture](programs.htm) link. I didn't show
an example program about hashes, so I will do so on the computer next class
(Thurs). It will be a tiny little "password" program. We also talked a bit
about [homework #4](hwk04.htm), which I will spend more time on tomorrow
(Thurs). I will also assign new homework by Friday of this week. I have also
posted today's [telnet session](010403.txt), as usual, under the
[programs](programs.htm) link. I will also post the [solutions to the midterm
exam](mid_solns.htm).

Thurs, apr 05 2001 (Lec 22):Today we looked at a couple Perl programs showing
the use of hashes in Perl. We also looked at the basic mechanics of the Perl-
CGI protocol. Note that the hash programs are posted under [programs from
lecture](programs.htm) link, and there are also links under [programs from
lecture](programs.htm) from some time ago, that show the HTML and Perl source
for the simple zip code program we looked at today in class. As I wrote to the
class list, _we have not yet learned enough new material to assign a new
homework_ , so that will need to wait til next week. Of course, today's telnet
session is posted as usual under the programs link. We also spent a good deal
of time going over the requirements of [homework 4](hwk04.htm).

Tues, apr 10 2001 (Lec 23): Today we looked at some more examples of Perl and
CGI stuff. I have created a link on our main class page that takes you to all
the [Perl-CGI examples](http://www.stern.nyu.edu/~dbarrish/c20.0056_sp00/) on
my Stern account. These are the ones I have been showing you in class. From
that page, you can download the HTML files, as well as the cgi (Perl) scripts.
You will need to make some simple changes when putting files from
_eureka.stern.nyu.edu_ onto _i5.nyu.edu_. For example, your Perl scripts on i5
should have as their first line:

#!/bin/perl

and you will also need to changed the  ACTION attribute. As usual, all files,
including the entire [telnet transcript](010410.txt), are posted under the
[programs from lecture](programs.htm) link.

Thurs, apr 12 2001 (Lec 24): Today we looked more closely at the mechanics of
Perl-CGI. We saw how a Perl (cgi) script received all data from the
corresponding HTML form in the formdata hash variable. We also saw the
distinction between user commands and system calls, looking at the man pages
for chmod as an example. We then saw that you cannot enter

% localtime

at the shell prompt, but that you can call this function (it's a C standard
routine, but does make a call to the Unix kernel) from a Perl program (or a C
program, and some other high-level languages, for that matter). Check out the
program [system_calls.perl](system_calls.perl) for this example. Today's
examples are posted under the [programs](programs.htm) link as usual. Please
recall there is a link on the main page to my [account at
Stern](http://www.stern.nyu.edu/~dbarrish/c20.0056_sp00/) showing all the
Perl-CGI examples. As usual, today's [telnet session](010412.txt) is also
posted under the [programs](programs.htm) link.

Sun, apr 15, 2001: Please note that I have posted hwk #5 under the
[homework](homework.htm) link!

Tues, apr 17 2001 (Lec 25): Today we talked more about Perl basics. We talked
about numbers vs. strings, and about scalar context vs. list context. Today's
programs are posted, as usual, under the [programs](programs.htm) link. As
usual, today's [telnet session](010417.txt) is also posted under the
[programs](programs.htm) link.

Thurs, apr 19 2001 (Lec 26): Today we talked about Unix system calls. We
discussed opening files (and the concept of file descriptors). We looked at
opening a file (and creating one with programmer-specified permissions), and
we looked at getting file info with stat. We did this by looking at some C
programs, posted on our website under the [programs](programs.htm) link. We
can also make all such system calls from Perl programs! Recall there is an
optional review session on reading day, _Tues May 1, in WWH 101, from 2 til 4
pm_. Of course, today's [telnet sesssion](010419.txt) is posted under the
[programs](programs.htm) link as usual.

Sun, apr 22, 2001: I have added a link on the [main page](index.htm#top) to
help guide you in [final exam review](final_review.htm). Please check it out!

Tues, apr 24 2001 (Lec 27): Today we took a gander at the opendir() and
readdir() routines, to open and read directory entries from within a C
program. We also talked a bit about [hwk #5](hwk05.htm). As usual, the entire
[telnet session](010424.txt) is posted under the [programs](programs.htm)
link.

Thurs, apr 26 2001 (Lec 28): Today we reviewed material from throughout the
term. Today was the last regularly scheduled class. Please check out programs
posted under [programs](programs.htm) link.

Tues, may 1 2001: Today we held an optional review session in room 101 for
those who could make it. _Today was not a regularly scheduled class_.

* * *

back to [ main page](index.htm#top)

