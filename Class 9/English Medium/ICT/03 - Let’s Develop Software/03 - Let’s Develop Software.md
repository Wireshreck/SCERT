---
class: 9
medium: English
subject: ICT
textbook: Information and Communications Technology IX, Part I
edition: First Edition 2025
chapter: 3
topic: Let’s Develop Software!
kind: chapter
tags:
  - class/9
  - medium/english
  - subject/ict
  - type/chapter
source: "[[../01 - Poster Images/ICT Part 1 (2025 Samagra).pdf]]"
---
# Chapter 3 — Let’s Develop Software!

**Standard IX · English Medium · ICT · printed pp. 37–47**

The chapter develops a PictoBlox digital alarm clock that can become a school water bell. It makes the software-design process concrete through two stages: prepare the interface with sprites and their positions, then code the sprites to respond to computer time and user input. A short Python animation extends the project and introduces text-based coding.

## Project structure

- The dial is the background; hour, minute, and second hands plus an alarm button are separate sprites. Adjust each sprite’s pivot point so the clock hands rotate around the dial’s centre (pp. 39–41).
- Sprite layer order controls which object appears in front. PictoBlox’s Looks block can move a sprite to the front or back layer (p. 39).
- The sensing `current` block exposes computer time fields such as hour, minute, and second (p. 42).
- The hands’ direction is updated from the corresponding time values. The second and minute hands move 6° per unit; the hour-hand direction combines the hour and minute values (pp. 41–43). See [[../Formulas/Clock Hand Angular Steps]].
- The Set Alarm button asks for hour and minute input. Variables store the response; the program waits until the stored time matches the current time, then plays a sound (pp. 43–44).
- A Python example animates a boy sprite moving toward a dispenser; on contact the costume changes, the character says a hydration reminder, and the example stops (pp. 45–46).

## Programming ideas

Block programming assembles instructions from draggable code blocks. The chapter contrasts this with text-based programming languages such as Python, Java, and C++. It defines syntax as the rules for correctly arranging instructions and symbols; indentation is part of Python syntax (pp. 38, 45–46).

See [[Concepts/Interface, Sprites and Pivot Points]], [[Concepts/Time, Variables and Event-driven Behaviour]], [[Concepts/Block Coding and Text-based Programming]], and [[../Formulas/Clock Hand Angular Steps]].

## Assessment and activities

The end questions test sprite front/back ordering and the correct time-dependent direction for rotating a sprite counter-clockwise (p. 47). Extended activities ask learners to animate bells when the alarm sounds and adapt the clock to run at regular intervals without user input. See [[Questions/Chapter 03 - Let’s Develop Software]].

## Figures and page references

- Table 3.1 sprite roles in the alarm clock (p. 39).
- Figures 3.1–3.2 interface and pivot-point positioning (p. 40).
- Figures 3.3–3.6 direction fields and clock-hand angle instructions (pp. 41–43).
- Figures 3.7–3.8 alarm input, variables, comparison, and sound (pp. 43–44).
- Figures 3.9–3.10 Python animation interface and code (pp. 45–46).
- Assessment and extended tasks (p. 47).

## Source reading note

Printed pages 37–47 from the Samagra 2025 Part I PDF were read and visually reviewed, including the sprite/function table, clock construction and angle diagrams, PictoBlox code blocks, Python animation figure, and exercises.
