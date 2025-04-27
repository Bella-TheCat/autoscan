import socket
from datetime import datetime
import subprocess

def port_scanner(target, port_range):
    print(f"Starting scan on {target}")
    print(f"Scanning ports: {port_range[0]} to {port_range[1]}\n")
    print(f"""\n
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣦⣶⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣯⠀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⡠⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣯⠉⠉⠛⠻⠿⠿⢿⣿⣿⣦⡑⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠹⠛⣿⣿⡿⢿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠈⠙⢿⣿⣦⡀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠶⠂
⠀⠀⠀⠀⠀⠀⠀⣰⣿⣯⢞⡴⠋⠀⣸⣿⣿⡇⠸⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣆⠀⢀⣀⣠⣶⣿⡤⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣼⣿⡷⢡⠞⠀⠀⠀⢹⣿⣿⠇⠀⠈⢿⣿⣷⣄⣄⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣷⣿⡿⠟⠋⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣸⣿⣿⣰⠋⠀⠀⠀⠀⢰⣿⣿⠀⠀⠀⠘⣿⣿⣿⣿⣆⠀⠀⠀⢀⣠⣴⣿⣿⣿⣿⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢰⡟⣾⣿⠇⠀⠀⠀⠀⠀⣾⣿⡿⠀⠀⠀⠀⠘⣿⣿⣿⣿⣀⣤⣾⣿⡿⠟⠉⠁⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣿⣃⣿⡟⠀⠀⠀⠀⠀⠀⣿⣿⣿⠀⠀⠀⠀⢀⣘⣿⣿⣿⣿⣿⠿⠉⠀⠀⠀⠀⢹⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣿⣿⡿⠃⠀⠀⠀⠀⠀⢠⣿⣿⡿⠀⢠⣴⣿⣿⣿⣿⡿⣿⣿⣿⡀⠀⠀⠀⠀⠀⢸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣿⣿⡇⠀⣧⠀⠀⠀⠀⣸⣿⣿⣧⣶⣿⣿⡿⠟⠋⠁⠀⠘⣿⣿⣿⡄⠀⠀⠀⠀⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢹⡏⣿⠸⣿⡄⠀⣀⣴⣿⣿⣿⡿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣥⣶⠀⢠⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠘⣿⣽⣶⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡿⣿⣿⣧⣾⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣼⣿⣿⣿⣿⣿⠛⢉⣿⣿⡿⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣷⣼⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠈⠙⣟⣹⡿⠋⠁⠈⠻⣯⡿⣿⣿⣿⣿⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⣿⣿⠟⢿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠘⠉⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣷⣦⣤⣀⣀⣀⣤⣴⣶⣿⣿⣿⡿⠟⠁⠀⠀⠉⠻⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣶⣬⣙⣛⡛⠛⠿⠿⠿⣿⣿⣿⡿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⠛⢄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⡿⠀⠈⠉⠉⠉⠙⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠘⠛⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡟⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠸⠇⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
    start_time = datetime.now()

    open_services = []  # this is the list that holds the open services (WE LOVE)

    try:
        for port in range(port_range[0], port_range[1] + 1):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.5)
            result = s.connect_ex((target, port))

            if result == 0:
                try:
                    service = socket.getservbyport(port)
                except OSError:
                    service = "unknown service"
                print(f"Port {port}: OPEN - Service: {service}")
                open_services.append(service)  # adds service to the list! (we love that guy so much)
            s.close()
    except KeyboardInterrupt:
        print("\nscan interrupted.")
    except socket.error:
        print(f"error connecting to {target}.")
    
    end_time = datetime.now()
    print(f"\nScan completed in: {end_time - start_time}")
    return open_services  # Return the list of open services (we love lists)

def metasploit_search_by_service(services):
    try:
        for service in services:
            print(f"\nSearching exploits for service: {service}\n")
            command = f"msfconsole -q -x 'search {service} type:exploit; exit'"
            result = subprocess.run(command, shell=True, text=True, capture_output=True)

            output = result.stdout.splitlines()
            excellent_exploits = []  # Collect exploits
            for line in output:
                if "excellent" in line.lower() and "yes" in line.lower():
                    excellent_exploits.append(line.strip())

            print(f"\nFound excellent exploits: {excellent_exploits}\n")

    except Exception as e:
        print(f"Failed to do Metasploit search: {e}")

# Input info
if __name__ == "__main__":
    target_ip = input("Enter target IP: ")
    start_port = int(input("Enter start port (min, 1): "))
    end_port = int(input("Enter end port (max, 65535): "))
    metasploitrun = input("Would you like to run a vulnerability search, Y or N?: ")
    
    if metasploitrun.lower() in ["y", "yes"]:
        print("\nMetasploit running")

        # Perform port scanning and collect services
        services = port_scanner(target_ip, (start_port, end_port))
        if services:
            metasploit_search_by_service(services)
        else:
            print("No open ports or services detected. Skipping Metasploit search.")

    elif metasploitrun.lower() in ["n", "no"]:
        print("\nNot using metasploit")
        port_scanner(target_ip, (start_port, end_port))
    else:
        print("\nhow hard is it to hit a simple Y or N???\nI made it so you can even say yes or no if you wanna be a jerk!\n")