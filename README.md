# Image Challenge for CADx 

- [How to get the data](#how-to-get-the-data)
- [Challenge 1](#challenge-1)
- [Challenge 2](#challenge-2)
- [Rules](#rules)
- [Point system](#point-system)
- [How to deliver](#how-to-deliver)

## How to get the data

Clone the repository to your machine. with the next line of code:

```
git clone git@github.com:EdAlita/imageChallenge.git
```

To install the required libraries for this challenge you can run the:


```
pip install -r requirements. txt
```

## Challenge 1

The data inside of the folder consists of the original images, the objective of this challenge is to obtain the target images that are displayed on the projector.

Some *hints* are going to be provided when we see appropriate.

## Challenge 2

In this challenge, you are provided with some input images, output images, a broken code, and test images. The objective is to fix the code and provide the output of the test images. 

The files in Challenge 2 have the next structure:

1. Submissions: The files used for uploading your submissions. 
2. test.py: the code to fix or if you want you can implement your code
3. Test: in this folder, there are some images, gt, and outputs for you to see if the code is fixed as we expected.


```
Challenge_2
├── Submissions
│   ├── q1.tif 
│   ├── q2.tif
│   └── q3.tif
├── test.py
└── Tests
    ├── gt_test1.png
    ├── gt_test2.png
    ├── test1_in.tif
    ├── test1_out.png
    ├── test2_in.tif
    └── test2_out.png
```

## Rules

1. The challenges are solved in the same teams as the lab's ones.
2. Avoid the use of AI such as Chat GPT.

## Point System

For your submission will be evaluated by DICE with the gt images, we will use the dice value and multiply it by 10 to calculate the score of each of the images, the total score will be the sum of all the images.

## How to deliver

You need to deliver your answer in this [link](https://forms.gle/jTufAkcqttV2KsJL7)

```
RESPECT THE NAME OF THE FILES FOR YOUR SUBMISSION

Challenge_1
 ├── output_1.jpg     //Prostate_image
 ├── output_2.jpg    //chest_image
 └── output_3.jpg    //brain

FOR THE ZIP FILE USE THIS STRUCTURE AND THE FILES NAMES

Challenge_2
 ├── q1.png
 ├── q2.png
 └── q3.png

```
