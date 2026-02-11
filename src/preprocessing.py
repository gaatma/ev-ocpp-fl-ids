import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

def load_data(train_path, test_path):
    train_df = pd.read_csv(train_path)
    test_df = pd.read_csv(test_path)
    return train_df, test_df


def preprocess(train_df, test_df):
    # Drop non-feature columns
    X_train = train_df.drop(columns=["label", "flow_id", "src_ip", "dst_ip"])
    y_train = train_df["label"]

    X_test = test_df.drop(columns=["label", "flow_id", "src_ip", "dst_ip"])
    y_test = test_df["label"]

    # Encode labels
    le = LabelEncoder()
    y_train_encoded = le.fit_transform(y_train)
    y_test_encoded = le.transform(y_test)

    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled, X_test_scaled, y_train_encoded, y_test_encoded