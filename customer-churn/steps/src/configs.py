from zenml.steps import BaseStepConfig


class StackEnsembleConfig(BaseStepConfig):
    """Configuration for Training Stacked Models"""

    first_model_name: str = "xgb"
    second_model_name: str = "cat"
    third_model_name: str = "lgb"