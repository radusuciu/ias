from collections import namedtuple
from typing import List
import statistics

RatioList = List[float]

Filter = namedtuple('Filter', ['fn', 'requires'])

def is_quantified(ratio: float) -> bool:
    return ratio > 0

def is_not_half_tryptic(full_sequence: str) -> bool:
    return full_sequence[0] in ['K','R','-'] and (full_sequence[-3] in ['K','R'] or full_sequence[-1] == '-')

def is_not_reverse(uniprot: str) -> bool:
    return not uniprot.startswith('Reverse_')

individual = {
    'is_quantified': Filter(is_quantified, 'ratio'),
    'is_not_half_tryptic': Filter(is_not_half_tryptic, 'sequence'),
    'is_not_reverse': Filter(is_not_reverse, 'uniprot')
}

def filter_20s(ratios: RatioList, ratio_cutoff=4) -> List[bool]:
    """Filter out erroneous seeming 20s."""
    # 20s are stripped if the following conditions are met:
    # - the set of ratios is not just composed of 0s and 20s
    # - there is only one 20
    # - the lowest non-zero, non-20 value is below a cutoff
    no_filter = [True] * len(ratios)
    if 20 not in ratios or ratios.count(20) > 1:
        return no_filter

    only_zeros_and_20s = len([x for x in ratios if x > 0 and x != 20]) == 0
    min_below_cutoff = min(ratios) < ratio_cutoff

    if not only_zeros_and_20s and min_below_cutoff:
        return [r != 20 for r in ratios]
    else:
        return no_filter

def filter_by_stdev(ratios: RatioList, stdev_cutoff=0.6, ratio_cutoff=4) -> List[bool]:
    """Filter ratios based on a standard deviation cutoff."""
    no_filter = [True] * len(ratios)
    quantified_ratios = [r for r in ratios if r > 0]

    # no-op if less than two ratios
    if len(quantified_ratios) < 2:
        return no_filter

    stdev = statistics.stdev(quantified_ratios)
    mean = statistics.mean(quantified_ratios)
    minimum = min(quantified_ratios)

    # if stdev is tight enough relative to the mean
    # or if all the ratios are above a certain threshold
    # return unchanged
    # else, set everything but the minimum to zero
    if (stdev != None and stdev / mean < stdev_cutoff) or minimum > ratio_cutoff:
        return no_filter
    else:
        return [r == minimum for r in ratios]


experiment = {
    'filter_20s': Filter(filter_20s, 'ratio'),
    'filter_by_stdev': Filter(filter_by_stdev, 'ratio')

}


experiment_group = {
    

}