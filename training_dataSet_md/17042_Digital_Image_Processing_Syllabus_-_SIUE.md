* * *

### **ECE 438 DIGITAL IMAGE PROCESSING SYLLABUS**

![](http://www.ee.siue.edu/~sumbaug/images/bfly.jpg)
![](http://www.ee.siue.edu/~sumbaug/images/bfly_ed4.jpg)
![](http://www.ee.siue.edu/~sumbaug/images/bfly_warp.jpg)

* * *

**Professor:** Dr. Scott Umbaugh **Office:** Engineering Building, Room EB3037

**Phone:** 650-2524, 2948 **e-mail:** sumbaug@ee.siue.edu

**Textbook:** _Computer Vision and Image Processing: A Practical Approach
Using CVIPtools_ , SE Umbaugh, Prentice Hall PTR, 1998

**Prerequisite:** ECE 351 and programming experience, or consent of instructor

**Class Format:** Two lectures and 1 lab per week, two tests, quizzes and term
project

**Goals and Objectives:** Introduce the student to analytical tools and
methods which are currently used in digital image processing as applied to
image information for human viewing. Then apply these tools in the laboratory
in image restoration, enhancement and compression.

* * *

### **COURSE OUTLINE**

  * Introduction, 4 Lectures, Chapter 1
  * Image Analysis, 4 Lectures, Chapter 2
  * Image Transforms, 6 Lectures, Chapter 2 

_**TEST #1**_

  * Image Enhancement, 4 Lectures, Chapter 4
  * Image Restoration, 4 Lectures, Chapter 3
  * Image Compression, 4 Lectures, Chapter 5

_**TEST #2**_

_**PROJECT DUE -- 16th week_**

* * *

Project will be some application of image enhancement, restoration or
coding/compression technique to digital image(s). Software will be written in
the C programming language to implement the image processing method.

**GRADING** : Test #1 - 20%, Test #2 - 20%, Quizzes - 20%, Lab Exercises -
20%, Project - 20%

_Note: There will be 6 or 7 pop-quizzes, 5 will be used in the grade. They
will be closed book/notes and about 5 minutes, and will be on the second class
meeting of the week. They will cover the reading for that week._

****

## **ECE 438 LECTURE SCHEDULE**

**WEEK** | **TOPICS** | **READING** | **LABORATORY** |

1 | Overview, human visual system | pp. 1-24, 293-298 | Chap. 6, Introductory
Lab |

2 | HVS, image model | pp. 24-36 , pp. 375-388 | Chap. 6, Introductory Lab |

3 | Image analysis, preprocessing | pp. 37-53 | #1, p. 399 |

4 | Preprocessing, CVIPtools | pp. 53-61 | #2, p. 401 |

5 | Discrete transforms, fourier | pp. 97-106, pp. 401-403 | #3. p. 401 |

6 | discrete cosine, walsh-hadamard | pp. 106-113 | #4: 1,2,3, p. 404 |

7 | filtering, wavelet transform | pp. 113-130 | #5 p. 404, Chap. 6 |

8 | _**Review and TEST #1**_ |  |  |

9 | Image enhancement, gray scale mods, histogram mod | pp. 197-219 | #6, p.
406 |

10 | Enhancement: pseudocolor, sharpen. smooth

**_Project Proposal Due_** |  pp. 219-237 | #7, p. 406 |

11 | Image restoration: degradation model, noise removal, inverse filters, |
pp. 151-174 | Project |

12 | Freq. filters, geometric transforms, | pp. 174-195 | Project |

13 | image compression: system model, fidelity criteria, lossless methods |
pp. 237-258 | Project |

14 | image compression: lossy methods | pp. 258-292 | Project |

15 | **_Review and TEST #2**_ |  |  Project |

16 | Demo term project to professor and TA

**_Project Paper Due**_ |  | ****

## **ECE 438 Image Processing - Semester Project**

**Semester Project:** The project will consist of designing, implementing, and
analyzing the results for an image processing problem. You can work alone or
with a partner. The project will be selected by the students, subject to
approval by the professor. A paper will be written describing the project and
discussing what was learned during the project. The final paper should be
about 8 to 15 pages, typed and double-spaced; include images ! In the paper
include an appendix containing program listing(s). The students will give a
short presentation of their project in the lab to the class, the professor,
and the lab instructor.

**Grading:** The project is worth 20% of your term grade, broken down as
follows:

  * Overall Project.. 10%
  * Paper...................... 5%
  * Presentation......... 5%

_**Possible Project Topics:**_

  * FFT, WHT, PCT or DCT filtering/compression - butterworth, etc.
  * Histogram modification - apply and compare different methods
  * Histogram specification - program to enhance portions of an image, e.g. blow up in size and improve contrast
  * image restoration - blurred images, noisy images, inverse filtering, statistical modeling and recovery 
  * image encoding - DPCM, transform applications (DFT, FFT, WHT, DCT, Hotelling), Huffman codes.
  * other related topics of your choice

* NOTE: If you do not have any specific images that you want to use, take a look at the image database directories JFK, NASA and UFO. 

**Week What is due**

  * 10 Brief, 1 page max., project proposal
  * 16 Project paper due. Short demonstration to professor and lab instructor about project - show images in lab and discuss

_**Suggested Project Process:**_

  * 1) Find an area of interest from the lab or from class.
  * 2) Define experiment(s) you wish to pursue
  * 3) Define C function(s) to implement related to project
  * 4) Code and debug your function(s)
  * 5) Test your functions on some real images
  * 6) Process images/do the experiments
  * 7) Compare and contrast your results to other similar results from using CVIPtools functions, or research results in library from similar experiments - Analyze results using appropriate metrics, tabulate or plot, etc.
  * 8) Write report, include images
  * 9) Demonstration to the class

## **ECE 438 Digital Image Processing Lab  Outline**

| **Week** | **TOPICS - reading: Chapters 6 and 8, CVIPtools  ** | **

1&2 **| Introduction to C programming language and SUN-based image
acquisition/processing system and CVIPlab via thresholding program | **

3 **| arithmetic/logic operations | **

4 **| Image geometry operations | **

5 **| Fourier Transform exercise | **

6 **| Image enhancement: spatial convolution masks | **

7 **| Transform part II: filtering | **

8 **| (Test #1) | **

9 **| Histogram modification I: stretch, shrink, slide | **

10 **| Histogram modification II: unsharp masking

Project proposal due. | **

11-15 **| Work on project -- application of image enhancement or
coding/compression.

Will be written in the C programming language. | **

16 **| Demo project to Professor and lab TA

**ECE 438 - Example Past Term Projects**

  * Hadamard-ordered Walsh transform on 16x16 blocks for compression
  * FFT for frequency domain digital filtering
  * Fast walsh transform for compression compared to 0,1st,2nd order-hold
  * Zooming algorithm using Lagrange method of interpolation
  * Huffman encoding for compression
  * 2-D to 3-D gray-level intensity mapping
  * 3-D rotation and translation
  * Removal of blur from uniform linear motion 
  * High frequency enhancement techniques on UFO/JFK photos:
  * Local- based on statistics, - based on neighborhood histogram EQ
  * Histogram stretch
  * Global histogram EQ
  * Unsharp masking
  * Convolutions, high-pass filters
  * Sharpen, roberts, sobel colored edge, bitplane
  * Histogram equalization and image coloring enhancement for X-ray images
  * Histogram EQ and direct histogram specification using VGA/mouse drivers
  * Global vs. Local Histogram EQ
  * FFT and FWT on 16x16 blocks for filtering
  * Arithmetic coding for compression
  * Differential coding 1-D and 2-D
  * Homomorphic filtering
  * DCT for compression - JPEG algorithm ****

**Brief Bibliography**

**Books**

  * 1\. Digital Image Processing - R.C.Gonzalez & P.Wintz
  * 2\. Robot Vision - B.K.P.Horn
  * 3\. Computer Vision - D.H.Ballard & C.M.Brown
  * 4\. Syntactic Pattern Recognition : An introduction -R.C.Gonzalez and M.G.Thomason
  * 5\. Pattern Recognition - A Statistical Approach - P.A. Devijver and J. Kittler
  * 6\. Digital Image Processing - W. K. Pratt
  * 7\. Fundamentals of Digital Image Processing - A.K. Jain
  * 8\. Digital Picture Processing - A. Rosenfeld and A.C. Kak
  * 9\. Pattern Classification and Scene Analysis - R.O. Duda and P.E. Hart
  * 10\. Object Recognition by Computer - W.E.L. Grimson
  * 11\. Digital Pictures - A.N. Netravali and B.G. Haskell
  * 12\. Vision in Man and Machine - M.D. Levine
  * 13\. Pattern Recognition Statistical, Structural and Neural Approaches, R.J Schalkoff, John Wiley & Sons NY
  * 14\. Digital Image Processing and Computer Vision, R.J. Schalkoff, Wiley
  * 15\. Artificial Intelligence: An Engineering Approach, R.J. Schalkoff, McGraw-Hill 
  * 16\. Algorithms for Graphics and Image Processing, Theo Pavlidis, Computer Science Press, call no.: T385.P381982
  * 17\. Handbook of Pattern Recognition and Image Processing, K.S. Fu and T.Y. Young, Academic Press
  * 18\. The Image Processing Handbook, John C. Russ, CRC Press SIUE Library call #: TA1632.R881992 (reference) ****

**Journals**

  * 1\. IEEE Transactions on Pattern Analysis and Machine Intelligence
  * 2\. IEEE Transactions on Computers
  * 3\. Pattern Recognition
  * 4\. Computer Vision, Graphics and Image Processing
  * 5\. IEEE Transactions on Medical Imaging
  * 6\. Computerized Medical Imaging and Graphics
  * 7\. IEEE Transactions on Image Processing
  * 8\. IEEE Engineering in Medicine and Biology
  * 9\. IEEE Transactions on Signal Processing
  * 10\. IEEE Transactions on Neural Networks
  * 11\. IEEE Transactions on Geoscience and Remote Sensing
  * 12\. Photogrammetric Engineering and Remote Sensing
  * 13\. International Journal of Remote Sensing
  * 14\. Journal of Visual Communication and Image Representation ****

**15\. Numerous Conference Proceedings from the following professional
groups:**

  * IEEE - Institute of Electrical and Electronic Engineers
  * SPIE - The International Society for Optical Engineering
  * SMPTE - The Society of Motion Picture and Television Engineers
  * PRS - Pattern Recognition Society ****

