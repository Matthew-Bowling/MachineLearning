submission_value = testing_data[['PassengerId']]
submission_value['Survived'] = logistic_clf.predict(testing_data)
submission_value.to_csv('submission.csv', sep=',', encoding='utf-8')
