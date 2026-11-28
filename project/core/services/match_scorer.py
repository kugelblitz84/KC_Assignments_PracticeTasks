from project.core.services.text_tokenizer import tokenize_text

def calculate_match_score(text1, text2):
    tokens1 = tokenize_text(text1)
    tokens2 = tokenize_text(text2)

    if not tokens1 or not tokens2:
        return 0.0

    common_tokens = tokens1.intersection(tokens2)
    total_tokens = len(tokens1.union(tokens2))

    match_score = len(common_tokens) / total_tokens
    return match_score