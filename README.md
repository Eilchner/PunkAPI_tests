# PunkAPI_tests

`test_ebc_srm` checks if the EBC value is correct based on the SRM value. Converting SRM to EBC requires the SRM value to be multiplied by 1.97 or 2 (2 is more common since it's easier to calculate). Because of this discrepancy the test checks if EBC is between SRM * 1.97 and SRM * 2

`test_date` checks if the First Brew date is after the date we use in the API param ("brewed_after"), after verifying that it's saved in the correct format - MM/YYYY
