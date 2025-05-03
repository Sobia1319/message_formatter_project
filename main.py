import sys


from message_formatter.message_formatter import tech_border_decorator, emoji_highlight_decorator

# Simple function that returns a message
def simple_message(text):
    return text

# Apply the first decorator
@tech_border_decorator
def boxed_message(text):
    return text

# Apply the second decorator
@emoji_highlight_decorator
def emoji_message(text):
    return text

# Apply both decorators (stacked)
@emoji_highlight_decorator
@tech_border_decorator
def fancy_message(text):
    return text

# Demonstrate various message formatting
if __name__ == "__main__":
    message = "Hello, welcome to my message formatter!"
    
    print("Original message:")
    print(simple_message(message))
    print("\nWith tech border:")
    print(boxed_message(message))
    print("\nWith emoji highlights:")
    print(emoji_message(message))
    print("\nWith both decorators:")
    print(fancy_message(message))