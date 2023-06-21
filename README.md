# 🔮 AI Agents

*Welcome to our list of popular AI autonomous agents. Your favorite one is missing? Add them via pull request. Discussion and feedback appreciated :heart:*


[![Discord](https://img.shields.io/static/v1?label=Join&message=our%20discord!&color=mediumslateblue)](https://discord.gg/5GmKg5Uz)
 <a href="https://github.com/tizkovatereza/AI/pulls">    <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?longCache=true" alt="Pull Requests">
</a>  <a href="https://twitter.com/e2b_dev" target="_blank">
<img src="https://img.shields.io/twitter/follow/e2b.svg?logo=twitter">  </a>

# Open Source Projects

## [AgentGPT](https://agentgpt.reworkd.ai/)
A browser-based implementation of AutoGPT, accessible via a no-code platform
<details>

### How it works
- A no-code platform
- Assigning a goal to the agent, witnessing its thinking process, and formulation of an execution plan and taking actions accordingly

### Features
- Uses OpenAI **functions**
- Supports gpt-3.5-16k, pinecone and pg_vector databases

### Links
- [Website](https://agentgpt.reworkd.ai/)
- [GitHub](https://github.com/reworkd/AgentGPT)

### Stack
- Frontend: NextJS + Typescript
- Backend: FastAPI + Python
	- DB: MySQL through docker with the option of running SQLite locally

### Links
- [Documentation](https://docs.reworkd.ai/)
-  [GitHub](https://github.com/reworkd/AgentGPT)
</details>



## [AI Legion](https://gpt3demo.com/apps/ai-legion)
Similar in spirit to AutoGPT and Baby AGI, but written in TypeScript
<details>

- Author: eumemic
- [Website](https://gpt3demo.com/apps/ai-legion)
- [GitHub](https://github.com/eumemic/ai-legion)
- [Twitter](https://twitter.com/dysmemic)
</details>



## [AutoGPT](https://autogpt.net/)

<details>

- A lot like BabyAGI combined with LangChain tools.
- Can execute many commands such as Google Search, browse websites, write to files, and execute Python files
- [GitHub](https://github.com/Significant-Gravitas/Auto-GPT)
</details>

## [BabyAGI](https://github.com/yoheinakajima/babyagi)
<details>


### How it works
- Creates tasks based on the result of previous tasks and a predefined objective.
- The script then uses OpenAI's NLP capabilities to create new tasks based on the objective
- Leverages OpenAI's GPT-4, pinecone vector search, and LangChainAI framework
- Default model is OpenAI GPT3-turbo
- The system maintains a task list for managing and prioritizing tasks
- It autonomously creates new tasks based on completed results and reprioritizes the task list accordingly, showcasing the adaptability of AI-powered language models


###Links
- Paper: [Task-driven Autonomous Agent Utilizing GPT-4, Pinecone, and LangChain for Diverse Applications](https://yoheinakajima.com/task-driven-autonomous-agent-utilizing-gpt-4-pinecone-and-langchain-for-diverse-applications/)
- [Founder's twitter](https://twitter.com/yoheinakajima)
- [Twitter thread describing the system](https://twitter.com/yoheinakajima/status/1640934493489070080)


</details>


## [BabyCatAGI](https://replit.com/@YoheiNakajima/BabyCatAGI)
BabyCatAGI is a mod of BabyBeeAGI, which is a mod of OG BabyAGI
<details>


### How it works
- Just 300 lines of code
- This was built as a continued iteration on the original BabyAGI code in a lightweight way. Differences to BabyAGI include the following:
	- Task Creation Agent runs once
	- Execution Agent loops through tasks
	- Task dependencies for pulling relevant results
	- Two tools: search_tool and text_completion
	- “Mini-agent” as tool
	- Search tool combines search, scrape, chunking, and extraction.
	- Results combined to create summary_report


### How to use
- Fork this into a private Repl
- Add your OpenAI API Key (required) and SerpAPI Key (optional)
- Update the OBJECTIVE variable
- Press "Run" at the top.

### Links
- [Twitter](http://twitter.com/babyAGI)
- [GitHub](https://github.com/yoheinakajima/babyagi)
- Author: @yoheinakajima (Twitter)

</details>


## [Bloop](https://bloop.ai/)
> Just make sure to communicate that it's a code search engine that uses an AI agent.

<details>
</details>

## [Butternut AI](Butternut.ai)
> Closed source.

<details>
</details>


## [Camel](https://github.com/camel-ai/camel)
Communicative Agents for “Mind” Exploration of Large Scale Language Model Society
> It's more like an agent architecture than an agent itself. Just make sure you communicate this.

<details>

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


## [Cognosys](https://cognosys.ai)
> Closed source.


Web based version of AutoGPT/babyAGI

<details>

- Friendly UI for building AI agents
- Author: Sully Omarr
- Twitter: https://twitter.com/SullyOmarr

</details>


## [Databerry](https://www.databerry.ai/)


<details>
</details>



## [Factory](https://www.factory.ai/)
> Closed source.

<details>
</details>

## [Fixie](https://www.fixie.ai/)
> Closed source.

<details>
- Not open source
</details>

## [Friday](https://github.com/amirrezasalimi/friday/)
> Closed source.

A developer assistant able to make whole nodejs project with unlimited prompts
<details>

### How it works
- Provides a core prompt for building the foundation of your application
- Allows you to add unlimited sections, each of which is a prompt representing a specific part of your app

### Features
- Friday utilizes GPT-4 for AI assistance, but it has been tested and optimized with GPT-4-32k for improved speed and better results.
- It requires 2 small requests for your app's base and 1 request per section you provide.
- Friday employs esbuild behind the scenes for every app created by it.

### Links
- **Author:** [Amirreza Salimi](https://twitter.com/amirsalimiiii)

</details>


## [GitWit](https://www.gitwit.dev/)

<details>
</details>


## [GPT Engineer](https://github.com/AntonOsika/gpt-engineer)
Specify your project, and the AI agent constructs the entire code base.


GPT Engineer is made to be easy to adapt, extend, and make your agent learn how you want your code to look. It generates an entire codebase based on a prompt.
<details>

Model: GPT 4
Specify what you want it to build, the AI asks for clarification, and then builds it.

### Features
- You can specify the "identity" of the AI agent by editing the files in the identity folder.

Editing the identity, and evolving the main_prompt, is currently how you make the agent remember things between projects.

Each step in steps.py will have its communication history with GPT4 stored in the logs folder, and can be rerun with scripts/rerun_edited_message_logs.py.

### Links
- Author: [Anton Osika](https://twitter.com/antonosika)
- [Twitter review by @Attack](https://twitter.com/Attack/status/1671165869064609792)

</details>


## [Grit](https://www.grit.io/)
> Closed source.

<details>
</details>


## [HayStack Agent](https://docs.haystack.deepset.ai/docs/agent)
> This is not an agent but SDK for creating agents. Like LangChain or LlamaIndex.

<details>
</details>


## [Heymoon.ai](https://heymoon.ai/)
> Closed source
Personal assistant for life: to keep you on top of your calendar, tasks and information

<details>

### Features
- Personal assistant for life: to keep you on top of your calendar, tasks and information. Was at Llama event demo


</details>


## [Hyperwrite](https://www.hyperwriteai.com/)
> Closed source. Not sure if agent-like. Probably more like generative AI.

Your personal AI writing assistant

<details>
</details>


## [Jarvis]()

<details>
</details>


## [Lindy](https://www.lindy.ai/)
- Lindy is an AI assistant that can help with all your tasks, from calendar management and email drafting to contract sending and beyond.

<details>

### How it works
- Lindy is still in a beta version

### Features
- Lindy triages your email
- She learns from your inbox and automatically surfaces the highest-priority emails for you
- Automatic conflict handling
- Daily briefing
- Contract management
- Meeting note taking
- Summarization



</details>


## [Loop GPT](https://github.com/farizrahman4u/loopgpt/tree/main)

 <details>
- Languages: Python
- Default model: GPT-3.5-turbo (also possible with GPT-4)
- Modular Auto-GPT Framework
- Plug N Play" API - Extensible and modular "Pythonic" framework, not just a command line tool
- Easy to add new features, integrations and custom agent capabilities, all from python code, no nasty config files!
- Minimal prompt overhead - Every token counts. We are continuously working on getting the best results with the least possible number of tokens.
- Human in the Loop - Ability to "course correct" agents who go astray via human feedback.
- Full state serialization - can save the complete state of an agent, including memory and the states of its tools to a file or python object. No external databases or vector stores required (but they are still supported)!
	</details>

## [LocalGPT](https://github.com/PromtEngineer/localGPT)
Inspired by privateGPT

 <details>

### How it works
- Most of the description on readme is inspired by the original privateGPT
- Model: Vicuna-7B
- Using InstructorEmbeddings
- Both Embeddings as well as LLM will run on GPU. It also has CPU support if you do not have a GPU
- Built with Langchain

### Features
- Ask questions to your documents without an internet connection, using the power of LLMs. 100% private, no data leaves your execution environment at any point. You can ingest documents and ask questions without an internet connection!


### Links
- [YouTube - LocalGPT: OFFLINE CHAT FOR YOUR FILES [Installation & Code Walkthrough]](https://www.youtube.com/watch?v=MlyoObdIHyo&ab_channel=PromptEngineering)
</details>


## [Mini AGI](https://github.com/muellerberndt/mini-agi)

<details>

- MiniAGI is a minimal general-purpose autonomous agent based on GPT-3.5 / GPT-4. Can analyze stock prices, perform network security tests, create art, and order pizza
- MiniAGI is a simple autonomous agent compatible with GPT-3.5-Turbo and GPT-4. It combines a robust prompt with a minimal set of tools, chain-of-thoughts, and short-term memory with summarization. It is also capable of inner monologue and self-criticism.
</details>


## [Pezzo](https://www.pezzo.ai/)
>
<details>
</details>


## [Saga](https://saga.so/)
> Maybe link directly to their AI product? https://saga.so/ai
> It's not an agent yet though, I think. They're moving in the agent direction.
<details>
</details>


## [Second](https://www.second.dev/)
> Closed source.
<details>
</details>


## [Smol developer](https://github.com/smol-ai/developer)

<details>
</details>

## [Superagent](https://www.superagent.sh/)</details>
> Not a single agent. You can create agents without coding with this tool.
<details>
</details>


## [Sweep](https://sweep.dev/)
> Closed source.
<details>
</details>

## [Teenage AGI](https://github.com/seanpixel/Teenage-AGI/blob/main/README.md#experiments)

Can recall infinite memory, THINKS before it speaks, and doesn't lose memory after being shutting down
<details>

### How it works
- Model: GPT-4
- Language: Python
- Uses OpenAI and Pinecone to give memory to an AI agent and also allows it to "think" before making an action (outputting text)
- Also, just by shutting down the AI, it doesn't forget its memories since it lives on Pinecone and its memory_counter saves the index that it's on

**Here is what happens every time the AI is queried by the user:**

- AI vectorizes the query and stores it in a Pinecone Vector Database
- AI looks inside its memory and finds memories and past queries that are relevant to the current query
- AI thinks about what action to take
- AI stores the thought from Step 3
- Based on the thought from Step 3 and relevant memories from Step 2, AI generates an output
- AI stores the current query and its answer in its Pinecone vector database memory

### Links
- Created by [@sean_pixel](https://twitter.com/sean_pixel)
!

</details>


## [“Westworld” simulation](https://theolvs.github.io/westworld/)
Westworld is a multi-agent simulation library, its goal to simulate and optimize systems and environments with multiple agents interacting.
<details>

- Researchers from Stanford and Google created an interactive sandbox env with 25 Gen AI agents can simulate human behavior
- They walk in the park, join for coffee at a cafe, and share news with colleagues. They demonstrated surprisingly good social
- Westworld's inspiration is drawn from Unity software and Unity ML Agents, adapted in Python


[Underlying paper - Generative Agents](https://arxiv.org/abs/2304.03442)
- A paper simulating interactions between tens of agents
- Presenting an architecture that extends a language model to store and synthesize the agent's experiences, enabling dynamic behavior planning in an interactive sandbox environment with generative agents


### Links
- [GitHub](https://github.com/TheoLvs/westworld)
- [Documentation](https://theolvs.github.io/westworld/ )

### Languages
- The library is available on PyPi via
pip install westworld
- [Javascript version (being developed)](https://github.com/TheoLvs/westworldjs)

### Current features

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

</details>




## [Yourgoal]()
> Open source

Swift implementation of BabyAGI.

<details>
Author: PJ Gray
Twitter: https://twitter.com/pj4533
</details>

# Companies building agents


## [AIrplane](https://www.airplane.dev/)
> Note: Airplane isn't AI agent. It's a company with a product for building internal tools. They're building an AI assistant here https://www.airplane.dev/autopilot. This is the link I'd be using. It's closed source.

Turning APIs, SQL queries, and scripts into apps for the entire team


<details>

### How it works
- A developer-centric approach to building internal UIs and workflows

### Features
- Airplane lets you turn SQL queries, JavaScript/Python code, HTTP requests, etc into tasks
- Allows to run tasks through a no-code dashboard
- Tasks for customer support, on-call runbooks, and scheduled tasks

### Links
- [Documentation](https://docs.airplane.dev/)
- [Twitter](https://twitter.com/AirplaneDev)


</details>


## [Aomni](https://www.aomni.com/)
> Note: Closed source.

An AI agent specifically designed for research
<details>

### How it works
- Breaks down a high level research question into a step-by-step plan, and executes it
- Diverse tools, including a full web browser
- Can access internet information without the need for an API
- "We don't generate content using AI, as it can be unreliable. Instead, we extract relevant information from trusted sources, cluster and process it into a user-friendly format."
- AI-powered query planner intelligently routes and executes requests, ensuring correctness and diverse source selection

### Links
-[Discord](https://discord.com/invite/a367ncqEsm)

</details>


## [BitBuilder](https://www.bitbuilder.ai/)


"Virtual intern for developers", generates code via PRs raised against your repository
<details>

### How it works
- Create an Issue
- Approve the Implementation Plan
- Review the Pull Request

### Features
- Writing code
- Reviewing changes
- Addressing comments
- Answering questions

 ### BitBuilder Junior
- BitBuilder Junior is an intern-level code generation tool that lives in your GitHub repository. It follows instructions to implement unamibigous code changes by changing multiple files, writing tests for generated code, and matching the style, framework, and libraries you're already using.

### Links
- [GitHub Marketplace](https://github.com/marketplace/document-guardian)
- [Slack](https://bitbuilder-ai.slack.com/join/shared_invite/zt-1tlrds3n4-rpmgIGM6XrB5W97005IA1Q#/shared-invite/email)
- [Installation(https://docs.bitbuilder.ai/install)]



</details>



## [Hex Magic](https://hex.tech/product/magic-ai/)

<details>
</details>


## [LastMile AI](https://lastmileai.dev/)
> I spoke with them, they're building an SDK that should be something like "Langchain for enterprises". Not an agent
<details>
- Not an open-source project
</details>


## [Minion AI](https://minion.ai/)
> Closed source. Made by creator GitHub Copilot.
<details>
</details>


## [MultiOn](https://multion.ai/)
> Closed source.
<details>
</details>


## [Naut ai](https://www.naut.ai/)
> Closed source. I'll be talking to a founder next Thursday.
<details>
</details>






<br>

## :wave: Wanna discuss AI agents and more?

- [Hit us up on discord](https://discord.gg/5GmKg5Uz)
- [Pick a date for call in our calendar](https://calendly.com/tereza-tizkova/30min)
- Write us at hello@e2b.dev

<br>

# 💪 Contributors 💪

<a href="https://github.com/tizkovatereza/AI/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=tizkovatereza/AI" />
</a>

Made with [contrib.rocks](https://contrib.rocks).