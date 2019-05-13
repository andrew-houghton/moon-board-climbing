import pickle

test_data, score_data = pickle.load(open("scores.pickle", "rb"))
correct = 0
for i in range(len(test_data)):
    if test_data[i] == score_data[i]:
        correct += 1

print(f"Graded {correct} correctly out of {len(test_data)}")
