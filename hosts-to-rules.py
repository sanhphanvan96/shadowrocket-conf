# download the file from https://raw.githubusercontent.com/bigdargon/hostsVN/master/hosts
input_file = 'hosts.txt'
output_file = 'hosts-for-shadowrocket.txt'

# Open the input file and read lines
with open(input_file, 'r') as file:
    lines = file.readlines()

# Open the output file to write the converted rules
with open(output_file, 'w', encoding='utf-8') as file:
    warning_count = 0
    valid_count = 0
    
    for idx, line in enumerate(lines, 1):
        # Strip any leading/trailing whitespace
        line = line.strip()
        
        # Skip empty lines or lines that don't start with '0.0.0.0'
        if not line or not line.startswith('0.0.0.0'):
            continue

        # Split by whitespace
        parts = line.split()
        if len(parts) != 2:
            print(f"[WARNING] Line {idx}: Invalid format (expected 2 parts, got {len(parts)}): {line}")
            warning_count += 1
            continue
        
        ip, domain = parts
        
        if ip != '0.0.0.0':
            print(f"[WARNING] Line {idx}: IP not 0.0.0.0: {line}")
            warning_count += 1
            continue
        
        # Write the converted rule to the output file
        # file.write(f'DOMAIN-SUFFIX,{domain},REJECT\n')
        file.write(f'DOMAIN-SUFFIX,{domain}\n')
        valid_count += 1

print(f'\nConversion complete. Check the {output_file} file for the results.')
print(f'   Valid rules written: {valid_count}')
print(f'   Warnings: {warning_count}')
