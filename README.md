# FASTAPI Profile API

A simple FastAPI application that returns user information along with a random cat fact from [catfact.ninja](https://catfact.ninja/). It exposes a single GET endpoint at `/me` that returns:

- Your profile (name, email, stack)
- A random cat fact from the Cat Facts API
- A dynamic UTC timestamp

## Set Up

1. Clone the repository

```bash
git clone https://github.com/your-username/fastapi-profile-api.git
cd fastapi-profile-api
```

2. Create a virtual environment and activate it

```bash
python3 -m venv env
source env/bin/activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Run the FastAPI app

```bash
fastapi dev app.py
```

5. Open your browser visit and visit [http://127.0.0.1:8000/me]

## Response Format

```json
{
  "status": "success",
  "user": {
    "email": "mohamedcali@gmail.com",
    "name": "Mohamed Ali",
    "stack": "Python/FastAPI"
  },
  "timestamp": "2025-10-18T12:34:56.789Z",
  "fact": "Cats sleep for 70% of their lives."
}
```

## License

This project is licensed under the [MIT License](LICENSE).

You are free to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of this software, under the conditions of the MIT License.
