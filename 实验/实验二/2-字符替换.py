def replace(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    updated_content, num_replacements = content.replace('Hi', 'Hello'), content.count('Hi')
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(updated_content)
    print(f"共替换{num_replacements}个")

def main():
    input_file_path = r'./实验/实验二/input.txt'
    output_file_path = r'./实验/实验二/output.txt'
    replace(input_file_path, output_file_path)