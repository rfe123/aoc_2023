package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
)

func isSymbol(c byte) bool {
	symbols := "*#+$"
	for i := 0; i < len(symbols); i++ {
		if c == symbols[i] {
			return true
		}
	}
	return false
}

func findNumbers(row string) []string {
	re := regexp.MustCompile(`\d+`)
	return re.FindAllString(row, -1)
}

func readGridFromFile(filename string) ([]string, error) {
	file, err := os.Open(filename)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	var grid []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		grid = append(grid, scanner.Text())
	}

	if err := scanner.Err(); err != nil {
		return nil, err
	}
	return grid, nil
}

func main() {
	// Read the grid from input.txt
	grid, err := readGridFromFile("input.txt")
	if err != nil {
		fmt.Println("Error reading file:", err)
		return
	}

	totalSum := 0

	// Loop through the grid
	for i, row := range grid {
		numbers := findNumbers(row)
		for _, numStr := range numbers {
			startIdx := 0
			endIdx := len(numStr)

			hasAdjacentSymbol := false
			// Check left and right in the same row
			if startIdx > 0 && isSymbol(row[startIdx-1]) {
				hasAdjacentSymbol = true
			} else if endIdx < len(row) && isSymbol(row[endIdx]) {
				hasAdjacentSymbol = true
			}

			// Check above and below in the grid
			for k := startIdx; k < endIdx; k++ {
				if i > 0 && isSymbol(grid[i-1][k]) || i < len(grid)-1 && isSymbol(grid[i+1][k]) {
					hasAdjacentSymbol = true
					break
				}
			}

			// Add the number if it has adjacent symbols
			if hasAdjacentSymbol {
				num, _ := strconv.Atoi(numStr)
				totalSum += num
			}
		}
	}

	fmt.Println("Sum of numbers with adjacent symbols:", totalSum)
}
