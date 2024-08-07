import subprocess

def verbose_ping(dest_addr, timeout=2, count=4):
    command = f"ping -c {count} -W {timeout} {dest_addr}"
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    
    if process.returncode == 0:
        return f"Ping to {dest_addr} successful: {output.decode('utf-8')}"
    else:
        return f"Ping to {dest_addr} failed: {error.decode('utf-8')}"

# Example usage:
result = verbose_ping("www.example.com", timeout=3, count=5)
print(result)
