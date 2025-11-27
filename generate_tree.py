import os

def list_files(startpath):
    # 1. Customize your exclusion lists here
    ignore_dirs = {'venv', '__pycache__', '.git', '.idea', '.vscode', 'build', 'dist'}
    ignore_ext = {'.pyc'}

    for root, dirs, files in os.walk(startpath):
        # Modify dirs in-place to prevent walking into ignored folders
        dirs[:] = [d for d in dirs if d not in ignore_dirs]
        
        level = root.replace(startpath, '').count(os.sep)
        indent = '│   ' * (level)
        print(f'{indent}├── {os.path.basename(root)}/')
        
        subindent = '│   ' * (level + 1)
        for f in files:
            if not any(f.endswith(ext) for ext in ignore_ext):
                print(f'{subindent}├── {f}')

if __name__ == '__main__':
    list_files('.')