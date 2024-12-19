# Hanoi Tower Detection and Solver with Robot

This project combines computer vision techniques to detect the state of a Hanoi Tower puzzle from an image and then solves the puzzle using a custom Hanoi Tower solver.

## Project Structure

- `main.py`: The main script that orchestrates the detection and solving process.
- `hanois.py`: Contains classes for the Hanoi Tower game logic (`HanoiGame`, `HanoiTower`, `HanoiMovement`).
- `location_circles_lab.py`: Implements the `DetectHanoiTower` class for image processing and tower detection.

## How it works

1. **Image Processing**: 
   - The program takes an image file as input (`examples/imagen_20241205_143702.png`).
   - It uses the `DetectHanoiTower` class to process the image and detect the state of the Hanoi Towers.

2. **Hanoi Tower Setup**:
   - Based on the detected state, it initializes a `HanoiGame` object.
   - The game is set up with 3 towers and 5 discs.

3. **Solving**:
   - The program generates a solution using `getRandomHanoiSolutionArray()`.
   - The solution is then converted into a matrix format.

4. **Output**:
   - The final solution is printed as a list of matrices, each representing a step in solving the puzzle.

## Usage

Run the `main.py` script: