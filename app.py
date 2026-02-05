import json
import os
import sqlite3
import re
from openai import OpenAI

def get_path(fname):
    return os.path.join(os.path.dirname(__file__), fname)

def get_api_key(path):
    with open(get_path(path)) as f:
        return json.load(f)["openaiKey"]



# set up SQL Database
print("Setting up database...")
sqliteDbPath = get_path("aidb.sqlite")
setupSqlPath = get_path("setup.sql")
setupSqlDataPath = get_path("setupData.sql")

if os.path.exists(sqliteDbPath):
    os.remove(sqliteDbPath)

con = sqlite3.connect(sqliteDbPath)
cursor = con.cursor()

with open(setupSqlPath) as f:
    setup_sql_script = f.read()

with open(setupSqlDataPath) as f:
    setup_data_script = f.read()

cursor.executescript(setup_sql_script)
cursor.executescript(setup_data_script)
print("Database Set")

def runSql(query):
    try:
        result = cursor.execute(query).fetchall()
        return result
    except Exception as e:
        return f"SQL ERROR: {e}"

api_key = get_api_key("config.json")
client = OpenAI(api_key=api_key)

with open(setupSqlPath) as f:
    SCHEMA = f.read()

def zero_shot_prompt(question):
    return f"""
You are an expert SQL generator.
Return ONLY a SQL SELECT query.

Database schema:
{SCHEMA}

Question: {question}
"""

def single_domain_prompt(question):
    return f"""
Convert natural language to SQL.

Schema:
{SCHEMA}

Examples:

Q: List all users from USA
SQL: SELECT name FROM users WHERE country='USA';

Q: Top 2 longest movies
SQL: SELECT title FROM movie ORDER BY duration_min DESC LIMIT 2;

Now answer:

Q: {question}
SQL:
"""

def cross_domain_prompt(question):
    return f"""
You translate questions into SQL.

Example from another database:

School DB:
students(id, name)
courses(id, title)
enrollments(student_id, course_id)

Q: Students in more than 2 courses
SQL: SELECT s.name
     FROM students s
     JOIN enrollments e ON s.id=e.student_id
     GROUP BY s.name
     HAVING COUNT(*)>2;

Now apply the same reasoning to THIS schema:

{SCHEMA}

Q: {question}
SQL:
"""

def clean_sql_response(text):
    # Remove markdown code fences
    text = re.sub(r"```sql", "", text, flags=re.IGNORECASE)
    text = re.sub(r"```", "", text)

    # Remove leading/trailing whitespace
    text = text.strip()

    match = re.search(r"(select .*?;)", text, re.IGNORECASE | re.DOTALL)
    if match:
        return match.group(1).strip()

    return text

def build_prompt(strategy, question):
    if strategy == "zero":
        return zero_shot_prompt(question)
    elif strategy == "single":
        return single_domain_prompt(question)
    elif strategy == "cross":
        return cross_domain_prompt(question)
    else:
        raise ValueError("Invalid strategy")

def generate_sql(question, strategy):
    prompt = build_prompt(strategy, question)

    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    sql = clean_sql_response(response.choices[0].message.content.strip()) 

    if not sql.lower().startswith("select"):
        print(f"SQL string: {sql}")
        raise Exception("Only SELECT statements allowed")

    return sql

def explain_results(question, results):
    prompt = f"""
User asked: {question}

SQL query results:
{results}

Explain this in a friendly sentence.
"""

    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    question = "Which movie has the highest average rating?"
    strategy = "single"   # change: zero | single | cross

    print(f"\nStrategy: {strategy}")
    print("Question:", question)

    sql_query = generate_sql(question, strategy)
    print("\nGenerated SQL:\n", sql_query)

    results = runSql(sql_query)
    print("\nRaw Results:", results)

    # answer = explain_results(question, results)
    # print("\nFinal Answer:\n", answer)
