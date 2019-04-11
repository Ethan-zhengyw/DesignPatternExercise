from company import ConcreteCompany, HRDepartment, FinanceDepartment


def main():
    head_company = ConcreteCompany("Head Company")
    head_company_hr = HRDepartment("Head Company HR Department")
    head_company_finance = FinanceDepartment("Head Company Finance Department")
    head_company.add_department(head_company_hr)
    head_company.add_department(head_company_finance)

    first_level_company = ConcreteCompany("First-Level Company")
    flc_hr = HRDepartment("First-Level Company HR Department")
    flc_finance = FinanceDepartment("First-Level Company Finance Department")
    first_level_company.add_department(flc_hr)
    first_level_company.add_department(flc_finance)

    second_level_company_1 = ConcreteCompany("Second-Level Company 1")
    slc1_hr = HRDepartment("Second-Level Company 1 HR Department")
    slc1_finance = FinanceDepartment("Second-Level Company 1 Finance Department")
    second_level_company_1.add_department(slc1_hr)
    second_level_company_1.add_department(slc1_finance)

    second_level_company_2 = ConcreteCompany("Second-Level Company 2")
    slc2_hr = HRDepartment("Second-Level Company 2 HR Department")
    slc2_finance = FinanceDepartment("Second-Level Company 2 Finance Department")
    second_level_company_2.add_department(slc2_hr)
    second_level_company_2.add_department(slc2_finance)

    first_level_company.add_department(second_level_company_1)
    first_level_company.add_department(second_level_company_2)
    head_company.add_department(first_level_company)

    head_company.display_structure(1)
    head_company.do_duty()


main()
