def string_with_arrows(text, pos_start, pos_end):
    result = ''  # Initialize an empty string to store the result

    # Calculate the starting and ending indices of the lines containing the specified positions
    idx_start = max(text.rfind('\n', 0, pos_start.idx), 0)
    idx_end = text.find('\n', idx_start + 1)
    if idx_end < 0:
        idx_end = len(text)

    # Generate each line
    line_count = pos_end.ln - pos_start.ln + 1
    for i in range(line_count):
        # Calculate line columns for each line
        line = text[idx_start:idx_end]  # Extract the line from the text
        col_start = pos_start.col if i == 0 else 0
        col_end = pos_end.col if i == line_count - 1 else len(line) - 1

        # Append the line to the result
        result += line + '\n'
        # Add spaces for column start position and arrows (^) for the specified range
        result += ' ' * col_start + '^' * (col_end - col_start)

        # Re-calculate indices to process the next line
        idx_start = idx_end
        idx_end = text.find('\n', idx_start + 1)
        if idx_end < 0:
            idx_end = len(text)

    # Replace any tab characters with empty string (remove tabs)
    return result.replace('\t', '')
