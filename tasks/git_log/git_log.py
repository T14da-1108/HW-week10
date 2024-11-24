from typing import TextIO


def reformat_git_log(input_stream: TextIO, output_stream: TextIO) -> None:
    """
    Reformats the git log output from the input stream and writes to the output stream.

    :param input_stream: The input stream containing git log lines.
    :param output_stream: The output stream to write the reformatted log lines.
    """
    for line in input_stream:
        # Split each line by tab character
        parts = line.strip().split("\t")

        # Extract the first 7 characters of the SHA-1 and the message
        sha1 = parts[0][:7]  # First 7 characters of SHA-1
        message = parts[-1]  # The message part

        # Adjust the message to fit within the 80 character limit
        remaining_length = 80 - len(sha1) - 1  # Subtract the length of SHA-1 and separator '.'
        dots_length = max(0, remaining_length - len(message))  # Calculate the number of '.' to add

        # Format the line and write to the output stream
        formatted_line = f"{sha1}{'.' * dots_length}{message}\n"
        output_stream.write(formatted_line)
