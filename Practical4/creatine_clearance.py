# psudocode for calculating creatine clearance using the Cockcroft-Gault formula
# var age, weight, concentration, gender
# var clearance = (140 - age) * weight / (concentration * 72) * (0.85 if female)
def crcl(age, weight, concentration, gender):
    """
    Calculate creatine clearance using the Cockcroft-Gault formula.
    
    Parameters:
    age (int): Age of the patient in years
    weight (float): Weight of the patient in kg
    concentration (float): Serum creatinine concentration in umol/l
    gender (bool): Gender of the patient (True for 'male' or False for 'female')
    
    Returns:
    float: Calculated creatinine clearance in umol/l*min
    """ 
    clearance = (140 - age) * weight / (concentration * 72)
    if not gender:
        clearance *= 0.85
    return clearance

# main function to test the calculate_creatine_clearance function
def main():
    while True:
        try:
            age = int(input("Enter the age of the patient in years: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer for age.")
        else:
            if 0 <= age <= 100:
                break
            else:
                print("Invalid input. Please enter an age between 0 and 100.")
    
    while True:
        try:
            weight = float(input("Enter the weight of the patient in kg: "))
        except ValueError:
            print("Invalid input. Please enter a valid number for weight.")
        else:            
            if 20 <= weight <= 80:
                break
            else:
                print("Invalid input. Please enter a weight between 20 and 80 kg.")
                
    while True:
        try:
            concentration = float(input("Enter the serum creatinine concentration in umol/l: "))
        except ValueError:
            print("Invalid input. Please enter a valid number for serum creatinine concentration.")
        else:
            if 0 <= concentration <= 100:
                break
            else:
                print("Invalid input. Please enter a serum creatinine concentration between 0 and 100 umol/l.")
                
    while True:
        gender_input = input("Enter the gender of the patient ('male' or 'female'): ")
        if gender_input in ["male", "female"]:
            gender = True if gender_input == "male" else False
            break
        else:
            print("Invalid input. Please enter 'male' or 'female'.")
    clearance = round(crcl(age, weight, concentration, gender), 2)
    print(f"The calculated creatinine clearance is: {clearance} umol/l*min")
          
if __name__ == "__main__":
    main()
    