import argparse

from markov import build_model, generate


def main():
    p = argparse.ArgumentParser(description="markov chain text generator")
    p.add_argument("corpus", help="path to a plain-text corpus file")
    p.add_argument("--order", type=int, default=2)
    p.add_argument("--count", type=int, default=3)
    p.add_argument("--length", type=int, default=25, help="max tokens per line")
    args = p.parse_args()

    with open(args.corpus, encoding="utf-8") as f:
        text = f.read()
    model = build_model(text, order=args.order)

    for i in range(args.count):
        print(generate(model, order=args.order, max_tokens=args.length, seed=i))


if __name__ == "__main__":
    main()
