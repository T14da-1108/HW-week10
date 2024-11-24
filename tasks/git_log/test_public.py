import io

from .git_log import reformat_git_log


###################
# Structure asserts
###################


###################
# Tests
###################


def test_reformat_git_log() -> None:
    input_data = (
        "0cd8619f18d8ecad1e5d2303f95ed206c2d6f92b\tFri Sep 23 10:59:32 2016 -0700\t"
        "Brett Cannon\tbrettcannon@users.noreply.github.com\tUpdate PEP 512 (#107)\n"
        "94dbee096b92f10ab83bbcf88102c6acdc3d76d1\tThu Sep 22 12:39:58 2016 +0100\t"
        "Thomas Kluyver\ttakowl@gmail.com\tUpdate PEP 517 to use pyproject.toml from PEP 518 (#51)\n"
    )

    input_stream = io.StringIO(input_data)
    output_stream = io.StringIO()

    reformat_git_log(input_stream, output_stream)

    expected_output = (
        "0cd8619....................................................Update PEP 512 (#107)\n"
        "94dbee0..................Update PEP 517 to use pyproject.toml from PEP 518 (#51)\n"
    )
    output_stream.seek(0)

    assert output_stream.read() == expected_output


def test_reformat_git_log_basic() -> None:
    input_data = "abcdef123456\t2022-03-01\tJohn Doe\tjohn@example.com\tInitial commit\n"
    expected_output = "abcdef1........................................................Initial commit\n"

    input_stream = io.StringIO(input_data)
    output_stream = io.StringIO()

    reformat_git_log(input_stream, output_stream)

    output_stream.seek(0)
    actual_output = output_stream.read()

    assert actual_output == expected_output


def test_reformat_git_log_short_message() -> None:
    input_data = "abcdef123456\t2022-03-01\tJohn Doe\tjohn@example.com\tHi\n"
    expected_output = "abcdef1...........................................................................Hi\n"

    input_stream = io.StringIO(input_data)
    output_stream = io.StringIO()

    reformat_git_log(input_stream, output_stream)

    output_stream.seek(0)
    actual_output = output_stream.read()

    assert actual_output == expected_output


def test_reformat_git_log_long_message() -> None:
    long_message = "This is a very long commit message that takes up a lot of space"
    input_data = f"abcdef123456\t2022-03-01\tJohn Doe\tjohn@example.com\t{long_message}\n"
    expected_output = f"abcdef1........................{long_message[:49]}\n"

    input_stream = io.StringIO(input_data)
    output_stream = io.StringIO()

    reformat_git_log(input_stream, output_stream)

    output_stream.seek(0)
    actual_output = output_stream.read()

    assert actual_output == expected_output[:80]  # Ensure message truncates at 80 characters


def test_reformat_git_log_multiple_entries() -> None:
    input_data = (
        "abcdef123456\t2022-03-01\tJohn Doe\tjohn@example.com\tInitial commit\n"
        "123456abcdef\t2022-03-02\tJane Doe\tjane@example.com\tSecond commit\n"
    )
    expected_output = (
        "abcdef1........................................................Initial commit\n"
        "123456a........................................................Second commit\n"
    )

    input_stream = io.StringIO(input_data)
    output_stream = io.StringIO()

    reformat_git_log(input_stream, output_stream)

    output_stream.seek(0)
    actual_output = output_stream.read()

    assert actual_output == expected_output


def test_reformat_git_log_edge_case_empty_message() -> None:
    input_data = "abcdef123456\t2022-03-01\tJohn Doe\tjohn@example.com\t\n"
    expected_output = "abcdef1...........................................................................\n"

    input_stream = io.StringIO(input_data)
    output_stream = io.StringIO()

    reformat_git_log(input_stream, output_stream)

    output_stream.seek(0)
    actual_output = output_stream.read()

    assert actual_output == expected_output


def test_input_stream_unchanged() -> None:
    input_data = "abcdef123456\t2022-03-01\tJohn Doe\tjohn@example.com\tInitial commit\n"

    input_stream = io.StringIO(input_data)
    output_stream = io.StringIO()

    reformat_git_log(input_stream, output_stream)

    input_stream.seek(0)

    assert input_stream.read() == input_data


def test_reformat_git_log_() -> None:
    input_data = (
        "0cd8619f18d8ecad1e5d2303f95ed206c2d6f92b\tFri Sep 23 10:59:32 2016 -0700\tBrett Cannon\t"
        "brettcannon@users.noreply.github.com\tUpdate PEP 512 (#107)\n"
        "94dbee096b92f10ab83bbcf88102c6acdc3d76d1\tThu Sep 22 12:39:58 2016 +0100\tThomas Kluyver\t"
        "takowl@gmail.com\tUpdate PEP 517 to use pyproject.toml from PEP 518 (#51)"
    )

    expected_output = (
        "0cd8619....................................................Update PEP 512 (#107)\n"
        "94dbee0..................Update PEP 517 to use pyproject.toml from PEP 518 (#51)\n"
    )

    input_stream = io.StringIO(input_data)
    output_stream = io.StringIO()

    reformat_git_log(input_stream, output_stream)

    assert output_stream.getvalue() == expected_output
