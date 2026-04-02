import pandas as pd

def create_callback(model, widgets, remarks_pane, confidence_pane):

    def get_index(widget):
        return widget.options.index(widget.value) if widget.value is not None else None

    def callback(event):
        data = pd.DataFrame([{
            "Account.Balance": get_index(widgets["account_balance"]),
            "Duration.of.Credit..month.": get_index(widgets["duration_of_credit_month"]),
            "Payment.Status.of.Previous.Credit": get_index(widgets["payment_status_of_previous_credit"]),
            "Purpose": get_index(widgets["purpose"]),

            # numeric
            "Credit.Amount": widgets["credit_amount"].value,

            "Value.Savings.Stocks": get_index(widgets["value_savings_stocks"]),
            "Length.of.current.employment": get_index(widgets["employment_duration"]),

            # numeric
            "Instalment.per.cent": widgets["rate"].value,

            "Sex...Marital.Status": get_index(widgets["marital_status"]),
            "Guarantors": get_index(widgets["guarantors"]),
            "Duration.in.Current.address": get_index(widgets["current_address_duration"]),
            "Most.valuable.available.asset": get_index(widgets["valuable_asset"]),

            # numeric
            "Age..years.": widgets["age_years"].value,

            "Concurrent.Credits": get_index(widgets["concurrent_credits"]),
            "Type.of.apartment": get_index(widgets["apartment_type"]),

            # numeric
            "No.of.Credits.at.this.Bank": widgets["num_credits_at_bank"].value,
            "No.of.dependents": widgets["num_dependents"].value,

            "Telephone": get_index(widgets["telephone"]),
            "Foreign.Worker": get_index(widgets["foreign_worker"])
        }])

        pred = model.predict(data)[0]
        prob = model.predict_proba(data).max()

        print(pred)
        if pred == 1:
            credit_label = "Good"
            color = "green"
        else:
            credit_label = "Bad"
            color = "red"

        remarks_pane.object = (
            f"<b style='font-size:16px;'>Credit: </b>"
            f"<span style='color:{color}; font-weight:bold; font-size:16px;'>"
            f"{credit_label}</span>"
        )

        confidence_pane.object = (
            f"<b style='font-size:16px;'>Confidence: </b>"
            f"<span style='color:gray;'>{round(prob*100,2)}%</span>"
        )

    return callback