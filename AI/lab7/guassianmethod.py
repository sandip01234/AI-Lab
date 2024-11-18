from sklearn import preprocessing
from sklearn.naive_bayes import GaussianNB

# Original arrays
weather = ["rainy", "overcast", "sunny", "rainy", "sunny", "overcast", "rainy", "sunny", "overcast", "rainy", "sunny", "rainy", "sunny", "overcast"]
temperature = ["cool", "hot", "mild", "cool", "hot", "mild", "cool", "hot", "mild", "cool", "hot", "mild", "hot", "cool"]
humidity = ["normal", "high", "normal", "high", "normal", "high", "normal", "high", "normal", "high", "normal", "high", "normal", "high"]
wind = ["weak", "strong", "weak", "strong", "weak", "strong", "weak", "strong", "weak", "strong", "weak", "strong", "weak", "strong"]
play = ["yes", "no", "yes", "yes", "no", "yes", "no", "yes", "yes", "no", "yes", "no", "yes", "no"]

# Initialize LabelEncoder
le = preprocessing.LabelEncoder()

# Encode the arrays
we = le.fit_transform(weather)
temp = le.fit_transform(temperature)
hum = le.fit_transform(humidity)
wi = le.fit_transform(wind)
pl = le.fit_transform(play)

# Convert np.int64 to plain integers
we = we.tolist()
temp = temp.tolist()
hum = hum.tolist()
wi = wi.tolist()
pl = pl.tolist()

# Print the encoded arrays
print("Encoded Weather: ", we)
print("Encoded Temperature: ", temp)
print("Encoded Humidity: ", hum)
print("Encoded Wind: ", wi)
print("Encoded Play: ", pl)

# Combine features into a single input list (now using plain integers)
features = list(zip(we, temp, hum, wi))
print("Features (Input): ", features)

# Print actual output (play)
print("Actual Output (Play): ", pl)

# Create and train the model
model = GaussianNB()
model.fit(features, pl)

# Test the model with a sample input (optional, here just testing the model)
sample = [[2, 1, 0, 1]]  # Represents sunny, hot, normal humidity, strong wind
prediction = model.predict(sample)
print("Prediction for sample input [sunny, hot, normal, strong]:", prediction)
