"""
This is a boilerplate pipeline
generated using Kedro 0.18.2
"""

import logging
from typing import Any, Dict, Tuple



def split_data(
     parameters: Dict[str, Any]
) :
    """Splits data into features and target training and test sets.

    Args:
        data: Data containing features and target.
        parameters: Parameters defined in parameters.yml.
    Returns:
        Split data.
    """

    print(parameters)

    return (1,2,3,4)

