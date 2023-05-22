# attendance-system-

Hello everyone! I'm excited to share with you my latest project - an attendance program that I've developed from scratch.
I've always been passionate about finding ways to make attendance tracking more efficient and accurate.
With this program, I've created an intuitive and user-friendly interface that allows you to easily track attendance, generate reports, and streamline your administrative processes. Whether you're a small business owner, a team leader, or a teacher, this program can help you save time and improve your attendance management.

LBPH Face Recognizer is a simple and effective face recognition algorithm that can handle variations in lighting, pose, and expression. However, it may not perform well under conditions such as occlusion or low resolution images.

what is Local Binary Pattern (LBP) ?
Local Binary Pattern (LBP) is a simple yet powerful texture descriptor used in computer vision and image analysis. It was first introduced by Ojala et al. in 1996 and has since gained popularity due to its robustness, simplicity, and efficiency.

The basic idea behind LBP is to extract a texture pattern from an image by comparing the intensity values of a pixel with its surrounding neighbors. Specifically, for each pixel in an image, the LBP operator compares its intensity value with those of its surrounding neighbors. If the neighbor's intensity value is greater than or equal to the center pixel's intensity value, it is assigned a value of 1, otherwise, it is assigned a value of 0. This binary code is then converted into a decimal value, which represents the local pattern around that pixel.

The LBP operator can be applied to different scales and sizes of neighborhoods, resulting in various types of LBP descriptors. For example, the original LBP operator uses an 8-neighborhood, which means it compares the center pixel with its 8 surrounding neighbors. However, variants of LBP have been proposed that use different neighborhood sizes and shapes, such as circular or elliptical neighborhoods.

LBP has various applications, including texture classification, object recognition, and facial analysis. In facial analysis, LBP is commonly used as a feature descriptor for face recognition tasks, such as gender classification, emotion recognition, and age estimation.
I've used Haar cascades models to detect the face (face ROI) and LBPHFaceRecognizer to recognize every photo with its user_ID

How LBPHFaceRecognizer works .?
LBPH (Local Binary Patterns Histograms) Face Recognizer is a popular face recognition algorithm that works by extracting local binary patterns from a face image and computing a histogram of these patterns. Here's a brief overview of how it works:

First, the algorithm takes an input image and converts it to grayscale.

Next, it divides the image into small regions called "cells" and computes a local binary pattern for each pixel in each cell. A local binary pattern is a binary code that represents the relationship between the intensity of a pixel and its surrounding pixels.

Then, the algorithm calculates a histogram of the local binary patterns within each cell. This histogram represents the distribution of the local patterns within that cell.

The histograms from all the cells are concatenated to create a feature vector that represents the input face image.

Finally, the algorithm compares the feature vector of the input image with the feature vectors of a set of known faces in a database using a distance metric, such as Euclidean distance or cosine distance. The closest match is considered to be the recognized face.
