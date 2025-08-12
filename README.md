# Math Question Generation Project

## Project Overview
This project generates new math questions similar to given base questions using LLM approaches. The questions follow a specific format and include curriculum-aligned subject, unit, and topic classifications.

## Project Structure
- `questions/` - Generated math questions
- `images/` - Question images and diagrams
- `output/` - Final formatted output
- `src/` - Source code for question generation

## Base Questions
1. **Uniform Combinations**: Counting principle problem with table data
2. **Sphere Packing**: Geometry problem with visual representation

## Curriculum Hierarchy
The project uses a structured curriculum hierarchy for classifying questions:
- Subject: Quantitative Math
- Units: Problem Solving, Algebra, Geometry and Measurement, Numbers and Operations, Data Analysis & Probability
- Topics: Various specific topics within each unit

## Output Format
Questions follow a specific format with metadata tags including:
- @title, @description, @question, @instruction
- @difficulty, @order, @options, @explanation
- @subject, @unit, @topic, @plusmarks

## Usage
Run the main script to generate new questions:
```bash
python src/generate_questions.py
```

## Requirements
- Python 3.8+
- Required packages listed in requirements.txt 