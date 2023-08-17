<h1 align="center">
	🔮 Awesome AI Agents
	<p align="center">
		<a href="https://discord.gg/U7KEcGErtQ" target="_blank">
			<img src="https://img.shields.io/static/v1?label=Join&message=%20discord!&color=mediumslateblue">
		</a>
		<a href="https://twitter.com/e2b_dev" target="_blank">
			<img src="https://img.shields.io/twitter/follow/e2b.svg?logo=twitter">
		</a>
	</p>
</h1>


<img src="/assets/landscape-latest.png" width="100%" alt="Chart of AI Agents Landscape" />

Welcome to our list of AI agents.
We structured the list into two parts:
- [Open source projects](#open_hands-open-source-projects)
- [Closed-source projects and companies](#lock-closed-source-projects-and-companies)

The list is done according to our best knowledge, although definitely not comprehensive.
Discussion and feedback appreciated! :heart:

## Have anything to add?
You have something to add or improve about our list? Do it via pull request.

## Who's behind this?
This list is made by the team behind [e2b](https://github.com/e2b-dev/e2b). E2b is building AWS for AI agents. We help developers to deploy, test, and monitor AI agents. E2b is agnostic to your tech stack and aims to work with any tooling for building AI agents.

## Join the community
- Follow us on [Twitter](https://twitter.com/e2b_dev)
- [Join Twitter community](https://twitter.com/i/communities/1670204079619055616) for AI agents
- [Join our Discord](https://discord.gg/U7KEcGErtQ)
- Want to discuss anything about AI agents? [Schedule a call with us](https://calendly.com/tereza-tizkova/30min)

Feel free to reach out to us at [hello@e2b.dev](mailto:hello@e2b.dev).

# :open_hands: Open-source projects

## [AgentGPT](https://agentgpt.reworkd.ai/)
A browser-based implementation of AutoGPT, accessible via a no-code platform
<details>

### Description
- A no-code platform
- Process:
	- Assigning a goal to the agent
	- Witnessing its thinking process
	- Formulation of an execution plan
	- Taking actions accordingly
- Uses OpenAI functions
- Supports gpt-3.5-16k, pinecone and pg_vector databases
- Stack
	- Frontend: NextJS + Typescript
	- Backend: FastAPI + Python
	- DB: MySQL through docker with the option of running SQLite locally

<!--
### Features
- Uses OpenAI **functions**
- Supports gpt-3.5-16k, pinecone and pg_vector databases

### Stack
- Frontend: NextJS + Typescript
- Backend: FastAPI + Python
	- DB: MySQL through docker with the option of running SQLite locally
	-->

### Links
- [Documentation](https://docs.reworkd.ai/)
- [Website](https://agentgpt.reworkd.ai/)
- [GitHub](https://github.com/reworkd/AgentGPT)
</details>

<!-- This is a comment that appears only in the raw text -->


## [AI Legion](https://github.com/eumemic/ai-legion)
A platform for agents to work together, similar in spirit to AutoGPT and Baby AGI, but written in TypeScript
<details>


### Description
- An LLM-powered autonomous agent platform
- A framework for autonomous agents who can work together to accomplish tasks
- Interaction with agents done via console direct messages

### Links
- Author: [eumemic](https://github.com/eumemic)
- [Website](https://gpt3demo.com/apps/ai-legion)
- [GitHub](https://github.com/eumemic/ai-legion)
- [Twitter](https://twitter.com/dysmemic)
</details>

## [Aider](https://github.com/paul-gauthier/aider)

A command line tool that lets you pair your program with GPT-3.5/GPT-4, to edit code stored in your local git repository

<details>

### Description
- Aider is a command line tool that lets you pair program with GPT-3.5/GPT-4, to edit code stored in your local git repository
- You can start a new project or work with an existing repo. And you can fluidly switch back and forth between the aider chat where you ask GPT to edit the code and your own editor to make changes yourself
- Aider makes sure edits from you and GPT are committed to git with sensible commit messages. Aider is unique in that it works well with pre-existing, larger codebases

### Links  
- [Website](https://aider.chat/)
- Author: [Paul Gauthier](https://github.com/paul-gauthier) (Github)
- [Discord Invite](https://discord.com/invite/Tv2uQnR88V)

</details>

## [AutoGPT](https://agpt.co/?utm_source=awesome-ai-agents)

An experimental open-source attempt to make GPT-4 fully autonomous, with >140k stars on GitHub

<details>

### Description
- Chains together LLM "thoughts", to autonomously achieve whatever goal you set
- Internet access for searches and information gathering
- Long-term and short-term memory management
- Can execute many commands such as Google Search, browse websites, write to files, and execute Python files and much more
- GPT-4 instances for text generation
- Access to popular websites and platforms
- File storage and summarization with GPT-3.5
- Extensibility with Plugins
- "A lot like BabyAGI combined with LangChain tools"
- Features added in release 0.4.0
	- File reading
	- Commands customization
	- Enhanced testing

<!--
### Features added in release 0.4.0
- File reading
- Commands customization
- Enhanced testing
-->

### Links
- [Twitter](https://twitter.com/Auto_GPT/?utm_source=awesome-ai-agents)
- [GitHub](https://github.com/Significant-Gravitas/Auto-GPT/?utm_source=awesome-ai-agents)
- [Facebook](https://www.facebook.com/groups/1330282574368178/?utm_source=awesome-ai-agents)
- [Linkedin](https://www.linkedin.com/company/autogpt/?utm_source=awesome-ai-agents)
- [Discord](https://discord.gg/autogpt/?utm_source=awesome-ai-agents)
- Author: [Significant Gravitas](https://twitter.com/SigGravitas/?utm_source=awesome-ai-agents)
</details>



## [Automata](https://github.com/emrgnt-cmplxty/automata)
Crafting a sophisticated system that autonomously generates its own code based on the context of your project.

<details>

### Description
- Model: GPT 4
- Automata takes your project as a context, receives tasks, and executes the instructions seamlessly.
- Features
	- Automata aims to evolve into a fully autonomous, self-programming Artificial Intelligence system.
	- It's designed for seamless integration with all available agent platforms and LLM providers.
	- Utilizes the novel code search algorithm, SymbolRank, and associated tools to build superior coding intelligence.
	- Modular, fully configurable design with minimal reliance on external dependencies

### Links

- Author: [Owen Colegrove](https://twitter.com/ocolegro)
<!--

### Features
- Automata aims to evolve into a fully autonomous, self-programming Artificial Intelligence system.
- It's designed for seamless integration with all available agent platforms and LLM providers.
- Utilizes the novel code search algorithm, SymbolRank, and associated tools to build superior coding intelligence.
- Modular, fully configurable design with minimal reliance on external dependencies.

-->

</details>

## [AutoPR](https://github.com/irgolic/AutoPR)
AI-generated pull requests to fix issues, powered by ChatGPT
<details>

### Description
- Triggered by adding a label containing AutoPR to an issue, AutoPR will:
	- Plan a fix
	- Write the code
	- Push a branch
	- Open a pull request

### Links
- [Discord](https://discord.com/invite/ykk7Znt3K6)

</details>

## [Autonomous HR Chatbot](https://github.com/stepanogil/autonomous-hr-chatbot)

A prototype enterprise application - an Autonomous HR Assistant powered by GPT-3.5.

<details>

### Description
- An agent that can answer HR related queries autonomously using the tools it has on hand.
- Powered by GPT-3.5
- Current tools assigned to the agent (with more on the way):
	- Timekeeping Policy
	- Employee Data
	- Calculator

### Links
- Medium: [Creating a (mostly) Autonomous HR Assistant with ChatGPT and LangChain’s Agents and Tools](https://pub.towardsai.net/creating-a-mostly-autonomous-hr-assistant-with-chatgpt-and-langchains-agents-and-tools-1cdda0aa70ef)
- [GitHub](https://github.com/stepanogil/autonomous-hr-chatbot)
- Author: [Stephen Bonifacio](https://twitter.com/Stepanogil)
- Video Demo: [Youtube Link](https://www.youtube.com/watch?v=id7XRcEIBvg&ab_channel=StephenBonifacio)
</details>

## [BabyAGI](https://github.com/yoheinakajima/babyagi)

A simple framework for managing tasks using AI
<details>



### Description
- A pared-down version of the original [Task-Driven Autonomous Agent](https://twitter.com/yoheinakajima/status/1640934493489070080?s=20)
- Creates tasks based on the result of previous tasks and a predefined objective.
- The script then uses OpenAI's NLP capabilities to create new tasks based on the objective
- Leverages OpenAI's GPT-4, pinecone vector search, and LangChainAI framework
- Default model is OpenAI GPT3-turbo
- The system maintains a task list for managing and prioritizing tasks
- It autonomously creates new tasks based on completed results and reprioritizes the task list accordingly, showcasing the adaptability of AI-powered language models


### Links
- Paper: [Task-driven Autonomous Agent Utilizing GPT-4, Pinecone, and LangChain for Diverse Applications](https://yoheinakajima.com/task-driven-autonomous-agent-utilizing-gpt-4-pinecone-and-langchain-for-diverse-applications/)
- [Discord](https://discord.com/invite/TMUw26XUcg)
- [Founder's Twitter](https://twitter.com/yoheinakajima)
- [Twitter thread describing the system](https://twitter.com/yoheinakajima/status/1640934493489070080)


</details>


## [BabyBeeAGI](https://yoheinakajima.com/babybeeagi-task-management-and-functionality-expansion-on-top-of-babyagi/)
A task management and functionality expansion on top of BabyAGI

<details>

### Description
- A more advanced version of the original BabyAGI code
- - Improves upon the original framework, by introducing a more complex task management prompt, allowing for more comprehensive analysis and synthesis of information
- Designed to handle multiple functions within one task management prompt
- Built on top of the GPT-4 architecture, resulting in slower processing speeds and occasional errors
- Provides a framework that can be further built upon and improved, paving the way for more sophisticated AI applications
- One of the significant differences between BabyAGI and BabyBeeAGI is the complexity of the task management prompt

### Links
- [Tweet](https://twitter.com/yoheinakajima/status/1652732735344246784)
- [GitHub](https://github.com/yoheinakajima/babyagi/blob/main/classic/BabyBeeAGI.py)
- [Replit](https://replit.com/@YoheiNakajima/BabyBeeAGI?v=1)
- Author: [@yoheinakajima](https://twitter.com/yoheinakajima) (Twitter)

</details>


## [BabyCatAGI](https://replit.com/@YoheiNakajima/BabyCatAGI)
BabyCatAGI is a mod of BabyBeeAGI, which is a mod of OG BabyAGI
<details>


### Description
- Just 300 lines of code
- This was built as a continued iteration on the original BabyAGI code in a lightweight way. Differences to BabyAGI include the following:
	- Task Creation Agent runs once
	- Execution Agent loops through tasks
	- Task dependencies for pulling relevant results
	- Two tools: search tool and text completion
	- “Mini-agent” as tool
	- Search tool combines search, scrape, chunking, and extraction.
	- Results combined to create summary report


<!--
### How to use
- Fork this into a private Repl
- Add your OpenAI API Key (required) and SerpAPI Key (optional)
- Update the OBJECTIVE variable
- Press "Run" at the top.
-->

### Links
- [Tweet](https://twitter.com/yoheinakajima/status/1657448504112091136)
- [GitHub](https://github.com/yoheinakajima/babyagi/blob/main/classic/BabyCatAGI.py)
- [Replit](https://replit.com/@YoheiNakajima/BabyCatAGI)
- Author: [@yoheinakajima](https://twitter.com/yoheinakajima) (Twitter)

</details>

## [BabyDeerAGI](https://twitter.com/yoheinakajima/status/1666313838868992001)
Newest mod of BabyAGI, at ~350 lines of code
<details>

### Description
- Features
	- Parallel tasks (making it faster)
	- 3.5-turbo only (GPT-4 not required)
	- User input tool
	- Query rewrite in web search tool
	- Saves results


### Links
- [Tweet](https://twitter.com/yoheinakajima/status/1666313838868992001)
- [GitHub](https://github.com/yoheinakajima/babyagi/blob/main/classic/BabyDeerAGI.py)
- [Replit](https://replit.com/@YoheiNakajima/BabyDeerAGI)
- Author: [@yoheinakajima](https://twitter.com/yoheinakajima) (Twitter)

</details>


## [BabyCommandAGI](https://github.com/saten-private/BabyCommandAGI)

An AI agent designed to test what happens when you combine CLI and LLM, which are more traditional interfaces than GUI (created by @saten-private)

<details>

### Description
- An AI agent based on @yoheinakajima's [BabyAGI](https://github.com/yoheinakajima/babyagi) which executes shell commands
- Automatic Programming, Successfully created an app automatically just by providing feedback. The procedure can be found [here](https://twitter.com/saten_work/status/1674855573412810753).
- Automatic Environment Setup, Successfully installed a Flutter environment on Linux in a container, created the Flutter app, and launched it. The procedure can be found [here](https://twitter.com/saten_work/status/1667126272072491009).
- Aside from setting up the environment, it seems to be able to handle a bit of general tasks such as [Generating text, like poems, code, scripts, musical pieces, email, and letters, translating languages](https://anyaitools.com/babycommandagi/?utm_source=SocialAutoPoster&utm_medium=Social&utm_campaign=Twitter)
- There is a risk of breaking the environment. Please run in a virtual environment such as Docker.
- GPT-4 or higher is recommended

### Links
- [Founder's Twitter](https://twitter.com/saten_work)
- [Twitter thread describing the system](https://twitter.com/saten_work/status/1654571194111393793)

</details>


## [BambooAI](https://github.com/pgalko/BambooAI)

The BambooAI library is a user-friendly semi-autonomous AI agent designed to make data exploration and analysis more accessible to non-programmers.

<details>

### Description
- BambooAI runs in a loop (until user decides to end it).
- Allows mixing of different models with different capabilities, token costs and context windows for different tasks.
- Maintains the memory of previous conversations.
- Builds the prompts dynamically utilising relevant context from Pinecone vector DB.
- Offers a narrative or asks follow up questions if required.
- For codified responses, the task is broken down into a list of steps and a pseudo-code algorithm is built.
- Based on the algorithm, it devises the python code for dataset analysis, modeling or plotting.
- Debugs the code which then executes, auto-corrects if needs to, and displays the output to user.
- Ranks the final answers, and asks user for feedback.
- Builds a vector DB knowledge-base, based on the rank and the user feedback.

### Links
- [GitHub](https://github.com/pgalko/BambooAI)
- [Creators's Twitter](https://twitter.com/pgalko)

</details>


## [BeeBot](https://github.com/AutoPackAI/beebot)
An Autonomous AI Assistant designed to perform a wide range of practical tasks autonomously

<details>
	
### Description
- "BeeBot is currently a work in progress and should be treated as an early stage research project. Its focus is not on production usage at this time."

	
### Links
- [GitHub](https://github.com/AutoPackAI/beebot)
- [Tweet](https://twitter.com/Douglas_Schon/status/1681094815021187072?s=20)
</details>


## [Bloop](https://bloop.ai/)
A GPT-4 powered semantic code search engine that uses an AI agent

<details>

### Description
- Powered by GPT-4 and semantic code search, precise code navigation
- Built on stack graphs and scope queries
- Fast code search and regex matching engine written in Rust
- Allows to find Code on Rust and Typescript
- Allows to stage changes
- The agent searches both your local and remote repositories with natural language, regex and filtered queries
- Bloop can be run via app (easy to download via GitHub)

### Links
- [GitHub](https://github.com/BloopAI/bloop)
- ["Getting started" guide](https://bloop.ai/docs/getting-started)
- [Bloop apps](https://github.com/BloopAI/bloop/releases)

</details>


## [Camel](https://github.com/camel-ai/camel)
An agent architecture for “Mind” Exploration of Large Scale Language Model Society

<details>

### Description
1) AI user agent: give instructions to the AI assistant with the goal of completing the task.
2) AI assistant agent: follow AI user’s instructions and respond with solutions to the task

### Links
- [Paper - CAMEL: Communicative Agents for “Mind”
Exploration of Large Scale Language Model Society](https://ghli.org/camel.pdf)
- [Colab demo](https://colab.research.google.com/drive/1AzP33O8rnMW__7ocWJhVBXjKziJXPtim?usp=sharing)
- [GitHub](https://github.com/camel-ai/camel)
- [Hugging face datasets](https://huggingface.co/camel-ai)
- [Slack](https://camel-kwr1314.slack.com/join/shared_invite/zt-1vy8u9lbo-ZQmhIAyWSEfSwLCl2r2eKA#/shared-invite/email)
- Authors: Guohao Li∗ Hasan Abed Al Kader Hammoud* Hani Itani* Dmitrii Khizbullin, Bernard Ghanem

</details>

## [ChemCrow](https://github.com/ur-whitelab/chemcrow-public)
A chemistry agent that performs tasks across synthesis, drug discovery, and materials design

<details>

### Decsription
- ChemCrow is an open source package for the accurate solution of reasoning-intensive chemical tasks
- It integrates 13 expert-design tools to augment LLM performance in chemistry and demonstrate effectiveness in automating chemical tasks
- Built with Langchain
- The LLM is provided with a list of tool names, descriptions of their utility, and details about the expected input/output. It is then instructed to answer a user-given prompt using the tools provided when necessary. The instruction suggests the model to follow the ReAct format - Thought, Action, Action Input, Observation. One interesting observation is that while the LLM-based evaluation concluded that GPT-4 and ChemCrow perform nearly equivalently, human evaluations with experts oriented towards the completion and chemical correctness of the solutions showed that ChemCrow outperforms GPT-4 by a large margin. This indicates a potential problem with using LLM to evaluate its own performance on domains that requires deep expertise. The lack of expertise may cause LLMs not knowing its flaws and thus cannot well judge the correctness of task results. (Source: [Weng, Lilian. (Jun 2023). LLM-powered Autonomous Agents". Lil’Log. https://lilianweng.github.io/posts/2023-06-23-agent/.](https://lilianweng.github.io/posts/2023-06-23-agent/))




### Links
- [Paper](https://arxiv.org/abs/2304.05376)
- [GitHub](https://github.com/ur-whitelab/chemcrow-public)
- [HackerNews Discussion](https://news.ycombinator.com/item?id=35607616)

</details>

## [Clippy](https://github.com/ennucore/clippy/)

The purpose of Clippy is to develop code for or with the user. It can plan, write, debug, and test some projects autonomously. For harder tasks, the best way to use it is to look at its work and provide feedback to it.

<details>

### Links
- [GitHub](https://github.com/ennucore/clippy/)
- Author: [Lev Chizhov](http://lev.la/) 

</details>

## [Cody by ajhous44](https://github.com/ajhous44/cody)

An AI assistant designed to let you interactively query your codebase using natural language. By utilizing vector embeddings, chunking, and OpenAI's language models, Cody can help you navigate through your code in an efficient and intuitive manner.

<details>

### Links
- [GitHub](https://github.com/ajhous44/cody)
- Author: [@ajhous44](https://github.com/ajhous44/) (Github)

</details>

## [Cody by Sourcegraph](https://docs.sourcegraph.com/cody)

An AI code assistant from Sourcegraph that writes code and answers questions for you by reading your entire codebase and the code graph.

<details>

### Links
- [GitHub](https://github.com/sourcegraph/sourcegraph/tree/main/client/cody)
- Author: [@sourcegraph](https://twitter.com/sourcegraph) (Twitter)

</details>

## [Cursor](https://www.cursor.so/)

The AI-first Code Editor. Build software faster in an editor designed for pair-programming with AI.

<details>

### Links
- [Website](https://www.cursor.so/)
- [GitHub (Issue Only)](https://github.com/getcursor/cursor)
- [Discord](https://discord.com/invite/PJEgRywgRy)

</details>

## [Databerry](https://www.databerry.ai/)
A super-easy no-code platform for creating AI chatbots trained on your own data

<details>

### Description
- One of the easiest and fastest no-code platform I have encountered
- After creating new agent, picking a model, data and other settings, they are ready to be deployed to website, Slack, Crisp, or Zapier
- Limit of agent in the free version
- Stack
	- Next.js
	- Joy UI
	- LangchainJS
	- PostgreSQL
	- Prisma
	- Qdrant
- Features
	- Streamline customer support, onboard new team members, and more
	- Load data from anywhere
	- No-code: User-friendly interface to manage your datastores and chat with your data
	- Secured API endpoint for querying your data
	- Auto sync data sources (coming soon)
	- Auto generates a ChatGPT Plugin for each datastore

<!--
### Stack
- Next.js
- Joy UI
- LangchainJS
- PostgreSQL
- Prisma
- Qdrant


### Features
- Streamline customer support, onboard new team members, and more
- Load data from anywhere
- No-code: User-friendly interface to manage your datastores and chat with your data
- Secured API endpoint for querying your data
- Auto sync data sources (coming soon)
- Auto generates a ChatGPT Plugin for each datastore

-->

### Links
- [Documentation](https://docs.databerry.ai/introduction)
- [Discord](https://discord.com/invite/FSWKj49ckX)
- [GitHub](https://github.com/gmpetrov/databerry)

</details>

## [Deepnote AI Copilot](https://deepnote.com/blog/introducing-deepnote-ai)
An AI code copilot that instantly suggests code and works with the whole notebook context
<details>

## Description
- Deepnote's AI Copilot, with its efficient and contextual code suggestions, is paving the way for a future of AI-powered data exploration in notebooks
- AI Copilot
- Cut back on repetition and increase efficiency for data scientists
- Code suggestions
- Understanding the full scope of your notebook
- The more text and code you write as context, the more relevant code suggestions you will see
- "We are soon introducing conversational AI features that will aid in generating, editing, debugging, and understanding both code and SQL. Beyond this, we are working on more ambitious projects designed to harness the unique attributes of notebooks as a computational medium."

## Links
- [Twitter](https://twitter.com/DeepnoteHQ?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor)

</details>

## [DemoGPT](https://github.com/melih-unsal/DemoGPT)
An AI that enables quick demo generation for LLM-based applications using just prompts
<details>

## Description
- DemoGPT leverages the power of Language Models (LLMs) to provide fast and effective demo creation for applications.
- Automates the prototyping process, making it more efficient and saving valuable time.
- Understands and processes the given prompts to generate relevant applications.
- Integrated with LangChain for generating application code through iterative parsing of LangChain's documentation with a "Tree of Transformations" (ToT) approach.
- The roadmap for DemoGPT includes constant updates and improvements based on user feedback and real-world application, working towards refining the technology and solving the hallucination problem.
- "We are planning to introduce features that will further enhance the application generation process, making it more user-friendly and efficient."

## Links
- [Github](https://github.com/melih-unsal/DemoGPT)
- [Website](https://www.demogpt.io/)
- [Twitter](https://twitter.com/demo_gpt)
- [Streamlit App](https://demogpt.streamlit.app/)
- [Huggingface Space](https://huggingface.co/spaces/melihunsal/demogpt)

</details>

## [DevGPT](https://github.com/jina-ai/dev-gpt)
Team of virtual developers

<details>

### Description
- "Tell your AI team what microservice you want to build, and they will do it for you. Your imagination is the limit!!
- Welcome to Dev-GPT, where we bring your ideas to life with the power of advanced artificial intelligence! Our automated development team is designed to create microservices tailored to your specific needs, making your software development process seamless and efficient. Comprised of a virtual Product Manager, Developer, and DevOps, our AI team ensures that every aspect of your project is covered, from concept to deployment.

### Links
- [Discord](https://discord.com/invite/AWXCCC6G2P)

</details>

## [DevOpsGPT](https://github.com/kuafuai/DevOpsGPT)
DevOpsGPT: AI-Driven Software Development Automation Solution

<details>

### Description
Welcome to the AI Driven Software Development Automation Solution, abbreviated as DevOpsGPT. We combine LLM (Large Language Model) with DevOps tools to convert natural language requirements into working software. This innovative feature greatly improves development efficiency, shortens development cycles, and reduces communication costs, resulting in higher-quality software delivery.

### Features and Benefits
* Improved development efficiency: No need for tedious requirement document writing and explanations. Users can interact directly with DevOpsGPT to quickly convert requirements into functional software.
* Shortened development cycles: The automated software development process significantly reduces delivery time, accelerating software deployment and iterations.
* Reduced communication costs: By accurately understanding user requirements, DevOpsGPT minimizes the risk of communication errors and misunderstandings, enhancing collaboration efficiency between development and business teams.
* High-quality deliverables: DevOpsGPT generates code and performs validation, ensuring the quality and reliability of the delivered software.
* [Enterprise Edition] Existing project analysis: Through AI, automatic analysis of existing project information, accurate decomposition and development of required tasks on the basis of existing projects.
* [Enterprise Edition] Professional model selection: Support language model services stronger than GPT in the professional field to better complete requirements development tasks, and support private deployment.
* [Enterprise Edition] Support more DevOps platforms: can connect with more DevOps platforms to achieve the development and deployment of the whole process.

### Links
- [Creator Website](https://www.kuafuai.net/)
- [Demo Video](https://youtu.be/IWUPbGrJQOU)

</details>

## [English Compiler](https://github.com/uilicious/english-compiler)
POC AI based Compiler, for converting english based markdown specs, into functional code
<details>


### Description
- "We know that all great™ projects start with awesome™ detailed functional specifications. Which is typically written in English, or its many other spoken language alternatives.
- So what if, instead of writing code from functional specs, we simply compile it directly to code?
- Into a future, where we replace nearly everything, with just written text."

### Links
- [Creator's Twitter](https://twitter.com/picocreator)

</details>

## [Friday](https://github.com/amirrezasalimi/friday/)

A developer assistant able to make whole nodejs project with unlimited prompts
<details>

### Description
- Provides a core prompt for building the foundation of your application
- Allows you to add unlimited sections, each of which is a prompt representing a specific part of your app
- Features
	- Friday utilizes GPT-4 for AI assistance, but it has been tested and optimized with GPT-4-32k for improved speed and better results.
	- It requires 2 small requests for your app's base and 1 request per section you provide.
	- Friday employs esbuild behind the scenes for every app created by it.

### Links
- **Author:** [Amirreza Salimi](https://twitter.com/amirsalimiiii)

</details>

## [Godmode](https://godmode.space/)
A project inspired by Auto-GPT and BabyAGI, conducting  various kinds of tasks via nice UI

<details>

## Description
- A web platform inspired by AutoGPT and BabyAGI
- What it can do:
	- Order your coffee at Starbucks
	- Perform market analysis
	- Find and negotiate a lease
- Supports GPT-3.5 & GPT-4


## Links
- [GitHub](https://github.com/FOLLGAD/Godmode-GPT)
- Authors: [Emil Ahlbäck](https://twitter.com/emilahlback), [Lonis](https://twitter.com/_Lonis_)
- [Discord](https://discord.com/invite/vSzCcDDwz3)
- [Tweet](https://twitter.com/_Lonis_/status/1646641412182536196)

</details>

## [GPT Engineer](https://github.com/AntonOsika/gpt-engineer)
An AI agent that generates an entire codebase based on a prompt

<details>

### Description
- Model: GPT 4
- Specify your project, and the AI agent asks for clarification, and then constructs the entire code base
- Features
	- Made to be easy to adapt, extend, and make your agent learn how you want your code to look. It generates an entire codebase based on a prompt
	- You can specify the "identity" of the AI agent by editing the files in the identity folder
	- Editing the identity and evolving the main prompt is currently how you make the agent remember things between projects
	- Each step in steps.py will have its communication history with GPT4 stored in the logs folder, and can be rerun with scripts/rerun_edited_message_logs.py

<!--

### Features
- Made to be easy to adapt, extend, and make your agent learn how you want your code to look. It generates an entire codebase based on a prompt
- You can specify the "identity" of the AI agent by editing the files in the identity folder
- Editing the identity, and evolving the main prompt, is currently how you make the agent remember things between projects
- Each step in steps.py will have its communication history with GPT4 stored in the logs folder, and can be rerun with scripts/rerun_edited_message_logs.py

-->

### Links
- [Discord](https://discord.com/invite/8tcDQ89Ej2)
- Author: [Anton Osika](https://twitter.com/antonosika)
- [Twitter review by @Attack](https://twitter.com/Attack/status/1671165869064609792)

</details>

## [GPT Migrate](https://github.com/0xpayne/gpt-migrate)
Easily migrate your codebase from one framework or language to another

<details>

### Description
- Pick from different LLMs
- Ability to allow GPT Migration to generate and run unit tests for the new codebase
- Ability to select source and target language of the migration
- Ability to customize the agent's workflow (setup -> migrate -> test)
- GPT Migrate team is working on adding [benchmarks](https://github.com/0xpayne/gpt-migrate#-benchmarks) for the agent

### Links
- [Website](https://gpt-migrate.com/)
- Author: [Josh Payne](https://twitter.com/joshpxyne)
- [Announcement](https://twitter.com/joshpxyne/status/1675254164165910528)


</details>


## [GPT Researcher](https://github.com/assafelovic/gpt-researcher)
GPT based autonomous agent that does online comprehensive research on any given topic

<details>

### Description
- Can produce detailed, factual and unbiased research reports
- Offers customization options for focusing on relevant resources, outlines, and lessons
- Addresses issues of speed and determinism, offering a more stable performance and increased speed through parallelized agent work, as opposed to synchronous operation
- Inspired by AutoGPT and the Plan-and-Solve paper
- The main idea is to run "planner" and "execution" agents, whereas the planner generates questions to research, and the execution agents seek the most related information based on each generated research question

### Links
- [Website](https://tavily.com/)
- [Discord](https://discord.com/invite/2pFkc83fRq)
- Author: [Assaf Elovic](https://twitter.com/assaf_elovic)


</details>

## [GPT Runner](https://github.com/nicepkg/gpt-runner)
Conversations with your files which selected! Manage and run your AI presets!

<details>

### Description
- Conversation with your files which selected by you, no embedding, no vector database!
- It's also a AI Prompt Storybook. You can use it to manage some AI preset with your team. It support any IDE and language developer. We provide cli to run web and VSCode extension, Jetbrains plugin is coming soon.
- Private first, all data is local.
- We support both OpenAI and Anthropic (Claude-2)
- It support support for multiple languages.

![image](https://repository-images.githubusercontent.com/640476297/30741f73-caac-48bc-b500-1b7d6efde4c4)

### Links
- [Website](https://github.com/nicepkg/gpt-runner)
- Author: [Jinming Yang](https://github.com/2214962083)


</details>

## [Lemon Agent](https://github.com/felixbrock/lemon-agent)

Plan-Validate-Solve (PVS) Agent for accurate, reliable and reproducable workflow automation

<details>

### Description

- A standalone supervised Plan and Solve Agent specialized on performing read and write operations on various tools like GitHub, HubSpot or Airtable _(ACL 2023 Paper "[Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models](https://arxiv.org/abs/2305.04091)")_
- **Separation of tasks and human-in-the-loop interactions**: Lemon Agent is currently holding a Planner Agent and a Solver Agent to keep the agents focussed and increase accuracy. We are planning on adding additional agents real soon. In addition, Lemon Agent will ask for approval at relevant workflow steps to make sure the intended actions are executed.
- **Unlimited configuration options**: Lemon Agent gives you unlimited configuration options (see example here) when defining your workflow. For instance, you can tell Lemon Agent to ask for permission before executing a workflow step or to drop a 🧔‍♀️ dad joke every time the model executes a workflow step.
- **UI flexibility**: Build any UI on top or engage with Lemon Agent via the built-in CLI.
- **[Soon] Model & framework agnostic operations**: Lemon Agent is a standalone agent, but can easily be integrated into frameworks like LangChain and be used with any model.
- **Bonus**: Identify weak spots in your agent’s decision-making capabilities and move to a more deterministic behavior by further configuring your Lemon Agent workflows. **(.html file that can be run without any additional installation)**

### Links

- [Discord](https://discord.gg/fWU4rDYSxw)
- [Author's Twitter](https://twitter.com/felixbrockm)

</details>

## [Loop GPT](https://github.com/farizrahman4u/loopgpt/tree/main)
A re-implementation of the popular Auto-GPT project as a proper python package, written with modularity and extensibility in mind

 <details>

### Description
- Languages: Python
- Default model: GPT-3.5-turbo (also possible with GPT-4)
- Modular Auto-GPT Framework
- Plug N Play" API - Extensible and modular "Pythonic" framework, not just a command line tool
- Features
	- "Easy to add new features, integrations and custom agent capabilities, all from python code, no nasty config files!"
	- "Minimal prompt overhead - Every token counts. We are continuously working on getting the best results with the least possible number of tokens."
	- "Human in the Loop - Ability to "course correct" agents who go astray via human feedback."
	- "Full state serialization - can save the complete state of an agent, including memory and the states of its tools to a file or python object. No external databases or vector stores required (but they are still supported)!"

<!--
### Features
- "Easy to add new features, integrations and custom agent capabilities, all from python code, no nasty config files!"
- "Minimal prompt overhead - Every token counts. We are continuously working on getting the best results with the least possible number of tokens."
- "Human in the Loop - Ability to "course correct" agents who go astray via human feedback."
- "Full state serialization - can save the complete state of an agent, including memory and the states of its tools to a file or python object. No external databases or vector stores required (but they are still supported)!"

-->
</details>


## [LocalGPT](https://github.com/PromtEngineer/localGPT)
Inspired by privateGPT, allows using your own documents as an information source

 <details>

### Description
- Most of the description on readme is inspired by the original privateGPT
- Model: Vicuna-7B
- Using InstructorEmbeddings
- Both Embeddings as well as LLM will run on GPU. It also has CPU support if you do not have a GPU
- Built with Langchain

<!--
### Features
- Ask questions to your documents without an internet connection, using the power of LLMs. 100% private, no data leaves your execution environment at any point. You can ingest documents and ask questions without an internet connection!
-->

### Links
- [YouTube - LocalGPT: OFFLINE CHAT FOR YOUR FILES [Installation & Code Walkthrough]](https://www.youtube.com/watch?v=MlyoObdIHyo&ab_channel=PromptEngineering)
</details>


## [Mentat](https://github.com/biobootloader/mentat)
Mentat is the AI tool that assists you with any coding task, right from your command line.

Unlike Copilot, Mentat coordinates edits across multiple locations and files. And unlike ChatGPT, Mentat already has the context of your project - no copy and pasting required!

<details>

### Links  
- [Website](https://www.mentat.codes/)
- [Youtube](https://www.youtube.com/watch?v=lODjaWclwpY)
- Author: [Bio Bootloader](https://twitter.com/bio_bootloader) (Twitter)
- [Discord Invite](https://discord.com/invite/zbvd9qx9Pb)


</details>



## [Mini AGI](https://github.com/muellerberndt/mini-agi)
A minimal general-purpose autonomous agent based on GPT-3.5 / GPT-4
<details>

### Description
- MiniAGI is a minimal general-purpose autonomous agent based on GPT-3.5 / GPT-4
- Can analyze stock prices, perform network security tests, create art, and order pizza
- MiniAGI is a simple autonomous agent compatible with GPT-3.5-Turbo and GPT-4
- It combines a robust prompt with a minimal set of tools, chain-of-thoughts, and short-term memory with summarization
- Capable of inner monologue and self-criticism
</details>


## [Multi GPT](https://github.com/rumpfmax/Multi-GPT)
An experimental open-source attempt to make GPT-4 fully autonomous
<details>

### Description
- An experimental multi-agent system
- Multiple "expertGPTs" collaborate to perform a task
- Each with their own short and long-term memory and the ability to communicate with each other
- Features
	- Set a task and watch the experts get to work.
	- Internet access for searches and information gathering
	- Long-Term and Short-Term memory management
	- GPT-4 instances for text generation
	- Access to popular websites and platforms
	- File storage and summarization with GPT-3.5

### Links
- [Demo](https://www.loom.com/share/b6bec93065794eb8a47e2109697afa39)
- Authors: [Max Rumpf](https://twitter.com/md_rumpf) and [Significant Gravitas](https://twitter.com/SigGravitas)


</details>


## [OpenAGI](https://github.com/agiresearch/OpenAGI)
An open-source AGI R&D platform that enables agents for both benchmark tasks and open-ended tasks

<details>

### Description
- Powered by various language models such as GPT-4, Vicuna, LLaMA, and Flan-T5
- Supports multi-modality tool learning and task solving such as text, image, video and audio
- Supports task decomposition into both linear task-solving plans and non-linear task-solving plans
- Allows both benchmark task solving and open-ended task solving
- Provides easy-to-use evaluation protocols to evaluate task-solving ability
- Provide Reinforcement Learning from Task Feedback (RLTF) to allow continuously self-improving agent

### Links
- [GitHub](https://github.com/agiresearch/OpenAGI)
- [Paper](https://arxiv.org/abs/2304.04370)
- [Demo](https://www.youtube.com/watch?v=7RaXPPXi0-Y)

</details>



## [Pezzo](https://www.pezzo.ai/)
A development toolkit designed to streamline prompt design, version management, publishing, collaboration, troubleshooting, observability and more
<details>


### Description
- "Whether you are a technical person or a stakeholder, you can use Pezzo effectively. We don't believe that AI prompts should be designed in a developer's code editor. Aside from the technical issues with this approach, it blocks productivity."
- Features
	- Centralized Prompt Management: Manage all AI prompts in one place for maximum visibility and efficiency.
	- Streamlined Prompt Design, Publishing & Versioning: Create, edit, test and publish prompts with ease.
	- Observability: Access detailed prompt execution history, stats and metrics (duration, prompt cost, completion cost, etc.) for better insights.
	- Troubleshooting: Effortlessly resolve issues with your prompts. Time travel to retroactively fine-tune failed prompts and commit the fix instantly.
	- Cost Transparency: Gain comprehensive cost transparency across all prompts and AI models.
	- Simplified Integration: Reduce code overhead by 90% by consuming your AI prompts using the Pezzo Client, regardless of the model provider.

### Links
- [Documentation](https://docs.pezzo.ai/docs/intro.html)
- [GitHub](https://github.com/pezzolabs/pezzo)
</details>

## [Private GPT](https://www.privategpt.io/)
A tool for private interaction with documents, without a need for internet connection
<details>

### Description
- Built with LangChain, GPT4All, LlamaCpp, Chroma and SentenceTransformers
- A test project to validate the feasibility of a fully private solution for question answering using LLMs and Vector embeddings, not production ready


### Links
- [GitHub](https://github.com/imartinez/privateGPT)

</details>

## [PromethAI](https://github.com/topoteretes/PromethAI-Backend)

Personalized AI assistant that helps with nutrition and other goals

<details>

### Description
- "Personalized AI assistant that decomposes problems, offers solutions, and lets you use Agent actions to automate your flows"
- Features
  	- Helps users reach a solution by decomposing their requests into categories with a set of options (cuisine -> European)
  	- Has a dynamic UX/UI that helps avoid prompting
  	- Voice input supported
  	- Provides users with results of their queries and automates actions around them
  	- Remembers your past preferences and uses them to optimize your choices
- Tech
	- Powered by Langchain, decomposable async prompts + vector DB + Redis cache
 	- App built with Flutter + Dart
    	- Connected to Zapier NLP

### Links
- [GitHub](https://github.com/topoteretes/)
- [Website](https://prometh.ai)
- Author: [Vasilije M](https://twitter.com/tricalt)
</details>


## [React Agent](https://reactagent.io/)
An open-source React.js Autonomous LLM Agent
<details>

## Description
- An experimental autonomous agent
- Model: GPT-4
- Purpose: Gnerate and compose React components from user stories
- Stack
	- React
	- TailwindCSS
	- Typescript
	- Radix UI
	- Shandcn UI
	- OpenAI API
- The agent is taking a user story text and generating and composing multiple react components to generate the relevant screens, based on atomic design principles
- Features
	- Generate React Components from user stories
	- Compose React Components from existing components
	- Use a local design system to generate React Components
	- Use React, TailwindCSS, Typescript, Radix UI, Shandcn UI
	- Built with Atomic Design Principles
- It is still experimental but very interesting results, It is completely open-sourced, looking for contributors!

## Links
- [GitHub](https://github.com/eylonmiz/react-agent)
- [Documentation](https://docs.reactagent.io/)
- Authors: [Eylon Miz and](https://twitter.com/EylonMiz) and [Lee Twito](https://twitter.com/LeeTwito)

</details>

## [Smol developer](https://github.com/smol-ai/developer)
:hatching_chick: Your own junior developer. [Deployed in few seconds via e2b](https://app.e2b.dev/agent/smol-developer/?utm_source=awesome-ai-agents)
<details>

### Description
- Human-centric, coherent whole program synthesis
- Your own junior developer
- Allows to develop, debug, and decompile
- 200 LOC, half english
- 100k context can summarize both content and codebases
- Markdown is the best prompting DSL
- Copy and paste your errors as prompts
- Copy and paste curl output as prompts
- Write CSS animation by describing what u want
- GPT4 >>> GPT3.5/Anthropic Claude for codegen

### Links
- Author: [Swyx](https://twitter.com/swyx)
- [Demo](https://www.youtube.com/watch?v=UCo7YeTy-aE)
- [Twitter](https://twitter.com/SmolModels)
- [Meme](https://smol.ai/)


</details>

## [Superagent](https://www.superagent.sh/)</details>
Not a single agent, but a tool that allows creating agents without coding
<details>

### Description
- Simplifies the configuration and deployment of LLM Agents to production
- "One of the core principals of SuperAgent is to build with any third-party dependencies to proprietary tech"
- It provides a range of features and functionalities to make it easier for developers to build, manage and deploy AI agents to production including features such as built in memory and document retrieval via vector dbs, powerful tools, webhooks, cron jobs etc.
- There are two main types of agents: action agents and plan-and-execute agents

### Links
- [GitHub](https://github.com/homanp/superagent)
- [Documentation](https://docs.superagent.sh/introduction)
- [Discord](https://discord.com/invite/mhmJUTjW4b)
- Author: [Ismail Pelaseyed](https://twitter.com/pelaseyed)

</details>

## [SuperAGI](https://superagi.com/)
An open-source autonomous AI framework to enable development and deployment autonomous agents
<details>

### Description
- An AI agent framework
- Open source, but infrastructure is -source
- Features
	- Provision, Spawn & Deploy Autonomous AI Agents
	- Extend Agent Capabilities with Tools
	- Run Concurrent Agents Seamlessly
	- Graphical User Interface
	- Action Console
	- Multiple Vector DBs
	- Multi-Modal Agents
	- Agent Trajectory Fine-Tuning
	- Performance Telemetry
	- Optimized Token Usage
	- Agent Memory Storage
	- Looping Detection Heuristics
	- Concurrent Agents
	- Resource Manager


### Links
- [YouTube](https://www.youtube.com/@_superagi)
- [Discord](https://discord.com/invite/dXbRe5BHJC)
- [Subreddit](https://www.reddit.com/r/Super_AGI/)
- [Twitter](https://twitter.com/_superAGI)
- Author: [Ishaan Bhola](https://twitter.com/ishaanbhola)

</details>

## [Sweep](https://sweep.dev/)
A Github assistant the helps fix small bugs and implement small features
<details>

### Description
- To install, click the install button
- Then add the repository you want, make a quick ticket (e.g. writing tests)
- Prepend the ticket with "Sweep:" and let Sweep handle the rest

### Links
- [GitHub](https://github.com/sweepai)
- [Discord](https://discord.com/invite/sweep-ai)
- [Tricks for prompting Sweep](https://sweep-ai.notion.site/Tricks-for-prompting-Sweep-3124d090f42e42a6a53618eaa88cdbf1)


</details>

## [Teenage AGI](https://github.com/seanpixel/Teenage-AGI/blob/main/README.md#experiments)

A BabyAGI-inspired agent that can recall infinite memory, "thinks" before making action, and doesn't lose memory after being shutting down
<details>

### Description
- Model: GPT-4
- Language: Python
- Uses OpenAI and Pinecone to give memory to an AI agent and also allows it to "think" before making an action (outputting text)
- Also, just by shutting down the AI, it doesn't forget its memories since it lives on Pinecone and its memory counter saves the index that it's on
- A process that happens every time the AI is queried by the user:
	- AI vectorizes the query and stores it in a Pinecone Vector Database
	- AI looks inside its memory and finds memories and past queries that are relevant to the current query
	- AI thinks about what action to take
	- AI stores the thought from Step 3
	- Based on the thought from Step 3 and relevant memories from Step 2, AI generates an output
	- AI stores the current query and its answer in its Pinecone vector database memory

### Links
- Created by [@sean_pixel](https://twitter.com/sean_pixel)
- Inspired by paper ["Generative Agents: Interactive Simulacra of Human Behavior"](https://arxiv.org/abs/2304.03442)

</details>


## [“Westworld” simulation](https://theolvs.github.io/westworld/)
A multi-agent simulation library, with a goal to simulate and optimize systems and environments with multiple agents interacting
<details>

### Description
- Researchers from Stanford and Google created an interactive sandbox env with 25 Gen AI agents can simulate human behavior
- They walk in the park, join for coffee at a cafe, and share news with colleagues. They demonstrated surprisingly good social
- Westworld's inspiration is drawn from Unity software and Unity ML Agents, adapted in Python
- Languages
	- The library is available on PyPi via pip install westworld
	- [Javascript version (being developed)](https://github.com/TheoLvs/westworldjs)
- Features
	- Easy creation of Grid and non-grid environments
	- Objects (Agents, Obstacles, Collectibles, Triggers)
	- Subclassing of different objects to create custom objects
	- Spawner to generate objects randomly in the environment
	- Basic rigid body system for all objects
	- Simple agent behaviors (pathfinding, wandering, random walk, fleeing, vision range)
	- Automatic maze generation
	- Layer integration to convert image to obstacle and snap it to a grid
	- Sample simulations and sample agents for classic simulations
	- Simulation visualization, replay and export (gif or video)



### Links
- [GitHub](https://github.com/TheoLvs/westworld)
- [Documentation](https://theolvs.github.io/westworld/ )
- [Underlying paper - Generative Agents](https://arxiv.org/abs/2304.03442)
- A paper simulating interactions between tens of agents
- Presenting an architecture that extends a language model to store and synthesize the agent's experiences, enabling dynamic behavior planning in an interactive sandbox environment with generative agents
</details>

## [Voyager](https://voyager.minedojo.org/)
A LLM-powered embodied lifelong learning agent in Minecraft
<details>

### Description
- A LLM-powered embodied lifelong learning agent in Minecraft that continuously explores the world, acquires diverse skills, and makes novel discoveries without human intervention
- Voyager consists of three key components:
	- 1) an automatic curriculum that maximizes exploration
	- 2) an ever-growing skill library of executable code for storing and retrieving complex behaviors
	- 3) a new iterative prompting mechanism that incorporates environment feedback, execution errors, and self-verification for program improvement
- Voyager interacts with GPT-4 via blackbox queries, which bypasses the need for model parameter fine-tuning


### Links
- [GitHub](https://github.com/MineDojo/Voyager)
- [Paper - Voyager: An Open-Ended Embodied Agent with Large Language Models](https://arxiv.org/abs/2305.16291)
- [YouTube video](https://www.youtube.com/watch?v=uTg39rNMojo)
- [Tweet](https://twitter.com/DrJimFan/status/1662115266933972993)

</details>



## [WorkGPT](https://github.com/team-openpm/workgpt)
A GPT agent framework for invoking APIs
<details>

### Description
- WorkGPT is an agent framework in a similar fashion to AutoGPT or LangChain. You give it a directive and an array of APIs and it will converse back and forth with the AI until its directive is complete.
- For example, a directive could be to research the web for something, to crawl a website, or to order you an Uber. We support any and all APIs that can be represented with an OpenAPI file.
- WorkGPT now has OpenAI's new function invocation feature baked into it
	- While chaining together APIs was possible before (see AutoGPT), it was slow, expensive, and error prone
	- [The tweet announcing this feature](https://twitter.com/maccaw/status/1669367224694607875)

### Links
- Author: [Alex MacCaw](https://twitter.com/maccaw)

</details>


## [yAgents](https://github.com/yeagerai/yeagerai-agent)

yAgents is an Agent-Builder Agent made by Yeager.ai capable of designing, coding and debugging its own tools.

<details>

### Description
- Designed to help build, prototype, and deploy AI-powered tools and agents easily and efficiently.
- Built on the LangChain framework, allowing users of any technical background to create, improve, and deploy AI agents.
- Equipped with an interactive command line interface for real-time feedback and ease of navigation.
- Features session persistent memory to ensure data preservation across multiple sessions
- Quick and easy installation via pip.
- Contributions to expand and improve yAgents are highly encouraged.
-  Warnings
	- Requires GPT-4 API access.
	- Not tested for Windows systems

### Links
- [GitHub Repository](https://github.com/yeagerai/yeagerai-agent/?utm_source=awesome-ai-agents)
- [Discord](https://discord.com/invite/wKds24jdAX/?utm_source=awesome-ai-agents)
- [License: MIT](https://github.com/yeagerai/yeagerai-agent/blob/main/LICENSE/?utm_source=awesome-ai-agents)

</details>

## [Yourgoal](https://github.com/pj4533/yourgoal/?utm_source=awesome-ai-agents)

Swift implementation of BabyAGI

<details>

### Description
- "This is a Swift port of BabyAGI, an example of an AI-powered task management system that uses OpenAI and Pinecone APIs to create, prioritize, and execute tasks. The main idea behind this system is that it creates tasks based on the result of previous tasks and a predefined objective."

### Links
- Author: [PJ Gray](https://twitter.com/pj4533/?utm_source=awesome-ai-agents)
</details>


# :lock: Closed-source projects and companies

## [Adept AI](https://www.adept.ai/?utm_source=awesome-ai-agents)
A ML research and product lab building general intelligence by enabling humans and computers to work together creatively


<details>

### Description
- An AI teammate for everyone
- "Adept is building an entirely new way to get things done. It takes your goals, in plain language, and turns them into actions on the software you use every day."
- In early stage
- "We’re building a machine learning model that can interact with everything on your computer."


### Links
- [Twitter](https://www.adept.ai/?utm_source=awesome-ai-agents)
- [Linkedin](https://www.linkedin.com/company/adeptai/?utm_source=awesome-ai-agents)

</details>


## [Airkit.ai](https://www.airkit.ai)
Airkit is a developer-first platform for building, testing, and deploying AI Agents.


<details>

### Description

- A browser based studio for managing prompts, building tools, and testing your agents.
- Built in short-term and long-term memory management
- 1 click deployment. Embed anywhere with our Web SDK. 

### Links
- [Profile of the company](https://www.airkit.ai)
- [Twitter](https://twitter.com/AirkitAI)

</details>


## [Airplane Autopilot](https://www.airplane.dev/autopilot/?utm_source=awesome-ai-agents/)
Airplane is a company for building internal tools, they're building their autopilot AI assistant.


<details>

### Description

- A developer-centric approach to building internal UIs and workflows
- Turning APIs, SQL queries, and scripts into apps for the entire team
- Features
	- Airplane lets you turn SQL queries, JavaScript/Python code, HTTP requests, etc into tasks
	- Allows to run tasks through a no-code dashboard
	- Tasks for customer support, on-call runbooks, and scheduled tasks

### Links
- [Profile of the company](https://www.airplane.dev/?utm_source=awesome-ai-agents)
- [Documentation](https://docs.airplane.dev/?utm_source=awesome-ai-agents)
- [Twitter](https://twitter.com/AirplaneDev/?utm_source=awesome-ai-agents)
- [They're building an AI assistant here](https://www.airplane.dev/autopilot/?utm_source=awesome-ai-agents)


</details>


## [Aomni](https://www.aomni.com/?utm_source=awesome-ai-agents)

An AI agent specifically designed for business intelligence
<details>

### Description
- Breaks down a high level research question into a step-by-step plan, and executes it
- Diverse tools, including a full web browser
- Can access internet information without the need for an API
- "We don't generate content using AI, as it can be unreliable. Instead, we extract relevant information from trusted sources, cluster and process it into a user-friendly format."
- AI-powered query planner intelligently routes and executes requests, ensuring correctness and diverse source selection

### Links
- [Discord](https://discord.com/invite/a367ncqEsm/?utm_source=awesome-ai-agents)

</details>


## [BitBuilder](https://www.bitbuilder.ai/?utm_source=awesome-ai-agents)


"Virtual intern for developers", generates code via PRs raised against your repository
<details>

### Description
- Create an Issue
- Approve the Implementation Plan
- Review the Pull Request
- Features
	- Writing code
	- Reviewing changes
	- Addressing comments
	- Answering questions
- BitBuilder Junior
	- BitBuilder Junior is an intern-level code generation tool that lives in your GitHub repository. It follows instructions to implement unambiguous code changes by changing multiple files, writing tests for generated code, and matching the style, framework, and libraries you're already using.

### Links
- [GitHub Marketplace](https://github.com/marketplace/document-guardian)
- [Slack](https://bitbuilder-ai.slack.com/join/shared_invite/zt-1tlrds3n4-rpmgIGM6XrB5W97005IA1Q#/shared-invite/email)
- [Installation](https://docs.bitbuilder.ai/install)



</details>


## [broadn](https://www.broadn.io/?utm_source=awesome-ai-agents)


AI no-code copilot that allows users to build AI apps.
<details>

### Description
- broadn is a no-code platform that helps non-technical people build AI products in minutes. We're faster and more flexible than traditional no-code tools through an LLM powered conversational interface and an agent architecture that automates complex backend/workflow operations
- Features
	- Conversational interface
	- LLM/AI model connectors (text, image models, etc)
	- Create bespoke chatbots
	- Render UI components
	- Connect to external data via APIs

### Links
- Authors: [Calin Drimbau](https://twitter.com/calindrimbau) and [Victor Paraschiv](https://twitter.com/vicpara)
- [Twitter](https://twitter.com/getbroadn)

</details>


## [Butternut AI](https://butternut.ai/)
A tool for creating a fully-functioning, ready-to-launch website in 20 seconds

<details>

### Description
- No coding required thanks to user-friendly interface
- Full SEO optimization
- Picture Upload: Users can conveniently upload and regenerate their own pictures for unlimited customization of their profiles
- Profile Customization: Users have the flexibility to customize their profiles by hiding sections, adding social media links, and sharing contact details, allowing them to showcase their unique personality and brand
- Instant Preview: Users can instantly visualize their profile changes through a conveniently placed preview button, ensuring a quick assessment of the desired appearance
- 30% Faster Speed: The app achieves an impressive 30% increase in website generation speed, providing users with a fast and efficient website building experience.
</details>

## [Codium AI](https://www.codium.ai/)
AI-powered interactive code integrity dev tool enabling developers to ship software faster and with fewer bugs

<details>

### Description

- Generating meaningful tests for busy devs
- Exploring and analyzing your code, docstrings, comments, and by interacting with you
- Non-trivial tests (and trivial, too!) suggested right inside your IDE
	- Generates tests
	- Covers edge cases
	- Best practice, readability code suggestions
	-  Gives you the code explanation
- It is free


### Links
- [Twitter](https://twitter.com/CodiumAI)
- [LinkedIn](https://www.linkedin.com/company/codiumai)
- [YouTube](https://www.youtube.com/@Codium-AI)
- [Discord](https://discord.com/invite/SgSxuQ65GF)
- [GitHub](https://github.com/Codium-ai)


</details>

## [Commit](https://commit.dev)


Career Copilot and AI Agent for Software Developers

<details>

### Description
- Comprehensive job search
- Accurate job recommendations based on your skills, experience, and preferences
- AI-powered auto-applications

### Links
- CEO: [Greg Gunn](https://www.linkedin.com/in/gunnr)
- CTO: [Beier Cai](https://www.linkedin.com/in/beiercai)

</details>


## [Cognosys](https://cognosys.ai)


Web based version of AutoGPT/babyAGI

<details>

### Description
- Friendly UI for building AI agents


### Links
- Author: [Sully Omarr](https://twitter.com/SullyOmarr)

</details>



## [Diagram](https://diagram.com/)
AI-powered design tools for everything from copywriting to generating unique icons from text, recently acquired by Figma

<details>

### Description
- Magic Copy writes, edits, and rewrites Figma text layers so you can design with real copy
- Generating images in Figma while designing
- Magic Rename intelligently names your layers so you can spend more time designing
- Magician works right inside your favorite design tool (e.g., Figma)
- Possible to get all the latest AI design advancements + future spells in one convenient plugin


</details>

## [encode](https://encode.software)
A fully autonomous software engineer

<details>

### Description
- in alpha
- encode works with you and your team to get work done
- demo: https://encode.software/demo
</details>


## [Factory](https://www.factory.ai/)
Working on autonomous coding Droids for building software end-to-end

<details>

### Description
- In aplha stage
- It’s not supposed to be just another coding copilots like GitHub Copilot or Codeium, but autonomous agents capable of autonomously building software from end to end

### Links
- [CEO](https://twitter.com/matangrinberg)


</details>


## [Fine](https://www.fine.dev/)

AI software architect that analyzes your code and helps you solve tasks

<details>


### Links
- [Twitter](https://twitter.com/thisisfinedev)
- Author: [Dan Leshem](https://twitter.com/leshemco)
</details>


## [Fine Tuner](https://fine-tuner.ai/)

Platform for no-code building of AI agents

<details>

- With Fine-Tuner, you can build sophisticated, tailored AI agents at scale without any need for technical skills or coding. Just bring your data and ideas, and we'll provide the toolset you need to transform them into powerful AI solutions, capable of handling vast amounts of data and users. Take advantage of our scalable platform to meet your growing needs with ease and efficiency
- Connecting Your Chatbot to Your App

- FineTuner.ai is a no-code AI platform that enables users to create and deploy custom AI agents and components without any coding.
With an intuitive UI/UX and rapid API deployment, FineTuner.ai simplifies AI development, allowing users to focus on their unique use cases and ideas.

4.1. Access the API tab for an overview of the required tokens and parameters to connect your chatbot to your app using REST API endpoints.
- The Fine-Tuner REST API provides API endpoints for Fine-Tuner data types that allow to interact with your AI models remotely by sending and receiving JSON
- Authentication to the Fine-Tuner API is performed via HTTP Bearer Authentication
- Front end: Bubble


### Links
- [Twitter](https://twitter.com/finetuner_ai)
- [Step-by-step guide](https://fine-tuner.ai/resources?res=1682544317646x963647349155168300)
- [Author](https://twitter.com/0xAlbert_S3)
</details>

## [Fixie](https://www.fixie.ai/)
A platform for creating LLM-powered apps like AI agents

<details>

### Description
- Building and managing LLM powered applications
- A cloud-based platform-as-a-service that allows developers to build smart agents that couple LLMs with back-end logic to interface to data, systems, and tools


### Links
- [GitHub](https://github.com/fixie-ai)
- [Fixie Developer Portal](https://docs.fixie.ai/)
- [AI.JSX](https://docs.ai-jsx.com/)
- [Twitter](https://twitter.com/fixieai)
- [Discord](https://discord.com/invite/MsKAeKF8kU)

</details>

## [Floode](https://floodehq.com/)

An AI executive assistant that automates communication busywork.

<details>

### Description
- Works across all your communication and work tools: emails, social media DMs, calendar, Notion, etc.
- Adapted to your work habits.
- Ask your assistant to:
  - Craft messages
  - Auto-sort
  - Auto-schedule
  - Summarize, extract tasks and information

### Links
- Authors: [Sarah Allali](https://twitter.com/SarahAllali7) and [Nicolas Cabrignac](https://twitter.com/Nicowcbg)
- [Twitter](https://twitter.com/floodehq)

</details>

## [GitHub Copilot X](https://github.com/features/preview/copilot-x)
AI-powered software developer

<details>

### Description
- AI pair programmer
- Chat and terminal interfaces
- Support for pull requests
- Early adoption of OpenAI’s GPT-4

### Links
- [Community](https://github.com/orgs/community/discussions/)
- [Documentation](https://docs.github.com/en)
- [Twitter](https://twitter.com/GitHubCopilot)



</details>

## [GitLab Duo](https://about.gitlab.com/gitlab-duo/)
 A suite of AI capabilities for every step of the software development lifecycle
<details>

### Description
- A suite of AI-powered capabilities for #DevSecOps workflows
- A toolbox of features integrated into the DevSecOps Platform to help teams across the entire software development environment become more efficient
- Examples of what GitLab Duo can do:
	- Planning refinement
	- Security risk resolution
	- CI/CD pipeline health
	- Analytics charting.

### Links
- [Twitter](https://twitter.com/gitlab)


</details>

## [GitWit](https://www.gitwit.dev/)

A tool automating code generation, in beta version, created for full-stack developers
<details>

### Description
- GitWit uses a GPT-based agent to generate code and git to track changes made to files
- GitWit ties together large language models and modern developer tools
- It can spawn and modify codebases using just a single prompt
- GitWit is primarily aimed at full-stack developers, and is particularly loved by those with a learning mindset—such as those learning a new stack or technology
- It is in early beta and may require some experimentation with the prompts you enter
- You are offered to choose from code bases:
	- React + NextJS
	- Python using pip
	- A Chrome extension written in JavaScript
	- An AngularJS using npm.
	- Custom stack

</details>

## [Grit](https://www.grit.io/)
A beta version of a tool for fixing technical gap automatically, putting code migrations and dependency upgrades on autopilot

<details>

### Description
- Grit uses machine learning and static analysis to auto-generate pull requests for cleaning up technical debt
- Users can declare how they want their code to be structured and let Grit rewrite it for them

### Links
- [Linkedin](https://www.linkedin.com/company/getgrit/0)
- [Twitter](https://twitter.com/gritdotio)

</details>

## [Heights Platform](https://www.heightsplatform.com/)
Your AI Coach and and AI Copilot for course creators, community builders, and coaches. Built into an all-in-one course creation and community software.

<details>

### Description
- Heights AI Chat can make edits to your digital products, answer support questions, and provide advice on growing your business. 
- Heights AI Coach is your personal autonomous coach, helping you accomplish your unique goals
    - Your AI coach will ask you questions and analyze the products you create to provide you with new tasks and recommendations every week.
    - Information you share with your AI Coach will never be shared with another creator's AI Coach.
    - Any information submitted will never be used for AI language model training data.

### Links
- [AI Features](https://www.heightsplatform.com/features/ai)
- [Twitter](https://twitter.com/HeightsPlatform)

</details>


## [Hex Magic](https://hex.tech/product/magic-ai/)
Hex AI-powered tools for humans doing amazing things with data

<details>

### Description
- "A suite of powerful AI features meant to augment data people"
- Hex can explain and document your code
- Hex Magic features know about database schemas, past operations, and the project’s execution graph, so they can make deeper, more insightful recommendations

You can see more – and sign up for the waitlist – over here.

### Links
- [Launch post](https://hex.tech/blog/magic-private-beta/)

</details>

## [Heymoon.ai](https://heymoon.ai/)
Personal assistant for life: to keep you on top of your calendar, tasks and information

<details>

### Description
- Personal assistant for life: to keep you on top of your calendar, tasks and information
- Currently in a beta version

</details>


## [Kadoa](https://www.kadoa.com/)
Web Scraping on Autopilot with AI

<details>

### Description
- Using LLMs to generate web scrapers and data processing steps on the fly that adapt to website changes.
- Features
	- No coding or browser extension required.
	- The autonomous crawling agent efficiently locates the desired information on websites.
	- Adaptability to website changes makes it maintenance-free
	- Transforms data from multiple sources into the same structure
	- Handles all clicking and scrolling automatically
	- Handles proxies
	- Powerful integrations

### Links
- [Playground](https://www.kadoa.com/playground)
- Author: [Adrian Krebs](https://twitter.com/krebs_adrian)

</details>


## [Lindy](https://www.lindy.ai/)
An AI assistant that can help with daily tasks, e.g., calendar management, email drafting, and contract sending

<details>

### Description
- Lindy is still in a beta version
- Features
	- Lindy triages your email
	- She learns from your inbox and automatically surfaces the highest-priority emails for you
	- Automatic conflict handling
	- Daily briefing
	- Contract management
	- Meeting note taking
	- Summarization

### Links
- Author: [Flo Crivello](https://twitter.com/Altimor)

<!--
### Features
- Lindy triages your email
- She learns from your inbox and automatically surfaces the highest-priority emails for you
- Automatic conflict handling
- Daily briefing
- Contract management
- Meeting note taking
- Summarization
-->

</details>

## [Minion AI](https://minion.ai/)
Made by creator of GitHub Copilot, so far in a waitlist stage
<details>

### Links
- [Twitter](https://twitter.com/ai_minion)
- Author: [Alex Graveley](https://twitter.com/alexgraveley)
</details>


## [MultiOn](https://multion.ai/)
AI personal agent, holding the record for the first AI flight booking, food order (a burger) & workplace cert
<details>

### Description
- The agent runs and controls the local Google Chrome, which allows it to interact with the world/services/web apps, just like people interact with the world/services/web apps using Google Chrome
- The agent itself probably also runs locally and currently, it needs the local Google Chrome to function
- Our understanding from the demo video is that they use local code and a custom plugin in ChatGPT to control a web browser (e.g., Google Chrome). This setup enables MultiOn to perform tasks like ordering plane tickets as if a human were interacting with the browser directly
- Use cases
	- A lot of cool real use cases, e.g.,
	-Sending an email fully autonomously
	-Posting a tweet
	-Sending a tweet reply to a specific person with a specific message
	-Sending a Facebook message to a friend
	-Searching for vacation rentals and check pricing for an upcoming trip
	-Searching for a wedding venue and starting the wedding planning process
	-Scheduling a car wash
- After introducing the GPT function calling, MultiOn can call itself recursively to spawn more sub-agents
- Instead of calling multiple functions or APIs you just need one Universal Function that can interact with all services and have it call itself to accomplish more complex tasks in parallel

### Links
- [Twitter](https://twitter.com/MultiON_AI)
- Author: [Div Garg](https://twitter.com/DivGarg9)
</details>

## [Mutable AI](https://mutable.ai/)
AI Accelerated Software Development


<details>

### Description
- Features
	- AI Autocomplete
	- Production Quality Code with One Click
	- Prompt driven development
	- Test Generation (coming soon)

### Links
- [Discord](https://discord.com/invite/zAwadbmuVk)
- [Twitter](https://twitter.com/mutableai)
- [GitHub](https://github.com/mutableai/)

</details>


## [Naut](https://www.naut.ai/)
Still in an early stage, with waitlist for early access
<details>

### Description
"Build your team of AI agents that work for you.  Early access now live. Join waitlist."


### Links
- [Twitter](https://twitter.com/naut_ai)
</details>


## [Otherside's AI Assistant](https://www.hyperwriteai.com/personal-assistant)
An AI browsing assistant for everyday tasks, can operate a web browser to complete nearly any task

<details>


### Description
- AI agent that can use a web browser like a human
- "Just describe what you want it to do, and it will automatically operate Chrome to achieve your task."
- Examples of use cases: Booking flights, ordering food, researching complex topics, managing your email
- Designed to handle tasks from booking flights to conducting in-depth research, and everything in between.
- Examples of usage:
	- Organize Gmail inbox
	- Booking a flight
	- Ordering online
	- Finding hire candidates

### Links
- [Launch announcement](https://twitter.com/mattshumer_/status/1673730806865358848)
- [Google Chrome Extension](https://chrome.google.com/webstore/detail/hyperwrite-ai-writing-com/kljjoeapehcmaphfcjkmbhkinoaopdnd)
- [Article](https://venturebeat.com/ai/hyperwrite-unveils-breakthrough-ai-agent-that-can-surf-the-web-like-a-human/)

</details>

## [Proficient AI](https://proficientai.com)

Interaction APIs and SDKs that allow developers to build, deploy and operate conversational AI agents in their apps
<details>

### Description
- An end-to-end solution, with which it takes 3 minutes not weeks to get a user-facing agent up and running in your app (currently 3 SDKs including React)
- Powerful tools built into the admin dashboard and Admin API including analytics, monitoring, rate-limiting, content moderation, etc.
- minimizes or eliminates the need for custom backend infrastructure so you can focus on implementing the business logic
- Technology-agnostic solution that supports multiple LLM providers (currently 7 models from OpenAI and Anthropic) allowing you to easily switch between models with 1 click
- Ready-to-use, highly customizable and beautiful UI components rendering complex interaction trees with support for advanced features like streaming

### Links
- [Documentation](https://docs.proficientai.com)
- [GitHub](https://github.com/proficientai/js)
- [Discord](https://discord.gg/DVbwTM8erb)
</details>

## [Saga](https://saga.so/ai)

A digital AI assistant, an AI-powered workspace integrating notes, tasks, and tools
<details>

### Description
- Generating content
- Brainstorming ideas
- Translation
- Grammer check
- [Roadmap](https://sagahq.canny.io/)

### Links
- [Twitter](https://twitter.com/saga_hq)
- [Slack](https://sagacommunity.slack.com/join/shared_invite/zt-13m3lrrdt-1x6~l6sLuR8CX~4c3fWwHA#/shared-invite/email)
- [Discord](https://discord.com/invite/cgz2mUEq7P)


</details>


## [Second](https://www.second.dev/)
Automated migrations and upgrades for every codebase
<details>

### Description
- Migrate frameworks such as Angular to React, libraries such as Redux to React Context, or languages such as JavaScript to TypeScript
- Perform major version upgrades on any number of applications, of any size
- Upgrade frameworks such as Next.js 12 to 13, libraries such as MUI 4 to 5, or languages such as Python 2 to 3
- Target users: enterprise codebases
- [Roadmap](https://second.canny.io/)

### Links
- [YCombinator](https://www.ycombinator.com/companies/second)
- [Twitter](https://twitter.com/SecondDevHQ)
- [Linkedin](https://www.linkedin.com/company/secondhq/)
- [Discord](https://discord.com/invite/ZhYUEjsW3Z)
- Founder: [Eric Rowell](https://twitter.com/ericdrowell)


</details>

## [Spell](https://spell.so/)

AutoGPT agents with plugins
<details>

### Description
- "Delegate your tasks to autonomous AI agents. Transform your daily work with revolutionary and intuitive AI tools powered by GPT4"
- Access APIs like Zapier, Wolfram, etc.
- Open links
- Manipulate files
- Search web



### Links
- [Author's Twitter](https://twitter.com/rafal_makes)

</details>


## [Superluminal](https://superluminal.dev)
Add an AI copilot to your product's data dashboard with just a few lines of code.


<details>

### Description
- Get set up in minutes with the Superluminal React component, or use the API directly for custom solutions.
- Writes Python code to answer questions and perform tasks, similar to ChatGPT + CodeInterpreter.
- Fully managed compute infrastructure for the secure execution of generated code.
- Customize the look and feel to fit your product.
- Full support for graphs, pivots and filters in addition to textual answers.
- Enable your customers to extract more value from the data already on their dashboard with meaningful answers to high-level questions.


### Links
- [Twitter](https://twitter.com/getluminal/)
- [Linkedin](https://www.linkedin.com/company/74930600/)

</details>



<br>

## :wave: Wanna discuss AI agents and more?

- [Hit us up on discord](https://discord.gg/BRymvqUS)
- [Pick a date for a call in our calendar](https://calendly.com/tereza-tizkova/30min)
- Email us at hello@e2b.dev
- And be sure to join our [twitter community focused on AI agents](https://twitter.com/i/communities/1670204079619055616)


<a href="https://discord.gg/U7KEcGErtQ" target="_blank">
	<img src="https://img.shields.io/static/v1?label=Join&message=%20discord!&color=mediumslateblue">
</a>
<a href="https://twitter.com/e2b_dev" target="_blank">
	<img src="https://img.shields.io/twitter/follow/e2b.svg?logo=twitter">
</a>

<br>

<!-- More agents to add in the future

- GPTeam https://twitter.com/itstimconnors/status/1672278464362336256
- https://github.com/101dotxyz/GPTeam

- Neurite https://github.com/satellitecomponent/Neurite

- AutoGPT.js https://github.com/zabirauf/AutoGPT.js

- Street Fighter https://github.com/linyiLYi/street-fighter-ai

- GPT RPG https://github.com/dzoba/gptrpg

- Autopilot https://github.com/fjrdomingues/autopilot

- WinGPT - AI assistant for Windows https://news.ycombinator.com/item?id=36472854



-->
