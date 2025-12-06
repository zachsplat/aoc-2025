package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	data, _ := os.ReadFile(os.Args[1])
	lines := strings.Split(strings.TrimSpace(string(data)), "\n")
	rows := len(lines)
	cols := len(lines[0])

	grid := make([][]byte, rows)
	var sr, sc int
	for r, line := range lines {
		grid[r] = []byte(line)
		for c, ch := range line {
			if ch == '^' {
				sr, sc = r, c
			}
		}
	}

	// directions: up, right, down, left
	dr := []int{-1, 0, 1, 0}
	dc := []int{0, 1, 0, -1}

	simulate := func(g [][]byte) (int, bool) {
		r, c, dir := sr, sc, 0
		visited := make(map[[3]int]bool)
		cells := make(map[[2]int]bool)
		for {
			state := [3]int{r, c, dir}
			if visited[state] {
				return len(cells), true // loop
			}
			visited[state] = true
			cells[[2]int{r, c}] = true

			nr, nc := r+dr[dir], c+dc[dir]
			if nr < 0 || nr >= rows || nc < 0 || nc >= cols {
				return len(cells), false
			}
			if g[nr][nc] == '#' {
				dir = (dir + 1) % 4
			} else {
				r, c = nr, nc
			}
		}
	}

	p1, _ := simulate(grid)
	fmt.Println("p1:", p1)

	// part 2: try placing obstacle at each empty cell
	p2 := 0
	for r := 0; r < rows; r++ {
		for c := 0; c < cols; c++ {
			if grid[r][c] != '.' {
				continue
			}
			grid[r][c] = '#'
			_, looped := simulate(grid)
			if looped {
				p2++
			}
			grid[r][c] = '.'
		}
	}
	fmt.Println("p2:", p2)
}
