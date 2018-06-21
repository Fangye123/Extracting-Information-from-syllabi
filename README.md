# Extracting-Information-from-syllabi
Extracting information from syllabi

Team Members
Yichuan Xu B00771396
Fangye Tang B00612172
Ziyun Zhong B00774740
Jingya Sun B00755962

### Report link
https://drive.google.com/file/d/1NaWmuQd8lDcCOGle8VahJsjCJuMjQSLV/view?usp=sharing

### Abstract
This is the project, our team has developed a tool to read the title of syllabus from PDFs, with the help of Word Embedding, Deep Neural Networks and other state of the art technologies. Now users can simply submit a PDF and our application will automatically output the related information.


### Introduction
Last semester, our team developed a prototype called ‘DalBooster’, an Android App that’s designed to help students at Dalhousie University to manage their school work, in a much more intuitive way. In that app, it’s missing a desired function that could bring the one-click experience for students when they try to create a new course, where traditional apps require students to enter that information manually box by box. In this project we want to try the implementation to make that possible. The work to extract all the useful information like course information, grading schema are beyond the scope of this project but due to the limited time, therefore, we decided to implement the first step: Extract the title from syllabus. This report will include our intuition, methodology, related work and experiment results. 

### Conclusion
In this project we successfully used Deep Neural Network to predict the title of syllabi. The result turned out that the simpler Logistic Regression works better than the more complicated LSTM model in our case to just retrieve titles, where more complicated information may need better models. Also, we found out the better quality of data is correlated with better training process, so properly preprocessing the data is very important. The next step for us is to see if we can extract more information from syllabus.
