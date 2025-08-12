#!/usr/bin/env python3
"""
Simple Math Question Generation Script
Generates new math questions similar to base questions
"""

import os

class SimpleMathQuestionGenerator:
    def __init__(self):
        self.curriculum = {
            "Quantitative Math": {
                "Problem Solving": ["Numbers and Operations", "Algebra", "Geometry", "Problem Solving", "Probability and Statistics", "Data Analysis"],
                "Algebra": ["Algebraic Word Problems", "Interpreting Variables", "Polynomial Expressions (FOIL/Factoring)", "Rational Expressions", "Exponential Expressions (Product rule, negative exponents)", "Quadratic Equations & Functions (Finding roots/solutions, graphing)", "Functions Operations"],
                "Geometry and Measurement": ["Area & Volume", "Perimeter", "Lines, Angles, & Triangles", "Right Triangles & Trigonometry", "Circles (Area, circumference)", "Coordinate Geometry", "Slope", "Transformations (Dilating a shape)", "Parallel & Perpendicular Lines", "Solid Figures (Volume of Cubes)"],
                "Numbers and Operations": ["Basic Number Theory", "Prime & Composite Numbers", "Rational Numbers", "Order of Operations", "Estimation", "Fractions, Decimals, & Percents", "Sequences & Series", "Computation with Whole Numbers", "Operations with Negatives"],
                "Data Analysis & Probability": ["Interpretation of Tables & Graphs", "Trends & Inferences", "Probability (Basic, Compound Events)", "Mean, Median, Mode, & Range", "Weighted Averages", "Counting & Arrangement Problems"]
            }
        }
    
    def generate_question_1(self):
        """Generate a question similar to the uniform combinations problem"""
        return {
            "title": "Math Assessment - Combinatorics and Counting",
            "description": "This assessment focuses on counting principles and combinatorial problems involving real-world scenarios.",
            "question": "A restaurant offers a lunch special where customers can choose 1 main dish and 1 side dish. The menu shows the following options:\n\n## Lunch Special Menu\n| Main Dish | Side Dish |\n| :---: | :---: |\n| Grilled Chicken | French Fries |\n| Beef Burger | Coleslaw |\n| Fish Fillet | Mashed Potatoes |\n| Vegetarian Pasta | Garden Salad |\n| | Onion Rings |\n\nHow many different lunch combinations are possible?",
            "instruction": "Use the counting principle to determine the total number of possible combinations.",
            "difficulty": "moderate",
            "order": 1,
            "options": [
                "15 combinations",
                "20 combinations", 
                "25 combinations",
                "30 combinations",
                "35 combinations"
            ],
            "correct_answer": "20 combinations",
            "explanation": "Using the counting principle: Number of main dishes × Number of side dishes = 4 × 5 = 20 different combinations. Each main dish can be paired with any of the 5 side dishes, giving us 4 × 5 = 20 total possibilities.",
            "subject": "Quantitative Math",
            "unit": "Problem Solving", 
            "topic": "Counting & Arrangement Problems",
            "plusmarks": 1
        }
    
    def generate_question_2(self):
        """Generate a question similar to the sphere packing problem"""
        return {
            "title": "Math Assessment - Geometry and Spatial Reasoning",
            "description": "This assessment focuses on geometric concepts including area, volume, and spatial relationships.",
            "question": "A cylindrical container is designed to hold 8 tennis balls tightly packed in two layers. Each tennis ball has a radius of 3.5 centimeters. The top view shows a circular arrangement with 4 balls in the bottom layer and 4 balls in the top layer. Which of the following is closest to the dimensions of the cylindrical container?\n\n**Note**: The height accounts for two layers of balls, and the diameter accommodates the circular arrangement.",
            "instruction": "Calculate the dimensions needed to accommodate the tightly packed tennis balls in the cylindrical container.",
            "difficulty": "hard",
            "order": 2,
            "options": [
                "$7 \\times 7 \\times 14$ cm",
                "$7 \\times 7 \\times 21$ cm", 
                "$14 \\times 14 \\times 14$ cm",
                "$14 \\times 14 \\times 21$ cm",
                "$21 \\times 21 \\times 28$ cm"
            ],
            "correct_answer": "$14 \\times 14 \\times 21$ cm",
            "explanation": "Each tennis ball has a radius of 3.5 cm, so diameter = 7 cm. For the circular arrangement of 4 balls, the container diameter must be approximately 14 cm (2 × 7 cm). The height must accommodate 2 layers: 2 × 7 cm = 14 cm, plus some spacing, so approximately 21 cm total. Therefore, the closest dimensions are $14 \\times 14 \\times 21$ cm.",
            "subject": "Quantitative Math",
            "unit": "Geometry and Measurement",
            "topic": "Area & Volume", 
            "plusmarks": 1
        }
    
    def format_question_output(self, question_data):
        """Format question data according to the specified output format"""
        output = f"""@title {question_data['title']}
@description {question_data['description']}

@question {question_data['question']}
@instruction {question_data['instruction']}
@difficulty {question_data['difficulty']}
@order {question_data['order']}
@option {question_data['options'][0]}
@option {question_data['options'][1]}
@@option {question_data['correct_answer']}
@option {question_data['options'][3]}
@option {question_data['options'][4]}
@explanation {question_data['explanation']}
@subject {question_data['subject']}
@unit {question_data['unit']}
@topic {question_data['topic']}
@plusmarks {question_data['plusmarks']}

"""
        return output
    
    def create_markdown_document(self, questions):
        """Create a markdown document with the generated questions"""
        md_content = "# Math Question Generation - Assessment\n\n"
        md_content += "This document contains two newly generated math questions following the specified format and curriculum hierarchy.\n\n"
        
        for i, question in enumerate(questions, 1):
            md_content += f"## Question {i}\n\n"
            md_content += f"{question['question']}\n\n"
            
            md_content += "### Options:\n"
            for j, option in enumerate(question['options'], 1):
                marker = "✓" if option == question['correct_answer'] else "○"
                md_content += f"{marker} {option}\n"
            
            md_content += f"\n### Explanation:\n{question['explanation']}\n\n"
            
            md_content += "### Question Metadata:\n"
            md_content += f"- **Subject**: {question['subject']}\n"
            md_content += f"- **Unit**: {question['unit']}\n"
            md_content += f"- **Topic**: {question['topic']}\n"
            md_content += f"- **Difficulty**: {question['difficulty']}\n"
            md_content += f"- **Marks**: {question['plusmarks']}\n\n"
            
            if i < len(questions):
                md_content += "---\n\n"
        
        return md_content
    
    def generate_all_questions(self):
        """Generate all questions and create outputs"""
        print("Generating new math questions...")
        
        # Generate questions
        question1 = self.generate_question_1()
        question2 = self.generate_question_2()
        questions = [question1, question2]
        
        # Create output directory
        os.makedirs('output', exist_ok=True)
        
        # Save raw formatted output
        with open('output/questions_formatted.txt', 'w', encoding='utf-8') as f:
            for question in questions:
                f.write(self.format_question_output(question))
        
        # Create markdown document
        md_content = self.create_markdown_document(questions)
        with open('output/Math_Questions_Assessment.md', 'w', encoding='utf-8') as f:
            f.write(md_content)
        
        # Create text document (Word-like format)
        text_content = self.create_text_document(questions)
        with open('output/Math_Questions_Assessment.txt', 'w', encoding='utf-8') as f:
            f.write(text_content)
        
        print("Questions generated successfully!")
        print("Output files created in 'output/' directory")
        
        return questions
    
    def create_text_document(self, questions):
        """Create a text document that mimics Word document formatting"""
        content = "=" * 60 + "\n"
        content += "MATH QUESTION GENERATION - ASSESSMENT\n"
        content += "=" * 60 + "\n\n"
        
        content += "This document contains two newly generated math questions following the specified format and curriculum hierarchy.\n\n"
        
        for i, question in enumerate(questions, 1):
            content += f"QUESTION {i}\n"
            content += "-" * 40 + "\n\n"
            
            content += f"QUESTION TEXT:\n{question['question']}\n\n"
            
            content += "OPTIONS:\n"
            for j, option in enumerate(question['options'], 1):
                marker = "[CORRECT]" if option == question['correct_answer'] else "[ ]"
                content += f"{marker} {option}\n"
            
            content += f"\nEXPLANATION:\n{question['explanation']}\n\n"
            
            content += "METADATA:\n"
            content += f"Subject: {question['subject']}\n"
            content += f"Unit: {question['unit']}\n"
            content += f"Topic: {question['topic']}\n"
            content += f"Difficulty: {question['difficulty']}\n"
            content += f"Marks: {question['plusmarks']}\n\n"
            
            if i < len(questions):
                content += "=" * 60 + "\n\n"
        
        return content

def main():
    """Main function to run the question generator"""
    generator = SimpleMathQuestionGenerator()
    questions = generator.generate_all_questions()
    
    print("\n" + "="*50)
    print("GENERATED QUESTIONS SUMMARY")
    print("="*50)
    
    for i, question in enumerate(questions, 1):
        print(f"\nQuestion {i}:")
        print(f"Topic: {question['topic']}")
        print(f"Difficulty: {question['difficulty']}")
        print(f"Correct Answer: {question['correct_answer']}")
        print("-" * 30)

if __name__ == "__main__":
    main() 