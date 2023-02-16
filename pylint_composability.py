import pylint.lint

def analyze_composability_quality(source_code):
    # Run pylint on the source code
    pylint_output = pylint.lint.Run(source_code, do_exit=False)

    # Extract the composability score from the pylint output
    for message in pylint_output.linter.stats['by_msg']:
        if message == 'R0801': # pylint error code for composability score
            composability_score = pylint_output.linter.stats['by_msg'][message]

    return composability_score
