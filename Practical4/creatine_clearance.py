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
    age = int(input("Enter the age of the patient in years: "))
    weight = float(input("Enter the weight of the patient in kg: "))
    concentration = float(input("Enter the serum creatinine concentration in umol/l: "))
    gender_input = input("Enter the gender of the patient ('male' or 'female'): ")
    gender = True if gender_input == "male" else False
    clearance = crcl(age, weight, concentration, gender)
    print(f"The calculated creatinine clearance is: {clearance} umol/l*min")
          
if __name__ == "__main__":
    main()
    