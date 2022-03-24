import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split


class DataCleaning:
    def __init__(self, data) -> None:
        self.df = data

    def preprocess_data(self) -> None:
        self.df = self.df.drop(
            [
                "order_approved_at",
                "order_delivered_carrier_date",
                "order_delivered_customer_date",
                "order_estimated_delivery_date",
                "order_purchase_timestamp",
            ],
            axis=1,
        )
        self.df["product_weight_g"].fillna(
            self.df["product_weight_g"].median(), inplace=True
        )
        self.df["product_length_cm"].fillna(
            self.df["product_length_cm"].median(), inplace=True
        )
        self.df["product_height_cm"].fillna(
            self.df["product_height_cm"].median(), inplace=True
        )
        self.df["product_width_cm"].fillna(
            self.df["product_width_cm"].median(), inplace=True
        )
        # write "No review" in review_comment_message column
        self.df["review_comment_message"].fillna("No review", inplace=True)

        self.df = self.df.select_dtypes(include=[np.number])
        cols_to_drop = [
            "customer_zip_code_prefix",
            "order_item_id",
        ]
        self.df = self.df.drop(cols_to_drop, axis=1)

        return self.df

    def divide_data(self, df: pd.DataFrame) -> pd.DataFrame:
        X = df.drop("review_score", axis=1)
        y = df["review_score"]
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        return X_train, X_test, y_train, y_test

