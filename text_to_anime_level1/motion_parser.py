# motion_parser.py

def get_motion_from_text(prompt):
    """
    This function analyzes the input text (prompt)
    and returns the correct motion video file name
    based on keywords like 'walk', 'run', or 'wave'.
    """

    # Map motion keywords to video files
    motion_map = {
        "walk": "walk.mp4",
        "run": "run.mp4",
        "wave": "wave.mp4"
    }

    # Check if any motion keyword is in the prompt
    for key, clip in motion_map.items():
        if key in prompt.lower():
            return clip

    # Default animation if no motion keyword is found
    return "idle.mp4"


# Test the function
if __name__ == "__main__":
    prompt = input("Enter what the character should do: ")
    motion_file = get_motion_from_text(prompt)
    print(f"🎬 Selected motion file: {motion_file}")
