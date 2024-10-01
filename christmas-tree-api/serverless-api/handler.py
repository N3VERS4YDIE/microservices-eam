import json


def tree(event, context):
    query_params = event.get("queryStringParameters") or {}
    n = query_params.get("n", 10)

    try:
        n = int(n)
    except ValueError:
        return {
            "statusCode": 400,
            "body": json.dumps(
                {"message": "Invalid input. Please provide a valid integer."}
            ),
        }

    return christmas_tree(n)


def christmas_tree(n):
    char = "■"
    base_height = int(n * 0.2)
    tree_height = n - base_height
    base_width_radius = int(tree_height * 0.2)

    result = ""

    for i in range(tree_height):
        spaces = " " * (tree_height - i - 1)
        asterisks = char * (2 * i + 1)
        result += spaces + asterisks + "\n"

    for _ in range(base_height):
        spaces = " " * (tree_height - base_width_radius - 1)
        asterisks = char * (2 * base_width_radius + 1)
        result += spaces + asterisks + "\n"

    return result
