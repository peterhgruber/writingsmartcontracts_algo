# Writing Smart Contracts on Algorand (WSC)
peter.gruber@usi.ch, 2024-02-18

Writing Smart Contracts on Algorand is a hands-on one-semester course on blockchain applications and smart contracts. The course is aimed at students in economics, finance, law or communications. All examples are implemented in Python on the Algorand blockchain. The course requires minimal experience with programming or the blockchain.

## TLDR (executive summary)
+ Download entire repository
+ Do not change folder structure
+ Install Anaconda
+ Run Jupyter notebooks in the order of the numbers

## Philosophy
The course is designed as a **coherent** and easy entrance into the world of Smart Contracts. This is done by reducing requirements and frictions as much as possible. Concretely, students have to install only **one** program (the Anaconda environment) on their laptops. The entire class requires **only one programming language**, Python. Sample code is provided for all relevant concepts in easily readable Jupyter Notebooks. 

The coherent **course structure** contributes to the learning outcome. This course aims at **systematically constructing knowledge**, rather than presenting independent topics. Two examples for this: credentials created in chapter 3 will be used throughout the course, emphasizing the importance of managing credentials well. Similarly, tokens created in chapter 4 will be later on used in smart contracts.

## Duration
The course is aimed for teaching in approximately 24 to 30 class hours, commensurate with a 2-hour course for one semester or a 1-week intensive course. The work load is equivalent to 3ECTS. The course has been taught three times at Università della Svizzera italiana in the form of a one-week winter school, see [https://www.usi.ch/wsc](https://www.usi.ch/wsc)

## Goals
The course introduces students to the relevant theoretical concepts and provides a hands-on introduction to using the blockchain and writing smart contracts in Python. The goal is to equip students with the necessary skills and useful background knowledge for creating smart contracts and deploying them on the Algorand blockchain.

## Course Objectives
After this course, students will be able to interact programmatically with the Algorand blockchain. They will know how create and manage blockchain credentials. They will know how to create their own token. They will have learnt how to write stateless and stateful smart contracts in Python as well as how to deploy them and interact with them. They will have learnt how to express simple governance structures, business processes and financial assets as smart contracts. They will understand the differences between functional and contract-oriented programming and be aware of the unique security risks involved with blockchain technology.  Beyond the technical skills, they will have learnt how to plan and organize individual and group work on smart contracts.

## Methods and Course Work
Teaching focuses heavily on learning-by-doing. Every module consists of five steps:

1. Short lecture presenting a new concepts
2. Guided tour: professor and students work together through a Jupyter notebook
2. Unguided tour: students experiment with the Jupyter notebook
4. Individual exercises 
5. Discussion of students’ solutions in class

## Grading
Grading is based 20% on exercises during the course and 80% on projects at the end of the course.

# Material
**Important** almost all code in Juypter notebooks uses relative paths. Moving files or changing the structure of the folders *inside* `ClassMaterial` will break dependencies. 

#### ClassMaterial
All material aimed to be distributed to students. There are folders for every chapter which contain, where applicable, the follwoing subfolders (in the order of their use)

* **Slides** PDF slide sets with introductory material.
* **Code** Several Juypter notebooks, to be used in the order of their numbering. 
* **Quiz** A set of review questions.
* **Assignments** Problem sets and exercises
* **Material** Additional material and literature.

#### Course
Syllabus for the course.

#### Literature
Common literature folder for all course modules.

#### TeacherMaterial
This folder is avaiable to university teachers upon request to `peter.gruber@usi.ch` (please use your official email for contacting me). It contains the following additional material

* **Solutions** to quizzes, assignments and exercises in Jupyter notebooks
* **TeacherNotes** Additional background information
* **LaTeXSources** of assignments and slides

# Deployment to Students
Distribute the contents of the entire repository to students. 

* **Do not change the folder structure.** 
* When you have worked through the repository, **remove your `credentials` file before distributing to students.**

Students will have to bring their laptops and smart phones. They will have to install the following software (see also chapter 2 – Tools):

* **Anaconda** from  [https://www.anaconda.com/download]()
	* In Anaconda, we make exclusively use of JuypterLab and Python. 
	* Installation instructions for required Python packages such as `py-algorand-sdk` and `pyteal` are included in the Jupyter notebooks.
* **Algorand Pera Wallet**

Furthermore, a the (free) Algonode API wil be used

* **Algonode** at [https://algonode.io/]()

# Disclaimer
All code examples are **for educational purposes only** and have **not been audited** for security risks. 

Some examples are explicitly designed to **include security flaws** so that they can be discussed in class. **Do not use any of the code in real-world projects.** Do not use wallets that contain significant holdings in an educational context.

# License
* All software code is made available under MIT license (https://choosealicense.com/licenses/mit/)
* Text material (slides, assignments, quizzes) are made available under the creative commons license CC-BY 4.0 (https://creativecommons.org/licenses/by/4.0/). 

 