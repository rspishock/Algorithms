"""
The h-index is a metric that measures both the productivity and citation impact of a researcher.

Specifically, an author's h-index is the largest number h such that the researcher has published
h papers that have been cited at least h times.
"""

# paper: citations, expected h-index of 4 (b, d, h, i)  (4 papers with 4 or more citations)
papers = {'a': 1, 'b': 4, 'c': 1, 'd': 4, 'e': 2, 'f': 1, 'g': 3, 'h': 5, 'i': 6}


def h_index(papers):
    """Searches papers to find the author's h-index."""
    count = 1
    sorted_list = {k: v for k, v in sorted(papers.items(), key=lambda item: item[1])}  # sorts list by citation value

    # start counting from 1,

    print(sorted_list)  # TESTING


h_index(papers)
