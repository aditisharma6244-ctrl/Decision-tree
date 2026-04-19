class DecisionTree:
    def __init__(self):
        self.tree = None

    def fit(self, X, y):
        self.tree = self.build_tree(X, y)

    def build_tree(self, X, y):
        # If all outputs are same → return that value
        if len(set(y)) == 1:
            return y[0]
        feature_index = 0  
        values = set([row[feature_index] for row in X])
        tree = {}

        for value in values:
            X_sub = []
            y_sub = []

            for i in range(len(X)):
                if X[i][feature_index] == value:
                    X_sub.append(X[i][1:])  # remove used feature
                    y_sub.append(y[i])
            tree[value] = self.build_tree(X_sub, y_sub)
        return tree
    def predict(self, X):
        results = []
        for row in X:
            results.append(self.predict_row(row, self.tree))
        return results

    def predict_row(self, row, tree):
        if not isinstance(tree, dict):
            return tree

        feature_value = row[0]
        if feature_value in tree:
            return self.predict_row(row[1:], tree[feature_value])
        else:
            return None

X = [
    ['Sunny', 'Hot'],
    ['Rainy', 'Mild'],
    ['Sunny', 'Cool'],
    ['Rainy', 'Cool']
]

y = ['No', 'Yes', 'Yes', 'No']

model = DecisionTree()
model.fit(X, y)

test = [['Sunny', 'Cool']]
print("Prediction:", model.predict(test))
