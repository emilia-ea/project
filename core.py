from hexagrams import text_dict, yin, yang

def get_trigram(remainder: int) -> str:
    mapping = {
        1: f"{yang}\n{yang}\n{yang}",
        2: f"{yin}\n{yang}\n{yang}",
        3: f"{yang}\n{yin}\n{yang}",
        4: f"{yin}\n{yin}\n{yang}",
        5: f"{yang}\n{yang}\n{yin}",
        6: f"{yin}\n{yang}\n{yin}",
        7: f"{yang}\n{yin}\n{yin}",
        0: f"{yin}\n{yin}\n{yin}",
        8: f"{yin}\n{yin}\n{yin}",  # fallback
    }
    return mapping.get(remainder % 8)

def get_changed_lines(original: str, change_index: int) -> str:
    if change_index == 0:
        return original
    lines = original.strip().splitlines()
    idx = len(lines) - change_index
    if lines[idx] == yin:
        lines[idx] = yang
    elif lines[idx] == yang:
        lines[idx] = yin
    return "\n".join(lines) + "\n"

def get_hexagram_result(lines: str) -> str:
    key = lines.strip()
    return text_dict.get(key, "No corresponding text.")
