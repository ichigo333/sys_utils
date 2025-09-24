import subprocess

def stop_linux_service(service_name: str):
    try:
        subprocess.run(["sudo", "systemctl", "stop", service_name],check=True)
        print(f"Service '{service_name}' stopped successfully systemctl")
    except subprocess.CalledProcessError as e:
            print(f"Error stopping service '{service_name}' using 'systemctl': {e}")
    

def start_linux_service(service_name: str):
    try:
        subprocess.run(["sudo", "systemctl", "start", service_name],check=True)
        print(f"Service '{service_name}' started successfully systemctl")
    except subprocess.CalledProcessError as e:
            print(f"Error starting service '{service_name}' using 'systemctl': {e}")

stop_linux_service("apt-daily.timer")
start_linux_service("apt-daily.timer")