#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# --- CONFIGURATION ---
TOTAL_PROBLEMS=10 # Set this to the total number of problems you have

# --- PROGRESS TRACKING ---
PROGRESS_FILE=".progress"

# Check if the progress file exists. If not, create it and set progress to 1.
if [ ! -f "$PROGRESS_FILE" ]; then
    echo "1" > "$PROGRESS_FILE"
fi

current_problem=$(cat "$PROGRESS_FILE")
echo ">> Current level: Problem $current_problem"

if [ "$current_problem" -gt "$TOTAL_PROBLEMS" ]; then
    echo "Congratulations! You have solved all the problems."
    exit 0
fi

# --- FIND THE MODIFIED SOLUTION FILE ---
PROBLEM_DIR="problems/problem $current_problem"
MODIFIED_FILE=""
LANGUAGE=""

# Find the file that was changed in the last commit
LAST_COMMIT_FILES=$(git diff-tree --no-commit-id --name-only -r HEAD)

for file in $LAST_COMMIT_FILES; do
    if [[ "$file" == "$PROBLEM_DIR/solution.c" ]]; then
        MODIFIED_FILE="$PROBLEM_DIR/solution.c"
        LANGUAGE="c"
        break
    elif [[ "$file" == "$PROBLEM_DIR/solution.py" ]]; then
        MODIFIED_FILE="$PROBLEM_DIR/solution.py"
        LANGUAGE="python"
        break
    elif [[ "$file" == "$PROBLEM_DIR/solution.java" ]]; then
        MODIFIED_FILE="$PROBLEM_DIR/solution.java"
        LANGUAGE="java"
        break
    fi
done

if [ -z "$LANGUAGE" ]; then
    echo ">> No solution file for Problem $current_problem was modified. Nothing to check."
    exit 0
fi

echo ">> Detected change in: $MODIFIED_FILE"
echo ">> Validating solution using $LANGUAGE..."

# --- VALIDATION LOGIC ---
SUCCESS=false
case $LANGUAGE in
    c)
        echo ">> Compiling C code..."
        # Compile the test cases and the solution together
        gcc "$PROBLEM_DIR/test_cases.c" -o solution_executable
        echo ">> Running C tests..."
        # Run the compiled program. It will exit with 1 on failure.
        if ./solution_executable; then
            SUCCESS=true
        fi
        ;;
    python)
        echo ">> Running Python tests..."
        # Your unittest file handles everything.
        if python3 "$PROBLEM_DIR/test_cases.py"; then
            SUCCESS=true
        fi
        ;;
    java)
        echo ">> Compiling Java code..."
        # Compile both files. The -d flag places the .class files in the problem directory.
        javac -d "$PROBLEM_DIR" "$MODIFIED_FILE" "$PROBLEM_DIR/test_cases.java"
        echo ">> Running Java tests..."
        # Run the test_cases class. The -cp flag sets the classpath.
        if java -cp "$PROBLEM_DIR" test_cases; then
             SUCCESS=true
        fi
        ;;
esac

# --- UNLOCKING NEXT PROBLEM ---
if $SUCCESS; then
    echo "========================================"
    echo "✅ Problem $current_problem Solved! Correct!"
    echo "========================================"
    
    next_problem=$((current_problem + 1))
    echo "$next_problem" > "$PROGRESS_FILE"
    
    echo ">> Unlocked Problem $next_problem."
    exit 0
else
    echo "==============================================="
    echo "❌ Incorrect solution for Problem $current_problem."
    echo "==============================================="
    exit 1
fi