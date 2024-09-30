# download the file from https://raw.githubusercontent.com/bigdargon/hostsVN/master/option/hosts-iOS
input_file = 'hosts.txt'
output_file = 'hosts-for-shadowrocket.txt'

# Open the input file and read lines
with open(input_file, 'r') as file:
    lines = file.readlines()

# Open the output file to write the converted rules
with open(output_file, 'w') as file:
    for line in lines:
        # Strip any leading/trailing whitespace
        line = line.strip()
        # Skip empty lines or lines that don't start with '0'
        if not line or not line.startswith('0'):
            continue
        # Extract the domain part
        domain = line.split(' ')[1]
        # Write the converted rule to the output file
        # file.write(f'DOMAIN-SUFFIX,{domain},REJECT\n')
        file.write(f'DOMAIN-SUFFIX,{domain}\n')

print(f'Conversion complete. Check the {output_file} file for the results.')
