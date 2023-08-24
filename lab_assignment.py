class FlightTable:
    def __init__(self):
        self.matches = [
            {"Location": "Mumbai", "Team 01": "India", "Team 02": "Sri Lanka", "Timing": "DAY"},
            {"Location": "Delhi", "Team 01": "England", "Team 02": "Australia", "Timing": "DAY-NIGHT"},
            {"Location": "Chennai", "Team 01": "India", "Team 02": "South Africa", "Timing": "DAY"},
            {"Location": "Indore", "Team 01": "England", "Team 02": "Sri Lanka", "Timing": "DAY-NIGHT"},
            {"Location": "Mohali", "Team 01": "Australia", "Team 02": "South Africa", "Timing": "DAY-NIGHT"},
            {"Location": "Delhi", "Team 01": "India", "Team 02": "Australia", "Timing": "DAY"}
        ]

    def search_by_team(self, team_name):
        return [match for match in self.matches if team_name in (match["Team 01"], match["Team 02"])]

    def search_by_location(self, location):
        return [match for match in self.matches if match["Location"] == location]

    def search_by_timing(self, timing):
        return [match for match in self.matches if match["Timing"] == timing]


def main():
    table = FlightTable()

    while True:
        print("Search Options:")
        print("1. List of all the matches of a Team")
        print("2. List of Matches on a Location")
        print("3. List of Matches based on timing")
        print("4. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            team_name = input("Enter team name: ")
            matches = table.search_by_team(team_name)
        elif choice == 2:
            location = input("Enter location: ")
            matches = table.search_by_location(location)
        elif choice == 3:
            timing = input("Enter timing: ")
            matches = table.search_by_timing(timing)
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please choose again.")
            continue
        
        print("Search Results:")
        for match in matches:
            print(f"Location: {match['Location']}, Team 01: {match['Team 01']}, Team 02: {match['Team 02']}, Timing: {match['Timing']}")

if __name__ == "__main__":
    main()
