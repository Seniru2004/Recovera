class RecoveryService:


    def calculate_credit(
        self,
        invoice_amount: float,
        credit_percentage: float
    ):

        credit = (
            invoice_amount *
            credit_percentage /
            100
        )


        return round(
            credit,
            2
        )


    def check_eligibility(
        self,
        sla_breached: bool
    ):

        return sla_breached