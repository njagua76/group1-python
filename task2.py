'''
Create a program whose major task is to calculate an individual’s Net Salary by getting the inputs basic salary and benefits. Calculate the payee (i.e. Tax), NHIFDeductions, NSSFDeductions, gross salary, and net salary.

NB: Use KRA, NHIF, and NSSF values provided in the link below.
https://www.aren.co.ke/payroll/taxrates.htm
https://www.kra.go.ke/en/individual/calculate-tax/calculating-tax/paye

'''

# Calculates Net Salary based on KRA PAYE, SHIF, NSSF, and Housing Levy rates

def calculate_payee_tax(taxable_income):
    """
    Calculate PAYE (Pay As You Earn) tax based on 2025 KRA tax bands.
    Progressive tax rates are applied step by step.
    After calculating tax, personal relief (Ksh 2,400 per month) is deducted.
    """
    tax = 0
    
    if taxable_income <= 24000:
        tax = taxable_income * 0.10
    elif taxable_income <= 32333:
        tax = (24000 * 0.10) + (taxable_income - 24000) * 0.25
    elif taxable_income <= 500000:
        tax = (24000 * 0.10) + (8333 * 0.25) + (taxable_income - 32333) * 0.30
    elif taxable_income <= 800000:
        tax = (24000 * 0.10) + (8333 * 0.25) + (467667 * 0.30) + (taxable_income - 500000) * 0.325
    else:
        tax = (24000 * 0.10) + (8333 * 0.25) + (467667 * 0.30) + (300000 * 0.325) + (taxable_income - 800000) * 0.35

    # Subtract personal relief
    tax -= 2400
    return max(tax, 0)  


def calculate_shif_deduction(gross_salary):
    """
    SHIF (Social Health Insurance Fund) deduction.
    As of Oct 2024, all employees contribute 2.75% of gross salary.
    """
    return gross_salary * 0.0275


def calculate_nssf_deduction(gross_salary):
    """
    NSSF (National Social Security Fund) deduction under Tier I and II (2025 rules).
    - Tier I: 6% of income up to Ksh 8,000
    - Tier II: 6% of income between Ksh 8,001 and Ksh 72,000
    """
    tier1_limit = 8000
    tier2_limit = 72000
    rate = 0.06  # 6% contribution

    # Tier I contribution
    tier1 = min(gross_salary, tier1_limit) * rate

    # Tier II contribution (if salary > tier1_limit)
    tier2 = 0
    if gross_salary > tier1_limit:
        tier2 = min(gross_salary - tier1_limit, tier2_limit - tier1_limit) * rate

    return tier1 + tier2


def calculate_housing_levy(gross_salary):
    """
    Housing Levy contribution by employee.
    - Introduced in 2023, reintroduced in 2024.
    - Employee pays 1.5% of gross salary (fully tax deductible).
    """
    return gross_salary * 0.015


def calculate_salary():
    """
    Main function to calculate net salary under 2025 Kenyan laws.
    Steps:
    1. Input basic salary + benefits.
    2. Compute gross salary.
    3. Deduct NSSF, SHIF, and Housing Levy (all tax deductible).
    4. Apply PAYE tax on the remaining taxable income.
    5. Compute net salary = Gross - (NSSF + SHIF + Housing + PAYE).
    """
    # Get input from user
    basic_salary = float(input("Enter basic salary: "))
    benefits = float(input("Enter benefits: "))
    gross_salary = basic_salary + benefits

    # Step 1: Statutory deductions (all tax deductible)
    nssf = calculate_nssf_deduction(gross_salary)
    shif = calculate_shif_deduction(gross_salary)
    housing = calculate_housing_levy(gross_salary)

    # Step 2: Calculate taxable income
    taxable_income = gross_salary - (nssf + shif + housing)

    # Step 3: Calculate PAYE tax
    paye = calculate_payee_tax(taxable_income)

    # Step 4: Calculate total deductions and net salary
    total_deductions = nssf + shif + housing + paye
    net_salary = gross_salary - total_deductions

    # Step 5: Display results
    print("\n--- SALARY BREAKDOWN (2025) ---")
    print(f"Basic Salary: {basic_salary:,.2f}")
    print(f"Benefits: {benefits:,.2f}")
    print(f"Gross Salary: {gross_salary:,.2f}")
    print(f"NSSF Deduction: {nssf:,.2f}")
    print(f"SHIF Deduction: {shif:,.2f}")
    print(f"Housing Levy: {housing:,.2f}")
    print(f"Taxable Income: {taxable_income:,.2f}")
    print(f"PAYE Tax (after relief): {paye:,.2f}")
    print(f"Total Deductions: {total_deductions:,.2f}")
    print(f"Net Salary: {net_salary:,.2f}")


# Run program when file is executed
calculate_salary()