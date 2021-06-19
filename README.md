# Face-Recognition
A real time face recognition based attendence management system using Python, OpenCV.

## Basic functionalities
1. Detect faces in the frame.
2. Encode the face region and compare with known faces.
3. Label the name.

## Approach used
1. First the known faces are encoded and the encodings are stored along with their names in a list with which we are going to compare our live faces.
2. Access webcam using openCV and performing the following in a while loop
3. Create a list to store names of recognised faces (List is creates so we can store multiple names incase of multiple faces in a single frame)
4. Detect only the part of the frame where face is present, then encode that region of interest(ROI).
5. Now compare this encoding with the known encodings and if present label the face with their respective name else label as unknown.
6. The names of recognised faces are stored in a comma-separated-value file(csv file) along with date & time.
7. At the end ask the user for name of person whose number of days attendended need to be calculated, and check the csv file for the name and return as number.

