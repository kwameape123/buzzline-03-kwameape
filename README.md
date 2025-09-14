# buzzline-03-case

Streaming data does not have to be simple text.
Many of us are familiar with streaming video content and audio (e.g. music) files.

Streaming data can be structured (e.g. csv files) or
semi-structured (e.g. json data).

We'll work with two different types of data, and so we'll use two different Kafka topic names.
See [.env](.env).

- **Producers** publish streaming data to topics
- **Consumers** subscribe to topics to process data in real-time

## Task 1 Fork and Clone Project

1. Forked <https://github.com/denisecase/buzzline-02-case> into my GitHub account and created my own version of this project to run and experiment with.
2. Named my new project `buzzline-03-arnold.`


## Task 2 Manage Local Project Virtual Environment

Open your project in VS Code and use the commands for your operating system to:

1. Create a Python virtual environment
    ```python -3.11 -m ven .venv```
2. Activate the virtual environment
        ```.venv\Scripts\Activate```
3. Upgrade pip
    ```python -m pip install --upgrade pip```
    ```py -m pip install --upgrade pip wheel setuptools```
4. Install from requirements.txt
    ```python -m pip install -r requirements.txt```

## Task 3  Start Kafka (using WSL if Windows)

In P2, you downloaded, installed, configured a local Kafka service.
Before starting, run a short prep script to ensure Kafka has a persistent data directory and meta.properties set up. This step works on WSL, macOS, and Linux - be sure you have the $ prompt and you are in the root project folder.

1. Make sure the script is executable.
2. Run the shell script to set up Kafka.
3. Cd (change directory) to the kafka directory.
4. Start the Kafka server in the foreground.
5. Keep this terminal open - Kafka will run here
6. Watch for "started (kafka.server.KafkaServer)" message

```bash
chmod +x scripts/prepare_kafka.sh
scripts/prepare_kafka.sh
cd ~/kafka
bin/kafka-server-start.sh config/kraft/server.properties
```

**Keep this terminal open!** Kafka is running and needs to stay active.
---

### Note: Kafka topic name can be found in .evn file. Rainfall and Sales are the json and csv data respectively used for this project and can be loacted in the data folder.

## Task 4 Start a Kafka JSON Producer

This producer generates streaming JSON data for our topic.

In VS Code, open a terminal.
Use the commands below to activate .venv (if not active), and start the producer.

Windows:

```shell
.venv\Scripts\activate
py -m producers.json_producer_arnold
```



## Task 4. Start a Kafka JSON Consumer

This consumer processes streaming JSON data.

In VS Code, open a NEW terminal in your root project folder.
Use the commands below to activate .venv, and start the consumer.

Windows:

```shell
.venv\Scripts\activate
py -m consumers.json_consumer_arnold
```
---

## Task 5. Start a Kafka CSV Producer

Follow a similar process to start the csv producer.
You will need to:

1. Open a new terminal (yes another)!
2. Activate your .venv.
3. Know the command that works on your machine to execute python (e.g. py or python3).
4. Know how to use the -m (module flag to run your file as a module).
5. Know the full name of the module you want to run. Hint: Look in the producers folder.

Hint: Windows:

```shell
.venv\Scripts\activate
py -m producers.csv_producer_arnold
```

## Task 6. Start a Kafka CSV Consumer

Follow a similar process to start the csv consumer.
You will need to:

1. Open a new terminal (yes another)!
2. Activate your .venv.
3. Know the command that works on your machine to execute python (e.g. py or python3).
4. Know how to use the -m (module flag to run your file as a module).
5. Know the full name of the module you want to run. Hint: Look in the consumers folder.



Hint: Windows:

```shell
.venv\Scripts\activate
py -m consumers.csv_consumer_arnold
```

---

## How To Stop a Continuous Process

To kill the terminal, hit CTRL c (hold both CTRL key and c key down at the same time).

## About Data

JSON DATA
This dataset contains detailed records of average yearly rainfall for certain countries.

CSV DATA
This dataset contains detailed records of coffee sales from a vending machine.
The vending machine is the work of a dataset author who is committed to providing an open dataset to the community.



## Later Work Sessions

When resuming work on this project:

1. Open the project repository folder in VS Code. 
2. Start the Kafka service (use WSL if Windows) and keep the terminal running. 
3. Activate your local project virtual environment (.venv) in your OS-specific terminal.
4. Run `git pull` to get any changes made from the remote repo (on GitHub).

## After Making Useful Changes

1. Git add everything to source control (`git add .`)
2. Git commit with a -m message.
3. Git push to origin main.

```shell
git add .
git commit -m "your message in quotes"
git push -u origin main
```

## Save Space

To save disk space, you can delete the .venv folder when not actively working on this project.
You can always recreate it, activate it, and reinstall the necessary packages later.
Managing Python virtual environments is a valuable skill.

## License

This project is licensed under the MIT License as an example project.
You are encouraged to fork, copy, explore, and modify the code as you like.
See the [LICENSE](LICENSE.txt) file for more.
