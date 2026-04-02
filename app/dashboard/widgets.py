import panel as pn

def create_widgets():
    return {
        "account_balance": pn.widgets.Select(
            name="Account Balance",
            options=[
                'No running account',
                'No balance or debit',
                'Balance between 0 and less than 200 DM',
                'Balance greater than or equal to 200 DM or account active for at least 1 year'
            ]
        ),

        "duration_of_credit_month": pn.widgets.Select(
            name="Duration of Credit (months)",
            options=[
                'More than 54 months',
                'Between 49 and 54 months',
                'Between 43 and 48 months',
                'Between 37 and 42 months',
                'Between 31 and 36 months',
                'Between 25 and 30 months',
                'Between 19 and 24 months',
                'Between 13 and 18 months',
                'Between 7 and 12 months',
                '6 months or less'
            ]
        ),

        "payment_status_of_previous_credit": pn.widgets.Select(
            name="Payment Status of Previous Credit",
            options=[
                'Hesitant payment history',
                'Problematic account history',
                'No previous credits',
                'Previously paid credits',
                'No payment issues'
            ]
        ),

        "purpose": pn.widgets.Select(
            name="Loan Purpose",
            options=[
                'Other',
                'New car purchase',
                'Used car purchase',
                'Furniture acquisition',
                'Electronics (radio/television)',
                'Household appliances',
                'Repairs',
                'Education',
                'Vacation',
                'Retraining',
                'Business'
            ]
        ),

        "credit_amount": pn.widgets.IntInput(name="Credit Amount"),

        "value_savings_stocks": pn.widgets.Select(
            name="Savings and Investment Value",
            options=[
                'Unknown or no savings account',
                'Less than 100 DM',
                'Between 100 and less than 500 DM',
                'Between 500 and less than 1000 DM',
                '1000 DM or more'
            ]
        ),

        "employment_duration": pn.widgets.Select(
            name="Employment Duration",
            options=[
                'Unemployed',
                'Less than 1 year',
                'Between 1 and less than 4 years',
                'Between 4 and less than 7 years',
                '7 years or more'
            ]
        ),

        "rate": pn.widgets.IntInput(name="Installment Rate (%)"),

        "marital_status": pn.widgets.Select(
            name="Marital Status",
            options=[
                'Single (Male)',
                'Married (Male)',
                'Divorced (Male)',
                'Single (Female)',
                'Married (Female)'
            ]
        ),

        "guarantors": pn.widgets.Select(
            name="Guarantor Type",
            options=[
                'None',
                'Co-applicant',
                'Guarantor'
            ]
        ),

        "current_address_duration": pn.widgets.Select(
            name="Duration at Current Address",
            options=[
                'Less than 1 year',
                'Between 1 and less than 4 years',
                'Between 4 and less than 7 years',
                '7 years or more'
            ]
        ),

        "valuable_asset": pn.widgets.Select(
            name="Most Valuable Asset",
            options=[
                'Real estate',
                'Life insurance or savings agreement',
                'Vehicle or other assets',
                'No valuable assets'
            ]
        ),

        "age_years": pn.widgets.IntInput(name="Age (years)"),

        "concurrent_credits": pn.widgets.Select(
            name="Concurrent Credit Facilities",
            options=[
                'None',
                'Bank',
                'Retail stores'
            ]
        ),

        "apartment_type": pn.widgets.Select(
            name="Type of Residence",
            options=[
                'Rented',
                'Owned',
                'Provided free of charge'
            ]
        ),

        "num_credits_at_bank": pn.widgets.IntInput(
            name="Number of Existing Credits at this Bank"
        ),

        "num_dependents": pn.widgets.IntInput(
            name="Number of Dependents"
        ),

        "telephone": pn.widgets.Select(
            name="Telephone Availability",
            options=[
                'No',
                'Yes'
            ]
        ),

        "foreign_worker": pn.widgets.Select(
            name="Foreign Worker Status",
            options=[
                'Yes',
                'No'
            ]
        ),

        "submit": pn.widgets.Button(
            name="Analyze",
            button_type="primary"
        )
    }