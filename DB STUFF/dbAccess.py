import duckdb
import time

db = duckdb.connect("data.db")
print("WELCOME TO THE S-QUACK-L INTERFACE")
print("----------------------------------")
print("Input 'EXIT' to quit, or 'PRNT <table name>' to output a table.")

while True:
    query = input("Please enter the query to run: ")

    try:
        if query == "EXIT":
            break
        elif query[:4] == "PRNT":
            db.table(query[5:]).show()
        else:
            result = db.sql(query)
            if result:
                print(result)
            else:
                print("Run successfully!")
    except Exception as e:
        print(f"INVALID QUERY: {query}!\n{e}")

db.close()
print("THANK YOU FOR USING S-QUACK-L INTERFACE")
time.sleep(1.5)
