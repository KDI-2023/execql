from neo4j import GraphDatabase

from config import *

class HelloWorldExample:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def print_greeting(self, message: str):
        with self.driver.session() as session:
            greeting = session.execute_write(self._create_and_return_greeting, message)
            if message.startswith('CREATE') and 'Artwork' in message:
                print(message[32: -3])

    @staticmethod
    def _create_and_return_greeting(tx, message):
        result = tx.run(
            message
        )
        return result.single()


if __name__ == "__main__":
    greeter = HelloWorldExample(URI, NAME, PWD)

    # greeter.driver.verify_connectivity()
    greeter.print_greeting('MATCH (n)-[r]->() DELETE r')
    greeter.print_greeting('MATCH (n) DELETE n')

    with open('jlutag.cql', 'rb') as f:
        for line in f.read().decode('utf8').split('\n\n')[:-1]:
            greeter.print_greeting(line)

    print('end')

    greeter.close()

# MATCH (n)-[r]->() DELETE r
# MATCH (n) DELETE n
