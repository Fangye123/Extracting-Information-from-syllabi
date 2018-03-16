![cos426.jpg \(39279 bytes\)](cos426_banner.jpg)

###  Computer Graphics, Fall 2000

###  [Thomas Funkhouser](http://www.cs.princeton.edu/~funk)

[Department of Computer Science](http://www.cs.princeton.edu)  
[Princeton University](http://www.princeton.edu)  

* * *

  
General Information | Textbooks | Coursework | Syllabus | Links | References  
[Students](students/) | [Exercises](exercises/exercises.html) |
[Assignments](assignments/assignments.html) | [Final
Projects](projects/projects.html)

* * *

###  General Information

  * **Professor**
    * [Thomas Funkhouser](http://www.cs.princeton.edu/~funk/) (office hours: Mon 11AM-Noon), CS 422, [funk@cs.princeton.edu](mailto:funk@cs.princeton.edu)

  * **Teaching Assistants**
    * [Robert Osada](http://www.cs.princeton.edu/~rosada) (office hours: Friday 1-2PM), CS 413, rosada@cs.princeton.edu
    * [Misha Kazhdan](http://www.cs.princeton.edu/~mkazhdan) (office hours: Tues 3:30-4:30PM), CS 313, mkazhdan@cs.princeton.edu

  * **Lab Assistants**
    * [Dusty Lennon](http://www.princeton.edu/~dnlennon), dnlennon@cs.princeton.edu
    * [James Percy](http://www.princeton.edu/~jimpercy), jimpercy@cs.princeton.edu
    * [Casey McTaggart](http://www.princeton.edu/~mctagart), mctagart@cs.princeton.edu

  * **Times and Places**
    * Lectures: MWF 10AM, CS 105 (small auditorium).
    * Precepts: W 8PM, CS 102

  * **Prerequisites**
    * Data structures and algorithms (CS 226)
    * A good working knowledge of C programming (CS 217)
    * Linear algebra (as described in Appendix A of the course book)
    * No prior knowledge of graphics is assumed

  * **Keeping in touch**
    * [Send mail](mailto:cs426@princeton.edu) to the CS426 staff
    * Check out the [pu.cs.426](news://news.princeton.edu/pu.cs.426) newsgroup

* * *

###  Textbooks

  * **Required Textbook**
    * _Computer Graphics, C Version_ ,
  
Donald Hearn, M. Pauline Baker,  
2nd Edition, Prentice Hall, 1997, ISBN: 0135309247.

  * **Recommended Textbooks**
    * _OpenGL Programming Guide: The Official Guide to Learning OpenGL_ ,
  
Jackie Neider, Tom Davis, Mason Woo,  
3rd Edition, Addison-Wesley, 1999, ISBN: 0-201-46138-2.

    * _Computer Graphics: Principles and Practice_ ,
  
James D. Foley, Andries van Dam, Steven K. Feiner, John F. Hughes,  
2nd Edition in C, Addison-Wesley, 1995, ISBN: 0201848406.

* * *

###  Coursework

  * **"Midterm" Exam** (25%)
    * 7-9PM on Tuesday, 11/21 in CS 105
    * Closed book.   Bring a one-page "cheat sheet" with writing on both sides
    * It will be similar in style to last year's midterm ([ps](http://www.cs.princeton.edu/courses/archive/fall99/cs426/midterm/midterm.ps.gz), [pdf](http://www.cs.princeton.edu/courses/archive/fall99/cs426/midterm/midterm.pdf))


  * **Programming Assignments** (10% each)
    * [Assignment #1](assignments/assn1/assn1.html): Image Processing ([results](assignments/assn1/results/sld001.htm)) ([movies](assignments/assn1/results/movies))
    * [Assignment #2](assignments/assn2/assn2.html): Ray Tracing ([results](assignments/assn2/results.html))
    * [Assignment #3](assignments/assn3/assn3.html): OpenGL Rendering ([results](assignments/assn3/results.html))
    * [Assignment #4](assignments/assn4/assn4.html): Interactive Modeling ([results](assignments/assn4/results.html))
    * [Assignment #5](assignments/assn5/assn5.html): Keyframe Animation ([results](assignments/assn5/results/results.html))


  * **Final Project** (20%)
    * [Written proposal](projects/projects.html#Proposal) (due Sunday, December 10, 2000)
    * [Presentation of proposal](projects/projects.html#Presentation) (in class on Wednesday, December 13, 2000)
    * [Written final report ](projects/projects.html#Report)(due at 2PM on Tuesday, January 16, 2001)
    * [Demo day](projects/projects.html#Demo) (in CS105 at 2PM on Tuesday, January 16, 2001)
    * Results can be found [here](projects/projects.html#Results).

  * **Class Participation** (5%)
    * Contribute ideas in class

* * *

###  Syllabus

####  INTRODUCTION WEEK

    * **Fri 9/15: Introduction**
      * Topics: overview, applications
      * Readings: H &B 1, appendix A
      * Slides: [html](lectures/intro/index.htm), [postscript](lectures/intro/intro.ps.gz), [pdf](lectures/intro/intro.pdf)
      * Movies: Class of `98 morph ([sgi movie](http://www.cs.princeton.edu/courses/archive/fall98/cs426/assignments/morph/class.movie)), Ice Queen ([mpv](http://www.cs.princeton.edu/~zaijing/final_proj/final.mpv)), Horse ([quicktime](http://www.cs.princeton.edu/courses/archive/fall99/cs426/assignment5/results/art/mctagart_art.mov)), Santa ([mpeg](http://www.cs.princeton.edu/courses/archive/fall99/cs426/assignment5/results/art/thlui_art.mpg))

####  IMAGE PROCESSING WEEK

    * **Mon 9/18: Image Display and Color Models**
      * Topics: devices, color, perception
      * Readings: H &B 2.1-2.2, 4.3, 15.1-15.4
      * Slides: [html](lectures/raster/index.htm), [postscript](lectures/raster/raster.ps.gz), [pdf](lectures/raster/raster.pdf)
      * Exercises: [html](exercises/exercises.html#Raster)
    * **Wed 9/20: Image Quantization**
      * Topics: quantization, halftoning, dithering
      * Readings: H &B 14.4
      * Slides: [html](lectures/dither/index.htm), [postscript](lectures/dither/dither.ps.gz), [pdf](lectures/dither/dither.pdf)
      * Exercises: [html](exercises/exercises.html#Dither)
    * **Fri 9/22: Image Sampling and Reconstruction**
      * Topics: sampling, reconstruction, filtering
      * Readings: H &B 4.8
      * More Readings: [Hanrahan95] ``Basic Signal Processing,'' [ps](papers/hanrahan95.ps.gz), [pdf](papers/hanrahan95.pdf)
      * Slides: [html](lectures/sampling/index.htm), [postscript](lectures/sampling/sampling.ps.gz), [pdf](lectures/sampling/sampling.pdf)
      * Exercises: [html](exercises/exercises.html#Sampling)

####  RENDERING WEEK

    * **Mon 9/25: Image Warping**
      * Topics: warping
      * Readings: H &B 3.1-3.4, 3.11, 6
      * More Readings: [Smith95b]``A Pixel is Not a Little Square ...,'' [pdf](papers/smith95b.pdf)
      * Slides: [html](lectures/warp/index.htm), [postscript](lectures/warp/warp.ps.gz), [pdf](lectures/warp/warp.pdf)
      * Exercises: [html](exercises/exercises.html#Warp)
    * **Wed 9/27: Image Composition and Metamorphosis**
      * Topics: image composition and morphing
      * Readings: [Porter84] ``Compositing Digital Images''
      * More Readings: [Smith95a] ``Image Compositing Fundamentals,'' [pdf](papers/smith95a.pdf)
      * More Readings: [Beier92] ``Feature-based Image Metamorphosis,'' [pdf](papers/beier92.pdf)
      * Slides: [html](lectures/composite/index.htm), [postscript](lectures/composite/composite.ps.gz), [pdf](lectures/composite/composite.pdf)
      * Movies: Class of `98 morph ([sgi movie](http://www.cs.princeton.edu/courses/archive/fall98/cs426/assignments/morph/class.movie)), Robert Osada's fish morph ([quicktime](http://www.cs.princeton.edu/courses/archive/fall00/cs426/assignments/assn1/images/warp.mov), [avi](http://www.cs.princeton.edu/courses/archive/fall00/cs426/assignments/assn1/images/warp.avi))
      * Exercises: [html](exercises/exercises.html#Composite)
    * **Fri 9/29: 3D Rendering Overview**
      * Topics: 3D primitives, camera models, basic ideas
      * Readings: H &B 9, 10.1
      * Slides: [html](lectures/render/index.htm), [postscript](lectures/render/render.ps.gz), [pdf](lectures/render/render.pdf)
      * Due: Image processing assignment ([results](assignments/assn1/results/sld001.htm), [movies](assignments/assn1/results/movies))
      * Exercises: [html](exercises/exercises.html#3D Primitives)

####  RAY TRACING WEEK

    * **Mon 10/2: Ray Casting**
      * Topics: ray construction, ray-primitive intersections
      * Readings: H &B 14.6
      * Slides: [html](lectures/raycast/index.htm), [postscript](lectures/raycast/raycast.ps.gz), [pdf](lectures/raycast/raycast.pdf)
      * Exercises: [html](exercises/exercises.html#Ray Tracing)
    * **Wed 10/4: Accelerated Ray Casting**
      * Topics: bounding volumes, spatial data structures
      * Readings: H &B 7.3-7.4
      * Slides: [html](lectures/raycast2/index.htm), [postscript](lectures/raycast2/raycast2.ps.gz), [pdf](lectures/raycast2/raycast2.pdf)
    * **Fri 10/6: Illumination**
      * Topics: reflectance models, light models, shadows, refraction, illumination equations
      * Readings: H &B 14.1-14.2
      * Slides: [html](lectures/light/index.htm), [postscript](lectures/light/light.ps.gz), [pdf](lectures/light/light.pdf)
      * Exercises: [html](exercises/exercises.html#Direct Illumination)

####  TRANSFORMATIONS WEEK

    * **Mon 10/9: Modeling Transformations**
      * Topics: modeling transformations, hierarchical models
      * Readings: H &B 5.1-5.6, 7.4, 11.1-11.5, 11.7
      * Slides: [html](lectures/transform/index.htm), [postscript](lectures/transform/transform.ps.gz), [pdf](lectures/transform/transform.pdf)
      * Exercises: [html](exercises/exercises.html#Modeling Transformations)
    * **Wed 10/11: Viewing Transformations**
      * Topics: pipeline, coordinate systems, viewing transformations
      * Readings: H &B 9, 12.1-12.6
      * Slides: [html](lectures/pipeline/index.htm), [postscript](lectures/pipeline/pipeline.ps.gz), [pdf](lectures/pipeline/pipeline.pdf)
      * Exercises: [html](exercises/exercises.html#Viewing Transformations)
    * **Fri 10/13: Clipping**
      * Topics: viewports, clipping
      * Readings: H &B 6
      * Slides: [html](lectures/clip/index.htm), [postscript](lectures/clip/clip.ps.gz), [pdf](lectures/clip/clip.pdf)
      * Due: Ray tracing assignment

####  POLYGON RENDERING WEEK

    * **Mon 10/16: Scan Conversion**
      * Topics: scan conversion, shading
      * Readings: H &B 3.1-3.4, 3.11, 14.2, 14.5
      * Slides: [html](lectures/scan/index.htm), [postscript](lectures/scan/scan.ps.gz), [pdf](lectures/scan/scan.pdf)
    * **Wed 10/18: Textures**
      * Topics: mipmaps, bump maps, environment maps
      * Readings: H &B 14.9
      * More Reading: [Heckbert86] ``Survey of Texture Mapping,'' [ps](papers/heckbert86.ps.gz), [pdf](papers/heckbert86.pdf)
      * Slides: [html](lectures/texture/index.htm), [postscript](lectures/texture/texture.ps.gz), [pdf](lectures/texture/texture.pdf)
      * Exercises: [html](exercises/exercises.html#Textures)
    * **Fri 10/20: Hidden Surface Removal**
      * Topics: z-buffer, scan conversion, depth ordering
      * Readings: H &B 13
      * Slides: [postscript](lectures/hsr/hsr.ps.gz), [pdf](lectures/hsr/hsr.pdf)
      * Exercises: [html](exercises/exercises.html#Hidden Surface Removal)

####  GLOBAL ILLUMINATION WEEK

    * **Mon 10/23: Rendering Equation**
      * Topics: transport equations, approximation methods
      * Slides: [postscript](lectures/rendeq/rendeq.ps.gz), [pdf](lectures/rendeq/rendeq.pdf)
    * **Wed 10/25: Radiosity**
      * Topics: form factor computations, matrix solution methods, adaptive meshing
      * Readings: H &B 14.7
      * Slides: [postscript](lectures/radiosity/radiosity.ps.gz), [pdf](lectures/radiosity/radiosity.pdf)
      * Exercises: [html](exercises/exercises.html#Radiosity)
    * **Fri 10/27: Modeling**
      * Topics: overview, taxonomy
      * Readings: H &B 10.1,
      * Slides: [html](lectures/reps/index.htm), [postscript](lectures/reps/reps.ps.gz), [pdf](lectures/reps/reps.pdf)
      * Due: OpenGL rendering assignment

####  FALL BREAK WEEK

####  CURVED SURFACES WEEK

    * **Mon 11/6: Subdivision surfaces**
      * Topics: subdivision, mesh data structures
      * Readings: [Zoran 00] "Course Notes: Subdivision for Modeling and Animation," Chapter 1, [pdf](http://www.cs.princeton.edu/courses/archive/fall00/cs426/assignments/assn4/papers/sig2000_course23.pdf)
      * Slides: [html](lectures/subdivision/index.htm), [postscript](lectures/subdivision/subdivision.ps.gz), [pdf](lectures/subdivision/subdivision.pdf)
      * Exercises: [html](exercises/exercises.html#Meshes)
    * **Wed 11/8: Piecewise Polynomial Parametric Curves**
      * Topics: Blending functions, continuity
      * Readings: H &B 3.7, 10.2-10.8
      * Slides: [postscrip](lectures/curves/curves.ps.gz)t, [pdf](lectures/curves/curves.pdf)
    * **Fri 11/10: Spline Curves**
      * Topics: Bezier, Catmull-Rom, B-Splines
      * Readings: H &B 10.9, 10.12-10.13
      * Slides: [postscript](lectures/splines/splines.ps.gz), [pdf](lectures/splines/splines.pdf)
      * Exercises: [html](exercises/exercises.html#Curves)

####  SOLIDS WEEK

    * **Mon 11/13: Spline Surfaces**
      * Topics: tensor product spline surfaces, patches
      * Readings: 10.2-10.9, 10.12-10.13
      * Slides: [html](lectures/surfaces/index.htm), [postscript](lectures/surfaces/surfaces.ps.gz), [pdf](lectures/surfaces/surfaces.pdf)
      * Exercises: [html](exercises/exercises.html#Surfaces)
    * **Wed 11/15: Solids**
      * Topics: voxels, constructive solid geometry, bsps
      * Readings: H &B 10.15-10.17, 10.22
      * Slides: [html](lectures/solid/index.htm), [postscript](lectures/solid/solid.ps.gz), [pdf](lectures/solid/solid.pdf)
      * Exercises: [html](exercises/exercises.html#Solids)
    * **Fri 11/17: Model Construction**
      * Topics: interactive tools, sensors, computer vision, procedural methods
      * Readings: H &B 10.18-10.19
      * Slides: [html](lectures/procedural/index.htm), [postscript](lectures/procedural/procedural.ps.gz), [pdf](lectures/procedural/procedural.pdf)
      * Due: Modeling assignment

####  THANKSGIVING WEEK

    * **Mon 11/20: Midterm review**
      * Topics: question and answer session
      * Slides: html, postscript, pdf
    * **Tues 11/21: Midterm, 7-9PM, CS105**
      * Topics: everything
    * **Wed 11/22: Reserved**
      * Topics: recover from midterm
    * **Fri 11/24: Thanksgiving Break**

####  ANIMATION WEEK

    * **Mon 11/27:   Keyframe Animation**
      * Topics: animation overview, keyframing, articulated figures.
      * Readings: H&B 16.1-16.2, 16.4-16.5
      * Slides: [html](lectures/animation/index.htm), [postscript](lectures/animation/animation.ps.gz), [pdf](lectures/animation/animation.pdf)
      * More Readings: Lasseter87
    * **Wed 11/29: Kinematics & Dynamics**
      * Topics: physical simulations
      * Readings: H&B 10.20-10.21, 16.6
      * Slides: [html](lectures/kinematics/index.htm), [postscript](lectures/kinematics/kinematics.ps.gz), [pdf](lectures/kinematics/kinematics.pdf)
    * **Fri 12/1: Special Guest Lecture**
      * Speaker: Adam Finkelstein
      * Topic: cel animation

####  SPECIAL TOPICS WEEK

    * **Mon 12/4: Project Topics**
      * Topic: suggest course project topics
      * Info: [html](projects/projects.html)
    * **Wed 12/6: Special Guest Lecture**
      * Speaker: Lee Markosian
      * Topic: nonphotorealistic rendering
      * Slides: [html](lectures/npr/index.htm), [postscript](lectures/npr/npr.ps.gz), [pdf](lectures/npr/npr.pdf)
    * **Fri 12/8: Case Study**
      * Topic: Acoustic modeling
      * Slides: [html](lectures/acoustics/index.htm), [postscript](lectures/acoustics/acoustics.ps.gz), [pdf](lectures/acoustics/acoustics.pdf)
      * Due: Animation assignment

####  PROJECT WEEK

    * **Mon 12/11: Project Discussion**
      * Topic: discuss course projects with mentor
      * Due: Project proposal
    * **Wed 12/13: Project Presentations**
      * Topic: students will present course project ideas to class
    * **Fri 12/15: Course Review**
      * Topic: review

* * *

###  Links

  * **Graphics Software Documentation**
    * [OpenGL Information](http://www.opengl.org/)
    * [OpenGL Information from SGI](http://reality.sgi.com/opengl/)
    * [OpenGL Specification and Manual Pages](http://www.sgi.com/software/opengl/manual.html)
    * [GLUT Information](http://www.sgi.com/software/opengl/glut.html)
    * [GLUT Specification](http://reality.sgi.com/mjk/spec3/spec3.html)
    * [GLUT Sample Programs](http://trant.sgi.com/opengl/toolkits/glut-3.5/progs/progs.html)
    * [VRML Information](http://www.web3d.org/vrml/vrml.htm)
    * [VRML Specification](http://www.web3d.org/VRML2.0/FINAL/)

  * **Graphics Instructional Notes and Applets**
    * [Brown's exploratories project](http://www.cs.brown.edu/research/graphics/research/exploratory/)
    * [UC Davis' computer graphics notes on-line](http://graphics.cs.ucdavis.edu/on-line-notes/Notes.html)
    * [Image processing learning resources](http://www.dai.ed.ac.uk/HIPR2/)

  * **Graphics Information Repositories**
    * [Steve Hollasch's links](http://www.research.microsoft.com/~hollasch/cgindex/)
    * [Peter Shirley's list of graphics sites](http://www.graphics.cornell.edu/~shirley/graphics.html)
    * [Paul Heckbert's links](http://www.cs.cmu.edu/~ph/misc.html)
    * [Frank Crow's links](http://web.nvnv.org/~crow/Graphics_info.html)
    * [Fredo Durand's links](http://graphics.lcs.mit.edu/~fredo/Book/index.html)
    * [Dortmund's links](http://www.cs.utah.edu/vissim/resources/sites.html)
    * [George Washington University's links](http://www.seas.gwu.edu/~graphics/reference.html)
    * [Technomagi's links](http://www.technomagi.com/links/graphics.html)
    * [Magic Software's links](http://www.magic-software.com/)
    * [Karim Ratib's links](http://www2.iro.umontreal.ca/~ratib/code/)
    * [Yahoo - Computer Graphics](http://www.yahoo.com/Computers/Graphics/)
    * [3dsite](http://www.3dsite.com/3dsite/)

  * **Graphics Research Labs**
    * [Princeton's Computer Graphics & Geometry Group](http://www.cs.princeton.edu/gfx)
    * [Other graphics research labs](http://mambo.ucsc.edu/psl/cg.html)

  * **Graphics Bibliographies**
    * [Siggraph Bibliography](http://www.siggraph.org/publications/bibliography/)
    * [www.graphicspapers.com](http://www.graphicspapers.com)
    * [Bibliographies on Computer Graphics and Vision](http://liinwww.ira.uka.de/bibliography/Graphics/index.html)
    * [Ray Tracing Bibliography](http://www.acm.org/tog/resources/bib/)
    * [Radiosity Bibliography](http://www.ledalite.com/library-/rrt.htm)
    * [Eurographics digital library](http://www.eg.org/EG/DL)
    * [ACM Conference Proceedings on Computer Graphics](http://www.acm.org/pubs/contents/proceedings/graph/)

  * **Graphics Courses at Other Universities:**
    * Stanford University ([CS248](http://www.graphics.stanford.edu/courses/#cs248), [CS348A](http://www.graphics.stanford.edu/courses/#cs348a), [CS348B](http://www.graphics.stanford.edu/courses/#cs348b))
    * University of California at Berkeley ([CS184](http://www-inst.eecs.berkeley.edu/~cs184/), [CS284](http://www.cs.berkeley.edu/~sequin/CS284/), [CS285](http://www.cs.berkeley.edu/~sequin/CS285/cs285.html))
    * Massachusetts Institute of Technology ([6.837](http://graphics.lcs.mit.edu/classes/6.837/F98/))
    * University of Washington ([CS557](http://www.cs.washington.edu/education/courses/457/), [CS558](http://www.cs.washington.edu/education/courses/558/CurrentQtr/))
    * University of North Carolina at Chapel Hill ([COMP205](http://www.cs.unc.edu/Admin/Courses/descriptions/205.html), [COMP235](http://www.cs.unc.edu/Admin/Courses/descriptions/235.html),[COMP236](http://www.cs.unc.edu/~dm/UNC/COMP236/comp236.html))
    * California Institute of Technology ([CS/CNS174,](http://www.gg.caltech.edu/~cs174ta/cs174.shtml)[CS/CNS257](http://www.gg.caltech.edu/~cs257ta/cs257.shtml), [CS/CNS274](http://www.cs.caltech.edu/~ps/3DP), [CS/CNS284](http://www.cs.caltech.edu/~arvo/courses/TGM/description.html))
    * Cornell University ([CS417](http://simon.cs.cornell.edu/Info/Courses/Spring-99/CS417/), [CS418](http://www.tc.cornell.edu/Visualization/Education/cs418/))
    * Carnegie Mellon University ([15-462](http://www.cs.cmu.edu/afs/cs/academic/class/15462/web/462.html), [15-463](http://www.cs.cmu.edu/afs/andrew/scs/cs/15-463/pub/www/463.html))
    * Brown University ([CS123](http://www.cs.brown.edu/courses/cs123/))
    * University of Illinois ([CS318](http://www.cs.uiuc.edu/education/courses/descriptions/318.html), [CS319](http://www.cs.uiuc.edu/education/courses/descriptions/319.html))
    * University of Waterloo ([CS488/688](http://www.undergrad.math.uwaterloo.ca/~cs488/), [CS489/689](http://math.uwaterloo.ca/CS_Dept/grad.html))
    * University of Wisconsin ([CS-638](http://www.cs.wisc.edu/graphics/Courses/cs-638-1999/))

* * *

###  References

  * [Beier92]   T. Beier and S. Neely,
  
``[Feature-based Image Metamorphosis](papers/beier92.pdf),''  
_Computer Graphics_ (SIGGRAPH 92), 26, 2, 1992, 35-42.

  * [Hanrahan95], Pat Hanrahan,
  
``[Basic Signal Processing](papers/hanrahan95.pdf),''  
Chapter 9, Course Notes for CS426, 1995.

  * [Heckbert86]  Paul Heckbert,
  
``[Survey of Texture Mapping,](papers/heckbert86.pdf)''  
_IEEE Computer Graphics & Applications_, 6, 11, November, 1986, 56-67.

  * [Smith95a]  Alvy Ray Smith,
  
``[Image Compositing Fundamentals,](papers/smith95a.pdf)''  
Technical Memo 4, Microsoft Research, Aug 15, 1995.

  * [Smith95b]  Alvy Ray Smith,
  
``[A Pixel Is Not A Little Square ...](papers/smith95b.pdf)''  
Technical Memo 6, Microsoft Research, July 17, 1995.

  * [Smith95c]  Alvy Ray Smith,
  
``[Alpha and the History of Digital Compositing](papers/smith95c.pdf),"  
Technical Memo 7, Microsoft Research, August 157, 1995.

  * [Smith95d]  Alvy Ray Smith,
  
``[Gamma Correction,](papers/smith95d.pdf)"  
Technical Memo 7, Microsoft Research, Sept 1, 1995.

