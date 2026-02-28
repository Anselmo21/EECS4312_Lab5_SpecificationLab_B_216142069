# Student Name:
# Student ID:

"""
Stub file for the is allocation feasible exercise.

Implement the function `is_allocation_feasible` to determine whether a set of resource requests can be satisfied
given limited capacities.

Assumptions (reasonable/consistent format):
- `resources` maps resource names to non-negative numeric capacities.
- Each request is a dict mapping resource names to numeric required amounts.
- Requests are interpreted as *simultaneous* (i.e., total demand per resource is the sum across all requests).
- Any resource not present in `resources` has capacity 0 (so any positive request for it makes allocation infeasible).
"""

from typing import Dict, List, Union

Number = Union[int, float]


def is_allocation_feasible(
    resources: Dict[str, Number],
    requests: List[Dict[str, Number]]
) -> bool:
    """
    Determine whether a set of resource requests can be satisfied given limited capacities.

    Args:
        resources : Dict[str, Number], Mapping from resource name to total available capacity.
        requests : List[Dict[str, Number]], List of requests. Each request is a mapping
                   from resource name to the amount required.

    Returns:
        True if the allocation is feasible, False otherwise.
    """
    # Basic validation: capacities must be numeric and non-negative
    for rname, cap in resources.items():
        if not isinstance(cap, (int, float)):
            return False
        if cap < 0:
            return False

    # Aggregate total demand per resource across all requests
    total_demand: Dict[str, float] = {}

    for req in requests:
        if not isinstance(req, dict):
            return False

        for rname, amount in req.items():
            if not isinstance(amount, (int, float)):
                return False

            # Negative demand doesn't make sense in this context; treat as invalid / infeasible
            if amount < 0:
                return False

            total_demand[rname] = total_demand.get(rname, 0.0) + float(amount)

    # Check feasibility: demand must not exceed capacity for any resource
    for rname, demand in total_demand.items():
        cap = resources.get(rname, 0.0)  # missing resource => 0 capacity
        if demand > float(cap):
            return False

    return True
