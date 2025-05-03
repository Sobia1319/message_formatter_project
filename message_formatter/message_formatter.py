def tech_border_decorator(func):
    """
    A decorator that adds a tech-themed border around the message.
    Surrounds the message with computer/tech symbols.
    """
    def wrapper(*args, **kwargs):
        message = func(*args, **kwargs)
        
        # Calculate border length based on the message
        border_length = len(message) + 4
        
        # Create the decorated message with borders
        decorated_message = (
            "╔" + "═" * border_length + "╗\n"
            "║  " + message + "  ║\n"
            "╚" + "═" * border_length + "╝"
        )
        return decorated_message
    return wrapper


def emoji_highlight_decorator(func):
    """
    A decorator that adds tech/coding-related emojis before and after the message.
    """
    def wrapper(*args, **kwargs):
        message = func(*args, **kwargs)
        
        # Tech-related emojis
        emojis = "🚀 💻 🔧 "
        
        # Add emojis to the beginning and end of the message
        decorated_message = f"{emojis}{message}{emojis[::-1]}"
        return decorated_message
    return wrapper
