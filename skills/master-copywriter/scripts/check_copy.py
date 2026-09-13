#!/usr/bin/env python3
"""
check_copy.py - reading level and AI-tell audit for a draft.

Usage:
    python3 scripts/check_copy.py draft.txt
    cat draft.txt | python3 scripts/check_copy.py

Reports Flesch-Kincaid grade level and Flesch Reading Ease, then flags the
specific sentences and words that are pushing the grade up, plus the phrases
that make copy read as machine-written.

Fix what it flags. Do not chase the number for its own sake; a sentence that
scores 6.2 but sells is better than a sentence that scores 4.0 and does not.
"""

import re
import sys

VOWELS = "aeiouy"

# Phrases that read as AI-generated or as empty marketing filler.
BANNED = [
    "delve", "in today's fast-paced", "in today's world", "landscape",
    "it's not just", "it's not merely", "isn't just about", "more than just",
    "unlock", "unleash", "elevate", "empower", "harness the power",
    "game-changer", "game changer", "revolutionize", "revolutionary",
    "seamless", "seamlessly", "robust", "leverage", "utilize", "utilizing",
    "facilitate", "streamline", "optimize", "innovative", "cutting-edge",
    "state-of-the-art", "best-in-class", "world-class", "industry-leading",
    "holistic", "synergy", "paradigm", "ecosystem", "solution provider",
    "at the end of the day", "needless to say", "it's worth noting",
    "let's dive in", "dive deep", "deep dive", "navigate the",
    "embark on", "journey", "tapestry", "testament to", "realm of",
    "transformative", "unparalleled", "unprecedented", "meticulous",
    "curated", "bespoke", "elevate your", "take it to the next level",
    "in conclusion", "furthermore", "moreover", "additionally",
    "whether you're a", "look no further", "the perfect blend",
    "supercharge", "turbocharge", "next-level", "top-notch",
]

# Long words with short, better replacements.
SWAPS = {
    "utilize": "use", "utilise": "use", "facilitate": "help",
    "purchase": "buy", "additional": "more", "approximately": "about",
    "assistance": "help", "commence": "start", "demonstrate": "show",
    "endeavor": "try", "implement": "do", "individual": "person",
    "initiate": "start", "numerous": "many", "obtain": "get",
    "opportunity": "chance", "participate": "join", "previously": "before",
    "prior to": "before", "regarding": "about", "require": "need",
    "sufficient": "enough", "terminate": "end", "therefore": "so",
    "however": "but", "currently": "now", "immediately": "now",
    "receive": "get", "provide": "give", "attempt": "try",
    "consequently": "so", "subsequently": "then", "necessitate": "need",
    "component": "part", "objective": "goal", "methodology": "method",
    "significant": "big", "substantial": "big", "beneficial": "good",
    "optimal": "best", "accelerate": "speed up", "eliminate": "get rid of",
}


def syllables(word):
    word = word.lower().strip(".,!?;:'\"()[]")
    if not word:
        return 0
    count = 0
    prev_vowel = False
    for ch in word:
        is_vowel = ch in VOWELS
        if is_vowel and not prev_vowel:
            count += 1
        prev_vowel = is_vowel
    if word.endswith("e") and count > 1 and not word.endswith(("le", "ee")):
        count -= 1
    return max(count, 1)


def sentences(text):
    text = re.sub(r"\s+", " ", text)
    parts = re.split(r"(?<=[.!?])\s+|\n+", text)
    return [p.strip() for p in parts if p.strip() and re.search(r"[A-Za-z]", p)]


def words(text):
    return re.findall(r"[A-Za-z']+", text)


def main():
    if len(sys.argv) > 1:
        text = open(sys.argv[1], encoding="utf-8").read()
    else:
        text = sys.stdin.read()

    sents = sentences(text)
    wds = words(text)
    if not sents or not wds:
        print("Nothing to score.")
        return

    syl = sum(syllables(w) for w in wds)
    wps = len(wds) / len(sents)
    spw = syl / len(wds)

    fk = 0.39 * wps + 11.8 * spw - 15.59
    ease = 206.835 - 1.015 * wps - 84.6 * spw

    print("=" * 62)
    print(f"  Words {len(wds)}   Sentences {len(sents)}   Avg {wps:.1f} words/sentence")
    print(f"  Flesch-Kincaid grade level : {fk:.1f}")
    print(f"  Flesch Reading Ease        : {ease:.0f}  (aim 80+)")
    if fk <= 5.0:
        print("  VERDICT: at or under 5th grade. Good.")
    elif fk <= 6.5:
        print("  VERDICT: close. Cut the long sentences flagged below.")
    else:
        print("  VERDICT: too high. Break sentences, swap long words.")
    print("=" * 62)

    long_sents = [(len(words(s)), s) for s in sents if len(words(s)) > 20]
    if long_sents:
        print(f"\nLONG SENTENCES ({len(long_sents)}) - break each into two or three:")
        for n, s in sorted(long_sents, reverse=True)[:15]:
            print(f"  [{n}w] {s[:150]}")

    big = sorted({w.lower() for w in wds if syllables(w) >= 4 and len(w) > 7})
    if big:
        print(f"\nFOUR-SYLLABLE WORDS ({len(big)}) - replace with plain ones:")
        print("  " + ", ".join(big[:40]))

    low = text.lower()
    hits = [p for p in BANNED if p in low]
    if hits:
        print(f"\nAI TELLS AND BUZZWORDS ({len(hits)}) - delete or rewrite:")
        for p in hits:
            print(f"  \"{p}\"")

    swap_hits = [(k, v) for k, v in SWAPS.items() if re.search(rf"\b{k}\b", low)]
    if swap_hits:
        print(f"\nEASY SWAPS ({len(swap_hits)}):")
        for k, v in swap_hits:
            print(f"  {k} -> {v}")

    em = text.count("—") + text.count(" - ") + text.count("--")
    if em:
        print(f"\nDASHES: {em} found. Use a period, a comma, or a colon instead.")

    bangs = text.count("!")
    if bangs > 1:
        print(f"\nEXCLAMATION MARKS: {bangs}. They read as hype and lower response.")

    passive = re.findall(
        r"\b(?:is|are|was|were|be|been|being)\s+\w+(?:ed|en)\b", low)
    if passive:
        print(f"\nPOSSIBLE PASSIVE VOICE ({len(passive)}): "
              + ", ".join(sorted(set(passive))[:12]))

    print()


if __name__ == "__main__":
    main()
