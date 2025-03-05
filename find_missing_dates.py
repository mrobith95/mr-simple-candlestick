from datetime import datetime, timedelta

def find_missing_dates(date_list):
    # Convert string dates to datetime objects if needed
    date_list = [datetime.strptime(date, "%Y-%m-%d") for date in date_list]
    
    # Generate full date range between min and max date
    full_date_range = set(date_list[0] + timedelta(days=i) for i in range((date_list[-1] - date_list[0]).days + 1))
    
    # Find missing dates
    missing_dates = sorted(full_date_range - set(date_list))
    
    # Convert back to string format if needed
    return [date.strftime("%Y-%m-%d") for date in missing_dates]

### Example usage
##dates = ["2025-02-10", "2025-02-11", "2025-02-12", "2025-02-14", "2025-02-18"]
##missing = find_missing_dates(dates)
##print("Missing Dates:", missing)
## should return
## Missing Dates: ['2025-02-13', '2025-02-15', '2025-02-16', '2025-02-17']
