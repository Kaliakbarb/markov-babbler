# markov-babbler

An order-N Markov chain text generator. Trains on any plain-text
corpus and babbles new sentences that mimic its rhythm without ever
reproducing it verbatim.

    python cli.py corpus/proverbs.txt --order 2 --count 5

Higher `--order` values stay closer to the source phrasing; order 1
is closer to word soup, order 3+ starts reproducing long runs
verbatim once the corpus is small.
