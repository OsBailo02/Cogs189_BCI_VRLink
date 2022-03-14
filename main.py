from sklearn.linear_model import LinearRegression
import pandas as pd


class BCILinearRegressor():

    def __init__(self, focus_csv_path="./focus.csv", not_focus_csv_path="./not_focus.csv"):
        self.linear_regression = LinearRegression()
        self.focus_csv_path = focus_csv_path
        self.not_focus_csv_path = not_focus_csv_path
        self.train_linear_regressor()



    def train_linear_regressor(self):
        X = []
        Y = []
        #Read in CSV data for "focused" mental state [1]
        df = pd.read_csv(self.focus_csv_path)
        for value in df['raw_value']:
            X.append(value)
            Y.append(1)

        #Read in CSV data for "not focused" mental state [-1]
        df = pd.read_csv(self.not_focus_csv_path)
        for value in df['raw_value']:
            X.append(value)
            Y.append(-1)

        self.linear_regressor.fit(X, Y)

    def get_prediction(self, val):
        self.linear_regression.predict(val)

if __name__ == '__main__':
    bci = BCILinearRegressor()
    bci.train_linear_regressor()
    # time.sleep(10)
    # pyautogui.press('p')
