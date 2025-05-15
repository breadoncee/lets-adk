# AI Pilipinas Cebu Build with AI Workshop

This repository contains materials for the AI Pilipinas Cebu "Build with AI" Workshop. The workshop uses Python 3.12 and focuses on practical AI development skills.

## Workshop Setup

### Prerequisites

- Python 3.12
  - Download from [python.org](https://www.python.org/downloads/) or use your system's package manager
- Basic Python knowledge
- A text editor or IDE (VS Code recommended)

### Preparing Your Environment

1. Clone this repository
   ```
   git clone https://github.com/breadoncee/lets-adk.git
   cd lets-adk
   ```

2. Create a virtual environment
   ```
   python3.12 -m venv venv
   ```

3. Activate the virtual environment

   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```
   
   - On Windows (Command Prompt):
     ```
     venv\Scripts\activate.bat
     ```
   
   - On Windows (PowerShell):
     ```
     venv\Scripts\Activate.ps1
     ```

4. Install workshop dependencies
   ```
   pip install -r requirements.txt
   ```

### Deactivating the Virtual Environment

When you're done working on the workshop materials, you can deactivate the virtual environment:
```
deactivate
```