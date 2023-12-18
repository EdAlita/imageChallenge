# Image Challenge for CADx 

- [How to get the data](#how-to-get-the-data)
- [Challenge 1](#challenge-1)
- [Challenge 2](#challenge-2)
- [Rules](#rules)
- [Point system](#point-system)
- [How to deliver](#how-to-deliver)

## How to get the data

Clone the the repository to your own mahine. with the next line of code:

```
git clone git@github.com:EdAlita/imageChallenge.git
```

To install the requieremnts libraries to this callenge you can run:


```
pip install -r requirements. txt
```

## Challenge 1

The data inside of the folder consist of the original images, the objetive of this challenges is to obtain the tarjet images that are display on the projetor.

Some *hints* are going to be provide when we see appropiate.

## Challenge 2

In this challenge you are provide with some input images, output images, a broken code and the test images. The objetive is to fix the code and provide the output of the test images. 

The files in challenge 2 have the next structure:

1. Submitions: The files use for uploading your submitions. 
2. test.py: the code to fix or if you want you can implement your own code
3. Test: in this folder there are some images, gt and outputs for you to see if the code is fixed as we expected.


```
Challenge_2
├── Submititons
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

1. The challenges are solve in the same teams as the labs ones.
2. Avoid the use of AI such as Chat GPT.

## Point System

For your submission will be evaluated by DICE with the gt images, we will used the dice value and multiply it by 10 to calculated the score of each of the images, the total score will be the sum of all the images.

## How to deliver

Create a zip file with the next structure with your submition.

```
Team_name
├── Challenge_1
│   ├── output_1.jpg     //Prostate_image
│   ├── output_2.jpg    //chest_image
│   └── output_3.jpg    //brain
└── Challenge_2
    ├── q1.png
    ├── q2.png
    └── q3.png
```

Upload the file to the next drive, please only one submition per team.
