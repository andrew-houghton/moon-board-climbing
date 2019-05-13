def expected_diff(test_data, score_data):
    ex_sum_diff = sum([abs(test_data[i] - score_data[i]) for i in range(len(test_data))])
    print(f"Expected difference from correct grade: {ex_sum_diff/len(test_data)}")
