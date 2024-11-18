def loan_eligibility(age, stable_income, credit_score, criminal_record, defaulted_on_loan):
    if 18 <= age <= 65 and stable_income:
        return "Eligible for a loan."
    elif credit_score > 700:
        return "Eligible for a loan."
    elif criminal_record:
        return "Not eligible for a loan."
    elif defaulted_on_loan:
        return "Not eligible for a loan."
    else:
        return "Eligibility cannot be determined."

# User input
age = int(input("Enter the applicant's age: "))
stable_income = input("Does the applicant have a stable income? (yes/no): ").lower() == "yes"
credit_score = int(input("Enter the applicant's credit score: "))
criminal_record = input("Does the applicant have a criminal record? (yes/no): ").lower() == "yes"
defaulted_on_loan = input("Has the applicant defaulted on a loan before? (yes/no): ").lower() == "yes"

# Output
print(loan_eligibility(age, stable_income, credit_score, criminal_record, defaulted_on_loan))
