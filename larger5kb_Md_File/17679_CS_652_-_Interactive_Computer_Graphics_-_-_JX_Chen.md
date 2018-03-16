### George Mason University  
DEPARTMENT OF COMPUTER SCIENCE

CS 652 - Interactive Computer Graphics - Summer '2002

**[Actions](http://cs.gmu.edu/~jchen/cs652/cs652-chen.html#NEWS) |
[Assignments](http://cs.gmu.edu/~jchen/cs652/cs652-chen.html#ASSN) |
[Syllabus](http://cs.gmu.edu/~jchen/cs652/cs652-chen.html#SYLL) |
[Lab](http://cs.gmu.edu/~jchen/graphics.html)**  
[Description](http://cs.gmu.edu/~jchen/cs652/cs652-chen.html#DESCR) |
[Grading](http://cs.gmu.edu/~jchen/cs652/cs652-chen.html#GRAD) |
[TA](http://cs.gmu.edu/~jchen/cs652/cs652-chen.html#TA) |
[Groups](http://cs.gmu.edu/~jchen/cs652/cs652-chen.html#GRP) |
[Texts](http://cs.gmu.edu/~jchen/cs652/cs652-chen.html#TEXT) |
[References](http://cs.gmu.edu/~jchen/cs652/cs652-chen.html#REF)  

* * *

     [Professor Jim X. Chen](http://www.cs.gmu.edu/~jchen)      ST2 Room 409       Course office hour by appointment       Phone: (703) 993-1720       Teaching Assistant: Ms. Xiaorong Zhou: xzhou2@gmu.edu       (Prefix the subject with CS652)  

* * *

  
    

* **ACTIONS:**

**Join the _cs652@leibniz.gmu.edu_ mailing group:** email
[cs652-request@leibniz.gmu.edu](mailto:cs652-request@leibniz.gmu.edu) with
subject line read as _subscribe_ ; you may stay in the group or email
_cs652-request@leibniz.gmu.edu_ with subject line read as _unsubscribe_.

  * [Set up your working environment at home](http://www.cs.gmu.edu/~jchen/cs451/notes/setup.html): ([MS PowerPoint file)](http://www.cs.gmu.edu/~jchen/cs451/notes/setup.ppt)
  * **In IT &E Lab**, you can also use Mesa, an OpenGL simulator; copy and test out a sample program from: /opt/mesa/share/book (There is a makefile in the same directory.) If you use GLUT, there are examples under /opt/mesa/share/glut 
  * **[OpenGL 1.1.2 on workstations](http://sun.com/solaris/opengl/): ** Sun OpenGL is available on Sun workstations (room 12). X terminals (rm 133/137) cannot display OpenGL application output (no GLX extension installed).directory.) 
  * Feedback for your better learning: _[jchen @cs.gmu.edu](mailto:jchen@cs.gmu.edu)_

[Back to Top of Page](http://cs.gmu.edu/~jchen/cs652/cs652-chen.html#top)

* * *

**DESCRIPTION:**

CS 652 is a 3-credit course with prerequisite CS 583. It gives an introduction
to graphics principles, advanced graphics methods, OpenGL graphics library,
and programming.

    I am assuming you know the prerequisite material, C programming, vector analysis, and matrix calculations. After this class, you will be able to do graphics modeling and animation of certain objects or behaviors of your preference. 

[Back to Top of Page](http://cs.gmu.edu/~jchen/cs652/cs652-chen.html#top)

* * *

**GRADING POLICY:**

There are all together 100 points:

  * Homework assignments announced in class and due before next class (35 points) 
  * Random in class quizzes (35 points) 
  * A Final Exam (30 points) 

Your overall course score, S, will be the sum of these points.

  *          A: S is at least 90 points 
  *          A-: S is at least 85 (and less than 90) points 
  *          B+: S is at least 80 (and less than 85) points 
  *          B: S is at least 75 (and less than 80) points 
  *          C: S is at least 60 (and less than 75) points 
  *          F: S is less than 60 points 

Plus and minus:

  * From time to time I will offer extra credit questions. Their scores will be added to your score S. It is therefore possible to get total scores above 100 points. 
  * Class participation is also very important. Active participation will be rewarded with extra points toward your score S. 
  * Each assignment/project late may not be accepted. Therefore, you should plan on working early. If you cannot finish your assignment/project, you should turn in your partial work. 
  * If there is an accident or emergency and you let me know, I will consider it accordingly. 

[Back to Top of Page](http://cs.gmu.edu/~jchen/cs652/cs652-chen.html#top)

* * *

**TEACHING ASSISTANT:**

    [Ms. Xiaorong Zhou](http://cs.gmu.edu/department/TA%20Office%20hours.html), xzhou2@gmu.edu 

[Back to Top of Page](http://cs.gmu.edu/~jchen/cs652/cs652-chen.html#top)

* * *

**ASSIGNMENTS: (announced in class and due one day before next class)**

[Back to Top of Page](http://cs.gmu.edu/~jchen/cs652/cs652-chen.html#top)

* * *

**GROUPS AND COLLABORATION:**

    You can form into **study groups** , most of size 3. You can meet and discuss all homework questions freely and frequently in your group. **However, you must do your own homework and write your individual report/program.** You will learn much more working with your group than you would working alone. In short, collaborate freely, acknowledge all help and sources, and do your own individual work. 

[Back to Top of Page](http://cs.gmu.edu/~jchen/cs652/cs652-chen.html#top)

* * *

**SYLLABUS: (tentative)**

1-2. Introduction: applications; fundamental ideas; hardware architectures.

[http://cs.gmu.edu/~jchen/graphics/notes/setup.ppt](http://cs.gmu.edu/%7Ejchen/graphics/notes/setup.ppt)  
[http://cs.gmu.edu/~jchen/graphics/notes/Introduction.pdf  
](http://cs.gmu.edu/%7Ejchen/graphics/notes/Introduction.pdf)[http://cs.gmu.edu/~jchen/graphics/notes/hardware.pdf](http://cs.gmu.edu/%7Ejchen/graphics/notes/hardware.pdf)

    _Chapter 1 & 4 in Foley's text; Chapter 1 in Woo & Neider's text._       

3-4. 2D Graphics Concepts: drawing; filling; clipping, anti-aliasing.

[http://cs.gmu.edu/~jchen/graphics/notes/opengl.pdf](http://cs.gmu.edu/%7Ejchen/graphics/notes/opengl.pdf)  
[http://cs.gmu.edu/~jchen/graphics/notes/raster.pdf](http://cs.gmu.edu/%7Ejchen/graphics/notes/raster.pdf)  
[http://cs.gmu.edu/~jchen/graphics/notes/attributes.pdf](http://cs.gmu.edu/%7Ejchen/graphics/notes/attributes.pdf)
_Chapter 2 & 3 in Foley's text; Chapter 2 in Woo & Neider's text._

  
5-6. Transformation and viewing: rotating; translating; scaling.

[http://cs.gmu.edu/~jchen/graphics/notes/3Dmodels.prn.pdf](http://cs.gmu.edu/%7Ejchen/graphics/notes/3Dmodels.prn.pdf)  
[http://cs.gmu.edu/~jchen/graphics/notes/2Dtransf.pdf](http://cs.gmu.edu/%7Ejchen/graphics/notes/2Dtransf.pdf)  
[http://cs.gmu.edu/~jchen/graphics/notes/3Dtransf.prn.pdf](http://cs.gmu.edu/%7Ejchen/graphics/notes/3Dtransf.prn.pdf)

    _Chapter 5 in Foley's text; Chapter 2-3 in Woo & Neider's text._   


7-8. Viewing & Hierarchy: viewing in 3D; projections; display list.

[http://cs.gmu.edu/~jchen/graphics/notes/viewing.prn.pdf](http://cs.gmu.edu/%7Ejchen/graphics/notes/viewing.prn.pdf)  
[http://cs.gmu.edu/~jchen/graphics/notes/phigsview.prn.pdf](http://cs.gmu.edu/%7Ejchen/graphics/notes/phigsview.prn.pdf)  
[http://cs.gmu.edu/~jchen/graphics/notes/oglview.prn.pdf  
](http://cs.gmu.edu/%7Ejchen/graphics/notes/oglview.prn.pdf)[http://cs.gmu.edu/~jchen/graphics/notes/displaylist.pdf](http://cs.gmu.edu/%7Ejchen/graphics/notes/displaylist.pdf)

    _Chapter 6 in Foley's text; Chapter 3-4 in Neider's text. Chapter 3 &7 in Woo's text. _

  
9-10. Illumination & Shading: diffuse; specular; ambient; flat shading; smooth
shading; Giraud shading; Phong shading.

[http://cs.gmu.edu/~jchen/graphics/notes/lighting.pdf](http://cs.gmu.edu/%7Ejchen/graphics/notes/lighting.pdf)  
[http://cs.gmu.edu/~jchen/graphics/notes/shading.pdf](http://cs.gmu.edu/%7Ejchen/graphics/notes/shading.pdf)  
[http://cs.gmu.edu/~jchen/graphics/notes/gllight.pdf](http://cs.gmu.edu/%7Ejchen/graphics/notes/gllight.pdf)

    _Chapter 16 in Foley's text; Chapter 6 & 7 in Neider's text. Chapter 5 & 6 in Woo's text. _            11-12. Advanced techniques in OpenGL: blending, antialiasing, fog, bitmaps, fonts, images, texture mapping, and the framebuffers. 

[http://cs.gmu.edu/~jchen/graphics/notes/blending.pdf](http://cs.gmu.edu/%7Ejchen/graphics/notes/blending.pdf)  
[http://cs.gmu.edu/~jchen/graphics/notes/image.pdf](http://cs.gmu.edu/%7Ejchen/graphics/notes/image.pdf)  
[http://cs.gmu.edu/~jchen/graphics/notes/texture.pdf](http://cs.gmu.edu/%7Ejchen/graphics/notes/texture.pdf)

_Chapter 7-10 in Neider's text. Chapter 6-10 in Woo's text._

  
[](http://www.site.gmu.edu/~jchen6/CS652/CS652_8_15.pdf)

13\. Light & Color: light; color models.

[http://cs.gmu.edu/~jchen/graphics/notes/color.pdf](http://cs.gmu.edu/%7Ejchen/graphics/notes/color.pdf)  
[http://cs.gmu.edu/~jchen/graphics/notes/rgbcmy.pdf](http://cs.gmu.edu/%7Ejchen/graphics/notes/rgbcmy.pdf)  
[](http://cs.gmu.edu/%7Ejchen/graphics/notes/curves.pdf)

    _Chapter 13 in Foley's text; Chapter 5-6 in Neider's text. Chapter 4-5 in Woo's text._  
  
14\. Curves  & Surfaces: cubic curves; bicubic surfaces.     _Chapter 11 in
Foley's text; Chapter 11 in Neider's text. Chapter 12 in Woo's text._

[http://cs.gmu.edu/~jchen/graphics/notes/curves.pdf](http://cs.gmu.edu/%7Ejchen/graphics/notes/curves.pdf)  
[http://cs.gmu.edu/~jchen/graphics/notes/surfaces.pdf](http://cs.gmu.edu/%7Ejchen/graphics/notes/surfaces.pdf)  

  
15\. General introduction: physically-based modeling; real-time simulation;
distributed interactive simulation; Virtual Reality, etc.

    _Chapter 12, 14, 17-21 in Foley's text._

  
[Back to Top of Page](http://cs.gmu.edu/~jchen/cs652/cs652-chen.html#top)

* * *

**TEXT: (Required)**

  * Computer Graphics: Principles and Practice, Second Edition in C by James D. Foley, Andries van Dam, Steven K. Feiner and John F. Hughes Addison-Wesley 
  * OpenGL Programming Guide, by (Woo), Neider, Davis, Woo, Addison Wesley 

**TEXT: (Recommended)**

  * Interactive Computer Graphics: A Top-Down Approach with OpenGL by Edward Angel, Addison Wesley 

[Back to Top of Page](http://cs.gmu.edu/~jchen/cs652/cs652-chen.html#top)

* * *

**REFERENCES:**

    **[Graphics related journals and magazines including:](http://wuarchive.wustl.edu/graphics/graphics/bib/cg-journals)**

  * [ACM Transactions on Graphics](http://www.acm.org/tog/)
  * CVGIP: Graphical Models and Image Processing 
  * [IEEE Computer Graphics & Applications](http://www.computer.org/pubs/cg&a/cg&a.htm)
  * [Computer Graphics Forum](http://www.eg.org/Publications/CGF.html)
  * [ACM Transactions on Modeling and Computer Simulation](http://www.acm.org/pubs/tomacs/)
  * [IEEE Transactions on Visualization and Computer Graphics](http://www.computer.org/pubs/tvcg/tvcg.htm)
  * [IEEE Multimedia](http://www.computer.org/pubs/multimed/multimed.htm)
  * ACM Multimedia Systems Journal 
  * Computer Graphics World 
  * Computers and Graphics 
  * Visual Computer 
  * ..., etc. 

    **Graphics related conference proceedings including:**

  * [ACM SIGGRAPH Conference Proceedings](http://www.siggraph.org/)
  * [International ACM Conference on Computer Graphics & Interactive Techniques](http://www.acm.org/catalog/proceedings/siggraph.html)
  * [International Conference on Multimedia Information Systems](http://www.acm.org/catalog/proceedings/mmis.html)
  * [Multimedia: International ACM Conference on Multimedia](http://www.acm.org/catalog/proceedings/mm.html)
  * [Symposium on Interactive 3D Graphics](http://www.acm.org/catalog/proceedings/sig3d.html)
  * [Symposium on Solid Modeling Foundations and Applications](http://www.acm.org/catalog/proceedings/smfa.html)
  * [UIST: ACM Symposium on User Interface Software and Technology](http://www.acm.org/catalog/proceedings/uist.html)
  * [Volume Visualization Workshop](http://www.acm.org/catalog/proceedings/vvw.html)
  * [IEEE Virtual Reality Annual International Symposium 1997 (VRAIS '97)](http://www.eece.unm.edu/eece/conf/vrais/)
  * ..., etc. 

    **Some reference books of mine:**

  * [Computer Graphics from Addison Wesley](http://heg-school.aw.com/cseng/categories/cg.html)
  * Interactive Computer Graphics: A Top-Down Approach with OpenGLTM by Edward Angel 
  * Computer Graphics: Principles and Practice, Second Edition in C by James D. Foley, Andries van Dam, Steven K. Feiner and John F. Hughes 
  * Introduction to Computer Graphics by James D. Foley, Andries van Dam, Steven K. Feiner, John F. Hughes, and Richard L. Phillips 
  * Virtual Reality Systems by John Vince 
  * The Inventor Mentor and The Inventor Toolmaker: Extending Open Inventor, Release 2 by Josie Wernecke and the Open Architecture Group 
  * "Motif Programming: The essentials ... and more" by Marshall Brain, Digital Press 
  * "Computer Graphics" by Donald Hearn, Prentice Hall, C edition 
  * "COMPUTER GRAPHICS: an Object-Oriented Approach to the Art and Science" by Cornel Pokorny, Franklin, Beedle & Associates, Incorporated 
  * "Object-Oriented Programming with C++ and OSF/Motif" by Douglas A. Young, Prentice Hall, 2nd edition 

    **Graphics tools and groups related sites:**

  * [Motif](http://www.cen.com/mw3/)
  * [OpenGL](http://www.opengl.org/)
  * [VRML](http://vag.vrml.org/www-vrml/)
  * [IRIS Inventor and Open Inventor Center](http://www.sgi.com/Technology/Inventor.html)
  * [IRIS Explorer Centers](http://www.sgi.com/Technology/explorer.html)
  * [IRIS Performer Center](http://www.sgi.com/Technology/Performer/index.html)
  * [ImageVision Center](http://www.sgi.com/Technology/ImageVision/index.html)
  * [IRIS Impressario Center](http://www.sgi.com/Technology/Impressario/home.html)
  * [GMU Graphics Group](http://www.cs.gmu.edu/~jchen/team.html)
  * [MD/DC Computer Graphics Home Page](http://nemo.ncsl.nist.gov/~piatko/graphics.html)
  * [Computer Graphics Centers](http://mambo.ucsc.edu/psl/cg.html)

[Back to Top of Page

* * *

](http://cs.gmu.edu/~jchen/cs652/cs652-chen.html#top)_2002 by Jim X. Chen,
Department of Computer Science, George mason University_

