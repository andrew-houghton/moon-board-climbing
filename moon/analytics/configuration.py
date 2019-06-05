from moon.models.base_model import GradingModel
from moon.types.climbset import Climbset
from moon.analytics.grade_preprocess import BasePreprocessor
from moon.analytics.metrics import Metrics
from typing import Tuple


Grade=List[bool] # Various length
Climb=List[bool] # One hot encoded, 18*11 options


@dataclass
class Configuration:
    model: GradingModel
    climbs: Climbset
    preprocessing: BasePreprocessor
    metrics: Metrics
    data_split: Tuple[Tuple[List[Climb], List[Climb]], Tuple[List[Grade], List[Grade]]]
