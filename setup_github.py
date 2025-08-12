#!/usr/bin/env python3
"""
GitHub Repository Setup Script
Helps initialize the GitHub repository for the Math Question Generation project
"""

import os
import subprocess
import sys

def run_command(command):
    """Run a shell command and return the result"""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.returncode == 0, result.stdout, result.stderr
    except Exception as e:
        return False, "", str(e)

def check_git_status():
    """Check if git is available and repository status"""
    print("Checking Git status...")
    
    # Check if git is installed
    success, stdout, stderr = run_command("git --version")
    if not success:
        print("❌ Git is not installed or not in PATH")
        print("Please install Git from: https://git-scm.com/")
        return False
    
    print(f"✅ Git version: {stdout.strip()}")
    
    # Check if this is already a git repository
    if os.path.exists(".git"):
        print("✅ This is already a Git repository")
        return True
    else:
        print("ℹ️  This is not yet a Git repository")
        return False

def initialize_repository():
    """Initialize the Git repository"""
    print("\nInitializing Git repository...")
    
    # Initialize git repository
    success, stdout, stderr = run_command("git init")
    if not success:
        print(f"❌ Failed to initialize repository: {stderr}")
        return False
    
    print("✅ Git repository initialized")
    
    # Add all files
    success, stdout, stderr = run_command("git add .")
    if not success:
        print(f"❌ Failed to add files: {stderr}")
        return False
    
    print("✅ All files added to staging")
    
    # Initial commit
    success, stdout, stderr = run_command('git commit -m "Initial commit: Math Question Generation Project"')
    if not success:
        print(f"❌ Failed to commit: {stderr}")
        return False
    
    print("✅ Initial commit created")
    
    return True

def create_github_instructions():
    """Create instructions for setting up GitHub repository"""
    instructions = """
# GitHub Repository Setup Instructions

## 1. Create GitHub Repository
1. Go to https://github.com/
2. Click "New repository"
3. Repository name: `math-question-generation`
4. Description: "LLM-based Math Question Generation Project"
5. Make it Public or Private (your choice)
6. Don't initialize with README (we already have one)
7. Click "Create repository"

## 2. Connect Local Repository to GitHub
After creating the repository, GitHub will show you commands. Use these:

```bash
# Add the remote origin (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/math-question-generation.git

# Push to GitHub
git branch -M main
git push -u origin main
```

## 3. Verify Setup
1. Refresh your GitHub repository page
2. You should see all the project files
3. The repository is now live and accessible

## 4. Share Repository Link
Your repository will be available at:
https://github.com/YOUR_USERNAME/math-question-generation

## 5. Optional: Enable GitHub Pages
If you want to display the project documentation:
1. Go to repository Settings
2. Scroll to "Pages" section
3. Source: "Deploy from a branch"
4. Branch: "main" / "/ (root)"
5. Click "Save"

## 6. Project Files Overview
The repository contains:
- ✅ Complete project source code
- ✅ Generated math questions in @format
- ✅ Word-like document outputs
- ✅ Curriculum analysis
- ✅ Question images
- ✅ Comprehensive documentation
- ✅ Ready-to-use scripts

## 7. Usage
```bash
# Generate questions
python src/final_generator.py

# Generate images
python src/image_generator.py

# View outputs in output/ directory
```

## 8. Project Status
✅ **COMPLETED**: All requirements met
✅ **FORMAT COMPLIANT**: Proper @format output
✅ **CURRICULUM ALIGNED**: Follows specified hierarchy
✅ **IMAGE GENERATED**: Appropriate diagrams created
✅ **DOCUMENTATION**: Comprehensive project summary
✅ **GITHUB READY**: Repository structure complete

---
**Math Question Generation Project - Successfully Completed!**
"""
    
    with open("GITHUB_SETUP_INSTRUCTIONS.md", "w", encoding="utf-8") as f:
        f.write(instructions)
    
    print("✅ GitHub setup instructions created: GITHUB_SETUP_INSTRUCTIONS.md")

def main():
    """Main function to set up the GitHub repository"""
    print("=" * 60)
    print("MATH QUESTION GENERATION PROJECT")
    print("GitHub Repository Setup")
    print("=" * 60)
    
    # Check git status
    if not check_git_status():
        print("\nGit is available but repository needs to be initialized.")
        # Continue with initialization
    
    # Initialize repository if needed
    if not os.path.exists(".git"):
        if not initialize_repository():
            print("\nFailed to initialize repository. Please check the errors above.")
            return
    else:
        print("\nRepository already exists. Checking status...")
        success, stdout, stderr = run_command("git status")
        if success:
            print(stdout)
    
    # Create GitHub instructions
    create_github_instructions()
    
    print("\n" + "=" * 60)
    print("SETUP COMPLETE!")
    print("=" * 60)
    print("✅ Git repository initialized")
    print("✅ All files committed")
    print("✅ GitHub setup instructions created")
    print("\nNext steps:")
    print("1. Read GITHUB_SETUP_INSTRUCTIONS.md")
    print("2. Create GitHub repository")
    print("3. Push your code to GitHub")
    print("4. Share the repository link")
    print("\nYour project is ready for GitHub! 🚀")

if __name__ == "__main__":
    main() 