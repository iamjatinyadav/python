def compound_interest(principle, rate, time):
 
    # Calculates compound interest
    Amount = principle * (pow((1 + rate / 100), time))
    CI = Amount - principle
    print("Compound interest is", CI)



val=compound_interest(1200,5.4,2)

