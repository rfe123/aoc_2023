function is_symbol(c)
    return c in ['*', '#', '+', '$']
end

function find_numbers(row)
    return match.(r"\d+", row)
end

function read_grid_from_file(filename)
    open(filename, "r") do file
        return readlines(file)
    end
end

function sum_adjacent_symbols(grid)
    total_sum = 0

    # Loop through the grid
    for i in 1:length(grid)
        row = grid[i]
        println(row)
        numbers = find_numbers(row)

        for num_match in numbers
            num_str = string(num_match.match)
            start_idx = num_match.offsets[1]
            end_idx = num_match.offsets[2]

            has_adjacent_symbol = false

            # Check left and right in the same row
            if start_idx > 1 && is_symbol(row[start_idx - 1])
                has_adjacent_symbol = true
            elseif end_idx < length(row) && is_symbol(row[end_idx + 1])
                has_adjacent_symbol = true
            end

            # Check above and below in the grid
            for k in start_idx:end_idx
                if i > 1 && is_symbol(grid[i-1][k]) || i < length(grid) && is_symbol(grid[i+1][k])
                    has_adjacent_symbol = true
                    break
                end
            end

            # Add the number if it has adjacent symbols
            if has_adjacent_symbol
                total_sum += parse(Int, num_str)
            end
        end
    end

    return total_sum
end

# Read the grid from input.txt
grid = read_grid_from_file("input.txt")

println("Sum of numbers with adjacent symbols: ", sum_adjacent_symbols(grid))
