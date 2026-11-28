import re
def tokenize_text(text):
    
    STOP_WORDS: set[str] = {
        "a", "an", "the",
        "i", "me", "my", "mine", "myself",
        "we", "us", "our", "ours", "ourselves",
        "you", "your", "yours", "yourself",
        "he", "him", "his", "himself",
        "she", "her", "hers", "herself",
        "it", "its", "itself",
        "they", "them", "their", "theirs",
        "this", "that", "these", "those",
        "is", "am", "are", "was", "were",
        "be", "been", "being",
        "have", "has", "had", "having",
        "do", "does", "did", "doing",
        "can", "could", "would", "should",
        "will", "shall", "may", "might",
        "what", "which", "who", "whom",
        "how", "where", "when", "why",
        "and", "or", "but", "if", "then",
        "in", "on", "at", "to", "from",
        "for", "of", "by", "with", "as",
        "about", "into", "through", "during",
        "before", "after", "above", "below",
        "between", "under", "over",
        "there", "here", "some", "any",
        "all", "each", "every", "both",
        "such", "very", "just", "also",
        "please", "tell"
    }

    words = re.findall(r'\b\w+\b', text.lower())
    
    return set(words) - STOP_WORDS