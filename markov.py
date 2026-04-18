"""Order-N Markov chain text generator."""
import random
import re

END = "\0"


def tokenize(text):
    return re.findall(r"[\w'-]+|[.!?,;]", text, re.UNICODE)


def build_model(text, order=2):
    tokens = tokenize(text)
    model = {}
    padded = [END] * order + tokens + [END]
    for i in range(len(padded) - order):
        key = tuple(padded[i:i + order])
        nxt = padded[i + order]
        model.setdefault(key, []).append(nxt)
    return model


def generate(model, order=2, max_tokens=40, seed=None):
    rng = random.Random(seed)
    state = (END,) * order
    out = []
    for _ in range(max_tokens):
        choices = model.get(state)
        if not choices:
            state = (END,) * order
            choices = model.get(state)
            if not choices:
                break
        nxt = rng.choice(choices)
        if nxt == END:
            if out:
                break
            state = (END,) * order
            continue
        out.append(nxt)
        state = (*state[1:], nxt)
    return detokenize(out)


def detokenize(tokens):
    text = ""
    for tok in tokens:
        if tok in ".,!?;" and text:
            text = text.rstrip() + tok + " "
        else:
            text += tok + " "
    return text.strip().capitalize()
