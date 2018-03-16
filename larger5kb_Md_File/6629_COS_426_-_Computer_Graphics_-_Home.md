![cos426.jpg \(39279 bytes\)](cos426.jpg)

###  Computer Graphics, Fall 99

###  [Thomas Funkhouser](http://www.cs.princeton.edu/~funk)

[Department of Computer Science](http://www.cs.princeton.edu)  
[Princeton University](http://www.princeton.edu)  

* * *

  
General Information | Announcements | Textbooks | Coursework  
Syllabus | Exercises | Notes | Links |
[Students](http://www.cs.princeton.edu/courses/archive/fall99/cs426/students/index.html)
|
[Assignments](http://www.cs.princeton.edu/courses/archive/fall99/cs426/assignments.htm)

* * *

###  General Information

  * **Professor**
    * [Thomas Funkhouser](http://www.cs.princeton.edu/~funk/) (office hours: MW 11AM-Noon), CS 422, [funk@cs.princeton.edu](mailto:funk@cs.princeton.edu)

  * **Teaching Assistants**
    * [Wagner Toledo Correa](http://www.cs.princeton.edu/~wtcorrea) (office hours: T 1-2PM), CS 414, [wtcorrea@cs.princeton.edu](mailto:wtcorrea@cs.princeton.edu)
    * [Rob Kalnins](http://www.cs.princeton.edu/~rkalnins) (office hours: Th 4-5PM), CS 314, [rkalnins@cs.princeton.edu](mailto:rkalnins@cs.princeton.edu)

  * **Lab Assistants**
    * [Wilmot Li](http://www.cs.princeton.edu/~wilmotli) (lab hours: Fri 7-11PM), [wilmotli@cs.princeton.edu](mailto:wilmotli@cs.princeton.edu)
    * [Brian Fujito](http://www.cs.princeton.edu/~btfujito) (lab hours: Sat 2-6PM), [btfujito@cs.princeton.edu](mailto:btfujito@cs.princeton.edu)
    * [Addy Ngan](http://www.cs.princeton.edu/~waingan) (lab hours: Sun 2-6PM), [waingan@cs.princeton.edu](mailto:waingan@cs.princeton.edu)

  * **Times and Places**
    * Lectures: MWF 10AM, CS 105.
    * Precepts: W 8PM, CS 103 and F 2:30PM, CS 103

  * **Prerequisites**
    * Data structures and algorithms (CS 226)
    * A good working knowledge of C programming (CS 217)
    * Linear algebra (as described in Appendix A of the course book)
    * No prior knowledge of graphics is assumed

  * **Keeping in touch**
    * [Send mail](mailto:cs426@princeton.edu) to the CS426 staff
    * Check out the [pu.cs.426](news://news.princeton.edu/pu.cs.426) newsgroup

* * *

###  Announcements

  * **January 20 at 2PM in MECA**
    * [Final project demo day!](projects/final.html)
  * **Final Project Links**
    * [Rendering Caustics](http://www.princeton.edu/~jimpercy/cos426/6/index.html)
    * [Radiosity](http://www.princeton.edu/~dfussell/cos426/project/)
    * [More Realistic Keyframe Animation](http://lennon.princeton.edu/cs426)
    * [Project P-Funk](http://www.princeton.edu/~mikeredd/cos426/FinalWriteup.html)
    * [Modeling Natural Phenomena](http://www.princeton.edu/~kmulcahy/cos426/final/final.html)
    * [The Red Rover Experience](http://www.princeton.edu/~anoopg/cos426/final/finalreport.html)
    * [Cool Diving Experience](http://www.cs.princeton.edu/~mzhang/final/final.html)
    * [Morphing and Animation of Chess Pieces](http://www.cs.princeton.edu/~neilshah/cs426/final/index.html)
  * **Grading distributions**
    * [Assignments](chart1.pdf)
    * [Midterm](chart.pdf)

* * *

###  Textbooks

  * **Required Textbook**
    * _Computer Graphics, C Version_ ,
  
Donald Hearn, M. Pauline Baker,  
2nd Edition, Prentice Hall, 1997, ISBN: 0135309247.

  * **Recommended Textbooks**
    * _OpenGL Programming Guide: The Official Guide to Learning OpenGL_ , **Version 1.1**
  
Jackie Neider, Tom Davis, Mason Woo,  
2nd Edition, Addison-Wesley, 1997, ISBN: 0201461382.

    * _Computer Graphics: Principles and Practice_ ,
  
James D. Foley, Andries van Dam, Steven K. Feiner, John F. Hughes,  
2nd Edition in C, Addison-Wesley, 1995, ISBN: 0201848406.

* * *

###  Coursework

  * **"Midterm" Exam** (25%)
    * 7-9PM on Friday, December 10 in CS 105
    * Bring a one-page "cheat sheet" with writing on both sides
    * Closed book


  * **Programming Assignments** (10% each)
    * [Assignment #1](http://www.cs.princeton.edu/courses/archive/fall99/cs426/assignment1/assignment1.htm): Image Processing (check out some [results](http://www.cs.princeton.edu/courses/archive/fall99/cs426/assignment1/submissions/submissions.htm)!)
    * [Assignment #2](http://www.cs.princeton.edu/courses/archive/fall99/cs426/assignment2/assignment2.htm): OpenGL Rendering (check out some [results](http://www.cs.princeton.edu/courses/archive/fall99/cs426/assignment2/results/results.htm)!)
    * [Assignment #3](http://www.cs.princeton.edu/courses/archive/fall99/cs426/assignment3/assignment3.htm): Ray Tracing (check out some [results](http://www.cs.princeton.edu/courses/archive/fall99/cs426/assignment3/results/results.htm)!)
    * [Assignment #4:](assignment4/assignment4.htm) Procedural Modeling  (check out some [results](http://www.cs.princeton.edu/courses/archive/fall99/cs426/assignment4/submissions/submissions.htm)!)
    * [Assignment #5](assignment5/assignment5.htm): Keyframe Animation  (check out some [results](http://www.cs.princeton.edu/courses/archive/fall99/cs426/assignment5/results/results.htm)!)


  * **Final Project** (20%)
    * [Written proposal](projects/final.html) (due 12/13)
    * [Presentation of proposal](projects/final.html) (in class on 12/51 & 12/17)
    * [Written final report](projects/final.html) (due 1/11/00)
    * [Demo day](projects/final.html) (at 2PM on 1/20/00)

  * **Class Participation** (5%)
    * Contribute ideas in class

* * *

###  Syllabus

####  INTRODUCTION WEEK

    * **Fri 9/17: Introduction**
      * Topics: overview, applications
      * Readings: H &B 1, 4.3, appendix A
      * Slides: [html](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/intro/index.htm), [postscript](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/intro/intro.ps.gz), [pdf](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/intro/intro.pdf.gz)

####  IMAGE PROCESSING WEEK

    * **Mon 9/20: Raster Graphics**
      * Topics: devices, color, perception
      * Readings: H &B 2.1-2.2, 15.1-15.4
      * Slides: [html](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/raster/index.htm), [postscript](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/raster/raster.ps.gz), [pdf](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/raster/raster.pdf.gz)
    * **Wed 9/22: Image Quantization**
      * Topics: quantization, halftoning, dithering
      * Readings: H &B 14.4
      * Slides: [html](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/dither/index.htm), [postscript](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/dither/dither.ps.gz), [pdf](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/dither/dither.pdf.gz)
    * **Fri 9/24: Image Sampling and Reconstruction**
      * Topics: sampling, reconstruction, filtering
      * Readings: H &B 4.8
      * Slides: [html](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/sampling/index.htm), [postscript](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/sampling/sampling.ps.gz), [pdf](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/sampling/sampling.pdf.gz)

####  2D RENDERING WEEK

    * **Mon 9/27: Image Warping and Composition**
      * Topics: warping, composition
      * Readings: H &B 3.1-3.4, 3.11, 6
      * Slides: [html](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/warp/index.htm), [postscript](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/warp/warp.ps.gz), [pdf](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/warp/warp.pdf.gz)
    * **Wed 9/29: 2D Scan Conversion**
      * Topics: 2D primitives, scan conversion, antialiasing
      * Readings: H &B 3.1-3.4, 3.11, 6
      * Slides: [html](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/scan/index.htm), [postscript](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/scan/scan.ps.gz), [pdf](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/scan/scan.pdf.gz)
    * **Fri 10/1: 2D Rendering Pipeline**
      * Topics: clipping, window-to-viewport mappings, coordinate systems
      * Readings: H &B 5.1-5.6
      * Slides: [html](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/pipeline/index.htm), [postscript](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/pipeline/pipeline.ps.gz), [pdf](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/pipeline/pipeline.pdf.gz)

####  3D RENDERING WEEK

    * **Mon 10/4: 3D Rendering Pipeline**
      * Topics: 3D primitives, modeling transformations
      * Readings: H &B 9, 10.1, 11.1-11.5, 11.7
      * Slides: [html](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/transform/index.htm), [postscript](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/transform/transform.ps.gz), [pdf](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/transform/transform.pdf.gz)
    * **Wed 10/6: Viewing Transformations**
      * Topics: camera transformations, projections
      * Readings: H &B 12.1-12.6
      * Slides: [html](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/view/index.htm), [postscript](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/view/view.ps.gz), [pdf](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/view/view.pdf.gz)
    * **Fri 10/8: Lighting and Reflectance**
      * Topics: reflectance models, light models, Phong illumination equations
      * Readings: H &B 14.1-14.2
      * Slides: [html](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/light/index.htm), [postscript](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/light/light.ps.gz), [pdf](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/light/light.pdf.gz)

####  DIRECT ILLUMINATION WEEK

    * **Mon 10/11: Illumination and Shading**
      * Topics: Ray casting, flat shading, Gouraud, Phong
      * Readings: H &B 14.2, 14.5
      * Slides: [html](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/shade/index.htm), [postscript](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/shade/shade.ps.gz), [pdf](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/shade/shade.pdf.gz)
    * **Wed 10/13: Textures**
      * Topics: mipmaps, bump maps, environment maps
      * Readings: H &B 14.9
      * Slides: [postscript](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/texture/texture.ps.gz), [pdf](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/texture/texture.pdf.gz)
      * More Slides: [postscript](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/texture/rendering.ps.gz), [pdf](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/texture/rendering.pdf.gz)
    * **Fri 10/15: Hidden Surface Removal**
      * Topics: z-buffer, scan conversion, depth ordering
      * Readings: H &B 13
      * Slides: [postscript](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/hsr/hsr.ps.gz), [pdf](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/hsr/hsr.pdf.gz)

####  GLOBAL ILLUMINATION WEEK

    * **Mon 10/18: Ray Tracing**
      * Topics: ray tracing
      * Readings: H &B 14.6
      * Slides: [postscript](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/raytrace/raytrace1.ps.gz), [pdf](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/raytrace/raytrace1.pdf.gz)
    * **Wed 10/20: More Ray Tracing**
      * Topics: sampling, accelerations, hierarchical models
      * Readings: H &B 7.3-7.4
      * Slides: [postscript](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/raytrace/raytrace2.ps.gz), [pdf](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/raytrace/raytrace2.pdf.gz)
    * **Fri 10/22: Rendering Equation**
      * Topics: transport equations, approximation methods
      * Slides: [postscript](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/global/global.ps.gz), [pdf](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/global/global.pdf.gz)

####  MODELING WEEK

    * **Mon 10/25: Radiosity**
      * Topics: form factor computations, matrix solution methods, adaptive meshing
      * Readings: H &B 14.7
      * Slides: [postscript](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/radiosity/radiosity.ps.gz), [pdf](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/radiosity/radiosity.pdf.gz)
    * **Wed 10/27: Object Representations**
      * Topics: mesh representations
      * Readings: H &B 10.1
      * Slides: [postscript](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/mesh/mesh.ps.gz), [pdf](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/mesh/mesh.pdf.gz)
    * **Fri 10/29: Polygonal meshes**
      * Topics: mesh generation, mesh acquisition, sweeps
      * Readings: H &B 10.14
      * Slides: [postscript](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/sweep/sweep1.ps.gz), [pdf](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/sweep/sweep1.pdf.gz)
      * More Slides: [postscript](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/sweep/sweep2.ps.gz), [pdf](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/sweep/sweep2.pdf.gz)

####  FALL BREAK WEEK

####  CURVES WEEK

    * **Mon 11/8: Procedural Models**
      * Topics: sweeps, fractals, grammars
      * Readings: H &B 10.18-10.19
      * Slides: [html](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/procedural/index.htm), [postscript](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/procedural/procedural.ps.gz), [pdf](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/procedural/procedural.pdf.gz)
    * **Wed 11/10: Piecewise Polynomial Parametric Curves**
      * Topics: Blending functions, continuity
      * Readings: H &B 3.7, 10.2-10.8
      * Slides: [postscript](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/curves/curves1.ps.gz),[pdf](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/curves/curves1.pdf.gz)
    * **Fri 11/12: Spline Curves**
      * Topics: Bezier, Catmull-Rom, B-Splines
      * Readings: H &B 10.9, 10.12-10.13
      * Slides: [postscript](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/curves/curves2.ps.gz),[pdf](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/curves/curves2.pdf.gz)

####  SURFACES AND SOLIDS WEEK

    * **Mon 11/15: Surfaces**
      * Topics: tensor product spline surfaces, subdivision surfaces
      * Readings: 10.2-10.9, 10.12-10.13
      * Slides: [html](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/surfaces/index.htm), [postscript](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/surfaces/surfaces.ps.gz), [pdf](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/surfaces/surfaces.pdf.gz)
    * **Wed 11/17: Solids**
      * Topics: voxels, constructive solid geometry, bsps
      * Readings: H &B 10.15-10.17, 10.22
      * Slides: [html](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/solid/index.htm), [postscript](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/solid/solid.ps.gz), [pdf](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/solid/solid.pdf.gz)
    * **Fri 11/19: Representations of Geometry Review**
      * Topics: overview, taxonomy
      * Readings: H &B "Computational Representations of Geometry," Bruce Naylor, 1996.
      * Slides: [postscript](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/reps/reps.ps.gz), [pdf](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/reps/reps.pdf.gz)
      * More Slides: [html](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/reps/index.htm), [postscript](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/reps/naylor.ps.gz), [pdf](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/reps/naylor.pdf.gz)

####  THANKSGIVING WEEK

    * **Mon 11/22:   Animation**
      * Topics: overview, keyframing, articulated figures.
      * Readings: H&B 16.1-16.2, 16.4-16.5.
      * More Readings: Lasseter, "Principles of Traditional Animation Applied to 3D Computer Animation," SIGGRAPH 87.
      * Slides: [html](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/animation/index.htm), [postscript](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/animation/animation.ps.gz), [pdf](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/animation/animation.pdf.gz)
    * **Wed 11/24: Reserved**
      * Topics: animation examples.
    * **Fri 11/26: Thanksgiving Break**

####  ANIMATION WEEK

    * **Mon 11/29: Kinematics & Dynamics**
      * Topics: physical simulations
      * Readings: H&B 10.20-10.21, 16.6
      * Slides: [html](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/kinematics/index.htm), [postscript](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/kinematics/kinematics.ps.gz), [pdf](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/kinematics/kinematics.pdf.gz)
    * **Wed 12/1: Metamorphosis**
      * Topics: image morphs, 3D morphs
      * Readings: Beier  & Neely, "Feature-Based Image Metamorphosis," SIGGRAPH 92.
      * Slides: [postscript](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/morph/morph.ps.gz), [pdf](http://www.cs.princeton.edu/courses/archive/fall99/cs426/lectures/morph/morph.pdf.gz)
    * **Fri 12/3: Project Topics**
      * Topics: discuss final projects

####  MIDTERM WEEK

    * **Mon 12/6: Midterm Review**
      * Topics: review for midterm
    * **Wed 12/8: Midterm Review**
      * Topics: review for midterm
    * **Fri 12/10:   TA Midterm Review**
      * Topics: review for midterm with TAs
      * Readings: exercise questions
**Fri 12/10, 7-9PM: MIDTERM**

####  PROJECT WEEK

    * **Mon 12/13: Project Review**
    * **Wed 12/15: Project Presentations**
    * **Fri 12/17: Project Presentations**

* * *

###  Exercises

> * **[Color models](exercises/color.htm)**

> * **[Image processing](exercises/image.htm)**

> * **[2D primitives and transformations](exercises/2Drender.htm)**

> * **[3D primitives and transformations](exercises/3Drender.htm)**

> * **[Viewing transformations](exercises/viewing.htm)**

> * **[Lighting, reflectance,& shading](exercises/lighting.htm)**

> * **[Texture mapping](exercises/texture.htm)**

> * **[Hidden surface removal](exercises/hsr.htm)**

> * **[Ray tracing](exercises/raytrace.htm)**

> * **[Radiosity](exercises/radiosity.htm)**

> * **[Polygonal meshes](exercises/meshes.htm)**

> * **[Curves](exercises/curves.htm)**

> * **[Surfaces](exercises/surfaces.htm)**

> * **[Solids](exercises/solids.htm)**

> * **[Animation](exercises/animation.htm)**

* * *

###  Notes, Papers, and Applets

  * **Color and Perception**
    * [Brown University applets](http://www.cs.brown.edu/research/graphics/research/exploratory/appletindex.html)
    * [Color Picker Article](http://home.netscape.com/computing/webbuilding/studio/feature19981111-5.html) (written by Mike Bostock)

  * **Image Processing**
    * [Brown University applets](http://www.cs.brown.edu/research/graphics/research/exploratory/appletindex.html)
    * [Alvy Ray Smith on "Image Compositing Fundamentals"](ftp://ftp.research.microsoft.com/Users/alvy/PstScrpt/4_comp.ps)
    * [Alvy Ray Smith on "A Pixel is Not a Little Square"](ftp://ftp.research.microsoft.com/Users/alvy/PstScrpt/6_pixel.ps)
    * [Alvy Ray Smith on "Alpha and the History of Digital Compositing"](ftp://ftp.research.microsoft.com/Users/alvy/PstScrpt/7_alpha.ps)
    * [Alvy Ray Smith on "Varities of Digital Painting"](ftp://ftp.research.microsoft.com/Users/alvy/PstScrpt/8_paint.ps)
    * [Alvy Ray Smith on "Gamma Correction"](ftp://ftp.research.microsoft.com/Users/alvy/PstScrpt/9_gamma.ps)

  * **Rendering Pipeline**
    * [Patrick Min's applets](http://www.cs.princeton.edu/~min/cs426/applets.html)
    * [Brown University applets](http://www.cs.brown.edu/research/graphics/research/exploratory/appletindex.html)

  * **Ray Tracing**
    * [Ray tracing news](http://www.3dspot.com/rtnews/)
    * [Persistence of vision (POV) ray tracer](http://www.povray.org/)

  * **Implicit Surfaces**
    * [The Implicit Site](http://implicit.eecs.wsu.edu/)

  * **Modeling**
    * [BSP Tree FAQ](http://reality.sgi.com/bspfaq/)

  * **Graphics**
    * [www.vr.edu](http://www.vr.edu)

  * **OpenGL**
    * [Information](http://reality.sgi.com/opengl/)
    * [More Information](http://www.sgi.com/software/opengl/)
    * [Even More Information](http://reality.sgi.com/employees/mjk_asd/opengl-links.html)
    * [Specification and Manual Pages](http://www.sgi.com/software/opengl/manual.html)

  * **GLUT**
    * [Information](http://www.sgi.com/software/opengl/glut.html)
    * [Specification](http://reality.sgi.com/mjk/spec3/spec3.html)
    * [Sample Programs](http://trant.sgi.com/opengl/toolkits/glut-3.5/progs/progs.html)

  * **VRML**
    * [Information](http://www.web3d.org/vrml/vrml.htm)
    * [Specification](http://www.web3d.org/VRML2.0/FINAL/)

* * *

###  Links

  * **Similar Courses at Other Universities:**
    * Stanford University ([CS248](http://www.graphics.stanford.edu/courses/#cs248), [CS348A](http://www.graphics.stanford.edu/courses/#cs348a), [CS348B](http://www.graphics.stanford.edu/courses/#cs348b))
    * University of California at Berkeley ([CS184](http://www-inst.eecs.berkeley.edu/~cs184/), [CS284](http://www.cs.berkeley.edu/~sequin/CS284/), [CS285](http://www.cs.berkeley.edu/~sequin/CS285/cs285.html))
    * Massachusetts Institute of Technology ([6.837](http://graphics.lcs.mit.edu/classes/6.837/F98/))
    * University of Washington ([CS557](http://www.cs.washington.edu/education/courses/457/), [CS558](http://www.cs.washington.edu/education/courses/558/CurrentQtr/))
    * University of North Carolina at Chapel Hill ([COMP205](http://www.cs.unc.edu/Admin/Courses/descriptions/205.html), [COMP235](http://www.cs.unc.edu/Admin/Courses/descriptions/235.html), [COMP236](http://www.cs.unc.edu/~dm/UNC/COMP236/comp236.html))
    * California Institute of Technology ([CS/CNS174,](http://www.gg.caltech.edu/~cs174ta/cs174.shtml)[CS/CNS257](http://www.gg.caltech.edu/~cs257ta/cs257.shtml), [CS/CNS274](http://www.cs.caltech.edu/~ps/3DP), [CS/CNS284](http://www.cs.caltech.edu/~arvo/courses/TGM/description.html))
    * Cornell University ([CS417](http://simon.cs.cornell.edu/Info/Courses/Spring-99/CS417/), [CS418](http://www.tc.cornell.edu/Visualization/Education/cs418/))
    * Carnegie Mellon University ([15-462](http://www.cs.cmu.edu/afs/cs/academic/class/15462/web/462.html), [15-463](http://www.cs.cmu.edu/afs/andrew/scs/cs/15-463/pub/www/463.html))
    * Brown University ([CS123](http://www.cs.brown.edu/courses/cs123/))
    * University of Illinois ([CS318](http://www.cs.uiuc.edu/education/courses/descriptions/318.html), [CS319](http://www.cs.uiuc.edu/education/courses/descriptions/319.html))
    * University of Waterloo ([CS488/688](http://www.undergrad.math.uwaterloo.ca/~cs488/), [CS489/689](http://math.uwaterloo.ca/CS_Dept/grad.html))
    * University of Wisconsin ([CS-638](http://www.cs.wisc.edu/graphics/Courses/cs-638-1999/))

  * **Miscellaneous Graphics Links:**
    * [Yahoo! \- Computers and Internet:Graphics](http://www.yahoo.com/Computers_and_Internet/Graphics)
    * [ACM Conference Proceedings on Computer Graphics](http://www.acm.org/pubs/contents/proceedings/graph/)
    * [Peter Shirley's list of graphics sites](http://www.graphics.cornell.edu/~shirley/graphics.html)

