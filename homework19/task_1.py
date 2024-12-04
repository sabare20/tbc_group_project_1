import json

def read_json_file(input_file):
    try:
        with open(input_file, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
        return None
    except json.JSONDecodeError:
        print(f"Error: The file '{input_file}' is not a valid JSON file.")
        return None
def calculate_avg_salary(data):
    avg_salaries = {}

    for dept_key, dept_data in data.items():
        employees = dept_data.get('employees', [])
        total_salary = 0
        valid_salaries_count = 0

        for employee in employees:
            try:
                salary = float(employee.get("salary", 0))
                total_salary += salary
                valid_salaries_count += 1
            except ValueError:
                print(f"Warning: Invalid salary for {employee.get('name')} in {dept_data['name']}")

        avg_salary = total_salary / valid_salaries_count if valid_salaries_count > 0 else 0
        avg_salaries[dept_data["name"]] = f"{avg_salary:.2f}"  

    return avg_salaries

def write_json_file(output_file, data):
    try:
        with open(output_file, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Average salaries have been written to '{output_file}'.")
    except IOError:
        print(f"Error: Could not write to file '{output_file}'.")

def main():
    input_file = 'homework19/data.json'
    output_file = 'homework19/avg_salary.json'

    data = read_json_file(input_file)
    if data is None:
        return

    avg_salaries = calculate_avg_salary(data)
    if avg_salaries:
        print("Average salaries per department:")
        for department, avg_salary in avg_salaries.items():
            print(f"{department}: {avg_salary}")

        write_json_file(output_file, avg_salaries)

if __name__ == "__main__":
    main()