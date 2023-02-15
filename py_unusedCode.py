# this code can help wiht anlayzing how much of the code is unused.
import vulture

def analyze_reusability(directory):
    """
    Analyzes a microservice's codebase for potential code reuse using the Vulture library.

    Args:
        directory: A string representing the path to the microservice's code directory.

    Returns:
        A list of tuples representing the unused code found by Vulture. Each tuple contains
        a string representing the unused code and a tuple representing the line number and
        column number where the unused code was found.
    """
    v = vulture.Vulture()
    v.scan(directory)
    unused = v.unused_items()

    unused_code = []
    for item in unused:
        if not item.startswith("__") and not item.startswith("_") and not item.startswith("test_"):
            unused_code.append((item, v.lines[item]))

    return unused_code

# Example usage
unused_code = analyze_reusability('/path/to/microservice/code')
print(f"Unused code: {unused_code}")
