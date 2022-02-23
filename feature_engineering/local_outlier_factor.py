# Synthetic Dataset
from sklearn.datasets import make_classification

# Data processing
import numpy as np
import pandas as pd
from collections import Counter

# Visualization
import matplotlib.pyplot as plt

# Model and performance
from sklearn.model_selection import train_test_split
from sklearn.neighbors import LocalOutlierFactor
from sklearn.metrics import classification_report

if __name__ == '__main__':
    # Creating an imbalanced dataset
    x, y = make_classification(n_samples=100000,
                               n_features=2, n_informative=2,  # Using 2 informative features as predictors
                               n_redundant=0, n_repeated=0, n_classes=2, n_clusters_per_class=1,
                               weights=[0.995, 0.005],  # Ratio between the majority and minority classes
                               class_sep=0.5, random_state=0)

    # Convert the data we just created from a numpy array to a pandas dataframe.
    df = pd.DataFrame({'feature1': x[:, 0],
                       'feature2': x[:, 1],
                       'target': y})

    # Checking the data distribution
    distribution = df['target'].value_counts(normalize=True)
    """
    0: -> majority class %
    1: -> minority class %
    """
    print(distribution)

    # Splitting the dataset into train/test sets.
    # random_state ensures that the split will be the same in every execution. The integer value can be anything.
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=10)

    print("\nNumber of records in the training set: ", x_train.shape[0])
    print("Number of records in the testing set: ", x_test.shape[0])
    print(f"The training set has a {sorted(Counter(y_train).items())[0][1]} records for the majority class "
          f"and {sorted(Counter(y_train).items())[1][1]} records for the minority class.")

    """
    The Local Outlier Factor (LOF) algorithm can be used for outlier/anomaly detection and novelty detection.
    1) Outlier Detection includes outliers in the dataset and it fits the areas with high-density data in order to ignore
    the outliers and anomalies.
    2) Novelty Detection only includes the normal data points when training the model, then take a new dataset with
    outliers for prediction. The outliers in Novelty Detection are also called novelties.
    
    Which of the 2 to use depends on the dataset. In the case that outlier data are labeled, we can use either. But, if
    we don't we have to use Outlier Detection.
    """

    # Using sklearn's LOF.
    # Keep only the normal data for the dataset
    x_train_normal = x_train[np.where(y_train == 0)]

    # 1) Train the LOF model for Novelty Detection
    lof_novelty = LocalOutlierFactor(n_neighbors=5, novelty=True).fit(x_train_normal)

    # Predict novelties
    prediction_novelty = lof_novelty.predict(x_test)

    # Change the anomalies' values to make it consistent with the true values
    prediction_novelty = [1 if i == -1 else 0 for i in prediction_novelty]

    # Check model performance
    print("\nNovelty Detection performance:\n", classification_report(y_test, prediction_novelty))

    # -------------------------------------------------------------------------------------
    # 2) LOF model for Outlier Detection
    lof_outlier = LocalOutlierFactor(n_neighbors=5, novelty=False)

    # Predict novelties
    # We couldn't use fit_predict() with Novelty because the algorithm fits and predicts on different datasets
    prediction_outlier = lof_outlier.fit_predict(x_test)

    # Change the anomalies' values to make it consistent with the true values
    prediction_outlier = [1 if i == -1 else 0 for i in prediction_outlier]

    # Check model performance
    print("\nOutlier Detection performance:\n", classification_report(y_test, prediction_outlier))

    # -------------------------------------------------------------------------------------
    # Visualization of results
    # Put the testing set and predictions in the same dataframe.
    df_test = pd.DataFrame(x_test, columns=['feature1', 'feature2'])
    df_test['y_test'] = y_test
    df_test['prediction_novelty'] = prediction_novelty
    df_test['prediction_outlier'] = prediction_outlier

    # Visualize the actual and predicted anomalies
    fig, (ax0, ax1, ax2) = plt.subplots(1, 3, figsize=(18, 6), sharey=True)

    # Ground truth
    ax0.set_title('Original')
    ax0.scatter(df_test['feature1'], df_test['feature2'], c=df_test['y_test'], cmap='rainbow')

    # Local Outlier Factor Novelty Detection
    ax1.set_title("LOF Novelty Detection")
    ax1.scatter(df_test['feature1'], df_test['feature2'], c=df_test['prediction_novelty'], cmap='rainbow')

    # Local Outlier Factor Outlier Detection
    ax2.set_title("LOF Outlier Detection")
    ax2.scatter(df_test['feature1'], df_test['feature2'], c=df_test['prediction_outlier'], cmap='rainbow')

    plt.show()
