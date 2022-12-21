year_pattern = "[1-3][0-9]{3}"

months = [
    "January-March",
    "April-June",
    "July-September",
    "October-December"
]

month_pattern = '|'.join(months)
pattern = "(Q[1-3] Un-audited)"
eps_pattern_up = "[0-9][.][0-9]{2}"
eps_pattern_down = "[(][0-9][.][0-9]{2}[)]"