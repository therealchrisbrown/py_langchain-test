# Langchain vs GPT: Realtime Data Testing

## Overview

Working with GPT-4 (or previous models) often poses challenges in obtaining real-time data. While solutions like GPT-Builder or OpenAI Functions can address this issue, there's an additional complexity—OpenAI's opacity in revealing its parameters, restricting users from peering into the engine room.

This project explores a potential solution: leveraging Langchain. By combining Langchain with CometML for comprehensive monitoring, you can not only address the real-time data challenge but also gain insights into the underlying thought processes of the system.

## Key Features

- **Realtime Data Access:** Langchain facilitates the acquisition of real-time data, addressing a common limitation in working with GPT models.
  
- **Transparency and Monitoring:** CometML is employed to monitor each step, providing users with a clear understanding of the system's decision-making process.

- **Notebook Example:** The accompanying notebook demonstrates a straightforward implementation of the presented solution, showcasing how Langchain and CometML can be effectively utilized.

## Getting Started

To get started with this project, follow these steps:

1. Install requirements.txt
2. Set up all APIs in a .env file
3. Set up CometML for comprehensive logging.
4. Explore the provided notebook for a practical example.

## Used Packages

1. **Langchain:** The core package for addressing real-time data challenges.
2. **OpenAI:** Used in conjunction with Langchain for natural language processing.
3. **SERPAPI:** Integrated for additional functionalities related to Search Engine Results Pages (https://serpapi.com).
4. **CometML:** Employed for detailed logging and monitoring.

## Credits

Special thanks to Santiago on X for the idea.

## License

This project is licensed under the [MIT License](LICENSE), allowing for open collaboration and modification.
