class SLAService:


    def check_breach(
        self,
        guaranteed_uptime: float,
        actual_uptime: float
    ):

        breach = actual_uptime < guaranteed_uptime


        difference = (
            guaranteed_uptime - actual_uptime
        )


        return {
            "breach": breach,
            "uptime_difference": round(
                difference,
                2
            )
        }