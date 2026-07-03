from typing import List

from pydantic import BaseModel


class ProductComparison(BaseModel):

    product: str

    strengths: List[str]

    weaknesses: List[str]


class ComparisonResult(BaseModel):

    summary: str

    winner: str

    comparison: List[ProductComparison]