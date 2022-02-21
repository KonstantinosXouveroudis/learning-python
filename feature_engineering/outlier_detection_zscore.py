import pandas as pd


if __name__ == '__main__':
    df = pd.read_csv("data\\weight-height.csv")
    df['Z-Score'] = (df['Height'] - df['Height'].mean()) / df['Height'].std()

    print(df.sample(5))

    outliers = df[(df['Z-Score'] < -3) | (df['Z-Score'] > 3)]
    print("\nOutliers:\n", outliers)

    print("\nShape with outliers: ", df.shape)
    df = df[(df['Z-Score'] > -3) & (df['Z-Score'] < 3)]
    print("Shape without outliers: ", df.shape)

