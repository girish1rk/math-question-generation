#!/usr/bin/env python3
"""
Simple Image Generator for Math Questions
Creates basic diagrams and images for the generated questions
"""

import os
from PIL import Image, ImageDraw, ImageFont

class SimpleImageGenerator:
    def __init__(self):
        self.output_dir = "images"
        os.makedirs(self.output_dir, exist_ok=True)
    
    def create_lunch_menu_image(self):
        """Create an image for the lunch special menu question"""
        # Create a simple table-like image
        img = Image.new('RGB', (500, 400), color='white')
        draw = ImageDraw.Draw(img)
        
        # Draw title
        draw.text((150, 20), "Lunch Special Menu", fill='black')
        
        # Draw table structure
        draw.rectangle([50, 60, 450, 350], outline='black', width=3)
        draw.line([50, 120, 450, 120], fill='black', width=2)  # Header line
        draw.line([250, 60, 250, 350], fill='black', width=2)  # Vertical line
        
        # Draw headers
        draw.text((100, 80), "Main Dish", fill='black')
        draw.text((300, 80), "Side Dish", fill='black')
        
        # Draw menu items
        main_dishes = ["Grilled Chicken", "Beef Burger", "Fish Fillet", "Veg Pasta"]
        side_dishes = ["French Fries", "Coleslaw", "Mashed Potatoes", "Garden Salad", "Onion Rings"]
        
        y_pos = 140
        for i, dish in enumerate(main_dishes):
            draw.text((70, y_pos), dish, fill='black')
            y_pos += 30
        
        y_pos = 140
        for i, dish in enumerate(side_dishes):
            draw.text((270, y_pos), dish, fill='black')
            y_pos += 30
        
        # Save image
        img_path = os.path.join(self.output_dir, "lunch_special_menu.png")
        img.save(img_path)
        print(f"Created image: {img_path}")
        return img_path
    
    def create_tennis_container_image(self):
        """Create an image for the tennis ball container question"""
        # Create a simple diagram
        img = Image.new('RGB', (600, 400), color='white')
        draw = ImageDraw.Draw(img)
        
        # Draw title
        draw.text((150, 20), "Tennis Ball Container (Top View)", fill='black')
        
        # Draw container outline (circle)
        center_x, center_y = 300, 200
        radius = 120
        draw.ellipse([center_x-radius, center_y-radius, center_x+radius, center_y+radius], 
                    outline='black', width=3)
        
        # Draw tennis balls in circular arrangement
        ball_radius = 30
        angles = [0, 90, 180, 270]  # 4 balls in a circle
        
        for angle in angles:
            import math
            x = center_x + (radius - ball_radius) * math.cos(math.radians(angle))
            y = center_y + (radius - ball_radius) * math.sin(math.radians(angle))
            
            # Draw tennis ball
            draw.ellipse([x-ball_radius, y-ball_radius, x+ball_radius, y+ball_radius], 
                        fill='yellow', outline='black', width=2)
            
            # Add ball label
            draw.text((x-5, y-5), "T", fill='black')
        
        # Add dimensions
        draw.text((50, 350), "Container Diameter ≈ 14 cm", fill='black')
        draw.text((350, 350), "Ball Radius = 3.5 cm", fill='black')
        
        # Save image
        img_path = os.path.join(self.output_dir, "tennis_ball_container.png")
        img.save(img_path)
        print(f"Created image: {img_path}")
        return img_path
    
    def create_all_images(self):
        """Create all images for the questions"""
        print("Generating question images...")
        
        img1 = self.create_lunch_menu_image()
        img2 = self.create_tennis_container_image()
        
        print("All images created successfully!")
        return [img1, img2]

def main():
    """Main function to generate images"""
    generator = SimpleImageGenerator()
    generator.create_all_images()

if __name__ == "__main__":
    main() 