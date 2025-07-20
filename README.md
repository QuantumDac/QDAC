# Quantum Ledger (Python/QRL Fork)

**Local Development**

1. Clone or download the starter repo and enter directory:
   ```bash
   cd quantum-ledger
   ```
2. Create virtualenv & install dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```
3. Start node via Docker Compose:
   ```bash
   docker-compose up --build
   ```
